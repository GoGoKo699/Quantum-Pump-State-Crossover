# Manuscript scientific basis

## Central question and supported answer

**When does a bright coherent pump justify a quantum-state approximation,
rather than only accurate photon statistics?**

For the closed resonant nondegenerate trilinear Hamiltonian with vacuum
outputs, the answer is controlled by the ratio of generated pair number to
the pump's square-root photon-number scale, inside an explicitly proved
window. A single residual-state theorem gives three regimes: an accurate
pure TMSV, a finite-impurity crossover, and asymptotic distance one from every
pure state while the complete photon-count distribution remains accurate.
The output remains close to an established Gaussian phase-mixture family.

This is a theorem about the specified preparation and order of limits,
not an invented interaction or an assertion that the parametric approximation
is universally invalid. The phase mixture is obtained by tracing a quantum
pump, not imposed as initial technical noise.

## Manuscript-level claim hierarchy

| Level | Statement | Proof location |
|---|---|---|
| Central derivation | Explicit residual cubic-unitary state with a finite norm-error bound | [Theorem, Sec. 2](THEOREM.md); [domain review, Sec. 1](PROOF_REVIEW.md) |
| Physical state | Pump number marking and a phase-mixture reduced output with trace-distance control | [Theorem, Secs. 2.2–3](THEOREM.md) |
| Accuracy hierarchy | Counts remain accurate; nominal pure-state accuracy is equivalent to $\lambda_\alpha\to0$ in the proved window | [Validity window, Secs. 1–3](VALIDITY_WINDOW.md) |
| Strong separation | Vanishing fractional depletion and count error coexist with distance one from every pure state | [Validity window, Secs. 4–5](VALIDITY_WINDOW.md) |
| Gaussian comparison | A bounded quadrature statistic separates the exact state from every single Gaussian, not from their convex hull | [Theorem, Sec. 7](THEOREM.md); [validity window, Eq. W12](VALIDITY_WINDOW.md) |
| Time interpretation | Fixed-purity first-crossing law and its quantified remainder; no assumed exact monotonicity | [Analytical review, Secs. 3–4](PROOF_REVIEW.md) |
| Energy interpretation | Separate sector comparison controls the mean; trace distance alone is not used for an unbounded moment | [Theorem, Sec. 4](THEOREM.md); [validity window, Eq. W9](VALIDITY_WINDOW.md) |

The scaling-window corollary completes the accuracy statement; it introduces
no new pump input, interaction, loss process or measurement channel in the
generation dynamics. Its sufficient window is not promoted to the entire
undepleted regime. The enormous brightness parameters in bound-only examples
are not experimental proposals.

## Compact presentation

Open by crediting the established distinction between depletion and coherence
[DAPS1999, BDJ1998, KFD1993, CQ2024]. State the unresolved quantitative task:
a same-preparation dynamical approximation with controlled state error when
gain grows with brightness. Define $N=\alpha^2$, $r=\alpha gt$ and
$\lambda=(e^{2r}-1)/(8\alpha)$ before comparing scales.

The main statement can display the finite norm estimate, the physical-frame
coherence kernel, and the three-row accuracy hierarchy. One proof paragraph
explains why the exponentially amplified term is retained to all orders;
the remaining polynomial norms and operator-domain details belong with the
supporting proof. State the separate energy argument in the main text so that
count convergence is not mistaken for an unbounded-moment estimate.

Use the fixed-crossover purity figure to explain the finite transition and
the growing-window bound figure to show why state accuracy is a stronger
requirement than count accuracy. The [figure source and captions](../manuscript/FIGURES.md)
identify which curves are limits and which are finite-error bounds. The
first-crossing certificates demonstrate control of the onset, not a second
headline or a reason to center the paper on enormous photon numbers.

The quadrature law is a concrete way to expose the missing coherence. Its
phase-reference and shrinking-resolution assumptions must appear alongside
it. The count-preserving measurement class should also appear explicitly:
passive optics with vacuum ancillas and photon counting is not automatically
made inaccurate by the joint-state discrepancy.

## Statements the manuscript can and cannot make

The preparation is pure and evolution is unitary, so pump impurity certifies
entanglement between the pump and the two outputs jointly. The new explicit
sequence gives a second-Renyi entropy asymptotic for that partition. Neither
result is a quantitative assertion about signal versus idler entanglement.

The Gaussian mixture is an accurate reduced state, not a separable model of
the full pump/output state. It cannot be reused as a channel description for
an arbitrary input or a second interaction retaining the correlated pump.
A mixed Gaussian fit cannot remove the proved gap; a mixture of Gaussian
states can. This distinction excludes Wigner-negativity and convex-Gaussian-
hull claims.

The established phase-mixture family [VGF2019] and number-shift mechanism
[HS2025] must be credited before presenting their consequence. Our task is
to prove that the exact coherent-pump dynamics enters the claimed family
with the stated error, not to claim that the family was unknown.

The Chinni–Quesada short-time coefficients agree with the existing derivation.
Its eighth-order polynomial is nonuniform at the ultimate fixed-loss onset;
this does not refute the reported finite-range numerical behavior. The
D'Ariano–Paris–Sacchi overlap convention is a square root of target fidelity,
not pump purity. Those comparisons must not silently identify different
thresholds.

## Scope completion and significance

The manuscript's declared claims have explicit proofs, source mappings,
independent finite checks and reproducible figure data. Additional modes,
loss, optimized pump preparations, or a device study are different projects;
none is required to state this mathematical result correctly. No external
peer-review or exhaustive-priority claim is made. The original Hillery–Zubairy
full text and the complete Bandilla article remain outside the inspected
material; their known contributions are credited through the specified
accessible sources, not by inventing an absence finding.

The broad warning about undepleted pumps is old. The contribution to assess
is the error-controlled dynamical hierarchy, particularly the coexistence of
correct complete counts with nearly orthogonal pure-state descriptions.
That distinction makes the result worth writing up, but proof completeness
alone does not establish broad editorial significance. The [source audit](MANUSCRIPT_SOURCE_AUDIT.md)
and [bibliography](../manuscript/references.bib) provide the corresponding
attribution boundaries.
