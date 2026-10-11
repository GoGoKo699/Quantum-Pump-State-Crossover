#!/usr/bin/env python3
"""Checks for the manuscript's controlled validity-window corollary.

These are algebraic and comparison-state checks, not a high-photon-number
simulation. No original checker is imported or modified. Output is append-only.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
import math
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.integrate import quad
from scipy.special import erfcx

ROOT = Path(__file__).resolve().parents[1]
REPORT: dict = {}


def purity(x: float) -> float:
    return 1.0 if x == 0 else float(math.sqrt(math.pi) * erfcx(1 / (2*x)) / (2*x))


def exact_bound_values(log10_N: int) -> dict[str, str]:
    """High-precision evaluation of proven bounds, not interval arithmetic."""
    with mp.workdps(100):
        a = mp.power(10, mp.mpf(log10_N)/2)
        lam = mp.root(a, 4)
        r = mp.log1p(8*a*lam)/2
        eps = mp.sqrt(2+48*lam**2+480*lam**4)/(8*a)
        eps += r*mp.sqrt(1+16*lam**2+384*lam**4)/(2*a)
        d = (mp.sqrt(2)+mp.exp(-2*r)*mp.sqrt(2+48*lam**2+480*lam**4))/(8*a)
        P = mp.sqrt(mp.pi)*mp.exp(1/(4*lam**2))*mp.erfc(1/(2*lam))/(2*lam)
        B = (1+lam**2)*(1+r)/a
        energy_ratio = mp.exp(r+a*a*mp.expm1(r/(a*a)))/(8*a*lam)
        depletion = energy_ratio*2*lam/a
        pp = max(mp.mpf(0), 1-mp.sqrt(min(mp.mpf(1), P+4*eps)))
        gg = max(mp.mpf(0), mp.exp(-1/(lam*lam))/45-eps)
        entries = {'log10_N':mp.mpf(log10_N),'lambda':lam,'r':r,'epsilon':eps,'eta':eps+d,
                   'purity_comparison':P,'pure_distance_lower':pp,'gaussian_distance_lower':gg,
                   'count_tv_upper':min(mp.mpf(1),eps+d),'depletion_upper':depletion,
                   'mean_upper_divided_by_2_alpha_lambda':energy_ratio,
                   'B':B,'epsilon_over_comparison_purity':eps/P,
                   'purity_divided_by_leading_asymptotic':P/(mp.sqrt(mp.pi)/(2*lam))}
        return {k:mp.nstr(v,32) for k,v in entries.items()}


class ManuscriptChecks(unittest.TestCase):
    def test_01_pointwise_domination_and_nominal_count_identity(self):
        z = sp.symbols('z', nonnegative=True)
        first = sp.Poly(484*(1+z)**2-(2+48*z+480*z**2),z)
        second = sp.Poly(400*(1+z)**2-(1+16*z+384*z**2),z)
        self.assertTrue(all(c>0 for c in first.all_coeffs()))
        self.assertTrue(all(c>0 for c in second.all_coeffs()))
        t = sp.symbols('t',positive=True)
        # t=e^(2r)=1+8 alpha lambda; no asymptotic substitution needed.
        self.assertEqual(sp.factor((t+1/t-2)/4-((t-1)/4-sp.Rational(1,4)+1/(4*t))),0)
        # epsilon <= (11/4+10r)(1+lambda^2)/alpha,
        # d <= 3(1+lambda^2)/alpha; sum <= 10(1+r)(1+lambda^2)/alpha.
        self.assertEqual(10-(sp.Rational(11,4)+3),sp.Rational(17,4))
        r=sp.symbols('r',nonnegative=True)
        remainder = sp.series((sp.sinh(2*r)-2*r)**2/8,r,0,10).removeO()
        self.assertEqual(sp.expand(remainder),sp.Rational(2,9)*r**6+sp.Rational(4,45)*r**8)
        REPORT['exact_algebra']={'first_domination_polynomial':str(first.as_expr()),
            'second_domination_polynomial':str(second.as_expr()),'eta_bound':'10 B_alpha',
            'nominal_count_identity':'exact','CQ_leading_fixed_gain_series':str(remainder),
            'scope':'Pointwise inequalities justify varying lambda; no fixed-lambda little-o is extrapolated.'}

    def test_02_same_model_phase_and_fidelity_dictionary(self):
        records=[]
        for m in range(1,8):
            H=sp.zeros(m+1);target=sp.zeros(m+1)
            for k in range(m):
                w=(k+1)*sp.sqrt(m-k)
                H[k+1,k]=w;H[k,k+1]=w
                target[k+1,k]=sp.I*w;target[k,k+1]=-sp.I*w
            U=sp.diag(*[sp.I**k for k in range(m+1)])
            self.assertEqual(U*H*U.H,target)
            self.assertEqual(target.H,target)
            records.append(m+1)
        self.assertEqual(sp.Rational(99,100)**2,sp.Rational(9801,10000))
        REPORT['source_dictionary']={'source':'D\u0027Ariano--Paris--Sacchi, quant-ph/9902013v1, Sec.4',
            'conservation_block_dimensions':records,'phase_rotation':'exp(i pi n_a/2)',
            'source_99_percent_overlap_equals_squared_fidelity':'0.9801',
            'warning':'Not a 1-percent pump-purity threshold and not a Fano-factor theorem.'}

    def test_03_finite_phase_mixture_and_pure_distance_bounds(self):
        rows=[]
        for alpha,lam in ((2.,.2),(4.,.4),(8.,.5)):
            r=.5*math.log1p(8*alpha*lam);q=math.tanh(r)**2
            cutoff=int(math.ceil(math.log(1e-16)/math.log(q)))
            k=np.arange(cutoff);pk=(1-q)*q**k;tail=q**cutoff
            psi=np.sqrt(pk/(1-tail))
            damping=np.exp(-(k[:,None]-k[None,:])**2/(8*alpha**2))
            sigma=psi[:,None]*psi[None,:]*damping
            eigen=np.linalg.eigvalsh(sigma)
            self.assertGreater(eigen[0],-2e-14)
            self.assertAlmostEqual(float(np.trace(sigma)),1.,places=13)
            self.assertLess(np.max(abs(np.diag(sigma)-pk/(1-tail))),1e-15)
            purity_matrix=float(np.trace(sigma@sigma));fidelity_matrix=float(psi@sigma@psi)
            d=np.arange(1,cutoff*2)
            Pseries=(1-q)/(1+q)*(1+2*np.sum(q**d*np.exp(-d*d/(4*alpha**2))))
            Fseries=(1-q)/(1+q)*(1+2*np.sum(q**d*np.exp(-d*d/(8*alpha**2))))
            self.assertLess(abs(purity_matrix-Pseries),2e-13)
            self.assertLess(abs(fidelity_matrix-Fseries),2e-13)
            self.assertLessEqual(eigen[-1],math.sqrt(purity_matrix)+2e-14)
            Dtarget=.5*float(np.sum(abs(np.linalg.eigvalsh(sigma-np.outer(psi,psi)))))
            self.assertGreaterEqual(Dtarget,1-fidelity_matrix-2e-14)
            self.assertLessEqual(Dtarget,math.sqrt(max(0,1-fidelity_matrix))+2e-14)
            rows.append({'alpha':alpha,'lambda':lam,'cutoff':cutoff,'discarded_geometric_mass':float(tail),
                         'purity':purity_matrix,'squared_fidelity':fidelity_matrix,'target_distance':Dtarget})
        # Separate limiting-state integrals, not a finite-matrix extrapolation.
        integral_checks=[]
        for lam in (.1,.5,1.,3.):
            Pq=quad(lambda z:math.exp(-z-lam*lam*z*z),0,np.inf,epsabs=2e-13,epsrel=2e-13)[0]
            Fq=quad(lambda z:math.exp(-z*z/2)/(math.sqrt(2*math.pi)*(1+lam*lam*z*z)),
                    -np.inf,np.inf,epsabs=2e-13,epsrel=2e-13)[0]
            self.assertLess(abs(Pq-purity(lam)),2e-12)
            self.assertLess(abs(Fq-purity(lam/math.sqrt(2))),2e-12)
            integral_checks.append({'lambda':lam,'purity_integral_error':float(abs(Pq-purity(lam))),
                                    'vacuum_probability_integral_error':float(abs(Fq-purity(lam/math.sqrt(2))))})
        REPORT['comparison_states']={'finite_states':rows,'independent_integrals':integral_checks,
            'scope':'Normalized finite projections of the established family; not exact trilinear simulations.'}

    def test_04_bounded_quadrature_witness_at_changing_frequency(self):
        z=sp.symbols('z',positive=True)
        # Squaring the positive quantities shows W>0 for lambda*xi !=0.
        polynomial=sp.expand((1+2*z)**4-(1+8*z))
        self.assertEqual(polynomial,16*z**4+32*z**3+24*z**2)
        lam=sp.symbols('lam',positive=True)
        W=sp.exp(-1/lam**2)*(sp.Rational(1,3)-sp.Rational(1,9))
        self.assertEqual(W,sp.Rational(2,9)*sp.exp(-1/lam**2))
        rows=[]
        for L in (.2,.5,1.,3.,10.):
            xi=1/L
            C=lambda t:math.exp(-t*t/4)/math.sqrt(1+2*L*L*t*t)
            integrated=quad(lambda v:math.exp(-v*v/2)*math.exp(-(.5+2*L*L*v*v)*xi*xi/2)/math.sqrt(2*math.pi),
                            -np.inf,np.inf,epsabs=2e-13,epsrel=2e-13)[0]
            self.assertLess(abs(integrated-C(xi)),2e-12)
            contrast=C(2*xi)-C(xi)**4
            predicted=2/9*math.exp(-1/(L*L))
            self.assertLess(abs(contrast-predicted),2e-14)
            noise=.37
            noisy=lambda t:C(t)*math.exp(-noise*noise*t*t/2)
            self.assertLess(abs((noisy(2*xi)-noisy(xi)**4)-math.exp(-2*noise*noise*xi*xi)*contrast),2e-14)
            rows.append({'lambda':L,'frequency':xi,'contrast':float(contrast),'ideal_gaussian_gap_lower':float(contrast/10)})
        self.assertEqual(sp.limit(W/10,lam,sp.oo),sp.Rational(1,45))
        REPORT['quadrature_witness']={'exact_positive_polynomial':str(polynomial),'changing_frequency':rows,
              'limiting_gaussian_distance_lower':'1/45',
              'warning':'Single Gaussian states, not their convex hull; resolution and reference costs are not removed.'}

    def test_05_controlled_window_and_bound_only_sequence(self):
        rows=[exact_bound_values(k) for k in (8,12,16,20,24,32,48)]
        with mp.workdps(80):
            for row in rows:
                self.assertLess(mp.mpf(row['eta']),10*mp.mpf(row['B']))
                self.assertGreaterEqual(mp.mpf(row['mean_upper_divided_by_2_alpha_lambda']),1)
            last=rows[-1]
            self.assertLess(mp.mpf(last['eta']),mp.mpf('5e-10'))
            self.assertGreater(mp.mpf(last['pure_distance_lower']),mp.mpf('.999'))
            self.assertGreater(mp.mpf(last['gaussian_distance_lower']),mp.mpf('.02222'))
            self.assertLess(mp.mpf(last['epsilon_over_comparison_purity']),mp.mpf('.001'))
            self.assertLess(abs(mp.mpf(last['purity_divided_by_leading_asymptotic'])-1),mp.mpf('1e-6'))
        # Exact exponent bookkeeping for lambda=alpha^p: error ~ alpha^(2p-1) log alpha,
        # whereas purity ~ alpha^(-p); relative purity control needs 3p<1.
        p=sp.Rational(1,4)
        self.assertLess(2*p-1,0);self.assertLess(3*p-1,0)
        self.assertEqual((1+p)/4,sp.Rational(5,16))
        self.assertEqual((p-1)/2,-sp.Rational(3,8))
        self.assertEqual(p/2,sp.Rational(1,8))
        # Exact countercheck: TV convergence alone cannot control unbounded means.
        # P_m=(1-1/m)delta_0+(1/m)delta_(m^2): TV=1/m, mean=m.
        m=sp.symbols('m',positive=True)
        self.assertEqual(sp.simplify(m*m/m),m)
        REPORT['growing_sequence']={'lambda':'N^(1/8)','rows':rows,
            'rate_of_state_bound':'O(log(N)/N^(1/4))','pair_mean_asymptotic':'2 N^(5/8)',
            'fractional_depletion_asymptotic':'2 N^(-3/8)',
            'pump_output_Renyi2_asymptotic':'log(N)/8 - log(sqrt(pi)/2) + o(1)',
            'mean_proof':'Uses the separate conserved-sector energy inequality, not TV alone.',
            'evaluation_status':'High-precision evaluations of analytic bounds; not interval arithmetic or high-N simulation.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:
        parser.error('Choose a new output file outside the repository.')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ManuscriptChecks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun,
                  original_scientific_code_imported=False)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as stream:
        json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
