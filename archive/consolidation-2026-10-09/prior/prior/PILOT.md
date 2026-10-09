# A pump can be nearly undepleted and finitely entangled

**Fresh Merlin–Arthur pilot, 9 October 2026.** This is an independent problem after the departure from oscillator-gate robustness cost. No scientific repository was read, created, or modified. No previous proof or scientific checker was imported. The calculation below is new author-side work in a standard model; attribution and significance are assessed separately.

## 1. Physical question and fixed model

Does negligible fractional pump depletion justify replacing a pump by a deterministic classical amplitude when predicting the quantum output of down-conversion?

Use the established resonant, lossless, nondegenerate trilinear Hamiltonian

\[
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\qquad g>0,
\]

with initial state \(|\alpha\rangle_c|0,0\rangle_{ab}\), real \(\alpha>0\), mean initial pump population \(N=\alpha^2\), dimensionless time \(\tau=gt\), and nominal gain \(r=\alpha\tau\). The conserved quantities are \(n_c+n_a\) and \(n_c+n_b\). The total state remains pure. Pump mixedness therefore measures entanglement across **pump versus signal-plus-idler**, not entanglement between signal and idler separately.

This is exactly the model and initial-state convention of Chinni–Quesada [CQ24], Eqs. (1)–(4), not a new Hamiltonian. No technical pump noise, unobserved loss channel, feedback, or postselection is introduced. The external-amplitude approximation is \(|\alpha\rangle\otimes S(r)|00\rangle\), where \(S(r)=\exp[r(a^\dagger b^\dagger-ab)]\).

The significance-bearing premise is tested inside the energy-conserving dynamics: a statement about small fractional energy transfer is not silently replaced by a statement about small state-vector error. The theoretical result does not borrow a claim of experimental accessibility from an unverified device.

## 2. Controlled crossover theorem

For fixed \(\lambda\ge0\), choose

\[
r_\alpha(\lambda)=\tfrac12\ln(1+8\alpha\lambda),\qquad
\tau_\alpha(\lambda)=r_\alpha(\lambda)/\alpha.
\tag{1}
\]

Displace the pump by its initial amplitude and remove the nominal signal squeezing. Write

\[
|\Psi_\alpha(r)\rangle=D_c(\alpha)S(r)|\psi_\alpha(r)\rangle.
\]

In the displaced frame call the pump annihilator \(d\). Put

\[
R=1+n_a+n_b+a^\dagger b^\dagger+ab.
\]

Then, uniformly for \(\lambda\) in any fixed compact interval,

\[
\boxed{|\psi_\alpha(r_\alpha(\lambda))\rangle
\longrightarrow |\chi_\lambda\rangle
=\exp[\lambda(d-d^\dagger)R]|0,0,0\rangle}
\tag{2}
\]

in Hilbert-space norm, with an explicit \(O_\Lambda(\ln\alpha/\alpha)\) error bound below. The frame transformation is a method of analysis, not an extra physical unsqueezing operation supplied to the apparatus. Gaussian interaction frames are an established tool [GIF22, V26].

### 2.1 Exact frame generator

Let \(K_+=a^\dagger b^\dagger\), \(K_-=ab\), \(Q=1+n_a+n_b\), \(A=K_+-K_-\), \(L=K_++K_--Q\), and \(p=d-d^\dagger\), \(T=d+d^\dagger\). The exact anti-Hermitian generator for the state in the frame is

\[
G_\alpha(u)=\frac{e^{2u}}{4\alpha}pR
+\frac{e^{-2u}}{4\alpha}pL+\frac1{2\alpha}TA.
\tag{3}
\]

This follows by conjugating the displaced interaction with \(S(u)\): \(S^\dagger a S=a\cosh u+b^\dagger\sinh u\). No pump term has been dropped in (3).

The first term integrates exactly to \(V(u)=\exp[\ell(u)pR]\), with

\[
\ell(u)=(e^{2u}-1)/(8\alpha).
\]

The other two terms are the remainder. The relevant commutators are

