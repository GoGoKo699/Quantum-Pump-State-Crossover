# Correct photon counts, incorrect pure-state description

**9 October 2026. Follow-up to the coherent-pump crossover pilot.** The Hamiltonian, initial coherent pump, vacuum signal and idler, and order of limits are unchanged. The incoming thirteen-file pilot is preserved under `prior/`. No repository or other spin-off was accessed. The derivations below are author-side work, not external proof review or a priority certificate.

## 1. Result and scope

Keep

\[
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\quad
|\Psi(0)\rangle=|\alpha\rangle_c|00\rangle_{ab},\quad
N=\alpha^2,\quad \tau=gt,\quad r=\alpha\tau.
\]

For a fixed crossover coordinate \(\lambda\ge0\), take

\[
r=r_\alpha(\lambda)=\tfrac12\log(1+8\alpha\lambda).
\]

The preserved pilot proves that after the pump displacement and nominal squeezing are removed, the exact pure state approaches

\[
|\chi_\lambda\rangle=\exp[\lambda pR]|000\rangle,
\quad p=d-d^\dagger,\quad
R=1+n_a+n_b+a^\dagger b^\dagger+ab.
\]

It gives the explicit state-norm bound \(\epsilon_\alpha\) in its Eq. (7), uniform on bounded lambda intervals. In particular pump purity tends to

\[
\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}dz.
\]

**New consequence.** The exact reduced signal-idler state is also trace-close to an explicit phase-averaged two-mode squeezed vacuum. Its entire pair-number probability distribution approaches the undepleted-pump distribution in total variation, and its mean pair number has the same leading asymptotic. Nevertheless, its purity and fidelity with the pure squeezed vacuum remain finitely below one.

This is an approximation to one specified input state and one time scaling, not an energy-unconstrained channel approximation. The Gaussian phase averaging is a representation of a reduced state after tracing out the quantum pump, not added technical noise and not a Markovian phase-diffusion process. It does not turn the globally entangled state into a separable state.

## 2. A joint number-marking approximation

Write the nominal squeezed vacuum as

\[
|\mathrm{TMSV}_r\rangle=\sum_{k\ge0}s_k|k,k\rangle,\qquad
s_k=\operatorname{sech}r\,(\tanh r)^k.
\]

Define a normalized pure state

\[
\boxed{
|\Phi_{\alpha,r}\rangle
=\sum_{k\ge0}s_k\,|\alpha-k/(2\alpha)\rangle_c|k,k\rangle_{ab}.
}\tag{1}
\]

The pump is displaced by an amount marking the number of generated pairs. This is an approximation, not the exact conserved-number-sector decomposition: individual coherent components in (1) need not have the exact conserved energy. It should not be used as an exact generator at other times or with other inputs.

### Controlled comparison with the pilot state

On the subspace \(n_a=n_b\), let

\[
Q=1+n_a+n_b,\quad C=a^\dagger b^\dagger+ab,\quad
L=C-Q,\quad A=a^\dagger b^\dagger-ab.
\]

The same unitary transformation \(D_c(-\alpha)S_{ab}(-r)\) used for the exact state maps (1) to \(e^{pB_\alpha}|000\rangle\), where

\[
B_\alpha=\frac{S(-r)n_aS(r)}{2\alpha}
=\frac{e^{2r}R-e^{-2r}L-2I}{8\alpha}.
\]

Since \(e^{2r}=1+8\alpha\lambda\),

\[
B_\alpha-\lambda R=\frac{R-e^{-2r}L-2I}{8\alpha}.
\]

For \(V_s=e^{s\lambda pR}\), the pilot's exact finite commutators give

\[
V_s^\dagger L V_s=L-4s\lambda pA+4s^2\lambda^2p^2R.
\]

Consequently

\[
\|p(R-2I)|000\rangle\|=\sqrt2,
\]
\[
\|p(L-4s\lambda pA+4s^2\lambda^2p^2R)|000\rangle\|^2
=2+48s^2\lambda^2+480s^4\lambda^4.
\]

Duhamel's identity, with the exact interpolating unitary multiplying the remainder, yields

\[
\boxed{
\|e^{pB_\alpha}|000\rangle-|\chi_\lambda\rangle\|
\le d_\alpha(\lambda)
:=\frac{\sqrt2+e^{-2r}\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}.
}\tag{2}
\]

