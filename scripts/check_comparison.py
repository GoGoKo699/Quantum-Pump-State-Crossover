#!/usr/bin/env python3
"""Bounded source-dictionary and reduced-state checks for the pump crossover.

No prior checker or scientific module is imported. Finite cutoffs and quadrature
convergence are diagnostics, not proofs of an infinite-dimensional limit.
"""
from __future__ import annotations
import argparse, json, sys, unittest
from pathlib import Path
sys.dont_write_bytecode = True
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import erfcx, roots_hermite
from scipy.linalg import expm

REPORT = {}

def gain(alpha, lam):
    if alpha <= 0 or lam < 0: raise ValueError('Require alpha>0 and lambda>=0')
    return np.log1p(8*alpha*lam)/2

def purity(lam):
    return 1. if lam == 0 else float(np.sqrt(np.pi)*erfcx(1/(2*lam))/(2*lam))

def norm_bounds(alpha, lam):
    r=gain(alpha,lam)
    A=np.sqrt(2+48*lam**2+480*lam**4)
    B=np.sqrt(1+16*lam**2+384*lam**4)
    eps=A/(8*alpha)+r*B/(2*alpha)
    extra=(np.sqrt(2)+np.exp(-2*r)*A)/(8*alpha)
    return eps,extra

def exact_frame(alpha, lam, npump=40, npair=80, rtol=5e-11, atol=5e-13):
    """Tensor action in the exact cosh/sinh-conjugated generator.

    This deliberately does not use the leading-plus-remainder decomposition.
    Pair basis index k means |k,k>. Pump index is displaced-frame excitation.
    """
    r=gain(alpha,lam);vac=np.zeros((npump,npair));vac[0,0]=1
    kpweights=np.arange(1,npair);q=2*np.arange(npair)+1
    sqrtp=np.sqrt(np.arange(1,npump))[:,None]
    def rhs(u,y):
        s=y.reshape(npump,npair)
        kp=np.zeros_like(s);km=np.zeros_like(s)
        kp[:,1:]=s[:,:-1]*kpweights;km[:,:-1]=s[:,1:]*kpweights
        c,h=np.cosh(u),np.sinh(u)
        first=c*c*kp+h*h*km+c*h*s*q
        second=c*c*km+h*h*kp+c*h*s*q
        out=np.zeros_like(s)
        out[:-1,:]+=sqrtp*first[1:,:]
        out[1:,:]-=sqrtp*second[:-1,:]
        return (out/alpha).ravel()
    sol=solve_ivp(rhs,(0,r),vac.ravel(),method='DOP853',rtol=rtol,atol=atol)
    if not sol.success: raise RuntimeError(sol.message)
    return sol.y[:,-1].reshape(npump,npair),sol.nfev

def phase_geometric(alpha,lam,p):
    """Exact normalized amplitudes S(-r) exp(i theta n_a) S(r)|00>."""
    r=gain(alpha,lam);t=np.tanh(r);theta=p/(np.sqrt(2)*alpha)
    em1=np.expm1(1j*theta)
    den=(1-t*t)-t*t*em1
    amplitude=(1-t*t)/den
    z=t*em1/den
    return amplitude,z

def leading_geometric(lam,p):
    w=np.sqrt(2)*lam*p
    return 1/(1-1j*w),1j*w/(1-1j*w)

def pure_phase_overlap(alpha,lam):
    """Joint-state norm using the exact geometric-series overlap and quadrature."""
    def distance_density(p):
        A,z=phase_geometric(alpha,lam,p);B,w=leading_geometric(lam,p)
        ov=B.conjugate()*A/(1-w.conjugate()*z)
        return np.exp(-p*p)*(2-2*ov.real)/np.sqrt(np.pi)
    value,err=quad(distance_density,-9,9,epsabs=3e-14,epsrel=2e-9,limit=200)
    return np.sqrt(max(0,value)),err

def phase_frame_density(alpha,lam,cutoff,order=100):
    x,w=roots_hermite(order)
    A,z=phase_geometric(alpha,lam,x)
    v=A[:,None]*z[:,None]**np.arange(cutoff)[None,:]
    rho=(v.T*(w/np.sqrt(np.pi)))@v.conj()
    return rho