\[
[R,A]=2R,\qquad [R,L]=4A,\qquad[p,T]=2.
\]

Consequently,

\[
V^\dagger pV=p,\quad V^\dagger TV=T-2\ell R,\quad
V^\dagger AV=A-2\ell pR,
\]
\[
V^\dagger LV=L-4\ell pA+4\ell^2p^2R.
\tag{4}
\]

### 2.2 Norm bound without assuming a convergent Dyson series

Direct action on the three-mode vacuum gives

\[
\|p(L-4\ell pA+4\ell^2p^2R)|0\rangle\|^2
=2+48\ell^2+480\ell^4,
\]
\[
\|(T-2\ell R)(A-2\ell pR)|0\rangle\|^2
=1+16\ell^2+384\ell^4.
\tag{5}
\]

Duhamel's identity, with the exact unitary on the left of the remainder and \(V(u)|0\rangle\) on the right, therefore yields

\[
\epsilon_\alpha(r):=\|\psi_\alpha(r)-V(r)|0\rangle\|
\le\int_0^r\!\left[
\frac{e^{-2u}}{4\alpha}\sqrt{2+48\ell(u)^2+480\ell(u)^4}
+\frac1{2\alpha}\sqrt{1+16\ell(u)^2+384\ell(u)^4}
\right]du.
\tag{6}
\]

At \(r=r_\alpha(\lambda)\), \(0\le\ell(u)\le\lambda\), so the elementary bound

\[
\epsilon_\alpha\le
\frac{\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}
+\frac{r_\alpha(\lambda)\sqrt{1+16\lambda^2+384\lambda^4}}{2\alpha}
\tag{7}
\]

proves (2). It is uniform on compact crossover intervals, including zero. The term \(e^{2r}/\alpha\) is retained nonperturbatively; a finite short-time Taylor expansion in \(\tau\) is not used.

**Domains.** The exact Hamiltonian is the self-adjoint direct sum of finite matrices in joint eigenspaces of \(n_c+n_a,n_c+n_b\). Displacement and squeezing are unitary changes of frame. The leading unitary is well-defined because its pump quadrature strongly commutes with the nonnegative signal operator \(R\). In suitable rotated quadrature coordinates, it multiplies a Gaussian wavefunction by a cubic phase; the resulting state is Schwartz for finite \(\lambda\). All polynomial actions in (4)–(6) have finite norms and justify the Duhamel calculation by domain approximation. No operator-norm bound on an unbounded cubic Hamiltonian is asserted.

## 3. The limiting pump state and its purity

Define commuting signal quadratures

\[
x_+=(x_a+x_b)/\sqrt2,\qquad p_-=(p_a-p_b)/\sqrt2,
\quad R=x_+^2+p_-^2.
\]

In vacuum both have independent centered Gaussian distributions of variance \(1/2\); hence \(R\) has density \(e^{-u}\) on \(u\ge0\). Conditional on \(R=u\), (2) displaces the pump by \(-\lambda u\). After tracing out signal and idler,

\[
\boxed{\rho_{p,\infty}(\lambda)
=\int_0^\infty e^{-u}|-\lambda u\rangle\langle-\lambda u|du.}
\tag{8}
\]

Here the initial displacement \(\alpha\) has been removed. The physical pump is obtained by restoring it. Equation (2) implies trace-norm convergence to (8) for this displaced pump; its purity is invariant under the displacement and signal squeezing.

The coherent-state overlap gives

\[
\begin{aligned}
\mathcal P(\lambda)
&=\iint_0^\infty e^{-u-v-\lambda^2(u-v)^2}du\,dv\\
&=\int_0^\infty e^{-z-\lambda^2z^2}dz\\
&=\frac{\sqrt\pi}{2\lambda}
 e^{1/(4\lambda^2)}\operatorname{erfc}(1/(2\lambda)),
\end{aligned}\tag{9}
\]

with \(\mathcal P(0)=1\). Thus \(\mathcal P_\alpha(\lambda)\to\mathcal P(\lambda)<1\) for any fixed positive \(\lambda\). The conservative error is