Both \(pB_\alpha\) and \(pR\) generate well-defined unitaries: the pump quadrature strongly commutes with the self-adjoint signal operator. The displayed Duhamel actions are finite polynomial actions on Schwartz vectors. As in the pilot, no unbounded-operator norm or convergent Dyson-series assumption is used.

Combining (2) with the pilot theorem gives

\[
\boxed{
\|\Psi_\alpha(r)-\Phi_{\alpha,r}\|
\le\epsilon_\alpha(\lambda)+d_\alpha(\lambda)
=:\eta_\alpha(\lambda)
=O_\Lambda(\log\alpha/\alpha).
}\tag{3}
\]

The conservative bound may exceed one for small amplitudes; the asymptotic and the exact inequalities have their usual meanings. The alpha-dependent state (1) is not the fixed limiting frame state; it is a useful approximation in the physical frame.

## 3. Exact reduced-state form and the effective phase uncertainty

Tracing the pump in (1), using the overlap of real coherent amplitudes, gives

\[
\boxed{
\sigma_{ab}(\alpha,r)
=\sum_{k,l\ge0}s_ks_l
\exp\!\left[-\frac{(k-l)^2}{8N}\right]
|k,k\rangle\langle l,l|.
}\tag{4}
\]

Equivalently,

\[
\sigma_{ab}=\mathbb E_\vartheta
\left[e^{i\vartheta n_a}|\mathrm{TMSV}_r\rangle\langle\mathrm{TMSV}_r|
e^{-i\vartheta n_a}\right],\qquad
\vartheta\sim\mathcal N\!\left(0,\frac1{4N}\right).
\tag{5}
\]

The Gaussian can be wrapped modulo \(2\pi\) without changing (5). It is a reduced-state representation, not an assumed random phase in the initially pure pump.

For the actual signal-idler state,

\[
\boxed{
\tfrac12\|\rho_{ab}(\alpha,r)-\sigma_{ab}(\alpha,r)\|_1
\le\eta_\alpha(\lambda)\longrightarrow0.
}\tag{6}
\]

The phase standard deviation is only \(1/(2\sqrt N)\), but populated pair-number separations are of order \(\sqrt N\). Their product is finite, so coherence between those components is appreciably reduced. This expresses the source of the finite state error without requiring a large fractional energy change.

### Independent Gaussian-overlap check

Condition on the displaced pump momentum \(P=(d-d^\dagger)/(i\sqrt2)\). Its vacuum density is \(e^{-P^2}/\sqrt\pi\), and \(\vartheta=P/(\sqrt2\alpha)\). In the unsqueezed signal frame,

\[
S(-r)e^{i\vartheta n_a}S(r)|00\rangle
=A_P\sum_{k\ge0}z_P^k|k,k\rangle,
\]
\[
A_P=\frac{1-t^2}{1-t^2e^{i\vartheta}},\qquad
z_P=\frac{t(e^{i\vartheta}-1)}{1-t^2e^{i\vartheta}},\qquad t=\tanh r.
\]

One checks \(|A_P|^2/(1-|z_P|^2)=1\). As alpha increases at fixed lambda,

\[
A_P\to\frac1{1-i\sqrt2\lambda P},\qquad
z_P\to\frac{i\sqrt2\lambda P}{1-i\sqrt2\lambda P},
\]

which are exactly the coefficients of \(e^{i\sqrt2\lambda PR}|00\rangle\). The numerical check evaluates the geometric-series overlap and its Gaussian integral rather than approximating these states by a huge physical photon cutoff.

## 4. Which predictions remain correct?

### The complete pair-count distribution

The diagonal of (4) is exactly

\[
p_k=(1-q)q^k,\qquad q=\tanh^2r,
\]

the undepleted-pump distribution. Equation (6) and contractivity under measurement imply

\[
\boxed{\frac12\sum_{k\ge0}|\Pr_{\rm exact}(n_a=n_b=k)-p_k|
\le\eta_\alpha(\lambda)\to0.}\tag{7}
\]

The exact dynamics always has support in \(n_a=n_b\). Each individual signal or idler marginal is therefore diagonal in its number basis. Each marginal separately approaches the corresponding thermal state in trace distance, even though the joint pair state does not approach the pure squeezed vacuum.

### Passive optical processing without a phase reference

