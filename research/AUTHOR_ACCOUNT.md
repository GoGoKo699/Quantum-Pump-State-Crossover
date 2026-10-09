# Coherent-pump crossover: the physical claim

## Question

A classical pump can predict the number of generated photons correctly while
predicting their joint quantum state incorrectly. The issue is not whether
pump quantum fluctuations exist; that mechanism, its effect on squeezing,
and Gaussian interaction-frame methods are established. The question here is
whether the distinction can be stated for one exact dynamical model with an
error that vanishes in a specified limit.

## Model and limit

A pure coherent pump and two vacuum output modes evolve under

$$
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\qquad
|\Psi(0)\rangle=|\alpha\rangle_c|00\rangle_{ab},\quad N=\alpha^2.
$$

There is no loss, external drive replenishment, or technical pump phase noise.
This is an effective closed resonant three-mode Hamiltonian. With
$r=\alpha gt$, increase $\alpha$ at

$$r=\tfrac12\log(1+8\alpha\lambda),\qquad 0<\lambda<\infty\text{ fixed}.$$

The ordinary fixed-gain classical-pump limit is not contradicted. This gain
grows with brightness. All uniform error statements use bounded intervals of
$\lambda$, not a simultaneous large-$\lambda$ limit.

## State theorem

After removing nominal pump displacement and output squeezing, the exact
state is within $O_\Lambda(\log\alpha/\alpha)$ in vector norm of

$$
|\chi_\lambda\rangle=e^{\lambda(d-d^\dagger)R}|000\rangle,
\qquad R=1+n_a+n_b+a^\dagger b^\dagger+ab.
$$

In the physical frame, an equally controlled description is

$$
\sum_{k\ge0}\operatorname{sech}r\,\tanh^k r\,
|\alpha-k/(2\alpha)\rangle_c|k,k\rangle_{ab}.
$$

Generated pair-number differences are recorded by small pump displacements.
These are small relative to the macroscopic pump amplitude but remain
resolvable on its quantum fluctuation scale. Tracing out the pump gives a
phase-averaged two-mode squeezed vacuum with phase variance $1/(4N)$.

That phase-averaged family itself is established: the 2019
Vintskevich--Grigoriev--Filippov treatment obtains it from an initially
phase-smeared pump. Here the pump starts pure, and the emergent width and
uniform state error follow from the quantum dynamics. The input preparation
and approximation domain cannot be changed when making that comparison.

## What is accurate and what is not

The phase average leaves the entire pair-count distribution unchanged.
The exact output counts therefore approach the nominal geometric distribution
in total variation, and each individual output approaches its thermal
marginal in trace distance. Every total-output-number-conserving POVM has
asymptotically the nominal probabilities, including passive optics with vacuum
ancillas and counting.

A separate sector-energy estimate, combined with bounded truncations of the
count distribution, gives

$$\langle n_a\rangle\sim2\lambda\sqrt N,\qquad
(N-\langle n_c\rangle)/N\sim2\lambda/\sqrt N.$$

This mean is not deduced from trace distance alone. Relative depletion
vanishes even though the absolute converted energy grows.

At the same times the pump and joint-output purity tend to

$$\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}dz<1.$$

At $\lambda=1/2$ the limiting purity is about $0.757872$, and the fidelity
with the nominal pure squeezed vacuum is about $0.842738$. Global purity
makes pump mixedness an entanglement statement across pump versus both
outputs, not a measure of signal--idler entanglement separately.

More strongly, a phase-referenced squeezed-quadrature record
$Y=e^r(x_a-x_b)/\sqrt2$ has limiting characteristic function

$$\langle e^{i\xi Y}\rangle\longrightarrow
\frac{e^{-\xi^2/4}}{\sqrt{1+2\lambda^2\xi^2}}.$$

Its violation of the modulus identity obeyed by every Gaussian quadrature
law gives a positive trace-distance separation from **each single Gaussian
state**, even a mixed, retuned, brightness-dependent choice. Nevertheless,
the output approaches an explicit convex mixture of Gaussian states. No
Wigner-negativity or separation from that convex hull is implied.

The signature requires a phase reference and physical resolution of order
$N^{-1/4}$. Fixed positive additive resolution washes out this homodyne
distinction. No device operating window, universal failure of photon-counting
applications, or metrological advantage follows.

## When a fixed loss of purity occurs

For a prescribed loss $\delta$, define
$\mathcal P(\lambda_\delta)=1-\delta$. Uniform state control proves the
first-crossing law, now with a quantified remainder:

$$
gt_\delta=
\frac{\log\alpha+\log(8\lambda_\delta)}{2\alpha}
+O_\delta(\log\alpha/\alpha^2).
$$

No global monotonicity of the exact purity is required. Rational
finite-parameter enclosures are provided in [the analytical review](PROOF_REVIEW.md).
The closest same-model paper's sixth- and eighth-order short-time
coefficients agree; extrapolating their fixed-degree polynomial to this
logarithmically growing gain is nonuniform.

## Proof and attribution

The residual generator has one exponentially amplified cubic term, retained
nonperturbatively, and two terms controlled by an explicit Duhamel estimate
on a common Schwartz domain. A second state comparison gives pair-number
marking. An independent positive-number-sector comparison supplies energy
control. Probability contraction and bounded characteristic functions give
the measurement conclusions. The first crossing follows from a uniform
purity envelope and a strictly decreasing limiting curve.

The [theorem](THEOREM.md), [proof review](PROOF_REVIEW.md),
[original source map](SOURCES.md), and [additional source comparison](SOURCE_REVIEW.md)
separate these derivations from inherited models, methods, and state families.
The result under assessment is a uniform dynamical crossover and its
observable-dependent validity, not the discovery of pump noise. The historical
Hillery--Zubairy full-text boundary remains explicit. The present review finds
no blocking defect within the stated model but is not external peer review.