\[
|\mathcal P_\alpha-\mathcal P|\le4\epsilon_\alpha.
\tag{10}
\]

At \(\lambda=1/2\), \(\mathcal P=0.757872156141312\ldots\); at \(\lambda=1\), it is \(0.545641360765047\ldots\). These are finite pump-versus-rest entanglements as the pump amplitude diverges, not a perturbatively infinitesimal purity loss.

The limiting pump marginal itself has a positive coherent-state mixture. It is not a nonclassicality witness for the isolated pump. Its non-Gaussian quadrature characteristic function is, for the displaced \(X=(d+d^\dagger)/\sqrt2\),

\[
\langle e^{itX}\rangle_\infty
=\frac{e^{-t^2/4}}{1+i\sqrt2\lambda t}.
\tag{11}
\]

This is a bounded-observable statement supported directly by trace-norm convergence. No unbounded quadrature-moment convergence is inferred merely from norm convergence.

### The signal state is not just a squeezed vacuum with the wrong gain

For comparison with the nominal two-mode squeezed vacuum, the squared state fidelity converges to

\[
F_{\rm TMSV}\to\mathcal P(\lambda/\sqrt2).
\tag{12}
\]

At \(\lambda=1/2\), this equals \(0.842738458576109\ldots\). More generally, signal-plus-idler has the same purity as the pump because the total state is pure. Its fidelity with **any** pure state is at most \(\sqrt{\mathcal P_\alpha}\). A deterministic classical pump, even with a revised time-dependent mean amplitude, still evolves signal vacuum into a pure Gaussian state in this model. It cannot remove this mixedness by gain recalibration.

This is not a no-go theorem for stochastic classical descriptions of selected reduced observables. Tracing the leading unitary over the pump momentum also represents the signal marginal as a classical mixture of Gaussian unitaries. That representation does not give a separable description of the full pump–signal quantum state.

## 4. Fractional depletion tends to zero independently of state convergence

Because photon number is unbounded, norm convergence alone does not justify a statement about mean depletion. A separate bound is available.

In an initial pump-number sector \(m\), write amplitudes in \(|m-k,k,k\rangle\) and let \(\bar k_m(\tau)\) be their mean pair number. The exact off-diagonal coefficients are \((k+1)\sqrt{m-k}\). Cauchy–Schwarz gives

\[
\partial_\tau\bar k_m\le2\sqrt m\sqrt{\bar k_m(\bar k_m+1)},
\quad \bar k_m(0)=0,
\]

and hence \(\bar k_m\le\sinh^2(\sqrt m\tau)\). The inequality follows by integrating after replacing the square-root denominator at zero by a positive regularization, then taking its limit. The upper comparison remains valid even if the true derivative subsequently becomes negative.

For the coherent initial pump, number expectations are Poisson-weighted sector averages. Using \(\sqrt m\le(m+\alpha^2)/(2\alpha)\) and the Poisson generating function yields

\[
\boxed{
0\le \frac{N-\langle n_c\rangle}{N}
=\frac{\langle n_a\rangle}{\alpha^2}
\le \frac{1}{4\alpha^2}
\exp\!\left[r+\alpha^2\left(e^{r/\alpha^2}-1\right)\right].}
\tag{13}
\]

At (1), the right side is

\[
\frac{1+8\alpha\lambda}{4\alpha^2}
\exp\!\left[O\!\left(\frac{\ln^2\alpha}{\alpha^2}\right)\right]
\sim\frac{2\lambda}{\alpha}.
\tag{14}
\]

Thus finite pump entanglement occurs with a vanishing **fraction** of pump photons converted. Absolute conversion can still be large; this is not zero-energy entanglement creation.

For a concrete bound within this ideal model, at \(N=10^{12}\) and \(\lambda=1/2\), (7), (10), and (13) imply purity within \(9\times10^{-5}\) of 0.75787216 and fractional depletion below \(1.000001\times10^{-6}\). This is an evaluated analytical bound, not a trillion-photon simulation or an operating point of a specified optical device.