On the pair support, \(e^{i\vartheta n_a}\) is the same as \(e^{i\vartheta(n_a+n_b)/2}\). Thus every POVM commuting with total signal photon number has exactly the same outcome probabilities on (4) and on the pure TMSV. A passive optical network with vacuum ancillary modes followed by photon counting is an example. Equation (6) transfers this equality to an asymptotically vanishing outcome-distribution error for the exact state, uniformly over those measurements.

This conclusion does not cover mixing with another coherent or squeezed phase reference, an active phase-sensitive operation, multiple independently pumped sources, or a measurement using the correlated pump. In particular it is not a theorem about arbitrary Gaussian boson sampling circuits. Sensitivity to coherence between total-number sectors depends on the available phase reference, an established structural issue rather than a new measurement principle.

### The mean photon number: use the independent energy bound too

Total variation alone does not control an unbounded mean. Here the pilot's separate sector-energy estimate supplies the missing control.

The geometric distributions obey \(k/\alpha\Rightarrow 2\lambda U\), where U has the unit exponential distribution. Equation (7) implies the same weak limit for the exact counts. For any fixed cutoff M, expectations of \(\min(k/\alpha,M)\) converge, so

\[
\liminf_{\alpha\to\infty}\frac{\langle n_a\rangle}{\alpha}\ge2\lambda.
\]

The independent pilot Eq. (13) gives the matching upper bound

\[
\limsup_{\alpha\to\infty}\frac{\langle n_a\rangle}{\alpha}\le2\lambda.
\]

Therefore, for every fixed positive lambda,

\[
\boxed{\langle n_a\rangle\sim2\lambda\sqrt N,
\qquad\frac{N-\langle n_c\rangle}{N}\sim\frac{2\lambda}{\sqrt N}.}\tag{8}
\]

The same leading mean is predicted by the nominal TMSV. The fractional-depletion estimate is now an asymptotic equality, obtained by combining bounded-observable convergence with a separate energy inequality, not by assuming that state norm controls photon number.

### Joint state accuracy nevertheless fails

The preserved limit and (6) yield

\[
\operatorname{Tr}\rho_{ab}^2\to\mathcal P(\lambda),\qquad
F_\alpha:=\langle\mathrm{TMSV}_r|\rho_{ab}|\mathrm{TMSV}_r\rangle
\to\mathcal P(\lambda/\sqrt2).
\]

The target projector is a bounded observable, so

\[
\boxed{\liminf\frac12\|\rho_{ab}-|\mathrm{TMSV}_r\rangle\langle\mathrm{TMSV}_r|\|_1
\ge1-\mathcal P(\lambda/\sqrt2)>0.}\tag{9}
\]

At lambda=1/2, pump and pair purities tend to 0.757872156141312, the target fidelity tends to 0.842738458576109, and the trace-distance lower bound is 0.157261541423891. Both marginal thermal descriptions and every measurement in the preceding number-conserving class become accurate, while an unrestricted joint-state claim does not.

The projector is a mathematical distinguishability test, not a claimed experimental implementation. Applying a nominal inverse squeezer would require its own phase-referenced resource. Reversing the exact trilinear evolution while retaining the same correlated pump is a different operation and can undo entanglement; it must not be confused with tracing out the pump and applying an independent classical inverse.

## 5. What the closest source already contains

### Chinni–Quesada: exact transformed generator, but a different asymptotic extrapolation

The same-model primary source [CQ] has the same coherent-pump initial state and number-sector conservation. Its general Appendix C Eq. (99), with the displacement fixed at alpha and squeezing set to r=alpha*tau, gives exactly the pilot's transformed generator. Its selected self-consistent frame instead takes

\[
\partial_\tau\beta=-\tfrac12\sinh(2\eta),\qquad
\partial_\tau\eta=\beta,
\]

and uses Eq. (100). The frame and the residual cubic operators are therefore inherited.

At our crossover, their classical-frame functions satisfy

\[
\beta=\alpha-\lambda+o(1),\qquad\eta=r+O_\Lambda(1/\alpha).
\]

To see this without extrapolating a time polynomial, use the invariant \(\beta^2+\sinh^2\eta=\alpha^2\), the positive-pump branch, and

\[
0\le r-\eta\le\alpha^{-2}\int_0^r\sinh^2u\,du
=\alpha^{-2}\left[\tfrac14\sinh(2r)-\tfrac12r\right].
\]

Their moving frame thus has the limiting residual state

\[
e^{\lambda p(R-I)}|000\rangle=D_c(\lambda)|\chi_\lambda\rangle.
\]

