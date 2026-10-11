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

## Controlled dynamical result

The theorem gives a **controlled derivation of the crossover
from a pure coherent pump**, uniform state error, independent energy control,
and resulting separation between number-statistical and joint-state validity,
including a quantitatively controlled purity-onset time. The
[source map](SOURCES.md) credits the established state family, pump-noise
mechanism, Gaussian-frame method, and number-shift precedents.