## 5. Fixed-purity-loss onset

Let \(0<\varepsilon<1\), and let \(\tau_\varepsilon(\alpha)\) be the first time the pump purity reaches \(1-\varepsilon\). Equation (9) is strictly decreasing from one to zero. Define its unique positive solution \(\lambda_\varepsilon\) by

\[
\mathcal P(\lambda_\varepsilon)=1-\varepsilon.
\]

Uniform convergence on compact \(\lambda\)-intervals brackets the first crossing: below any fixed \(\lambda_-<\lambda_\varepsilon\) the exact purity remains above the threshold for sufficiently large \(\alpha\), and above any \(\lambda_+>\lambda_\varepsilon\) it has already crossed. Hence

\[
\boxed{
\tau_\varepsilon(\alpha)=
\frac{\ln\alpha+\ln(8\lambda_\varepsilon)+o(1)}{2\alpha}.
}
\tag{15}
\]

Equivalently, \(gt_\varepsilon\sim\ln N/(4\sqrt N)\). For a one-percent purity loss, \(\lambda_{.01}=0.0717744482431\ldots\) and \(\ln(8\lambda_{.01})=-0.554785198638\ldots\).

The quantum-state crossover is reached at gain \(r=\tfrac14\ln N+O(1)\), before the nominal mean pair population reaches order \(N\). This does not claim that logarithmic gain scales or quantum-pump limits to squeezing are newly discovered; see the source comparison.

## 6. Matched sources, overlap, and limits

**[CQ24] Chinni and Quesada, Physical Review A 110, 013712 (2024), arXiv:2312.09239.** The exact same Hamiltonian, coherent initial pump, conserved sectors and pump-purity objective appear in Eqs. (1)–(7) and Sec. IV. The source already establishes pump entanglement, its non-Gaussian character, and the inequivalence of pump depletion and entanglement. Its Appendix D, Eqs. (119)–(120), estimates a fixed purity-loss threshold by an eighth-order time polynomial, giving \(\alpha^{-3/4}\), alongside a finite-range numerical exponent about -0.769. Our controlled strong-amplitude first-crossing law (15) has a different asymptotic form. This does not invalidate those finite-range numerical data or their short-time expansion: the issue is extrapolating a fixed-degree time expansion when \(r\) grows logarithmically with amplitude. The direct threshold convention is \(1-\mathcal P=\varepsilon\); the source's finite-cutoff normalization tends to that convention at large amplitude. Readable primary HTML v2 and the current primary PDF were compared. Requested PDF screenshots failed, so no plotted data were digitized or used.

**[HS25] Horoshko and Shchesnovich, Physical Review A 112, 033706 (2025), arXiv:2503.18828v2.** Their degenerate, two-mode model is not the same nondegenerate three-mode problem. The introduction credits the long-established parametric-approximation limits to Hillery and Zubairy; Sec. III explicitly discusses logarithmic squeezing scales and the limitations of unbounded-operator perturbation expansions. Sec. IV provides an energy-conserving approximate treatment with observable-specific validity criteria. These precedents rule out claiming that undepleted-energy and quantum-state validity are newly distinguished. No result for their degenerate model is silently replaced by our nondegenerate coefficient.

**[GIF22] Yanagimoto et al., Optica 9, 379 (2022), arXiv:2111.13799.** Sec. II, Eqs. (5)–(12), explicitly displaces the pump and removes Gaussian squeezing to expose residual cubic quantum dynamics. The paper studies pump–signal entanglement and non-Gaussianity, including multimode waveguides. Our frame choice and the existence of cubic residual dynamics are inherited methods. The candidate addition is the growing-gain asymptotic limit, its norm remainder, and its explicit purity law—not the frame method.

