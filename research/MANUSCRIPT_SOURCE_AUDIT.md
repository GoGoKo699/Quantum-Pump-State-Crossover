# Manuscript source audit and contribution boundary

Read together with the [earlier equation-level comparison](SOURCE_REVIEW.md)
and [original source record](SOURCES.md). This audit adds a direct 1999
same-model predecessor and a 1998 strong-pump analysis. It does not replace
prior readings, infer absence from inaccessible papers, or claim exhaustive
priority clearance. Bibliographic entries are in
[references.bib](../manuscript/references.bib).

## 1. D'Ariano–Paris–Sacchi: depletion is not a state-validity criterion

G. M. D'Ariano, M. G. A. Paris and M. F. Sacchi, *On the parametric
approximation in quantum optics*, Nuovo Cimento B **114**, 339 (1999),
[arXiv:quant-ph/9902013v1](https://arxiv.org/pdf/quant-ph/9902013).
The primary text was read, especially the introduction, Sec. 4, Eqs. (26)–(34),
and conclusion. The [author's publication list](https://wordpress.qubit.it/people/dariano/publications-dariano/)
confirms journal, volume, first page and year.

The paper explicitly treats coherent-pump nondegenerate conversion with
vacuum outputs. It tests the approximation through output-state overlap
and also examines number distributions. It already argues that pump
coherence, rather than undepletion alone, controls validity. Its empirical
pump-Fano threshold is a numerical observation, not a general theorem to
adopt without proof. Figures were not digitized; failed screenshot retrievals
supply no numerical evidence.

**Our source dictionary:** their $\kappa(abc^\dagger+a^\dagger b^\dagger c)$
is related to our Hamiltonian by a phase rotation of one output; equivalently
one can choose their coherent pump phase $\beta=i\alpha$. This does not change
the photon-number or phase-adjusted state comparison. Their overlap is
$\mathcal O=\sqrt{\operatorname{Tr}(\rho_{\rm exact}\rho_{\rm target})}$,
so its square is our target fidelity. Their 99% overlap threshold is not a
1% pump-purity loss.

The manuscript must not claim the first demonstration that an undepleted
pump can yield an inaccurate state. The additional result to assess is the
controlled growing-gain state limit and the simultaneous count/state
separation in [the validity window](VALIDITY_WINDOW.md), not the older
qualitative criterion.

## 2. Bandilla–Drobný–Jex: negligible depletion at optimal squeezing

A. Bandilla, G. Drobný and I. Jex, *The classical parametric approximation
for three-wave interactions*, Optics Communications **156**, 112–122 (1998),
[doi:10.1016/S0030-4018(98)00404-0](https://doi.org/10.1016/S0030-4018(98)00404-0).
The publisher's abstract, introduction and selected-section preview were
read; a complete article PDF was not obtained.

That preview explicitly analyzes classical trajectories, pump-coordinate
scaling and quantum fluctuations of the initial fields, and states that pump
depletion at optimal two-mode squeezing becomes negligible for a strong
coherent pump. Thus negligible depletion accompanying a quantum squeezing
limitation is an established result. The preview does not justify an absence
claim about every theorem in the unread sections. Our trace-norm estimates,
complete count-distance bounds and pure-state-orthogonality corollary are
proved from the present dynamics, not inferred from those trajectories.

## 3. Existing closest comparisons retained

| Reference | What is inherited or directly overlaps | What must remain distinct |
|---|---|---|
| Chinni–Quesada (2024), PRA 110, 013712 | Same preparation and Hamiltonian, Gaussian-frame generator, pump entanglement and short-time purity coefficients | The fixed-degree onset polynomial is not a uniform growing-gain estimate. Our coefficient agreement and different fixed-loss asymptotic are both stated. |
| Vintskevich–Grigoriev–Filippov (2019), PRA 100, 053811 | Exactly the phase-averaged density-matrix family after a width substitution | Their width represents initial pump incoherence; here it is derived by tracing an initially pure pump. The source's sufficient validity condition does not cover this crossover. |
| Yanagimoto et al. (2022), Optica 9, 379 | Gaussian interaction frame, residual non-Gaussian dynamics, pump/output entanglement and quadrature noise | The frame and noise mechanism are not new; the explicit uniform norm bound is the present theorem's input to its measurement conclusions. |
| Kinsler–Fernée–Drummond (1993), PRA 48, 3310 | Pump phase uncertainty, squeezed/antisqueezed mixing, strong-pump squeezing scale and finite-expansion caution | The inspected author draft is dated 2002, not a verified identical publisher copy. Damaged extracted equations are not used for exact coefficients. |
| Horoshko–Shchesnovich (2025), PRA 112, 033706 | Number-shift overlap and error-specific validity analysis | Degenerate model and stated pair-index approximation domain are not silently transferred to the nondegenerate $k\sim\sqrt N$ or growing-window theorem. |
| Flórez et al. (2018), NJP 20, 123022 | A second interaction retaining the pump can reverse the first exactly | The reduced phase-mixture state does not describe subsequent joint operations on that correlated pump; an independent phase reference is a different resource. |

The Chinni–Quesada primary HTML and the relevant Gaussian-frame and
Horoshko–Shchesnovich primary texts were reread. The Vintskevich author-posted
text was checked again. The Kinsler draft reading remains the previously
recorded one. The Flórez publisher text confirms the exact reversal argument;
no metrological sensitivity or device performance number is borrowed.

## 4. Historical and adjacent reading boundaries

Hillery–Zubairy, *Path-integral approach to the quantum theory of the
degenerate parametric amplifier*, PRA **29**, 1275 (1984), remains available
at publisher-abstract and institutional-metadata level only in this review.
Publisher PDF and full-text endpoint retrievals failed. Its detailed historical
conditions are credited indirectly through the readable later papers, including
D'Ariano–Paris–Sacchi and Horoshko–Shchesnovich. The original body is not
represented as read. Similarly, the complete Bandilla article is not represented
as available merely because the extended preview was useful.

Karasev–Teretenkov's 2025 *Parametric approximation as an open quantum
systems problem* was screened at primary HTML level. It concerns a different
open-system reduction, including a dissipative Jaynes–Cummings setting;
its perturbative corrections are not a same-model replacement for the
present theorem. It is context, not evidence of novelty or a required
ingredient of the present proof. No unrelated attached spin-off paper was
used to fill these source gaps.

## 5. The additional claim after all these comparisons

The manuscript's candidate contribution is a **uniformly controlled dynamical
validity hierarchy** for the specified coherent-pump/vacuum-output model.
It derives the full crossover state rather than prescribes an initial phase
mixture; proves count accuracy and leading energy separately; establishes a
bounded, reference-dependent non-Gaussian signature; and locates the first
fixed-purity crossing without assuming monotonic exact dynamics.

The growing-window corollary sharpens the hierarchy using the same finite
bounds. In one explicit regime, count errors and fractional depletion vanish
while the output's distance from every pure state tends to one. This is not
an additional state-family invention, a new interaction-frame technique, or
a claim that every photon-counting application fails.

Correctness, originality and significance are different judgments. The
historical comparisons substantially reduce the novelty of broad wording
about pump back-action. They do not supply the particular error-controlled
joint statement proved here. Whether that quantitative completion has broad
enough physical significance must be judged from the stated theorem, not from
source-access failures or the number of passing tests.