It has exactly the same entanglement and purity. The non-Gaussian crossover is not removed by absorbing the deterministic mean depletion into the Gaussian frame. This is our reconstruction from the source equations, not a quoted source limit theorem.

At fixed gain r, retaining the first inverse-alpha term gives

\[
|\psi_\alpha(r)\rangle
=|000\rangle-\frac{\cosh(2r)-1}{4\alpha}|1,0,0\rangle
-\frac{\sinh(2r)-2r}{4\alpha}|1,1,1\rangle+O_r(\alpha^{-2}).
\]

The first correction is pump-only; the second gives leading impurity

\[
1-\mathcal P_\alpha(r)
=\frac{[\sinh(2r)-2r]^2}{8\alpha^2}+o_r(\alpha^{-2}).\tag{10}
\]

For comparison of coefficients, expansion of its numerator gives

\[
\frac1{\alpha^2}\left(\frac29r^6+\frac4{45}r^8+\frac{82}{4725}r^{10}+\cdots\right).
\]

This agrees with the leading inverse-alpha part of the source Eq. (48). The source's additional \(-2r^8/(9\alpha^4)\) impurity term is a higher inverse-alpha correction, not a contradiction. Equation (10) is a fixed-gain consistency reconstruction; it is not the full crossover purity at fixed nonzero lambda, where all orders in lambda matter.

### Why the eighth-order threshold cannot be the large-alpha asymptotic

The source Appendix D Eq. (120) solves

\[
\frac29\alpha^4\tau^6+
\left(\frac4{45}\alpha^6-\frac29\alpha^4\right)\tau^8=\varepsilon
\]

and reports an alpha^(-3/4) estimate plus a finite-range numerical exponent near -0.769. At the controlled threshold \(\tau=[\log\alpha+O(1)]/(2\alpha)\), the left-hand polynomial tends to zero, while the exact impurity tends to the prescribed positive epsilon. Thus the polynomial cannot remain uniform at that threshold.

The preserved theorem instead gives

\[
\tau_\varepsilon(\alpha)
=\frac{\log\alpha+\log(8\lambda_\varepsilon)+o(1)}{2\alpha},
\qquad \mathcal P(\lambda_\varepsilon)=1-\varepsilon.
\tag{11}
\]

For epsilon=0.01, lambda_epsilon=0.071774448243058 and the logarithmic offset is -0.554785198638437.

Our directly computed 0.99-purity roots and the root of the source polynomial are:

| alpha | Exact-frame numerical root tau | Root of source eighth-order polynomial | Crossover-curve estimate tau |
|---:|---:|---:|---:|
| 30 | 0.0527763588184 | 0.0546993057308 | 0.0483806980085 |
| 100 | 0.0209443326941 | 0.0229232567090 | 0.0203382537060 |
| 1000 | 0.00318759749399 | 0.00420948949405 | 0.00317735506621 |
| 10000 | 0.000432929703849 | 0.000756964878790 | 0.000432786465743 |

The last column uses r_alpha(lambda_epsilon)/alpha, retaining the harmless +1 in the logarithm. Numerical roots are local bracketed crossings near the predicted threshold, not certified finite-alpha first crossings; the analytical asymptotic first-crossing statement is proved separately in the pilot. These are recalculated quantities, not digitized source figures. The source's cutoff-normalized target tends to the fixed 0.01 target used here.

The short-time coefficients and their useful finite-amplitude behavior are not refuted. In particular the polynomial is closer than the leading crossover estimate at alpha=30. A finite fitted power exponent is compatible with a slowly varying logarithmic correction; no source-fit parameters were re-estimated from unavailable plot data.

### Horoshko–Shchesnovich and the older path-integral scale

[HS] treats degenerate down-conversion, so its pair coefficients and gain convention are not interchangeable with ours. Its Eq. (42) is an energy-sector-correlated approximation, and its Eq. (53) explicitly tracks number-shifted coherent-pump coefficients in reduced-state coherences. Sections IV B–D state the small-pair-index accuracy condition n=o(sqrt(m)) in a sector with m initial pump photons.

At the present crossover the typical pair number is proportional to sqrt(N), not little-o(sqrt(N)). Their stated error estimate cannot simply be carried into this scaling. Nevertheless the **formal number-shift structure already explains the phase kernel**. For a coherent pump, C_m=exp(-N/2)alpha^m/sqrt(m!). A Gaussian central approximation to

