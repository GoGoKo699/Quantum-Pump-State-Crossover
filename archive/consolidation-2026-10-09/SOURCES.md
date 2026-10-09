# Source comparison and reading record

9 October 2026. These are primary-source comparisons, not exhaustive priority clearance. This consolidation did not read, alter, or use the older unrelated project PDFs as scientific inputs. No external paper PDF or figure is included in this package.

## [CQ] Chinni–Quesada: closest same-model purity analysis

K. Chinni and N. Quesada, *Beyond the parametric approximation: pump depletion, entanglement and squeezing in macroscopic down-conversion*, Physical Review A 110, 013712 (2024), arXiv:2312.09239v2.
https://arxiv.org/html/2312.09239v2

The source uses the same nondegenerate Hamiltonian and coherent pump/vacuum outputs. It already distinguishes depletion from pump entanglement and derives the general Gaussian-frame generator. The earlier follow-up's reconstruction of Appendix C and Eq. (48) is preserved. Appendix D Eqs. (119)–(120) and its text give a fixed-degree purity-threshold estimate and a finite-range fitted exponent. The controlled logarithmic first-crossing theorem agrees with the short-time coefficients but differs from their large-amplitude polynomial-root extrapolation. The same-model comparison is not replaced by a degenerate-model analogue.

This pass reread the primary HTML introduction, pump-purity discussion, and Appendix D prose. No plot was digitized or source data refitted. The complete equation-level reconstruction and numerical root comparisons remain in prior/FOLLOWUP.md, rather than being claimed as new work this round.

## [HS] Horoshko–Shchesnovich: formal number-shift and validity precedents

D. B. Horoshko and V. S. Shchesnovich, *Isoenergetic model for optical downconversion and error-specific limits of the parametric approximation*, Physical Review A 112, 033706 (2025), arXiv:2503.18828v2.
https://arxiv.org/html/2503.18828v2
https://journals.aps.org/pra/abstract/10.1103/wtcf-5pkh

The model is degenerate. The energy-correlated approximation and shifted coherent-pump amplitudes provide a formal predecessor for the Gaussian pair-number coherence kernel. Its stated small-pair-index accuracy domain is not silently promoted to a uniform estimate at k=Theta(sqrt(N)) or transferred to the nondegenerate model. The source also explicitly recounts historical path-integral high-gain validity conditions. Error-specific validity and the distinction between energy and state accuracy are therefore established motivations, not new general principles. The primary HTML historical/model passages were reread; detailed earlier equation comparison is preserved under prior/.

## [GIF] Gaussian interaction frames and non-Gaussian quadrature noise

R. Yanagimoto et al., *Onset of non-Gaussian quantum physics in pulsed squeezing with mesoscopic fields*, Optica 9, 379 (2022), arXiv:2111.13799.
https://arxiv.org/pdf/2111.13799

Primary PDF Sections II and V explain Gaussian interaction-frame reduction and connect residual quantum fluctuations to lab-frame squeezed quadratures. Equations (35)–(36) give the frame-to-quadrature relationship. The paper already discusses non-Gaussian noise, purity loss, and departures that Gaussian operations do not remove. The present bounded characteristic-function consequence must not be framed as the first measurable non-Gaussian effect of a quantum pump. Its claimed content is the explicit controlled large-brightness crossover law. No figure-specific numerical claim from this paper is used; the multimode waveguide dynamics and device operating windows are not reconstructed here.

## [KFD] Quantum-pump squeezing and finite-expansion caution

P. Kinsler, M. Fernée and P. D. Drummond, *Limits to squeezing and phase information in the parametric amplifier*, Physical Review A 48, 3310–3320 (1993).
https://doi.org/10.1103/PhysRevA.48.3310
https://www.researchgate.net/publication/13379119_Limits_to_squeezing_and_phase_information_in_the_parametric_amplifier

The publisher abstract was a pilot input. This pass additionally read the relevant introduction and Section II prose in the author-uploaded draft, hosted as content uploaded by Peter Drummond. That document is dated 12 September 2002 and identifies itself as a draft of the 1993 paper with updated references and email addresses; it is not being represented as a verified byte-identical publisher version.

It explicitly discusses both degenerate and nondegenerate models, pump phase uncertainty admixing antisqueezed fluctuations, an N^(-1/2) minimum squeezed-variance scale, and why finite asymptotic expansions require care at growing logarithmic gain. These mechanisms and scales are inherited. Several equations in the extracted draft text have encoding damage; no exact coefficient is transcribed from an unreadable expression, and the plots were not used. The publisher PDF and the linked downloadable author PDF were not retrieved. The readable prose suffices for the stated historical boundary, not an absence claim about the complete crossover theorem.

## [HZ] Historical path-integral source: remaining full-text boundary

M. Hillery and M. S. Zubairy, *Path-integral approach to the quantum theory of the degenerate parametric amplifier*, Physical Review A 29, 1275 (1984).
https://journals.aps.org/pra/abstract/10.1103/PhysRevA.29.1275

The publisher abstract states the fully quantized path-integral treatment, validity conditions, and reduced squeezing from pump quantization. The publisher PDF again failed to retrieve. Historical detailed conditions are credited through [HS] and the readable [KFD] discussion; the original full text remains unread. This boundary is not evidence of novelty or an obstruction to the mathematical proof.

## [F18] Reusing the correlated pump is not an independent reference

J. Flórez et al., New Journal of Physics 20, 123022 (2018), arXiv:1808.06136.
https://doi.org/10.1088/1367-2630/aaf3d2

The preceding source read of this fully quantum nonlinear-interferometer work is preserved in prior/SOURCES.md. This pass does not claim a new full-text review. The recorded exact-reversal example guards against treating the pump-traced reduced model as a description of subsequent dynamics retaining that pump. No sensitivity or hardware advantage is borrowed from the source.

## Mathematical status of the new quadrature consequence

The Gaussian shear, characteristic-function integration, trace-distance contraction, and modulus identity for Gaussian characteristic functions are elementary consequences explicitly proved in THEOREM.md. The witness is not claimed as a new general non-Gaussianity test. The limiting signal state is itself a convex Gaussian mixture: the result separates it from each single Gaussian state, not from the convex Gaussian hull. No Wigner-negativity claim is made.
