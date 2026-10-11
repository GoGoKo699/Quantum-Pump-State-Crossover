# Controlled validity window: accurate counts and asymptotically orthogonal states

This is a direct consequence of the **finite-parameter inequalities** in the
[crossover theorem](THEOREM.md), not a substitution of an unbounded parameter
into its compact-parameter convergence statement. The preparation, closed
resonant nondegenerate Hamiltonian, and definition of gain are unchanged.
The original theorem and its evidence are preserved.

## 1. The finite bounds and an explicit sufficient window

Let $\alpha\to\infty$, $N=\alpha^2$, and permit $\lambda=\lambda_\alpha\ge0$
to depend on brightness. Set

$$
r=\tfrac12\log(1+8\alpha\lambda),\qquad
B_\alpha=\frac{(1+\lambda^2)(1+r)}{\alpha}.
$$

The condition used throughout this note is

$$
\boxed{B_\alpha\longrightarrow0.} \tag{W1}
$$

It is sufficient, not a proposed maximal validity domain. The exact residual
state and the leading cubic-unitary state satisfy, at every finite
$\alpha>0,\lambda\ge0$,

$$
\|\psi_\alpha-\chi_\lambda\|\le\epsilon_\alpha(\lambda)
=\frac{\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}
 +\frac{r\sqrt{1+16\lambda^2+384\lambda^4}}{2\alpha}. \tag{W2}
$$

The physical-frame number-marking approximation has error at most
$\eta_\alpha=\epsilon_\alpha+d_\alpha$, where

$$
d_\alpha=\frac{\sqrt2+e^{-2r}\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}.
$$

These are the original pointwise estimates. Their Duhamel derivation only
uses finite polynomial norms on the leading state at each finite parameter;
it does not require a parameter-independent oscillator truncation. In
particular,

$$
\sqrt{2+48\lambda^2+480\lambda^4}\le22(1+\lambda^2),\qquad
\sqrt{1+16\lambda^2+384\lambda^4}\le20(1+\lambda^2)
$$

give the convenient, nonsharp domination

$$
\boxed{\epsilon_\alpha\le\eta_\alpha\le10B_\alpha.} \tag{W3}
$$

Consequently all the trace-distance and bounded-measurement consequences
survive along (W1). The sharper bounds (W2), rather than (W3), should be used
for finite certificates. Neither bound is a numerical propagation result.

## 2. Three accuracy regimes for the same initial state

Use squared target-state fidelity
$F_\alpha=\langle\mathrm{TMSV}_r|\rho_{ab}|\mathrm{TMSV}_r\rangle$ and
$D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1$. Write

$$
\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}\,dz.
$$

The residual-frame vacuum probability is exactly
$\mathcal P(\lambda/\sqrt2)$. To see this, condition on the normalized pump
momentum $Z$, a standard normal. The vacuum amplitude of
$e^{i\lambda ZR}$ is $(1-i\lambda Z)^{-1}$ because $R$ has the unit
exponential vacuum spectral law. Averaging its squared modulus gives
$\mathcal P(\lambda/\sqrt2)$. A projector is bounded, so (W2) gives the
finite inequality

$$
\boxed{|F_\alpha-\mathcal P(\lambda/\sqrt2)|\le\epsilon_\alpha.} \tag{W4}
$$

Here norm distance bounds pure-state trace distance, which contracts on
tracing out the pump. The usual projector probability difference is at most
that trace distance; no unbounded-moment estimate enters (W4).

Within (W1),

$$
\boxed{D(\rho_{ab},|\mathrm{TMSV}_r\rangle\langle\mathrm{TMSV}_r|)\to0
\quad\Longleftrightarrow\quad\lambda_\alpha\to0.} \tag{W5}
$$

Indeed $1-F_\alpha\le D\le\sqrt{1-F_\alpha}$, while $\mathcal P$ is
strictly decreasing from one. If $\lambda$ does not tend to zero, a
subsequence is bounded below by a positive constant, and (W4) bounds its
fidelity away from one. This also covers nonconvergent sequences.

The nominal mean pair number obeys the exact identity

