# Sources and attribution

The references below identify the model, methods, and physical mechanisms
underlying the result. The [phase-mixture and onset comparison](SOURCE_REVIEW.md)
gives the detailed formula dictionary; [references.bib](../manuscript/references.bib)
contains the bibliographic records.

## Tutorial: Yanagimoto et al. (2024) [YNG2024]

R. Yanagimoto et al., *Mesoscopic ultrafast nonlinear optics—the emergence
of multimode quantum non-Gaussian physics*, Optica **11**(7), 896–918 (2024).
[Author version, arXiv:2311.13775v1](https://arxiv.org/abs/2311.13775v1) ·
[Published review](https://doi.org/10.1364/OPTICA.514075)

Section II and Boxes 1–3 provide the single-source learning route. The
Gaussian-frame decomposition, exponentially amplified cubic interaction,
and logarithmic onset scale appear in the review's degenerate-amplifier
example. Its conditional-displacement onset criterion differs from the
pump-purity crossing studied here. The [tutorial bridge](TUTORIAL_BRIDGE.md)
translates the model and connects these established ideas to the
nondegenerate state approximation, finite error bounds, and count/state
validity hierarchy.

## Depletion and state validity: D'Ariano–Paris–Sacchi [DAPS1999]

G. M. D'Ariano, M. G. A. Paris and M. F. Sacchi, *On the parametric
approximation in quantum optics*, Nuovo Cimento B **114**, 339 (1999).
[Primary text, arXiv:quant-ph/9902013v1](https://arxiv.org/pdf/quant-ph/9902013v1)

Section 4, Eqs. (26)–(34), treats coherent-pump nondegenerate conversion with
vacuum outputs, comparing output-state overlap and photon-number
statistics. Pump coherence, rather than fractional depletion alone, is
already a state-validity criterion in this work. Its pump-Fano threshold
is an empirical numerical criterion.

Their Hamiltonian $\kappa(abc^\dagger+a^\dagger b^\dagger c)$ is related to
ours by a phase rotation of one output; equivalently their coherent pump
phase can be chosen as $\beta=i\alpha$. Their overlap is
$\mathcal O=\sqrt{\operatorname{Tr}(\rho_{\rm exact}\rho_{\rm target})}$,
so $\mathcal O^2$ is our squared-overlap fidelity. A 99% overlap threshold
therefore differs from a 1% pump-purity loss. The present
[validity window](VALIDITY_WINDOW.md) quantifies the simultaneous count/state
separation through a controlled growing-gain approximation.

## Strong-pump squeezing: Bandilla–Drobný–Jex [BDJ1998]

A. Bandilla, G. Drobný and I. Jex, *The classical parametric approximation
for three-wave interactions*, Optics Communications **156**, 112–122 (1998).
[Published article](https://doi.org/10.1016/S0030-4018(98)00404-0)

The publisher's abstract, introduction, and selected-section excerpt describe
classical trajectories, pump-coordinate scaling, and initial quantum
fluctuations. They establish that pump depletion at optimal two-mode
squeezing becomes negligible for a strong coherent pump. The present
state-distance and complete count-distance estimates follow from the
quantum dynamics and its explicit remainder bounds.

## Same-model purity and frame: Chinni–Quesada [CQ / CQ2024]

K. Chinni and N. Quesada, *Beyond the parametric approximation: pump depletion,
entanglement and squeezing in macroscopic down-conversion*, Physical Review A
**110**, 013712 (2024).
[Primary text, arXiv:2312.09239v2](https://arxiv.org/html/2312.09239v2) ·
[Published article](https://doi.org/10.1103/PhysRevA.110.013712)

This work uses the same Hamiltonian and coherent-pump/vacuum-output
preparation. Appendix C, Eqs. (96)–(100), gives the Gaussian-frame generator;
Eq. (48) gives short-time purity coefficients. Appendix D, Eqs. (119)–(120),
gives a fixed-degree purity-threshold estimate and a finite-range fitted
exponent. Our fixed-gain expansion reproduces the leading large-$\alpha$
parts of its sixth- and eighth-order coefficients. The logarithmic
first-crossing law concerns the nonuniform large-amplitude extrapolation
of that polynomial root; the
[explicit comparison](SOURCE_REVIEW.md) keeps this distinct from its
finite-range numerical behavior.

## Phase-averaged state family: Vintskevich–Grigoriev–Filippov [VGF2019]

S. V. Vintskevich, D. A. Grigoriev and S. N. Filippov, *Effect of an incoherent
pump on two-mode entanglement in optical parametric generation*, Physical
Review A **100**, 053811 (2019).
[arXiv:1905.05756v2](https://arxiv.org/abs/1905.05756v2) ·
[Published article](https://doi.org/10.1103/PhysRevA.100.053811)

Its Gaussian phase-averaged squeezed-state family is exactly our reduced
comparison state after the width substitution $w=1/(2\alpha)$. The source
introduces that width through initial pump incoherence; here the width
comes from tracing an initially pure quantum pump. The
[formula dictionary and validity comparison](SOURCE_REVIEW.md) explain the
preparation difference, the source's sufficient high-gain condition, and
the purity limit.

## Gaussian interaction frames: Yanagimoto et al. (2022) [GIF / GIF2022]

R. Yanagimoto et al., *Onset of non-Gaussian quantum physics in pulsed
squeezing with mesoscopic fields*, Optica **9**, 379 (2022).
[Primary text, arXiv:2111.13799](https://arxiv.org/pdf/2111.13799)

Sections II and V develop Gaussian interaction-frame reduction and connect
residual fluctuations to laboratory-frame squeezed quadratures, explicitly
in Eqs. (35)–(36). Pump/output entanglement, non-Gaussian noise, and deviations
that Gaussian operations cannot remove are established mechanisms. The
present bounded characteristic-function result quantifies them for the
specified nondegenerate growing-gain limit. This paper is distinct from the
2024 tutorial review.

## Pump phase uncertainty: Kinsler–Fernée–Drummond [KFD / KFD1993]

P. Kinsler, M. Fernée and P. D. Drummond, *Limits to squeezing and phase
information in the parametric amplifier*, Physical Review A **48**,
3310–3320 (1993).
[Published article](https://doi.org/10.1103/PhysRevA.48.3310) ·
[Author-posted draft](https://www.researchgate.net/publication/13379119_Limits_to_squeezing_and_phase_information_in_the_parametric_amplifier)

The introduction and Section II of the author draft dated 12 September 2002
support the mechanism comparison: pump phase uncertainty mixes antisqueezed
fluctuations into the squeezed quadrature in both degenerate and nondegenerate
models. The draft discusses the $N^{-1/2}$ minimum squeezed-variance scale
and the care needed with finite asymptotic expansions at logarithmically
growing gain. These mechanisms and scales precede the present theorem.

## Number shifts and error criteria: Horoshko–Shchesnovich [HS / HS2025]

D. B. Horoshko and V. S. Shchesnovich, *Isoenergetic model for optical
down-conversion and error-specific limits of the parametric approximation*,
Physical Review A **112**, 033706 (2025).
[Primary text, arXiv:2503.18828v2](https://arxiv.org/html/2503.18828v2) ·
[Published article](https://doi.org/10.1103/wtcf-5pkh)

The degenerate model supplies energy-correlated coherent-amplitude shifts
and a predecessor for the Gaussian pair-number coherence kernel, together
with error-specific validity criteria. Its approximation uses a stated
small-pair-index domain. The nondegenerate $k=\Theta(\sqrt N)$ regime and
varying-parameter window here instead have explicit state-error bounds.
The paper also reviews historical path-integral high-gain conditions.

## Historical path-integral treatment: Hillery–Zubairy [HZ / HZ1984]

M. Hillery and M. S. Zubairy, *Path-integral approach to the quantum theory
of the degenerate parametric amplifier*, Physical Review A **29**, 1275 (1984).
[Publisher abstract](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.29.1275)

The publisher abstract credits a fully quantized treatment, validity
conditions, and reduced squeezing due to pump quantization. The detailed
historical conditions discussed here are attributed through
Horoshko–Shchesnovich and the Kinsler–Fernée–Drummond author draft.

## Retaining the correlated pump: Flórez et al. [F18 / F2018]

J. Flórez et al., *The phase sensitivity of a fully quantum three-mode
nonlinear interferometer*, New Journal of Physics **20**, 123022 (2018).
[Published article](https://doi.org/10.1088/1367-2630/aaf3d2) ·
[arXiv:1808.06136](https://arxiv.org/abs/1808.06136)

A second interaction retaining the pump can reverse the first exactly.
Accordingly, our pump-traced approximation describes the reduced output,
while subsequent joint operations retaining the correlated pump require
the joint state. An independent phase reference defines a different
measurement resource.
