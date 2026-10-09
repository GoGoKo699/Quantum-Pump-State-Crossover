#!/usr/bin/env python3
"""Independent algebraic and exact-arithmetic checks of the scoped proof review.

No archived scientific module is imported. The first-crossing witnesses use
rational arithmetic and analytic remainder bounds, not a fitted trajectory.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
import math
from pathlib import Path
import sys
import unittest
import sympy as sp

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
REPORT: dict = {}


def exp_bounds(x: F, terms: int = 120) -> tuple[F, F]:
    """Enclose exp(x) by a positive Taylor sum and a geometric tail."""
    if x < 0 or x >= terms + 2:
        raise ValueError('Need 0 <= x < terms+2')
    term = F(1)
    partial = term
    for k in range(1, terms + 1):
        term *= x / k
        partial += term
    next_term = term * x / (terms + 1)
    return partial, partial + next_term / (1 - x / (terms + 2))


def sqrt_upper(x: F, digits: int = 12) -> F:
    """Rational upward enclosure, checked by squaring; no floating input."""
    if x < 0:
        raise ValueError('Nonnegative radicand required')
    scale = 10 ** digits
    m = math.isqrt(x.numerator * scale * scale // x.denominator)
    if F(m, scale) ** 2 < x:
        m += 1
    result = F(m, scale)
    assert result * result >= x
    return result


def purity_bounds(lam: F, order: int = 16) -> tuple[F, F]:
    """Odd/even Taylor enclosures after integration against exp(-z)."""
    if lam < 0 or order < 2 or order % 2:
        raise ValueError('Need lam >= 0 and an even order')
    terms = [F((-1) ** j * math.factorial(2 * j), math.factorial(j)) * lam ** (2 * j)
             for j in range(order + 1)]
    return sum(terms[:-1], F(0)), sum(terms, F(0))


def error_upper(alpha: int, lam: F, gain_upper: F) -> F:
    """Enclose the unchanged theorem's epsilon using rational upper roots."""
    return (sqrt_upper(2 + 48 * lam ** 2 + 480 * lam ** 4) / (8 * alpha)
            + gain_upper * sqrt_upper(1 + 16 * lam ** 2 + 384 * lam ** 4) / (2 * alpha))


def fraction_record(x: F) -> dict:
    return {'exact': str(x), 'decimal_diagnostic': float(x)}


def gaussian_moment(poly, variables):
    """Independent standard-normal moment functional on a polynomial."""
    value = 0
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        if any(n % 2 for n in powers):
            continue
        factor = sp.prod(sp.factorial2(n - 1) if n else 1 for n in powers)
        value += coefficient * factor
    return sp.factor(value)


