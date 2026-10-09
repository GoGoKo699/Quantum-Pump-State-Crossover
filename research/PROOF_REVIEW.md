# Analytical review and finite first-crossing certificates

## Scope and outcome

This author-side review checks the theorem at source revision
`a4069462777b9489c1fc1c7462e9d4c9fc326922`. It reconstructs the remainder
norms in continuous quadrature coordinates, checks the energy comparison and
measurement logic, and makes the existing first-crossing statement quantitative.
No blocking mathematical defect was identified in the stated coherent-pump,
vacuum-output, closed nondegenerate model. This is not external peer review or
exhaustive literature clearance. The original theorem and all archived files
remain unchanged.

The additional first-crossing bound below is a corollary of the existing norm
estimate. The [source review](SOURCE_REVIEW.md) separately narrows attribution:
the phase-averaged squeezed-state family has an explicit 2019 predecessor.

## 1. Domain justification and the exact residual generator

Let $M=2n_c+n_a+n_b$. Every eigenspace of $M$ is finite dimensional, and the
original trilinear Hamiltonian preserves it. Its self-adjoint realization is
the direct sum of those finite Hermitian blocks. The finite-occupation vectors
are a core; on the common occupation domain the Hamiltonian is bounded by a
constant times $(M+1)^{3/2}$. Conservation of $M$ preserves the norm of every
power of $M+1$ under the exact dynamics.

The coherent-pump/vacuum vector belongs to the intersection of these domains.
For every finite gain, displacement and squeezing preserve that oscillator
Schwartz space. The limiting cubic phase does too: in the coordinates below,
each derivative produces only a polynomial times a Gaussian. Thus all terms in
the differentiated frame have finite norm. Duhamel's identity uses the exact
unitary propagator on the left of the remainder, not a bounded cubic generator
or an assumed convergent Dyson series. The constants need not be uniform for
all Gaussian transformations; the norms actually required are evaluated
explicitly on the leading state.

Substitution of the exact squeezing transformation yields the three terms in
Eq. (8) of [the theorem](THEOREM.md). The exponentially growing term is
integrated without expansion. The other two give its displayed norm error
$\epsilon_\alpha(\lambda)$, uniform on fixed compact intervals of $\lambda$.

### Independent coordinate calculation of the remainder norms

Use real coordinates $x=\sqrt2 x_+$, $y=\sqrt2 p_-$ and
$z=\sqrt2 P_d$. Their vacuum probability measure consists of three independent
standard normals. In this representation,

$$
R=(x^2+y^2)/2,\quad p=iz,\quad T=2i\partial_z,\quad
L=2(\partial_x^2+\partial_y^2),\quad
A=-(x\partial_x+y\partial_y+1).
$$

The leading wave function, up to normalization, is

$$
\chi_\ell(x,y,z)=\exp[-(x^2+y^2+z^2)/4+i\ell z(x^2+y^2)/2].
$$

Apply $pL$ and $TA$ directly by differentiation, divide out this wave
function, and integrate the squared polynomial moduli against the vacuum
measure. This gives exactly

$$
\|pL\chi_\ell\|^2=2+48\ell^2+480\ell^4,\qquad
\|TA\chi_\ell\|^2=1+16\ell^2+384\ell^4.
$$

Also $\|p(R-2)\chi_0\|^2=2$. These independently reproduce all constants
used in the state estimate and number-marking comparison. They do not rely on
truncating an oscillator Hilbert space.

## 2. Checks that cannot be replaced by norm convergence

**Physical-frame number marking.** On the equal-pair subspace,
$S(-r)n_aS(r)/(2\alpha)=(e^{2r}R-e^{-2r}L-2I)/(8\alpha)$.
At the declared gain, its difference from $\lambda R$ is exactly
$(R-e^{-2r}L-2I)/(8\alpha)$. Both conditional-displacement generators are
well-defined there. Duhamel along the leading unitary gives the stated
additional error $d_\alpha$ and hence the physical-frame trace-distance
bound. Coherent branches are not being asserted to be exact conserved-number
sectors.

**Energy.** In pump sector $m$, the population flux contains
$(k+1)\sqrt{m-k}\,u_k^*u_{k+1}$. Bounding the square root by $\sqrt m$ and
using Cauchy--Schwarz gives
$\partial_\tau\bar k_m\le2\sqrt m\sqrt{\bar k_m(\bar k_m+1)}$.
Positive regularization at the initial zero yields the hyperbolic-sine
comparison. Number observables average sectors with the initial Poisson
weights: off-diagonal coherent-pump sectors do not contribute to them.
The tangent bound on $\sqrt m$ and the Poisson generating function give
Eq. (12). This independent upper estimate, together with bounded truncated
expectations from the count law, establishes the leading mean. Total
variation alone does not establish that mean or uniform integrability.

**Measurements.** Trace distance contracts under arbitrary POVMs, including
an $\alpha$-dependent squeezed-quadrature measurement. Each member of the
Gaussian family has a Gaussian law for that quadrature, including when its
covariance depends on $\alpha$. Therefore the two-frequency modulus test
really is uniform over individual Gaussian states. It is not a test of the
convex Gaussian hull. The probability-law proof never requires convergence of
an unbounded fourth moment. Number-conserving measurement invariance follows
from the pair-subspace identity, not a claim that every measurement is blind.

**First crossing.** The exact purity need not be globally monotone. The
strictly decreasing limiting purity and a bound applying to *all earlier*
crossover coordinates exclude an earlier threshold hit. Pointwise convergence
at one selected time would not be enough.