**[V26] Vendromin, Fontaine and Sipe, Physical Review A 113, 023707 (2026), arXiv:2510.06498v1.** The inspected primary HTML develops Gaussian/non-Gaussian separation for lossy microrings and discusses revealing non-Gaussian features by undoing Gaussian dynamics. It provides an important physical-context predecessor, not evidence that our closed three-mode limit is realized without loss in those devices. No figure-specific performance value is used here.

**[HZ84] Hillery and Zubairy, Physical Review A 29, 1275 (1984).** The publisher abstract confirms a fully quantized path-integral treatment and conditions for the parametric approximation. The complete old article was not read in this pilot; [HS25] reproduces relevant historical scale information. Absence of our expression from its abstract is not a priority conclusion.

**[KD93] Kinsler, Fernée and Drummond, Physical Review A 48, 3310 (1993)** and **[CB88] Crouch and Braunstein, Physical Review A 38, 4696 (1988)** already identify pump-quantum-noise restrictions on squeezing, including the coherent-pump \(N^{-1/2}\) variance scale. Only the primary publisher abstracts were inspected here. The squeezing limit is not our novelty claim, nor does it by itself give the pump's full purity crossover.

### Physical consequence-bearing assumptions

The theorem concerns a resonant, three-mode, closed interaction and coherent initial pump. It is not a generic statement about every broadband source, propagation loss, drive noise, or mixed pump. Increasing \(N\) at fixed microscopic \(g\) indefinitely can leave a rotating-wave or mode-isolation regime. Holding \(g\sqrt N\) fixed instead makes the crossover physical time grow logarithmically; fixed loss can then matter. No device operating window or gain-independent loss immunity is claimed. A pump-purity measurement certifies pump-versus-rest entanglement only with the stipulated globally pure, isolated preparation.

## 7. Decision

**One bounded GO for the controlled quantum-state crossover and its matched asymptotic comparison. No repository and no strong PRL forecast.** The promising remainder is a complete non-Gaussian limiting state with a uniform norm bound, yielding a fixed-purity-loss onset law and finite entanglement at rigorously vanishing fractional depletion. It addresses a stronger question than an error in mean photon number.

The strongest objection is that the leading residual cubic dynamics and logarithmic gain scale have substantial predecessors. An explicit purity function may be a concise completion of that literature, rather than a sufficiently consequential new result. A source-level reconstruction of the corresponding strong-pump limit in the older path-integral and modern Gaussian-frame/isoenergetic treatments is the next discriminating task. Adding loss, more modes, or a pump-state optimization is not an automatic prerequisite and should not be used to rescue the candidate.

## 8. Reproduction

Run `python check_pilot.py --output /absolute/new/report.json` with NumPy, SciPy and SymPy installed. Five groups cover exact commutators and vacuum remainder norms, the purity integral and bounded characteristic function, independently assembled conserved-sector dynamics, exact-frame cutoff refinement, and threshold/depletion controls.

The exact-frame equation retains all three terms of (3); its finite truncation is a numerical diagnostic, not a replacement for (6). The largest formal-check state representation has 8,064 pump-fluctuation/pair amplitudes; independent number-sector checks retain up to 72 initial pump photons with all allowed pairs in each sector. Those small sector checks are independent of the frame construction. Exploratory cutoff checks additionally examined up to 18,432 amplitudes; those exploratory runs are not counted as formal proof checks. Numerical purity refinement is much tighter than depletion-moment refinement; the public example uses the analytical depletion upper bound rather than presenting a cutoff expectation as certified.

No source tolerance was relaxed and no formal check failed. No old scientific checker was rerun. The proof is author-side and has not undergone external independent review. `evidence/first.json` and `evidence/repeat.json` preserve the executed results.


### Repeat-report identity

Both complete five-group scientific runs passed. Their JSON reports are not
byte-identical: one state-distance diagnostic differs by
1.1796119636642288e-16. All other fields agree. The full comparison is in
`evidence/REPORT_COMPARISON.json`; both original reports and logs are retained.
An initial packaging assertion expecting byte identity failed and was not used
to relabel the reports. No scientific formula, test assertion, or tolerance was
changed. The origin of that last-bit difference was not separately established.