class ProofChecks(unittest.TestCase):
    def test_01_continuous_coordinate_remainder_norms(self):
        x, y, z, ell = sp.symbols('x y z ell', real=True)
        R = (x*x + y*y) / 2
        phase = -(x*x + y*y + z*z) / 4 + sp.I * ell * z * R
        # p=i z, L=2(derivative_x^2+derivative_y^2),
        # A=-(x derivative_x+y derivative_y+1), T=2i derivative_z.
        # Differentiate exp(phase) via its polynomial logarithmic derivative:
        # this cancels the nonzero exponential exactly, without heuristic simplify.
        pL = sp.expand(sp.I*z*2*(sp.diff(phase,x,2)+sp.diff(phase,x)**2
                                  +sp.diff(phase,y,2)+sp.diff(phase,y)**2))
        A_ratio = -(x*sp.diff(phase,x)+y*sp.diff(phase,y)+1)
        TA = sp.expand(2*sp.I*(sp.diff(A_ratio,z)+A_ratio*sp.diff(phase,z)))
        norm_pL = gaussian_moment(pL*sp.conjugate(pL), (x,y,z))
        norm_TA = gaussian_moment(TA*sp.conjugate(TA), (x,y,z))
        self.assertEqual(sp.expand(norm_pL),2+48*ell**2+480*ell**4)
        self.assertEqual(sp.expand(norm_TA),1+16*ell**2+384*ell**4)
        self.assertEqual(gaussian_moment(z*z*(R-2)**2,(x,y,z)),2)
        # Multiplication by R and radial dilation reproduce the exact commutator.
        f = x**3*y + z*x
        A = lambda v: -(x*sp.diff(v,x)+y*sp.diff(v,y)+v)
        self.assertEqual(sp.expand(R*A(f)-A(R*f)),sp.expand(2*R*f))
        REPORT['coordinate_reconstruction']={'pL_squared_norm':str(norm_pL),
            'TA_squared_norm':str(norm_TA),'number_marking_squared_norm':2,
            'representation':'Three real quadrature coordinates; exact Gaussian polynomial integration.',
            'archived_modules_imported':False}

    def test_02_sector_energy_and_geometric_truncation(self):
        checks=[]
        for m in (1,3,7):
            # Exact real amplitudes; signs include cases with decreasing population.
            for sign in (1,-1):
                raw=[F(sign**k*(k+1)) for k in range(m+1)]
                norm=sum(v*v for v in raw)
                mean=sum(F(k)*v*v for k,v in enumerate(raw))/norm
                flux=2*sum((k+1)*sp.sqrt(m-k)*sp.Rational(raw[k]*raw[k+1]/norm)
                           for k in range(m))
                square_bound=4*m*sp.Rational(mean*(mean+1))
                self.assertTrue(bool(sp.simplify(square_bound-flux**2)>=0))
                checks.append({'pump_sector':m,'amplitude_sign':sign,'mean_pairs':str(mean)})
        q=sp.Rational(2,3)
        for cutoff in (1,4,12):
            # Tail-sum identity for a nonnegative integer variable, exact here.
            truncated=sum(q**j for j in range(1,cutoff+1))
            self.assertEqual(truncated,q*(1-q**cutoff)/(1-q))
        alpha,lam=sp.symbols('alpha lam',positive=True)
        u=1+8*alpha*lam
        mean_nominal=(u-1)**2/(4*u)
        self.assertEqual(sp.limit(mean_nominal/alpha,alpha,sp.oo),2*lam)
        REPORT['energy_check']={'exact_sector_checks':checks,'mean_scaling':'2*lambda',
            'moment_argument':'Independent sector upper bound plus bounded truncated expectations; not total variation alone.'}

    def test_03_rational_first_crossing_certificates(self):
        witnesses=[
            (10000,'0.068','0.0755',('4.3008590732','4.3008590733'),('4.3531624200','4.3531624201')),
            (100000,'0.0713','0.0723',('5.4757627932','5.4757627933'),('5.4827265728','5.4827265729')),
            (1000000,'0.07172','0.07183',('6.6299841061','6.6299841062'),('6.6307503884','6.6307503885'))]
        rows=[]
        threshold=F(99,100)
        for alpha,lo,hi,glo,ghi in witnesses:
            lo,hi=F(lo),F(hi)
            glo,ghi=tuple(map(F,glo)),tuple(map(F,ghi))
            for lam,gain in ((lo,glo),(hi,ghi)):
                exp_lo=exp_bounds(2*gain[0]);exp_hi=exp_bounds(2*gain[1])
                self.assertLess(exp_lo[1],1+8*alpha*lam)
                self.assertGreater(exp_hi[0],1+8*alpha*lam)
            p_lo=purity_bounds(lo);p_hi=purity_bounds(hi)
            e_lo=error_upper(alpha,lo,glo[1]);e_hi=error_upper(alpha,hi,ghi[1])
            lower_margin=p_lo[0]-4*e_lo-threshold
            upper_margin=threshold-p_hi[1]-4*e_hi
            self.assertGreater(lower_margin,0)
            self.assertGreater(upper_margin,0)
            rows.append({'alpha':alpha,'N':alpha**2,'lambda_interval':[str(lo),str(hi)],
                'dimensionless_time_interval':[fraction_record(glo[0]/alpha),fraction_record(ghi[1]/alpha)],
                'strict_lower_purity_margin':fraction_record(lower_margin),
                'strict_upper_purity_margin':fraction_record(upper_margin),
                'purity_enclosure_widths':[fraction_record(p_lo[1]-p_lo[0]),fraction_record(p_hi[1]-p_hi[0])],
                'state_error_upper':[fraction_record(e_lo),fraction_record(e_hi)]})
        REPORT['first_crossing']={'purity_loss':'1/100','rows':rows,
            'arithmetic':'Exact fractions; integrated Taylor sign bounds, positive exponential tail bounds, upward square-root enclosures.',
            'claim':'The exact infinite-dimensional first crossing lies in every displayed time interval. No exact-purity monotonicity or simulated trajectory is assumed.'}

    def test_04_asymptotic_threshold_and_source_polynomial(self):
        r,alpha,c=sp.symbols('r alpha c',positive=True)
        first=(sp.sinh(2*r)-2*r)**2/8
        series=sp.series(first,r,0,10).removeO()
        self.assertEqual(series,sp.Rational(2,9)*r**6+sp.Rational(4,45)*r**8)
        tau=(sp.log(alpha)+c)/(2*alpha)
        polynomial=sp.Rational(2,9)*alpha**4*tau**6+(sp.Rational(4,45)*alpha**6-sp.Rational(2,9)*alpha**4)*tau**8
        self.assertEqual(sp.limit(polynomial,alpha,sp.oo),0)
        lam=sp.symbols('lam',positive=True)
        gain=sp.log(1+8*alpha*lam)/2
        norm=(sp.sqrt(2+48*lam**2+480*lam**4)/(8*alpha)
              +gain*sp.sqrt(1+16*lam**2+384*lam**4)/(2*alpha))
        coefficient=sp.limit(alpha*norm/sp.log(alpha),alpha,sp.oo)
        self.assertEqual(coefficient,sp.sqrt(1+16*lam**2+384*lam**4)/4)
        self.assertEqual(sp.diff(gain/alpha,lam),4/(1+8*alpha*lam))
        REPORT['threshold_rate']={'fixed_gain_impurity_series':str(series),
            'published_eighth_order_polynomial_at_crossover_limit':0,
            'alpha_norm_error_over_log_alpha_limit':str(coefficient),
            'inference':'Uniform purity envelope and a strictly negative limiting derivative give time error O(log(alpha)/alpha^2).'}

    def test_05_old_phase_mixture_and_bounded_quadrature_law(self):
        # The VGF Eq. (56) family and our reduced approximant agree at width 1/(2 alpha).
        k,l,alpha=sp.symbols('k l alpha',real=True,positive=True)
        width=1/(2*alpha)
        self.assertEqual(sp.simplify(-(k-l)**2*width**2/2+(k-l)**2/(8*alpha**2)),0)
        q,z,lam,xi=sp.symbols('q z lam xi',positive=True)
        n=sp.symbols('n',integer=True,nonnegative=True)
        # Difference of two independent geometric variables, for d>=0.
        d=sp.symbols('d',integer=True,nonnegative=True)
        difference=sp.summation((1-q)**2*q**(2*n+d),(n,0,sp.oo))
        # Sympy gives a convergence-conditioned expression; verify algebraic rational factor.
        self.assertEqual(sp.simplify((1-q)**2/(1-q*q)-(1-q)/(1+q)),0)
        integral=sp.integrate(sp.exp(-(sp.Rational(1,2)+lam*lam*xi*xi)*z*z),(z,-sp.oo,sp.oo))/sp.sqrt(2*sp.pi)
        self.assertEqual(sp.simplify(integral-1/sp.sqrt(1+2*lam*lam*xi*xi)),0)
        a=sp.symbols('a',positive=True)
        self.assertEqual(sp.expand((1+a)**4-1-4*a),a**4+4*a**3+6*a**2)
        REPORT['measurement_and_source_dictionary']={'phase_width':'1/(2*alpha)',
            'VGF_family_coherence_kernel':'exp(-(k-l)^2/(8*N))',
            'geometric_difference_probability':'(1-q)/(1+q)*q^abs(d)',
            'Gaussian_integral':str(integral),
            'attribution':'The phase-averaged family is established; deriving this width from an initially pure coherent pump at growing gain is the dynamical claim.',
            'bounded_observable_scope':'Characteristic functions and distributions; no convergence of unbounded quadrature moments inferred.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:
        parser.error('Use a new output file outside this repository')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ProofChecks))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',test_groups=result.testsRun)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open('x') as stream:
        json.dump(REPORT,stream,indent=2,sort_keys=True,allow_nan=False);stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