\[
\sum_{n\ge0}C_{n+k}C_{n+l}
\]

with k,l=O(sqrt(N)) produces exp[-(k-l)^2/(8N)]. This is a kinematic implication of shifted coherent-number amplitudes, not a new physical-noise principle. Equations (3)–(6) provide the controlled dynamical statement for this nondegenerate model; the source's degenerate-model accuracy bound is not being silently strengthened or substituted.

The primary [HS] text also reproduces the Hillery–Zubairy conditions involving e^(2r)/alpha and r e^(2r)/alpha. Therefore neither the logarithmic gain scale nor the distinction between number accuracy and quantum-state validity can be claimed as a newly discovered principle. The complete 1984 article [HZ] remains unread after publisher and institutional access attempts; its primary abstract establishes the subject, while its detailed historical conditions are attributed through the explicitly identified [HS] account. This is a reading boundary, not evidence of originality or an unresolved mathematical obstruction.

### Gaussian interaction frames and phase reference

[GIF] Eqs. (5)–(12) already removes pump displacement and signal squeezing, leaving residual cubic dynamics and studying pump–signal entanglement. Its first single-mode example is degenerate; its later waveguide account is multimode. The leading residual generator here can be reconstructed from the same method. The candidate distinction is the uniformly controlled growing-gain state and its consequences, not the frame or the existence of non-Gaussian dynamics.

The phase-sensitive nonlinear-interferometer study [F18] retains and reuses the pump. It explicitly observes that a suitably phased second identical interaction reverses the first. That source is a useful guard against treating the pump-traced phase average as a law for all subsequent pump-assisted operations. No interferometric sensitivity advantage is derived here.

## 6. Contribution decision

**Continue this single crossover result for compact consolidation and focused contribution review; do not create a repository or claim a strong PRL forecast yet.** The useful statement is now stronger and more discriminating than a generic warning about undepleted pumps: within the same unitary model, the classical-pump prediction can become accurate for the complete number distribution, each local marginal, and a class of processed counting measurements, yet remain finitely inaccurate for the joint quantum state. The exact threshold law also differs from a same-model finite-polynomial asymptotic extrapolation.

The skeptical interpretation remains that the mechanism and its formal state structure follow naturally from established pump fluctuations, energy-sector correlations, and Gaussian frames. The inspected sources do not supply this complete uniform nondegenerate theorem or its purity-onset law, but that is not exhaustive priority clearance. The result's significance must come from the controlled separation of validity criteria, not from the absence of an erfc formula in an older paper or a generic claim that all applications fail.

No loss channel, extra mode, pump-state optimization, or external phase-reference apparatus is needed to state the present theorem. An implementation or a claim about phase-sensitive use would require its own accounting. The next consolidation should make the joint-state theorem, its norm/energy bounds, the number-versus-coherence consequence and the implication-level source comparison one self-contained account, without expanding the physical program.

## 7. Verification and preservation

Five new check groups pass on two complete final runs with byte-identical reports. They cover the exact source-frame dictionary, fixed-gain coefficient reconciliation, the new number-marking Duhamel bound, independently integrated hyperbolic-frame dynamics, Gaussian geometric-state overlaps, threshold comparisons, and a passive-measurement control. A new premature finite-amplitude convergence assertion failed on the first run; the original source and failed report remain under `development/` and `evidence/first.*`. The alpha=1000 threshold differs from its limiting lambda by 0.001488..., not less than 0.001. That case remains in the report as false for the stated convergence indicator; alpha=10000 was added and meets the unchanged indicator. This is not a change to any theorem or numerical solver tolerance.

The unchanged five-group pilot passed again and matched its canonical `first.json` byte-for-byte. Its original repeat-report discrepancy remains preserved; nothing was overwritten to improve report identity. All thirteen incoming files and their manifest are unchanged.

The new exact-frame evolution retains 4,608 amplitudes. One physical-frame counting diagnostic uses 18,432 matrix amplitudes after applying a truncated squeeze; this is a finite-cutoff diagnostic, not a large-N theorem. An 81-dimensional two-mode check verifies passive counting invariance. No protected project's checker was imported or rerun. `RUN_RECORD.json`, source-access notes and `evidence/REPORT_COMPARISONS.json` distinguish proofs, numerical assertions, report identity and source-reading boundaries.
