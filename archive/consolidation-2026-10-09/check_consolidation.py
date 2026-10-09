#!/usr/bin/env python3
"""Independent consolidation checks for the coherent-pump crossover.

No preceding scientific module is imported. Truncated evolutions are diagnostics;
the uniform state and measurement statements are proved in THEOREM.md.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import unittest
sys.dont_write_bytecode=True
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from scipy.special import eval_genlaguerre, gammaln, roots_hermitenorm, erfcx

REPORT={}

def gain(alpha,lam):
    if alpha<=0 or lam<0:raise ValueError('alpha>0 and lambda>=0 required')
    return np.log1p(8*alpha*lam)/2

def state_bound(alpha,lam):
    r=gain(alpha,lam)
    return np.sqrt(2+48*lam**2+480*lam**4)/(8*alpha)+r*np.sqrt(1+16*lam**2+384*lam**4)/(2*alpha)

def phi(lam,s):
    return np.exp(-s*s/4)/np.sqrt(1+2*lam*lam*s*s)

def witness(lam,s):
    return np.exp(-s*s)*(1/np.sqrt(1+8*lam*lam*s*s)-1/(1+2*lam*lam*s*s)**2)

def displacement(beta,size):
    """Exact infinite-oscillator displacement matrix elements on a finite block."""
    answer=np.zeros((size,size),complex);x=abs(beta)**2
    for m in range(size):
        for n in range(size):
            if m>=n:
                answer[m,n]=np.exp(-x/2+(gammaln(n+1)-gammaln(m+1))/2)*beta**(m-n)*eval_genlaguerre(n,m-n,x)
            else:
                answer[m,n]=np.exp(-x/2+(gammaln(m+1)-gammaln(n+1))/2)*(-beta.conjugate())**(n-m)*eval_genlaguerre(m,n-m,x)
    return answer

def quadrature_block(s,size):
    # exp(i*s*(x_a-x_b)/sqrt(2)) restricted to |k,k>.
    # Its matrix is the entrywise product of D(i*s/2) and D(-i*s/2).
    D=displacement(complex(0,s/2),size)
    return abs(D)**2

def frame(alpha,lam,npump,npair):
    """Direct left/right occupation-array action, rather than sparse Kronecker generator."""
    r=gain(alpha,lam)
    d=np.diag(np.sqrt(np.arange(1,npump)),1)
    p=d-d.T;t=d+d.T
    kp=np.diag(np.arange(1,npair),-1)
    q=np.diag(2*np.arange(npair)+1)
    R=kp+kp.T+q;L=kp+kp.T-q;A=kp-kp.T
    initial=np.zeros((npump,npair));initial[0,0]=1
    def rhs(u,state):
        v=state.reshape(npump,npair)
        out=(np.exp(2*u)*(p@v@R.T)+np.exp(-2*u)*(p@v@L.T)+2*(t@v@A.T))/(4*alpha)
        return out.ravel()
    sol=solve_ivp(rhs,(0,r),initial.ravel(),method='DOP853',rtol=2e-11,atol=2e-13)
    if not sol.success:raise RuntimeError(sol.message)
    state=sol.y[:,-1].reshape(npump,npair)
    return state,sol.nfev

class Checks(unittest.TestCase):
    def test_01_shear_and_non_gaussian_certificate(self):
        l,z=sp.symbols('l z',real=True)
        # Coordinates (x+,p+,x-,p-); exp(i*l*z*R) gives these Heisenberg shears.
        S=sp.Matrix([[1,0,0,0],[2*l*z,1,0,0],[0,0,1,-2*l*z],[0,0,0,1]])
        J=sp.diag(sp.Matrix([[0,1],[-1,0]]),sp.Matrix([[0,1],[-1,0]]))
        self.assertEqual(sp.simplify(S*J*S.T-J),sp.zeros(4))
        cov=S*S.T/2
        self.assertEqual(cov[2,2],sp.Rational(1,2)+2*l*l*z*z)
        self.assertEqual(cov[1,1],sp.Rational(1,2)+2*l*l*z*z)
        self.assertEqual(cov[1,2],0)
        a=sp.symbols('a',positive=True)
        self.assertEqual(sp.expand((1+a)**4-(1+4*a)),a**4+4*a**3+6*a*a)
        # A characteristic function at twice the argument obeys this relation for any Gaussian.
        s,v,mu=sp.symbols('s v mu',real=True)
        self.assertEqual(sp.exp(-v*(2*s)**2/2),sp.exp(-v*s*s/2)**4)
        rows=[]
        for lam in (.1,.5,1.):
            for s in (.3,1.,2.):
                measured=quad(lambda zz:np.exp(-zz*zz/2-.5*s*s*(.5+2*lam*lam*zz*zz))/np.sqrt(2*np.pi),-np.inf,np.inf,epsabs=1e-13,epsrel=1e-13)[0]
                self.assertLess(abs(measured-phi(lam,s)),2e-13)
                self.assertGreater(witness(lam,s),0)
                rows.append({'lambda':lam,'xi':s,'limiting_characteristic':float(phi(lam,s)),
                             'gaussian_identity_gap':float(witness(lam,s)),'all_gaussian_trace_distance_lower':float(witness(lam,s)/10)})
        REPORT['shear_and_certificate']={'covariance':str(cov),'rows':rows,
              'proof_scope':'The non-Gaussian witness concerns individual Gaussian states, including mixed ones, not their convex hull.'}

    def test_02_independent_displacement_and_geometric_state(self):
        # Exact displacement elements checked against a larger truncated exponential well below its boundary.
        lower=np.diag(np.sqrt(np.arange(1,36)),1)
        beta=.13+.21j
        numerical=expm(beta*lower.T-beta.conjugate()*lower)
        self.assertLess(np.linalg.norm(displacement(beta,8)-numerical[:8,:8]),2e-14)
        nodes,weights=roots_hermitenorm(180);weights=weights/np.sqrt(2*np.pi)
        n=192;k=np.arange(n)
        rows=[]
        for lam in (.1,.25,.5):
            angle=lam*nodes
            coeff=1/(1-1j*angle)
            ratio=1j*angle/(1-1j*angle)
            vectors=coeff[:,None]*ratio[:,None]**k
            rho=np.einsum('z,zi,zj->ij',weights,vectors,vectors.conj())
            tail=1-np.trace(rho).real
            self.assertLess(tail,2e-10)
            for s in (.5,1.,2.):
                value=np.trace(rho@quadrature_block(s,n))
                self.assertLess(abs(value-phi(lam,s)),3e-9)
                rows.append({'lambda':lam,'xi':s,'fock_characteristic_real':float(value.real),
                             'imaginary_residual':float(abs(value.imag)),
                             'analytic_value':float(phi(lam,s)),'omitted_norm_weight':float(tail)})
        REPORT['independent_readout']={'pair_cutoff':n,'gaussian_quadrature_order':180,'rows':rows,
                   'matrix_elements':'Infinite displacement matrix elements via Laguerre polynomials, not an exponentiated truncated readout.'}

    def test_03_exact_frame_homodyne_signature(self):
        rows=[];last=None
        for alpha in (10.,100.,1000.):
            lam=.5;state,nfev=frame(alpha,lam,48,128)
            rho=state.T@state
            chars=[float(np.trace(rho@quadrature_block(s,128))) for s in (1.,2.)]
            gap=abs(chars[1])-abs(chars[0])**4
            norm=np.linalg.norm(state)
            self.assertLess(abs(norm-1),2e-10)
            for s,val in zip((1.,2.),chars):self.assertLessEqual(abs(val-phi(lam,s)),2*state_bound(alpha,lam)+1e-8)
            if alpha==1000:
                fine,_=frame(alpha,lam,56,160)
                fine_rho=fine.T@fine
                refined=[float(np.trace(fine_rho@quadrature_block(s,160))) for s in (1.,2.)]
                changes=[abs(x-y) for x,y in zip(chars,refined)]
                self.assertLess(max(changes),2e-7)
                self.assertLess(abs(chars[0]-phi(lam,1)),.002)
                self.assertGreater(gap,.04)
            else:changes=None
            rows.append({'alpha':alpha,'N':alpha**2,'lambda':lam,'characteristic_at_1':chars[0],
                         'characteristic_at_2':chars[1],'gaussian_identity_gap':float(gap),
                         'reference_phi1':float(phi(lam,1)),'reference_phi2':float(phi(lam,2)),
                         'purity':float(np.trace(rho@rho)),'state_norm':float(norm),
                         'last_four_pump_weight':float(np.sum(state[-4:]**2)),
                         'last_four_pair_weight':float(np.sum(state[:,-4:]**2)),
                         'cutoff_refinement':changes,'function_evaluations':nfev})
        REPORT['full_generator_readout']={'runs':rows,'largest_frame_amplitudes':56*160,
          'scope':'Numerical truncation and refinement diagnostics; the asymptotic law follows from a bounded measurement and the state theorem.'}

    def test_04_physical_phase_model_and_resolution(self):
        nodes,weights=roots_hermitenorm(180);weights/=np.sqrt(2*np.pi)
        rows=[]
        for alpha in (10.,100.,1000.,10000.):
            lam=.5;r=gain(alpha,lam)
            theta=nodes/(2*alpha)
            # Stable variance of the *rescaled physical* squeezed quadrature.
            variance=.5+.5*np.expm1(4*r)*np.sin(theta/2)**2
            values=[]
            for s in (1.,2.):
                val=float(np.sum(weights*np.exp(-s*s*variance/2)))
                values.append(val)
                self.assertLessEqual(abs(val-phi(lam,s)),.1/alpha)
            rows.append({'alpha':alpha,'phase_model_phi1':values[0],'phase_model_phi2':values[1],
                          'physical_squeezed_quadrature_scale':float(np.exp(-r)),
                          'with_fixed_additive_std_0_1_gap_at_xi1':float((np.exp(-.25)-phi(lam,1))*np.exp(-.5*.1**2*np.exp(2*r))),
                          'with_matched_additive_std_exp_minus_r_gap_at_xi1':float((np.exp(-.25)-phi(lam,1))*np.exp(-.5))})
        self.assertLess(abs(rows[-1]['phase_model_phi1']-phi(.5,1)),1e-5)
        # Trace distance control of the witness: 2D for each characteristic and 8D for its fourth power.
        rng=np.random.default_rng(904);max_ratio=0
        for _ in range(200):
            p1,p2,q1,q2=(rng.random(4)*2-1)
            d=max(abs(p1-q1),abs(p2-q2))/2
            if d==0:continue
            ratio=abs((abs(p2)-abs(p1)**4)-(abs(q2)-abs(q1)**4))/(10*d)
            self.assertLessEqual(ratio,1+1e-14);max_ratio=max(max_ratio,ratio)
        REPORT['physical_readout_and_resolution']={'runs':rows,'lipschitz_diagnostic_max_ratio':float(max_ratio),
            'scope':'Ideal phase-referenced homodyne is a specified measurement. Fixed additive readout noise removes this scaled signal as N increases; no hardware operating window is inferred.'}

    def test_05_exact_remainder_polynomials_and_energy_scaling(self):
        # Repeat the analytical polynomial actions independently on a finite core.
        size=7;d=sp.zeros(size);kp=sp.zeros(size)
        for k in range(1,size):d[k-1,k]=sp.sqrt(k);kp[k,k-1]=k
        p=sp.kronecker_product(d-d.T,sp.eye(size));t=sp.kronecker_product(d+d.T,sp.eye(size))
        q=sp.diag(*[2*k+1 for k in range(size)])
        R=sp.kronecker_product(sp.eye(size),q+kp+kp.T)
        L=sp.kronecker_product(sp.eye(size),kp+kp.T-q)
        A=sp.kronecker_product(sp.eye(size),kp-kp.T)
        v=sp.zeros(size**2,1);v[0]=1
        l=sp.symbols('l',real=True)
        v1=p*(L-4*l*p*A+4*l*l*p*p*R)*v
        v2=(t-2*l*R)*(A-2*l*p*R)*v
        self.assertEqual(sp.expand((v1.T*v1)[0]),2+48*l*l+480*l**4)
        self.assertEqual(sp.expand((v2.T*v2)[0]),1+16*l*l+384*l**4)
        rows=[]
        for alpha in (10.,100.,1000.,1e6):
            lam=.5;r=gain(alpha,lam)
            upper=np.exp(r+alpha*alpha*np.expm1(r/alpha**2))/(4*alpha)
            geometric=np.sinh(r)**2/alpha
            self.assertGreater(upper,2*lam)
            rows.append({'alpha':alpha,'mean_pairs_over_alpha_upper':float(upper),
                         'nominal_mean_pairs_over_alpha':float(geometric),
                         'exact_state_norm_bound':float(state_bound(alpha,lam))})
        self.assertLess(abs(rows[-1]['mean_pairs_over_alpha_upper']-1),1e-6)
        REPORT['core_and_energy']={'polynomial_core_dimension':size**2,'rows':rows,
          'scope':'Independent polynomial identities and scalar estimates, not an inference of unbounded moments from norm convergence.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error('Use a new report path')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',groups=result.testsRun,prior_scientific_modules_imported=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
