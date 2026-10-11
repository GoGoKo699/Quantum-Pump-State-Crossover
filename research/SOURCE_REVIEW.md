# Phase-mixture and onset comparisons

The [source map](SOURCES.md) gives the complete attribution and bibliography.
This page compares the phase-averaged state family and same-model purity
expansion with the controlled dynamical result.

## The phase-averaged state family

S. V. Vintskevich, D. A. Grigoriev and S. N. Filippov, *Effect of an incoherent
pump on two-mode entanglement in optical parametric generation*, Physical
Review A **100**, 053811 (2019), arXiv:1905.05756v2, gives an explicit
phase-averaged squeezed-state family.

The comparison uses the author-posted arXiv v2 text, Sec. II A--B,
Eqs. (9)--(17), and Sec. VI A, Eqs. (50), (56)--(57).

- [arXiv record](https://arxiv.org/abs/1905.05756)
- [Author-posted text](https://www.researchgate.net/publication/337063825_Effect_of_an_incoherent_pump_on_two-mode_entanglement_in_optical_parametric_generation)
- [Publisher identifier](https://doi.org/10.1103/PhysRevA.100.053811)

### Exact state dictionary

The source first studies a three-mode parametric Hamiltonian with a removable
phase-convention difference from ours. Its generalized parametric approximation
averages the output squeezed state over the *initial pump's* phase distribution.
For Gaussian phase spread $w=\Delta\theta$, Eq. (56), after fixing the
irrelevant mean phase, is

$$
\rho_{kl}=(1-q)q^{(k+l)/2}\exp[-(k-l)^2w^2/2],\qquad q=\tanh^2r.
$$

Choosing $w=1/(2\alpha)$ gives **exactly the density-matrix family** used in
our physical-frame approximation. This phase-mixture family and its coherence
kernel are established. The source's symbol for a squeezing amplitude is not
our crossover coordinate $\lambda$.

The source also gives its purity through Eq. (57). Independently summing the
difference of two geometric random variables puts that expression in the form

$$
\operatorname{Tr}\rho^2=\frac{1-q}{1+q}
\left[1+2\sum_{d\ge1}q^d e^{-d^2w^2}\right].
$$

With $w=1/(2\alpha)$ and our growing gain, a Riemann-sum limit gives
$\int_0^\infty e^{-z-\lambda^2z^2}dz$. This limit follows from their family
with the specified width and gain; the dynamical state theorem establishes
that the exact coherent-pump evolution has this approximation.

### Preparation and approximation domain

The source introduces the width as initial incoherence of a mixed pump.
Our preparation is one pure coherent state, with no added phase noise. The
coherent-state Glauber--Sudarshan distribution is a point mass, not a Gaussian
of width $1/(2\alpha)$. That width cannot be inserted into the older initial
state while claiming to keep the preparation unchanged.

The present theorem instead derives the reduced mixture by tracing the pump
from a pure three-mode state, and proves a norm error tending to zero at the
specified growing gain. It also describes the pump--output entanglement; a
classical mixture by itself is not that joint-state description.

The older text explicitly includes a high-gain applicability condition of the
form $gt\,e^{4gt|\alpha|}\ll1$ in Sec. II A. In our variables this is
$(r/\alpha)e^{4r}\ll1$. At fixed positive crossover coordinate it grows as
$64\lambda^2\alpha r$, not as a small quantity. Consequently that stated
approximation domain does not certify the present crossover. The condition's
failure does not mean every observable becomes inaccurate: our count theorem
is precisely a distinction between validity criteria.

The same preparation/validity distinction prevents using the old phase-mixture
family as an approximation to subsequent operations that retain the correlated
pump. It is a reduced-state family, not a replacement joint dynamics.

### Gaussian coefficients and the joint-state overlap

Let $P=(d-d^\dagger)/(i\sqrt2)$ be the displaced pump momentum, whose
vacuum density is $e^{-P^2}/\sqrt\pi$. Conditional on $P$, the physical-frame
number-marking state has output phase $\vartheta=P/(\sqrt2\alpha)$. With
$t=\tanh r$, its unsqueezed output is exactly

$$
S(-r)e^{i\vartheta n_a}S(r)|00\rangle
=A_P\sum_{k\ge0}z_P^k|k,k\rangle,
\qquad
A_P=\frac{1-t^2}{1-t^2e^{i\vartheta}},\qquad
z_P=\frac{t(e^{i\vartheta}-1)}{1-t^2e^{i\vartheta}}.
$$

These coefficients follow by composing the two squeezers with the phase
rotation; they satisfy $|A_P|^2/(1-|z_P|^2)=1$. At fixed $\lambda$ and $P$,
the growing-gain limit gives

$$
A_P\longrightarrow A_P^{(0)}=\frac1{1-i\sqrt2\lambda P},\qquad
z_P\longrightarrow z_P^{(0)}=\frac{i\sqrt2\lambda P}{1-i\sqrt2\lambda P}.
$$

These are the coefficients of $e^{i\sqrt2\lambda PR}|00\rangle$ in the
residual state $|\chi_\lambda\rangle$. Summing the geometric overlap gives

$$
\left\|D_c(-\alpha)S(-r)|\Phi_{\alpha,r}\rangle
-|\chi_\lambda\rangle\right\|^2
=\int_{-\infty}^{\infty}\frac{e^{-P^2}}{\sqrt\pi}
\left[2-2\operatorname{Re}
\frac{\overline{A_P^{(0)}}A_P}
{1-\overline{z_P^{(0)}}z_P}\right]dP.
$$

This exact overlap identity underlies the Gaussian-quadrature comparison
check. The finite norm estimate itself follows from the Duhamel argument in
[the theorem](THEOREM.md), Section 2.2.

## Same-model onset comparison

Chinni--Quesada gives the general frame in Appendix C, Eqs. (96)--(100),
the pump-purity series in Eq. (48), and the threshold analysis in
Eqs. (119)--(120). Their eighth-order polynomial and its
$\alpha^{-3/4}$ root agree with the expressions recorded in our theorem.
The leading fixed-gain correction reproduces the leading large-$\alpha$
parts of their sixth- and eighth-order coefficients.
At the fixed-loss crossing
$gt_\delta=[\log\alpha+\log(8\lambda_\delta)+o(1)]/(2\alpha)$,
where $\mathcal P(\lambda_\delta)=1-\delta$, that finite polynomial tends
to zero while the exact purity loss equals $\delta$. The disagreement concerns its nonuniform large-amplitude root
extrapolation, not its coefficients or the usefulness of finite-range fits.

- [Chinni--Quesada primary HTML](https://arxiv.org/html/2312.09239v2)

### Relation to the self-consistent Gaussian frame

In the present phase convention, the source's general Appendix C generator,
with displacement fixed at $\alpha$ and squeezing $r=\alpha\tau$, gives
the exact residual generator in [the theorem](THEOREM.md), Eq. (8). Its
self-consistent frame instead uses real functions $\beta(\tau)$ and
$\eta(\tau)$ satisfying

$$
\partial_\tau\beta=-\tfrac12\sinh(2\eta),\qquad
\partial_\tau\eta=\beta,\qquad
\beta(0)=\alpha,\quad\eta(0)=0.
$$

The invariant is $\beta^2+\sinh^2\eta=\alpha^2$. On the positive-pump
branch, $0\le\eta\le r$ and

$$
1-\frac{\beta}{\alpha}
=\frac{\sinh^2\eta}{\alpha^2(1+\beta/\alpha)}
\le\frac{\sinh^2r}{\alpha^2}.
$$

Integrating with respect to nominal gain yields

$$
0\le r-\eta\le\frac1{\alpha^2}\int_0^r\sinh^2u\,du
=\frac1{\alpha^2}\left[\frac14\sinh(2r)-\frac12r\right].
$$

For $\lambda$ in a fixed compact interval and sufficiently large $\alpha$,
$r_\alpha(\lambda)<\operatorname{arsinh}\alpha$, so that branch remains
positive throughout the required interval. The bound gives
$\eta=r+O_\Lambda(\alpha^{-1})$; the invariant then gives
$\beta=\alpha-\lambda+o(1)$ at fixed $\lambda$. The residual state in this
moving frame is

$$
D_c(-\beta)S(-\eta)|\Psi_\alpha\rangle
=D_c(\alpha-\beta)S(r-\eta)|\psi_\alpha\rangle
\longrightarrow D_c(\lambda)|\chi_\lambda\rangle
=e^{\lambda p(R-I)}|000\rangle.
$$

Here $p=d-d^\dagger$ and $D_c(\lambda)=e^{-\lambda p}$ for real
$\lambda$. Thus the frame change only displaces the limiting pump and
preserves its entanglement and purity. This limit is a reconstruction from
the source's frame equations and the state theorem.

### Fixed-gain expansion and the short-time coefficients

At fixed $r$, the exact residual generator acting on vacuum is

$$
G_\alpha(u)|000\rangle
=-\frac{\sinh u\cosh u}{\alpha}|1,0,0\rangle
-\frac{\sinh^2u}{\alpha}|1,1,1\rangle.
$$

One Duhamel iteration therefore gives, with the pump listed first,

$$
|\psi_\alpha(r)\rangle
=|000\rangle
-\frac{\cosh(2r)-1}{4\alpha}|1,0,0\rangle
-\frac{\sinh(2r)-2r}{4\alpha}|1,1,1\rangle
+O_r(\alpha^{-2}).
$$

The norm remainder follows by bounding the second iterated remainder on
vacuum: products of two residual generators have finite polynomial norms
on the fixed gain interval, with the exact unitary to their left. No
infinite Dyson expansion is required. The first correction is pump-only;
the second gives the leading pump impurity

$$
1-\mathcal P_\alpha(r)
=\frac{[\sinh(2r)-2r]^2}{8\alpha^2}+o_r(\alpha^{-2}),
$$
$$
\frac{[\sinh(2r)-2r]^2}{8\alpha^2}
=\frac1{\alpha^2}\left(\frac29r^6+\frac4{45}r^8
+\frac{82}{4725}r^{10}+O(r^{12})\right).
$$

Substitution of $r=\alpha\tau$ reproduces the leading large-$\alpha$
parts of the source's sixth- and eighth-order time coefficients. Its
additional impurity term $-2r^8/(9\alpha^4)$ is of higher inverse-$\alpha$
order at fixed gain. This consistency expansion has a fixed-$r$ remainder;
the growing-gain crossover instead uses the full residual state and its
finite error bound.

## Controlled dynamical result

The theorem gives a **controlled derivation of the crossover
from a pure coherent pump**, uniform state error, independent energy control,
and resulting separation between number-statistical and joint-state validity,
including a quantitatively controlled purity-onset time. The
[source map](SOURCES.md) credits the established state family, pump-noise
mechanism, Gaussian-frame method, and number-shift precedents.