class Checks(unittest.TestCase):
    def test_01_source_frames_and_short_time_dictionary(self):
        r,a=sp.symbols('r a',positive=True)
        c,s=sp.cosh(r),sp.sinh(r)
        self.assertEqual(sp.simplify(c*c-(sp.exp(2*r)+sp.exp(-2*r)+2)/4),0)
        self.assertEqual(sp.simplify(s*s-(sp.exp(2*r)+sp.exp(-2*r)-2)/4),0)
        self.assertEqual(sp.simplify(c*s-(sp.exp(2*r)-sp.exp(-2*r))/4),0)
        A=(sp.cosh(2*r)-1)/4;B=(sp.sinh(2*r)-2*r)/4
        series=sp.series(2*B**2,r,0,12)
        self.assertEqual(sp.expand(series.removeO()).coeff(r,6),sp.Rational(2,9))
        self.assertEqual(sp.expand(series.removeO()).coeff(r,8),sp.Rational(4,45))
        self.assertEqual(sp.diff(A,r),sp.sinh(2*r)/2)
        self.assertEqual(sp.simplify(sp.diff(B,r)-sp.sinh(r)**2),0)
        # Reconstruct CQ's moving displacement/squeezing frame using its ODEs.
        rows=[]
        for alpha in (30.,300.,3000.):
            lam=.5;rf=gain(alpha,lam)
            def ode(u,v):
                delta,eta=v
                return [np.sinh(2*eta)/(2*alpha),1-delta/alpha]
            sol=solve_ivp(ode,(0,rf),[0.,0.],method='DOP853',rtol=2e-12,atol=2e-14)
            d,eta=sol.y[:,-1]
            conserved=(alpha-d)**2+np.sinh(eta)**2
            self.assertLess(abs(conserved-alpha**2)/alpha**2,2e-12)
            self.assertGreaterEqual(rf-eta,0)
            bound=(np.sinh(2*rf)/4-rf/2)/alpha**2
            self.assertLessEqual(rf-eta,bound*(1+1e-8))
            rows.append({'alpha':alpha,'lambda':lam,'pump_amplitude_shift':float(d),
                         'gain_difference':float(rf-eta),'gain_difference_bound':float(bound),
                         'relative_invariant_error':float(abs(conserved-alpha**2)/alpha**2)})
        self.assertLess(abs(rows[-1]['pump_amplitude_shift']-.5),2e-4)
        REPORT['source_dictionary']={'fixed_gain_pump_only_amplitude':str(-A/a),
            'fixed_gain_entangled_amplitude':str(-B/a),
            'leading_inverse_amplitude_impurity_series':str(series),
            'source_tau8_subleading_term':'-2*r^8/(9*alpha^4) in impurity; not in leading alpha^-2 term',
            'self_consistent_frame':rows,
            'attribution':'CQ Appendix C Eqs. 99-100; the fixed-gain resummation and limit here are reconstructions, not quoted source results.'}

    def test_02_number_marking_norm_bound(self):
        # Exact finite-core polynomial certificate for the new Duhamel remainder.
        n=7;c=sp.zeros(n);kp=sp.zeros(n)
        for j in range(1,n):c[j-1,j]=sp.sqrt(j);kp[j,j-1]=j
        p=c-c.T;q=sp.diag(*[2*j+1 for j in range(n)])
        R=kp+kp.T+q;L=kp+kp.T-q;A=kp-kp.T
        I=sp.eye(n);pp=sp.kronecker_product(p,I)
        RR=sp.kronecker_product(I,R);LL=sp.kronecker_product(I,L);AA=sp.kronecker_product(I,A)
        v=sp.zeros(n*n,1);v[0]=1
        first=pp*(RR-2*sp.eye(n*n))*v
        self.assertEqual((first.T*first)[0],2)
        x=sp.symbols('x',real=True)
        second=pp*(LL-4*x*pp*AA+4*x*x*pp*pp*RR)*v
        self.assertEqual(sp.expand((second.T*second)[0]),2+48*x*x+480*x**4)
        rows=[]
        for alpha in (10.,100.,1000.):
            for lam in (.1,.5,1.):
                distance,quad_error=pure_phase_overlap(alpha,lam)
                extra=norm_bounds(alpha,lam)[1]
                self.assertLess(distance,extra+2e-10)
                for pvalue in (-1.1,0.,.7):
                    coef,z=phase_geometric(alpha,lam,pvalue)
                    self.assertAlmostEqual(abs(coef)**2/(1-abs(z)**2),1,places=11)
                rows.append({'alpha':alpha,'lambda':lam,'joint_state_distance':float(distance),
                             'analytic_upper':float(extra),'quadrature_error_on_squared_distance':float(quad_error)})
        REPORT['number_marking']={'finite_polynomial_dimension':n*n,'comparisons':rows,
            'operator':'B_alpha=S(-r)n_a S(r)/(2alpha)=[exp(2r)R-exp(-2r)L-2I]/(8alpha)',
            'extra_norm_upper':'[sqrt(2)+exp(-2r)*sqrt(2+48lambda^2+480lambda^4)]/(8alpha)'}

    def test_03_exact_reduced_state_comparison(self):
        rows=[]
        for alpha in (10.,100.,1000.):
            lam=.5;state,nfev=exact_frame(alpha,lam,48,96)
            rho=state.T@state
            model=phase_frame_density(alpha,lam,96,160)
            model2=phase_frame_density(alpha,lam,96,240)
            eig=np.linalg.eigvalsh(rho-model)
            distance=.5*np.sum(abs(eig))
            purity_exact=np.sum(rho*rho)
            purity_model=np.sum(abs(model)**2)
            delta=sum(norm_bounds(alpha,lam))
            self.assertLess(abs(np.linalg.norm(state)-1),2e-10)
            self.assertLess(distance,delta+1e-8)
            self.assertLess(np.linalg.norm(model-model2),1e-9)
            self.assertGreater(np.trace(model).real,1-2e-7)
            self.assertLess(abs(purity_exact-purity_model),4*delta+1e-8)
            if alpha==10:
                # Check actual physical counts, not only unsqueezed-frame quantities.
                from scipy.sparse import diags
                from scipy.sparse.linalg import expm_multiply
                size=384;weights=np.arange(1,size,dtype=float)
                squeeze=diags(weights,-1,shape=(size,size))-diags(weights,1,shape=(size,size))
                embedded=np.zeros((size,48));embedded[:96,:]=state.T
                physical=expm_multiply(gain(alpha,lam)*squeeze,embedded)
                counts=np.sum(physical**2,axis=1)
                qq=np.tanh(gain(alpha,lam))**2
                geometric=(1-qq)*qq**np.arange(size)
                tv=.5*np.sum(abs(counts-geometric))
                self.assertLess(tv,distance+1e-6)
                self.assertLess(np.sum(counts[-10:]),1e-10)
            else:tv=None
            rows.append({'alpha':alpha,'lambda':lam,'trace_distance_to_phase_model':float(distance),
                         'analytic_distance_upper':float(delta),'exact_purity':float(purity_exact),
                         'phase_model_purity':float(purity_model),'exact_tmsv_fidelity':float(rho[0,0]),
                         'phase_model_tmsv_fidelity':float(model[0,0].real),
                         'phase_quadrature_refinement':float(np.linalg.norm(model-model2)),
                         'retained_phase_model_trace':float(np.trace(model).real),
                         'physical_count_total_variation_if_tested':None if tv is None else float(tv),
                         'pump_cutoff':48,'frame_pair_cutoff':96,'frame_amplitudes':4608,
                         'function_evaluations':nfev})
        self.assertGreater(rows[0]['trace_distance_to_phase_model'],rows[-1]['trace_distance_to_phase_model'])
        REPORT['state_comparison']={'runs':rows,'numerical_warning':'Finite-cutoff tests; the trace-norm theorem is analytical. Physical-count conversion diagnostic at alpha=10 uses 18432 matrix amplitudes.'}

    def test_04_onset_and_source_polynomial(self):
        eps=.01;star=brentq(lambda l:purity(l)-1+eps,.01,.2,xtol=5e-15)
        rows=[]
        for alpha in (30.,100.,1000.,10000.):
            def residual(l):
                state,_=exact_frame(alpha,l,16,32,rtol=2e-11,atol=2e-13)
                rho=state@state.T
                return np.sum(rho*rho)-1+eps
            root=brentq(residual,.05,.2,xtol=5e-12)
            exacttau=gain(alpha,root)/alpha
            A=4*alpha**6/45-2*alpha**4/9;B=2*alpha**4/9
            # Solve directly in gain to avoid powers of a tiny time.
            rpoly=brentq(lambda r:A*(r/alpha)**8+B*(r/alpha)**6-eps,.01,100)
            asymptau=gain(alpha,star)/alpha
            rows.append({'alpha':alpha,'exact_frame_onset_tau':float(exacttau),
                         'CQ_eighth_order_root_tau':float(rpoly/alpha),
                         'controlled_crossover_estimate_tau':float(asymptau),
                         'onset_lambda':float(root), 'distance_to_asymptotic_lambda':float(abs(root-star)), 'within_0_001_of_limit':bool(abs(root-star)<.001)})
        self.assertLess(abs(rows[-1]['onset_lambda']-star),.001)
        a,r=sp.symbols('a r',positive=True)
        imp=sp.Rational(2,9)*a**4*(r/a)**6+(sp.Rational(4,45)*a**6-sp.Rational(2,9)*a**4)*(r/a)**8
        self.assertEqual(sp.simplify(imp-((sp.Rational(2,9)*r**6+sp.Rational(4,45)*r**8)/a**2-sp.Rational(2,9)*r**8/a**4)),0)
        decay=sp.limit(imp.subs(r,sp.log(a)/2),a,sp.oo)
        self.assertEqual(decay,0)
        REPORT['onset_comparison']={'target_fixed_impurity':eps,'limiting_lambda':float(star),
            'logarithmic_offset':float(np.log(8*star)),'matched_roots':rows,
            'eighth_order_impurity_at_logarithmic_gain_limit':str(decay),
            'qualification':'Finite roots are our recalculation, not digitized source data; source cutoff-normalized target tends to this fixed target.'}

    def test_05_phase_sensitive_vs_number_conserving_tests(self):
        alpha=5.;r=1.1;cut=9;Kmax=4
        from scipy.linalg import block_diag
        lower=np.diag(np.sqrt(np.arange(1,cut)),1)
        a=np.kron(lower,np.eye(cut));b=np.kron(np.eye(cut),lower)
        Ntot=a.T@a+b.T@b
        U=expm(.37*(a.T@b-a@b.T))
        self.assertLess(np.linalg.norm(U@Ntot-Ntot@U),2e-13)
        amp=np.tanh(r)**np.arange(Kmax+1);amp/=np.linalg.norm(amp)
        ket=np.zeros(cut*cut)
        idx=np.arange(Kmax+1)*(cut+1);ket[idx]=amp
        pure=np.outer(ket,ket)
        mixed=np.zeros_like(pure)
        k=np.arange(Kmax+1)
        block=np.outer(amp,amp)*np.exp(-(k[:,None]-k[None,:])**2/(8*alpha**2))
        mixed[np.ix_(idx,idx)]=block
        countdiff=np.max(abs(np.diag(U@mixed@U.T)-np.diag(U@pure@U.T)))
        self.assertLess(countdiff,2e-14)
        self.assertLess(np.trace(mixed@pure),1)
        lam=.5
        P=purity(lam);F=purity(lam/np.sqrt(2))
        REPORT['measurement_control']={'two_mode_hilbert_dimension':cut*cut,
            'max_count_difference_after_passive_beam_splitter':float(countdiff),
            'finite_pure_target_fidelity':float(np.trace(mixed@pure)),
            'lambda':lam,'limit_purity':P,'limit_target_fidelity':F,
            'limit_trace_distance_lower_from_target_projector':1-F,
            'scope':'Total-number-conserving measurements and vacuum ancillas only. Additional phase references or active processing are not included.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error('Use a new evidence path')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',groups=result.testsRun,
                  prior_scientific_modules_imported=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(REPORT,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