$$
\bar n_{\mathrm{cl}}=\sinh^2r
=2\alpha\lambda-\frac14+\frac1{4(1+8\alpha\lambda)}. \tag{W6}
$$

Thus (W5) is equivalently $\bar n_{\mathrm{cl}}=o(\sqrt N)$ in this
controlled window. This is an observable-specific state criterion, not a
criterion for all undepleted gains or all possible pump preparations.
Historical quantum-pump restrictions already identify square-root
photon-number/high-gain scales; their first appearance is not claimed here.

| Sequence inside (W1) | Counts and individual marginals | Joint-state conclusion |
|---|---|---|
| $\lambda_\alpha\to0$ | Accurate | Nominal pure TMSV is accurate |
| $\lambda_\alpha\to\lambda_0>0$ | Accurate | Fixed purity and target-fidelity crossover |
| $\lambda_\alpha\to\infty$ | Accurate | Distance from every pure state tends to one |

The last row is established below. The first two are not new mechanisms;
the table identifies their common finite-error justification.

## 3. Counts remain accurate; energy still needs its separate proof

The physical-frame approximation is the established phase-averaged family

$$
\sigma_{ab}=\sum_{k,l\ge0}s_ks_l
 e^{-(k-l)^2/(8N)}|k,k\rangle\langle l,l|,
\qquad s_k=\operatorname{sech}r\,\tanh^kr,
\qquad D(\rho_{ab},\sigma_{ab})\le\eta_\alpha. \tag{W7}
$$

Its number distribution is exactly the nominal geometric law. Therefore
the complete pair-count distribution converges to the nominal prediction
in total variation under (W1), and each one-mode marginal converges to its
nominal thermal state in trace distance. Every POVM commuting with total
output photon number gives the same probabilities on $\sigma_{ab}$ and the
nominal pure TMSV, even when that POVM depends on $\alpha$.

The independent energy bound remains

$$
\frac{\langle n_a\rangle}{\alpha^2}
\le\frac{\exp[r+\alpha^2(e^{r/\alpha^2}-1)]}{4\alpha^2}. \tag{W8}
$$

Condition (W1) implies $\lambda=o(\sqrt\alpha)$ and $r=O(\log\alpha)$.
The right side of (W8) is

$$
\left(\frac{2\lambda}{\alpha}+\frac1{4\alpha^2}\right)
\exp\{\alpha^2(e^{r/\alpha^2}-1)-r\}=o(1).
$$

Hence fractional pump depletion vanishes. When also
$\alpha\lambda\to\infty$,

$$
\boxed{\langle n_a\rangle\sim2\alpha\lambda,\qquad
\frac{N-\langle n_c\rangle}{N}\sim\frac{2\lambda}{\alpha}.} \tag{W9}
$$

For the lower bound, (W7) and (W6) give
$k/(2\alpha\lambda)\Rightarrow\mathrm{Exp}(1)$; bounded truncations imply
$\liminf\langle k\rangle/(2\alpha\lambda)\ge1$. Dividing (W8) by
$2\lambda/\alpha$ gives the matching upper bound, since
$r^2/\alpha^2\to0$. This is not an inference of an unbounded mean from
total variation alone. The absolute number of converted photons diverges
in (W9); only its fraction vanishes.

## 4. Accurate counts with distance one from every pure state

The exact pump and output purities coincide because the full state is pure.
The existing finite bound is

$$
|\operatorname{Tr}\rho_{ab}^2-\mathcal P(\lambda)|\le4\epsilon_\alpha.
$$

For every pure state $|\phi\rangle$, its overlap with $\rho_{ab}$ is at
most $\|\rho_{ab}\|_\infty\le\sqrt{\operatorname{Tr}\rho_{ab}^2}$.
Projector discrimination therefore gives

$$
\boxed{\inf_{|\phi\rangle}
D(\rho_{ab},|\phi\rangle\langle\phi|)
\ge\left[1-\sqrt{\min\{1,\mathcal P(\lambda)+4\epsilon_\alpha\}}\right]_+.} \tag{W10}
$$

Because $\mathcal P(\lambda)\sim\sqrt\pi/(2\lambda)$, (W1) with
$\lambda\to\infty$ yields

