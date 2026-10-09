# Source review: an established state family and a dynamical crossover

## The additional direct predecessor

S. V. Vintskevich, D. A. Grigoriev and S. N. Filippov, *Effect of an incoherent
pump on two-mode entanglement in optical parametric generation*, Physical
Review A **100**, 053811 (2019), arXiv:1905.05756v2, gives an explicit
phase-averaged squeezed-state family.

The primary arXiv metadata and the author-posted full text were inspected.
The latter identifies itself as arXiv v2 and was uploaded by Sergey Filippov
on 22 February 2020. It is not asserted to be a byte-identical publisher PDF.
The relevant readable material is Sec. II A--B, Eqs. (9)--(17), and Sec. VI A,
Eqs. (50), (56)--(57). Figures, later citing-paper snippets on the hosting
page, and unreadable expressions were not used for any numerical claim.

- [arXiv record](https://arxiv.org/abs/1905.05756)
- [Author-posted text](https://www.researchgate.net/publication/337063825_Effect_of_an_incoherent_pump_on_two-mode_entanglement_in_optical_parametric_generation)
- [Publisher identifier](https://doi.org/10.1103/PhysRevA.100.053811)

### Exact dictionary, not just a thematic similarity

The source first studies a three-mode parametric Hamiltonian with a removable
phase-convention difference from ours. Its generalized parametric approximation
averages the output squeezed state over the *initial pump's* phase distribution.
For Gaussian phase spread $w=\Delta\theta$, Eq. (56), after fixing the
irrelevant mean phase, is

$$
\rho_{kl}=(1-q)q^{(k+l)/2}\exp[-(k-l)^2w^2/2],\qquad q=\tanh^2r.
$$

Choosing $w=1/(2\alpha)$ gives **exactly the density-matrix family** used in
our physical-frame approximation. The reduced Gaussian phase mixture and its
coherence kernel must therefore not be presented as newly invented states.
This is stronger attribution than merely crediting pump phase noise in general.
The source's symbol for a squeezing amplitude is not our crossover coordinate
$\lambda$.

The source also gives its purity through Eq. (57). Independently summing the
difference of two geometric random variables puts that expression in the form

$$
\operatorname{Tr}\rho^2=\frac{1-q}{1+q}
\left[1+2\sum_{d\ge1}q^d e^{-d^2w^2}\right].
$$

With $w=1/(2\alpha)$ and our growing gain, a Riemann-sum limit gives
$\int_0^\infty e^{-z-\lambda^2z^2}dz$. This last limit is our reconstruction
from their family, not a formula quoted from their article. Once the family
and its width are granted, the limiting purity and unchanged photon counts
are calculable consequences, not independent physical novelty claims.

### What the source does not establish for the present preparation

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

The primary Chinni--Quesada HTML was reread at the exact general frame
(Appendix C, Eqs. (96)--(100)), the pump-purity series (48), and the threshold
analysis (119)--(120). Their eighth-order polynomial and its
$\alpha^{-3/4}$ root agree with the expressions recorded in our theorem.
The leading fixed-gain correction reproduces their sixth- and eighth-order
coefficients. At $gt=[\log\alpha+O(1)]/(2\alpha)$, that finite polynomial
tends to zero, whereas our exact purity loss tends to a prescribed positive
constant. The disagreement concerns its nonuniform large-amplitude root
extrapolation, not its coefficients or the usefulness of finite-range fits.
No source plot was digitized.

- [Chinni--Quesada primary HTML](https://arxiv.org/html/2312.09239v2)

Horoshko--Shchesnovich's primary HTML and the Gaussian-frame paper were also
checked in the relevant comparison passages. The former supplies
error-specific validity and number-shift precedents in the degenerate model;
the latter supplies the interaction-frame strategy and non-Gaussian
quadrature-noise interpretation. Their mathematical scope is not silently
expanded to prove this theorem. These roles are retained in
[the original source map](SOURCES.md).

## Remaining historical reading boundary

The Hillery--Zubairy publisher full text was not obtained through the publisher
PDF, APS full-text endpoint, or institutional-record routes in this review.
The institutional item confirms bibliographic identity but does not supply the
article body. Its detailed historical conditions remain credited indirectly
through the readable newer sources, not presented as a fresh direct reading.
No access failure supports an absence or priority claim.

## Contribution after this comparison

The candidate contribution is the **controlled derivation of the crossover
from a pure coherent pump**, uniform state error, independent energy control,
and resulting separation between number-statistical and joint-state validity,
including a quantitatively controlled purity-onset time. The phase-averaged
family, phase-noise mechanism, Gaussian-frame method, and familiar limiting
calculations are not separately promoted.

The additional predecessor narrows attribution without refuting the dynamics
or supplying a same-input uniform estimate. Correctness, exact formula
novelty, and physical significance therefore remain separate assessments.
No exhaustive literature search or external priority certification is claimed.