## 3. Finite first-crossing theorem

Write $P_\alpha(\lambda)$ for the exact pump purity at
$\tau_\alpha(\lambda)=\log(1+8\alpha\lambda)/(2\alpha)$, and keep the
unchanged conservative bound

$$
|P_\alpha(\lambda)-\mathcal P(\lambda)|\le4\epsilon_\alpha(\lambda),
\qquad \mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}dz.
$$

Let the prescribed purity loss be $0<\delta<1$. Suppose $0<l<u$ satisfy

$$
\mathcal P(l)-4\epsilon_\alpha(l)>1-\delta,
\qquad
\mathcal P(u)+4\epsilon_\alpha(u)<1-\delta. \tag{R1}
$$

Then the exact first time $\tau_\delta(\alpha)$ at which purity reaches
$1-\delta$ obeys

$$
\boxed{\frac{\log(1+8\alpha l)}{2\alpha}
<\tau_\delta(\alpha)<
\frac{\log(1+8\alpha u)}{2\alpha}.} \tag{R2}
$$

**Proof.** The explicit $\epsilon_\alpha(\lambda)$ is nondecreasing, whereas
$\mathcal P$ is decreasing. At every $0\le s\le l$ the exact purity is at
least $\mathcal P(l)-4\epsilon_\alpha(l)$, strictly above threshold. At $u$
it is below threshold. Strong continuity of the state and continuity of
purity imply a first crossing between those times. This argument does not
assume monotonicity of the exact dynamics.

### Quantified remainder of the asymptotic onset law

Let $\lambda_\delta$ solve $\mathcal P(\lambda_\delta)=1-\delta$. On
$[l_0,u_0]=[\lambda_\delta/2,3\lambda_\delta/2]$,

$$
-\mathcal P'(\lambda)=2\lambda\int_0^\infty z^2e^{-z-\lambda^2z^2}dz
\ge m_\delta:=\frac{2l_0}{3}e^{-1-u_0^2}>0.
$$

Put $E_\alpha=\epsilon_\alpha(u_0)$ and
$\Delta_\alpha=8E_\alpha/m_\delta$. Once
$\Delta_\alpha<\lambda_\delta/2$, the endpoints
$\lambda_\delta\pm\Delta_\alpha$ have strict purity margins at least
$4E_\alpha$. Since
$\partial_\lambda\tau_\alpha=4/(1+8\alpha\lambda)$, (R2) gives

$$
\boxed{\tau_\delta(\alpha)=
\frac{\log\alpha+\log(8\lambda_\delta)}{2\alpha}
+O_\delta\!\left(\frac{\log\alpha}{\alpha^2}\right).} \tag{R3}
$$

Equivalently, the time remainder is $O_\delta(\log N/N)$ in dimensionless
units $gt$. This sharpens the previously stated $o(1/\alpha)$ remainder; it
is not a different leading time law or a new onset mechanism.

## 4. Exact-arithmetic certificates for one-percent purity loss

The following are outward bounds on the first crossing of purity $0.99$:

| Pump amplitude $\alpha$ | Mean pump photons $N$ | Certified interval for $gt_{0.01}$ |
|---:|---:|---:|
| $10^4$ | $10^8$ | $(0.00043008590732,\ 0.00043531624201)$ |
| $10^5$ | $10^{10}$ | $(0.000054757627932,\ 0.000054827265729)$ |
| $10^6$ | $10^{12}$ | $(0.0000066299841061,\ 0.0000066307503885)$ |

These enclose the exact infinite-dimensional first crossing. They are not
numerical propagation results, fits, optimal intervals, or device operating
points. The endpoints use $(l,u)=(0.068,0.0755)$, $(0.0713,0.0723)$, and
$(0.07172,0.07183)$ respectively.

For $\lambda\ge0$, integrating odd/even Taylor bounds for $e^{-\lambda^2z^2}$
gives rational enclosures

$$
\sum_{j=0}^{15}\frac{(-1)^j(2j)!\lambda^{2j}}{j!}
\le\mathcal P(\lambda)\le
\sum_{j=0}^{16}\frac{(-1)^j(2j)!\lambda^{2j}}{j!}. \tag{R4}
$$

This is a finite sign-controlled bound, not an assertion that the formal
infinite series converges. Every endpoint is rational. Square-root bounds
are rounded upward using integer square roots and verified by squaring.
Gain enclosures are checked against positive exponential Taylor sums through
order 120 with a geometric tail bound. All (R1) inequalities are then exact
rational comparisons. The smallest retained purity margin is greater than
$1.17\times10^{-7}$. The [checker](../scripts/check_proof_review.py) and
[reference report](../verification/proof-review.json) contain the exact
fractions and validation rules.

## 5. Verification and decision boundary

Five additional check groups separately reconstruct the quadrature-coordinate
remainder norms, energy and geometric-law identities, rational first-crossing
certificates, short-time/source asymptotics, and phase-mixture/measurement
dictionary. No archived code is imported into that checker. The existing
fifteen scientific groups and eight infrastructure tests remain unchanged.
Execution and canonical-report comparisons belong in the verification receipt
and PR record, not an assertion of external independence.

The supported outcome is continuation with a coherent scientific account and
more explicit finite-parameter guarantees. The [author account](AUTHOR_ACCOUNT.md)
sets out the claims in their physical order. The mathematical review does not
increase the originality of a phase-averaged state family already present in
prior literature, and does not resolve an unread historical article by proxy.