$$
\boxed{\inf_{|\phi\rangle}
D(\rho_{ab},|\phi\rangle\langle\phi|)\longrightarrow1.} \tag{W11}
$$

The minimizing pure state may depend on $N$. This is much stronger than
failure of one nominal gain calibration. It is still not a distance-one
claim about every mixed Gaussian state.

### A single Gaussian also remains separated

The existing bounded characteristic-function argument applies at any
frequency, including $\xi_\alpha=1/\lambda_\alpha$. Its non-Gaussianity
contrast then simplifies to

$$
W_\lambda(1/\lambda)=\frac29e^{-1/\lambda^2}.
$$

Thus for the set $\mathcal G$ of individual Gaussian states,

$$
\inf_{\gamma\in\mathcal G}D(\rho_{ab},\gamma)
\ge\left[\frac1{45}e^{-1/\lambda^2}-\epsilon_\alpha\right]_+,
\qquad
\liminf\inf_{\gamma\in\mathcal G}D(\rho_{ab},\gamma)\ge\frac1{45}. \tag{W12}
$$

The limit in (W12) assumes (W1) and $\lambda\to\infty$. The output still
approaches the **convex hull** of Gaussian states through (W7). These
statements are compatible: a mixture of Gaussian states need not itself
be Gaussian. No Wigner negativity or distance from the convex Gaussian
hull is asserted.

For completeness, the rescaled quadrature $e^rX_-/\lambda$ has limiting
characteristic function $(1+2\xi^2)^{-1/2}$, the law of $\sqrt2$ times a
product of two independent standard normals. The physical readout scale is
$\lambda e^{-r}\sim\sqrt{\lambda/(8\alpha)}$, which still shrinks here.
A phase reference and increasingly fine physical resolution remain
substantive requirements. The limiting contrast is not a fixed-resolution
device guarantee.

## 5. One explicit sequence, with no new physical resource

Take $\lambda_\alpha=\alpha^{1/4}=N^{1/8}$. Then

$$
r=\frac5{16}\log N+\frac12\log8+o(1),\qquad
\epsilon_\alpha,\eta_\alpha=O\!\left(\frac{\log N}{N^{1/4}}\right).
$$

Equations (W7)–(W11) give correct complete pair counts together with

$$
\langle n_a\rangle\sim2N^{5/8},\qquad
\frac{N-\langle n_c\rangle}{N}\sim2N^{-3/8},\qquad
\operatorname{Tr}\rho_{ab}^2\sim\frac{\sqrt\pi}{2}N^{-1/8}. \tag{W13}
$$

The purity equivalence, rather than merely convergence to zero, follows
because the error in (W2) is $o(N^{-1/8})$. The pump/output second-Renyi
entanglement entropy consequently is

$$
S_2=-\log\operatorname{Tr}\rho_{ab}^2
=\frac18\log N-\log(\sqrt\pi/2)+o(1). \tag{W14}
$$

This is an entropy across **pump versus both outputs**, not a formula for
signal/idler entanglement or the von Neumann entropy. The physical quadrature
scale for (W12) is $N^{-3/16}/\sqrt8$. These exponents describe the specified
sequence, not a universal device operating law. One can take other slowly
growing sequences satisfying (W1); this example is not an optimized bound.

## 6. What this adds to the manuscript

The compact-crossover state theorem remains the central derivation. This
corollary states the accuracy hierarchy using the same pointwise bounds:
correct photon counts can coexist not only with finite pure-state error,
but with asymptotic orthogonality to every pure state and growing pump/output
entanglement at vanishing fractional depletion. It also gives a necessary
and sufficient nominal-state criterion **inside an explicit controlled
window**. It does not solve the full depletion-time dynamics.

The older warnings about depletion, pump coherence, and phase-noise limits
must be credited; see [the manuscript source audit](MANUSCRIPT_SOURCE_AUDIT.md).
The [new checker](../scripts/check_manuscript_basis.py) checks exact algebra,
finite comparison-state identities, the original inequality constants, and
bound-only sequence examples. It does not simulate the enormous photon
numbers used to illustrate asymptotic certificates.
