# Model and claims

## Fixed physical task

One lossless resonant pump, signal, and idler obey
$H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab)$. The initial pump is
$|\alpha\rangle$ with real $\alpha>0$ and both outputs start in vacuum.
$N=\alpha^2$, $\tau=gt$, and $r=\alpha\tau$.

The theorem takes $\alpha\to\infty$ with
$r=\tfrac12\ln(1+8\alpha\lambda)$ at fixed finite $\lambda$. Uniform bounds
hold on every fixed compact interval of $\lambda$. Fixed gain, physical time,
or depletion would specify different limits. The Hamiltonian is an effective
closed three-mode model, not a certified multimode or lossy implementation.

## Main state theorem

After removing the pump displacement and nominal output squeezing, the exact
state is norm-close to

$$|\chi_\lambda\rangle=
\exp[\lambda(d-d^\dagger)R]|0,0,0\rangle,\qquad
R=1+n_a+n_b+a^\dagger b^\dagger+ab.$$

The explicit error is $O_\Lambda(\ln\alpha/\alpha)$, uniform for
$\lambda\in[0,\Lambda]$. A second, physical-frame approximation marks pair
number $k$ with pump amplitude $\alpha-k/(2\alpha)$. Its reduced output is

$$\sigma_{ab}=\sum_{k,l\ge0}s_ks_l e^{-(k-l)^2/(8N)}
|k,k\rangle\langle l,l|,\qquad
s_k=\operatorname{sech}r\,\tanh^k r.$$

These are approximations to the specified state, not channel estimates for
arbitrary inputs or replacement dynamics for reuse of the correlated pump.

## Consequences and the necessary distinctions

The full pair-count distribution converges to the nominal geometric law in
total variation. Each individual mode approaches its thermal marginal in
trace distance. A separate energy bound, not norm convergence alone, proves
$\langle n_a\rangle\sim2\lambda\sqrt N$ and vanishing converted fraction.

The pump and joint-output purities approach $\mathcal P(\lambda)<1$; the
fidelity with the nominal pure TMSV approaches
$\mathcal P(\lambda/\sqrt2)<1$. Globally pure evolution makes pump impurity
an entanglement diagnostic across pump versus both outputs.

The standardized squeezed quadrature has a non-Gaussian limiting probability
law and supplies a positive trace-distance lower bound from every individual
Gaussian state. The output nonetheless approaches the convex Gaussian hull.
Neither nonclassical pump marginal, Wigner negativity, Gaussian-hull
separation, nor signal–idler entanglement strength follows from this claim.

A fixed purity loss has first-crossing time
$gt_\epsilon=[\ln\alpha+\ln(8\lambda_\epsilon)+o(1)]/(2\alpha)$.
The comparison to a published finite-degree polynomial concerns its
nonuniform asymptotic extrapolation, not its coefficients or finite-range
numerical usefulness.

## Measurement scope

Every POVM commuting with total output photon number has asymptotically the
nominal statistics. Passive optics with vacuum ancillas and photon counting
is covered; an external phase reference or retained correlated pump changes
the task. The distinguishing homodyne record needs phase-referenced readout
on a physical scale $N^{-1/4}$. Fixed positive additive resolution erases
this particular distinction. No experimental operating window is inferred.

The proofs and explicit constants are in [the theorem](THEOREM.md), with
[attribution](SOURCES.md) and [contribution assessment](REVIEW.md) separate.

## Review and finite-parameter guarantees

The [analytical review](PROOF_REVIEW.md) supplies a continuous-coordinate
check of the remainder norms, a domain justification, and exact-arithmetic
intervals for the first one-percent purity crossing. For each fixed loss
$0<\delta<1$, it sharpens the onset-time remainder to
$O_\delta(\log\alpha/\alpha^2)$ without assuming global monotonicity of the
exact purity. This is a corollary of the existing state estimate.

The [additional source comparison](SOURCE_REVIEW.md) identifies the exact
phase-averaged squeezed-state family in Vintskevich, Grigoriev and Filippov
(2019). Its initial mixed-pump phase distribution is not the pure coherent
preparation here, and its stated approximation domain does not certify this
crossover. The candidate contribution is the controlled dynamical limit, not
invention of that reduced-state family. See the [compact account](AUTHOR_ACCOUNT.md).
