# From a Gaussian interaction frame to the count–state crossover

This guide connects one tutorial to the repository's result: a bright pump
can give accurate photon counts while leaving an inaccurate joint-state
prediction. Familiarity with bosonic creation operators, coherent states,
partial traces, and unitary evolution is assumed. The derivations here use
the [canonical theorem](THEOREM.md) and [validity window](VALIDITY_WINDOW.md).

## One tutorial and a focused reading route

**R. Yanagimoto et al., _Mesoscopic ultrafast nonlinear optics—The emergence
of multimode quantum non-Gaussian physics_, Optica 11(7), 896–918 (2024),
[arXiv:2311.13775v1](https://arxiv.org/abs/2311.13775v1).** Page numbers below
refer to the [26-page arXiv version](https://arxiv.org/pdf/2311.13775v1).

| Reading | Preparation for this repository |
|---|---|
| Sections II A–E, pp. 3–8 | Classical amplitudes, Gaussian fluctuations, and residual dynamics |
| Box 1, pp. 4–5: “The Gaussian interaction frame” | Factor displacement and squeezing out of the state |
| Box 2, pp. 7–8: “Mesoscopic optical parametric amplification” | Exponentially enhanced cubic interaction at large gain |
| Box 3, pp. 11–12: “Experimental considerations for mesoscopic OPA” | Logarithmic onset scale and sensitivity to noise and loss |

These passages provide the organizing physics. The bridge below supplies
the nondegenerate model and controlled state-error argument. The full
[sources](SOURCES.md) accompany this
single-source learning route.

The review's conditional-displacement onset criterion also differs from
our operational first crossing of a fixed pump-purity loss. The
[first-crossing proof](PROOF_REVIEW.md) controls that time and its remainder.

## Translate the model before translating equations

| Object | Review's Box 2 | This repository |
|---|---|---|
| Generated light | One degenerate signal mode $`a`$ | Distinct signal and idler $`a,b`$ |
| Pump | Mode $`b`$, mean amplitude $`\beta`$ | Mode $`c`$, initial real amplitude $`\alpha`$ |
| Pump brightness | $`n`$ | $`N=\alpha^2`$ |
| Residual frame | Displacement and Gaussian transformation | Pump displacement $`D_c(\alpha)`$ and two-mode squeezing $`S(r)`$ |

The model change requires fresh coefficients and phase conventions. In
particular, the review's conditional cat-state examples are different from
our output after tracing out the pump. Our reduced approximation belongs to
the convex hull of Gaussian states.

## 1. Remove the nominal Gaussian evolution

Our closed resonant model and preparation are

```math
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\qquad
\lvert\Psi(0)\rangle=\lvert\alpha\rangle_c\lvert00\rangle_{ab}.
```

Replacing the pump operator by its coherent amplitude predicts a two-mode
squeezed vacuum, abbreviated TMSV. Write the exact state instead as

```math
\lvert\Psi_\alpha(r)\rangle=D_c(\alpha)S(r)\lvert\psi_\alpha(r)\rangle,
\qquad S(r)=e^{r(a^\dagger b^\dagger-ab)},\qquad r=\alpha gt.
```

This is an exact change of frame. The approximation enters when deciding
whether the residual state stays close to vacuum. A large displacement
does not settle that question: squeezing can amplify the residual pump
fluctuations. [Theorem, Sections 1–2](THEOREM.md) fixes the preparation,
frame, and order of limits.

## 2. Keep the amplified cubic term to all orders

Let $`d`$ annihilate the displaced pump and define

```math
p=d-d^\dagger,\quad T=d+d^\dagger,\quad
Q=1+n_a+n_b,\quad C=a^\dagger b^\dagger+ab,
\qquad R=Q+C,\quad L=C-Q,\quad A=a^\dagger b^\dagger-ab.
```

Here $`p`$ is anti-Hermitian. The exact residual generator at gain $`u`$ is

```math
G_\alpha(u)=\frac{e^{2u}}{4\alpha}pR
+\frac{e^{-2u}}{4\alpha}pL+\frac1{2\alpha}TA.
```

Although each term contains $`1/\alpha`$, the first term accumulates to a
finite effect when

```math
\lambda=\int_0^r\frac{e^{2u}}{4\alpha}\,du
=\frac{e^{2r}-1}{8\alpha},\qquad
r=\tfrac12\log(1+8\alpha\lambda).
```

Its generators at different gains commute, so its evolution is exactly

```math
\lvert\chi_\lambda\rangle=e^{\lambda pR}\lvert000\rangle.
```

This exponential retains every power of the finite crossover parameter.
A fixed-degree short-time expansion cannot do that. The cubic structure
means one pump quadrature couples to a quadratic output observable. In
the theorem's quadrature normalization,
$`R=x_+^2+p_-^2`$; its two terms commute and have an exponential sum-of-squares
law in vacuum. See [Theorem, Sections 2 and 5](THEOREM.md) for the exact
algebra and spectral law.

## 3. Turn the frame picture into a finite error bound

Duhamel's identity compares the exact evolution with the retained cubic
evolution. The exact propagator is unitary; the remainder is evaluated on
the explicit leading state. Its polynomial vacuum norms give

```math
\|\psi_\alpha-\chi_\lambda\|\le\epsilon_\alpha(\lambda)
=\frac{\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}
+\frac{r\sqrt{1+16\lambda^2+384\lambda^4}}{2\alpha}.
```

For bounded $`\lambda`$, this tends to zero as
$`O(\log\alpha/\alpha)`$. The operators are unbounded, so the proof needs
a common domain. Conservation of occupation controls the exact evolution;
the leading cubic phase preserves the oscillator Schwartz space. The
[domain proof and remainder reconstruction](PROOF_REVIEW.md) justify the
comparison without assuming a bounded cubic operator or a convergent
infinite Dyson series.

Norm control gives trace-distance and bounded-measurement control. It
does **not** automatically give convergence of photon-number means. The
[separate energy argument](THEOREM.md), Section 4, uses conserved-number
sectors, a differential inequality, and bounded truncations of the count
law.

## 4. Return to photon counts and joint states

The physical-frame approximation marks the generated pair number with a
pump-amplitude shift that is small relative to its mean amplitude:

```math
\lvert\Phi_{\alpha,r}\rangle
=\sum_{k\ge0}s_k\lvert\alpha-k/(2\alpha)\rangle_c\lvert k,k\rangle,
\qquad s_k=\operatorname{sech}r\,\tanh^k r.
```

The [number-marking proof](THEOREM.md), Section 2.2, supplies a second
explicit error $`d_\alpha`$. Tracing out the pump then gives

```math
\sigma_{ab}=\sum_{k,l\ge0}s_ks_l e^{-(k-l)^2/(8N)}
\lvert k,k\rangle\langle l,l\rvert,\qquad
D(\rho_{ab},\sigma_{ab})\le\eta_\alpha:=\epsilon_\alpha+d_\alpha.
```

Here $`D=\tfrac12\|\rho-\sigma\|_1`$. The diagonal is precisely the
nominal geometric pair-count distribution; off-diagonal coherence is
suppressed. Equivalently, $`\sigma_{ab}`$ averages phase rotations of the
TMSV with phase variance $`1/(4N)`$. This phase distribution comes from
tracing a quantum pump initially in a pure state. It is not imposed
technical noise or a channel for arbitrary inputs.

Every total-output-number-conserving POVM gives identical probabilities
on this approximation and the nominal TMSV. Exact probabilities differ
by at most $`\eta_\alpha`$; see [Theorem, Section 3](THEOREM.md).

The same **finite** inequalities allow a varying parameter whenever

```math
B_\alpha=\frac{(1+\lambda_\alpha^2)(1+r)}{\alpha}\longrightarrow0.
```

| Sequence within this sufficient window | Complete counts | Joint output |
|---|---|---|
| $`\lambda_\alpha\to0`$ | Accurate | Nominal pure TMSV becomes accurate |
| $`\lambda_\alpha\to\lambda_0>0`$ | Accurate | Finite purity and fidelity crossover |
| $`\lambda_\alpha\to\infty`$ | Accurate | Distance from every pure state tends to one |

The [validity-window proof](VALIDITY_WINDOW.md) establishes all three rows
and vanishing fractional depletion. It is a sufficient controlled window,
not the whole undepleted regime. The last row follows because purity
vanishes, bounding the overlap with every pure state.

## Worked crossover: $`\lambda=1/2`$

Choose $`r=\tfrac12\log(1+4\alpha)`$ and let $`\alpha`$ grow. The
[energy and purity results](THEOREM.md), Sections 4–5, give

```math
\langle n_a\rangle\sim\sqrt N,\qquad
\frac{N-\langle n_c\rangle}{N}\sim N^{-1/2},\qquad
\operatorname{Tr}\rho_{ab}^2\longrightarrow0.7578721561.
```

The squared target-state fidelity tends to $`0.8427384586`$, so the
distance from the nominal pure TMSV has lower limit at least
$`0.1572615414`$. These are limiting values, not finite-brightness error
certificates. Pump impurity diagnoses entanglement across pump versus
both outputs jointly.

There is also a bounded observable: the cosine of the standardized
squeezed-quadrature record $`Y_\alpha=e^rX_-`$. At frequency one,

```math
\mathbb E\cos Y_\alpha\longrightarrow
\frac{e^{-1/4}}{\sqrt{3/2}}=0.6358881766,
\qquad
\mathbb E_{\mathrm{TMSV}}\cos Y_\alpha=e^{-1/4}=0.7788007831.
```

[Theorem, Section 7](THEOREM.md) proves this probability-law statement
and a two-frequency separation from every individual Gaussian state.
It also states the measurement resources: phase-locked references and
physical resolution on the shrinking scale $`e^{-r}=\Theta(N^{-1/4})`$.
A fixed positive additive Gaussian readout width erases this particular
distinction. A mixture of Gaussian states can be non-Gaussian; neither
Wigner negativity nor separation from their convex hull is claimed.

## Self-checks with answers

**Why does the coherence kernel have denominator $`8N`$?** Two real
coherent amplitudes differing by $`\Delta`$ have overlap
$`e^{-\Delta^2/2}`$. Here $`\Delta=(k-l)/(2\alpha)`$, giving
$`e^{-(k-l)^2/(8N)}`$. The diagonal is unchanged because $`\Delta=0`$.

**How can a vanishing phase width leave a finite effect?** At fixed
positive $`\lambda`$, typical pair numbers and their differences scale
as $`\alpha=\sqrt N`$. Hence $`(k-l)^2/N`$ stays order one even though
the phase standard deviation is $`1/(2\sqrt N)`$. The target state
itself grows with brightness.

**Why insist on a separate energy proof?** Consider probability
$`1-1/M`$ at zero and $`1/M`$ at $`M^2`$. Its total-variation distance
from a point mass at zero tends to zero, but its mean is $`M`$. Thus
accurate distributions in total variation need not have accurate
unbounded means. Our sector bound excludes precisely this logical gap.

[Complete theorem](THEOREM.md) · [Proof map](PROOF_MAP.md) ·
[Validity window](VALIDITY_WINDOW.md) · [Repository overview](../README.md)
