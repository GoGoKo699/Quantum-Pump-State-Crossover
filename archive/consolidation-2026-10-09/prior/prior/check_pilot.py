#!/usr/bin/env python3
"""Five independently specified check groups for the fresh pump pilot.

These are author-side algebraic and finite-dimensional diagnostics. They do not
establish prior-work novelty or replace the infinite-dimensional proof in PILOT.
"""
from __future__ import annotations
import argparse, json, sys, unittest
from pathlib import Path
sys.dont_write_bytecode=True
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import roots_laguerre
from scipy.sparse.linalg import expm_multiply
from pump_model import (operators,evolve_frame,evolve_number_sectors,purity_limit,
                        norm_error_bound,time_gain,depletion_fraction_upper)
REPORT={}

class Checks(unittest.TestCase):
    def test_01_exact_algebra_and_duhamel_vectors(self):
        # Exact finite-core polynomial actions; all occupied states lie below cutoff.
        n=7
        c=sp.zeros(n);kp=sp.zeros(n)
        for j in range(1,n):c[j-1,j]=sp.sqrt(j);kp[j,j-1]=j
        p=c-c.T;t=c+c.T;km=kp.T;q=sp.diag(*[2*j+1 for j in range(n)])
        R=kp+km+q;L=kp+km-q;D=kp-km;I=sp.eye(n)
        core=sp.eye(n)[:,:3]
        self.assertEqual((R*D-D*R-2*R)*core,sp.zeros(n,3))
        self.assertEqual((R*L-L*R-4*D)*core,sp.zeros(n,3))
        x=sp.symbols('x',real=True)
        pp=sp.kronecker_product(p,I);tt=sp.kronecker_product(t,I)
        RR=sp.kronecker_product(I,R);LL=sp.kronecker_product(I,L);DD=sp.kronecker_product(I,D)
        vac=sp.zeros(n*n,1);vac[0]=1
        A=pp*(LL-4*x*pp*DD+4*x*x*pp*pp*RR)*vac
        B=(tt-2*x*RR)*(DD-2*x*pp*RR)*vac
        normA=sp.expand((A.T*A)[0]);normB=sp.expand((B.T*B)[0])
        self.assertEqual(normA,2+48*x*x+480*x**4)
        self.assertEqual(normB,1+16*x*x+384*x**4)
        u=sp.symbols('u',real=True)
        self.assertEqual(sp.simplify(sp.cosh(u)**2-(sp.exp(2*u)+sp.exp(-2*u)+2)/4),0)
        self.assertEqual(sp.simplify(sp.cosh(u)*sp.sinh(u)-(sp.exp(2*u)-sp.exp(-2*u))/4),0)
        REPORT['algebra']={'A_norm_squared':str(normA),'B_norm_squared':str(normB),
            'core_dimension':n*n,'scope':'No truncated commutator is asserted at its artificial boundary.'}

    def test_02_purity_and_bounded_characteristic(self):
        records=[]
        nodes,weights=roots_laguerre(100)
        for lam in (.05,.1,.25,.5,1.):
            direct=quad(lambda x:np.exp(-x-lam*lam*x*x),0,np.inf,epsabs=2e-13)[0]
            two=float(weights@np.exp(-lam*lam*(nodes[:,None]-nodes[None,:])**2)@weights)
            self.assertAlmostEqual(direct,purity_limit(lam),places=12)
            # Large lambda converges more slowly with finite Gauss--Laguerre nodes.
            if lam<=.5:self.assertLess(abs(two-direct),2e-10)
            chi=quad(lambda x:np.exp(-x)*np.cos(np.sqrt(2)*lam*.7*x),0,np.inf)[0]
            chi-=1j*quad(lambda x:np.exp(-x)*np.sin(np.sqrt(2)*lam*.7*x),0,np.inf)[0]
            self.assertLess(abs(chi-1/(1+1j*np.sqrt(2)*lam*.7)),1e-10)
            records.append({'lambda':lam,'purity':direct,'double_quadrature':two,
                            'squeezed_vacuum_fidelity':purity_limit(lam/np.sqrt(2))})
        # Independent limiting-unitary Fock calculation at a modest lambda.
        c,kp,km,q,p,t,R,L,D=operators(48,96)
        from scipy.sparse import kron
        vac=np.zeros(48*96);vac[0]=1
        v=expm_multiply(.25*kron(p,R),vac).reshape(48,96)
        rho=v@v.T
        self.assertLess(abs(np.sum(rho*rho)-purity_limit(.25)),1e-10)
        self.assertLess(abs(np.sum(v[:,0]**2)-purity_limit(.25/np.sqrt(2))),1e-10)
        REPORT['limit_state']=records

    def test_03_independent_conserved_sector_dynamics(self):
        rows=[]
        for alpha,lam,M in ((2.,.25,48),(4.,.25,72)):
            r,tau=time_gain(alpha,lam)
            direct=evolve_number_sectors(alpha,tau,M)
            framed=evolve_frame(alpha,lam,M+1,M+1)
            c,kp,km,q,p,t,R,L,D=operators(M+1,M+1)
            shifted=expm_multiply(alpha*p,direct['state'])
            transformed=expm_multiply(-r*D,shifted.T).T
            normdiff=float(np.linalg.norm(transformed-framed['state']))
            self.assertLess(normdiff,2e-8)
            self.assertLess(abs(direct['purity']-framed['purity']),1e-9)
            self.assertLess(abs(direct['depletion_fraction']-framed['depletion_fraction']),1e-9)
            self.assertGreater(direct['retained_probability'],1-2e-13)
            self.assertLess(direct['depletion_fraction'],depletion_fraction_upper(alpha,lam))
            rows.append({'alpha':alpha,'lambda':lam,'sector_max':M,'retained_initial_probability':direct['retained_probability'],
                         'state_norm_difference':normdiff,'purity':direct['purity'],
                         'purity_difference':abs(direct['purity']-framed['purity'])})
        REPORT['independent_number_sectors']=rows

    def test_04_finite_amplitude_crossover_and_refinement(self):
        rows=[]
        for alpha in (10.,100.,1000.):
            low=evolve_frame(alpha,.5,48,80,rtol=1e-10,atol=1e-12)
            high=evolve_frame(alpha,.5,72,112,rtol=3e-11,atol=3e-13)
            self.assertLess(abs(low['purity']-high['purity']),2e-8)
            self.assertLess(high['state_norm_error_to_limit_truncation'],high['analytic_state_error_bound']+1e-7)
            self.assertLess(abs(high['purity']-high['limit_purity']),4*high['analytic_state_error_bound']+2e-8)
            self.assertLess(high['depletion_fraction'],high['depletion_upper'])
            data={k:v for k,v in high.items() if k not in ('rho_p_displaced','state')}
            data['purity_refinement_difference']=abs(low['purity']-high['purity'])
            data['depletion_refinement_difference']=abs(low['depletion_fraction']-high['depletion_fraction'])
            rows.append(data)
        self.assertGreater(rows[0]['purity'],rows[1]['purity'])
        self.assertGreater(rows[1]['purity'],rows[2]['purity'])
        REPORT['crossover_diagnostics']=rows

    def test_05_fixed_purity_loss_and_energy_bound(self):
        eps=.01
        lamstar=brentq(lambda x:purity_limit(x)-(1-eps),.01,.2,xtol=1e-14)
        offset=np.log(8*lamstar)
        rows=[]
        for alpha in (30.,100.,1000.):
            root=brentq(lambda x:evolve_frame(alpha,x,14,24,rtol=5e-11,atol=5e-13)['purity']-(1-eps),
                        .03,.3,xtol=5e-12)
            r,tau=time_gain(alpha,root)
            rows.append({'alpha':alpha,'numerical_lambda_at_1_percent_loss':root,'tau':tau,
                        'two_alpha_tau_minus_log_alpha':2*r-np.log(alpha)})
        self.assertLess(abs(rows[-1]['two_alpha_tau_minus_log_alpha']-offset),.025)
        a=1e6;lam=.5;r,tau=time_gain(a,lam)
        A=np.sqrt(2+48*lam*lam+480*lam**4)
        B=np.sqrt(1+16*lam*lam+384*lam**4)
        coarse=A/(8*a)+r*B/(2*a)
        self.assertLess(norm_error_bound(a,lam),coarse)
        self.assertLess(4*coarse,9e-5)
        self.assertLess(depletion_fraction_upper(a,lam),1.000001e-6)
        REPORT['fixed_threshold']={'purity_loss':eps,'limiting_lambda':lamstar,
            'asymptotic_offset':offset,'finite_amplitude_roots':rows,
            'large_N_rigorous_bound_example':{'alpha':a,'mean_pump_photons':a*a,'lambda':lam,
                'purity_center':purity_limit(lam),'conservative_purity_radius':4*coarse,
                'fractional_depletion_upper':depletion_fraction_upper(a,lam)},
            'scope':'Small finite root diagnostics; no fit used to establish the logarithmic asymptotic.'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():ap.error('Use a new evidence filename')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',groups=result.testsRun,
                  new_research_only=True,old_scientific_modules_imported=False)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(REPORT,indent=2,sort_keys=True,allow_nan=False)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
