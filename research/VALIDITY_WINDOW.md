# Controlled validity window: accurate counts and asymptotically orthogonal states

This is a direct consequence of the **finite-parameter inequalities** in the
[crossover theorem](THEOREM.md), not a substitution of an unbounded parameter
into its compact-parameter convergence statement. The preparation, closed
resonant nondegenerate Hamiltonian, and definition of gain are unchanged.

## 1. The finite bounds and an explicit sufficient window

Let $`\alpha\to\infty`$, $`N=\alpha^2`$, and permit $`\lambda=\lambda_\alpha\ge0`$
to depend on brightness. Set

```math
r=\tfrac12\log(1+8\alpha\lambda),\qquad
B_\alpha=\frac{(1+\lambda^2)(1+r)}{\alpha}.
```

The condition used throughout this note is

**Equation (W1).**

```math
\boxed{B_\alpha\longrightarrow0.}
```

It is sufficient, not a proposed maximal validity domain. The exact residual
state and the leading cubic-unitary state satisfy, at every finite
$`\alpha>0,\lambda\ge0`$,

**Equation (W2).**

```math
\|\psi_\alpha-\chi_\lambda\|\le\epsilon_\alpha(\lambda)
=\frac{\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}
 +\frac{r\sqrt{1+16\lambda^2+384\lambda^4}}{2\alpha}.
```

The physical-frame number-marking approximation has error at most
$`\eta_\alpha=\epsilon_\alpha+d_\alpha`$, where

```math
d_\alpha=\frac{\sqrt2+e^{-2r}\sqrt{2+48\lambda^2+480\lambda^4}}{8\alpha}.
```

These are the original pointwise estimates. Their Duhamel derivation only
uses finite polynomial norms on the leading state at each finite parameter;
it does not require a parameter-independent oscillator truncation. In
particular,

```math
\sqrt{2+48\lambda^2+480\lambda^4}\le22(1+\lambda^2),\qquad
\sqrt{1+16\lambda^2+384\lambda^4}\le20(1+\lambda^2)
```

give the convenient, nonsharp domination

**Equation (W3).**

```math
\boxed{\epsilon_\alpha\le\eta_\alpha\le10B_\alpha.}
```

Consequently all the trace-distance and bounded-measurement consequences
survive along (W1). The sharper bounds (W2), rather than (W3), should be used
for finite certificates.

## 2. Three accuracy regimes for the same initial state

Use squared target-state fidelity
$`F_\alpha=\langle\mathrm{TMSV}_r|\rho_{ab}|\mathrm{TMSV}_r\rangle`$ and
$`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. Write

```math
\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}\,dz.
```

The residual-frame vacuum probability is exactly
$`\mathcal P(\lambda/\sqrt2)`$. To see this, condition on the normalized pump
momentum $`Z`$, a standard normal. The vacuum amplitude of
$`e^{i\lambda ZR}`$ is $`(1-i\lambda Z)^{-1}`$ because $`R`$ has the unit
exponential vacuum spectral law. Averaging its squared modulus gives
$`\mathcal P(\lambda/\sqrt2)`$. A projector is bounded, so (W2) gives the
finite inequality

**Equation (W4).**

```math
\boxed{|F_\alpha-\mathcal P(\lambda/\sqrt2)|\le\epsilon_\alpha.}
```

Here norm distance bounds pure-state trace distance, which contracts on
tracing out the pump. The usual projector probability difference is at most
that trace distance; no unbounded-moment estimate enters (W4).

Within (W1),

**Equation (W5).**

```math
\boxed{D(\rho_{ab},|\mathrm{TMSV}_r\rangle\langle\mathrm{TMSV}_r|)\to0
\quad\Longleftrightarrow\quad\lambda_\alpha\to0.}
```

Indeed $`1-F_\alpha\le D\le\sqrt{1-F_\alpha}`$, while $`\mathcal P`$ is
strictly decreasing from one. If $`\lambda`$ does not tend to zero, a
subsequence is bounded below by a positive constant, and (W4) bounds its
fidelity away from one. This also covers nonconvergent sequences.

The nominal mean pair number obeys the exact identity

**Equation (W6).**

```math
\bar n_{\mathrm{cl}}=\sinh^2r
=2\alpha\lambda-\frac14+\frac1{4(1+8\alpha\lambda)}.
```

Thus (W5) is equivalently $`\bar n_{\mathrm{cl}}=o(\sqrt N)`$ in this
controlled window, for the specified coherent-pump and vacuum-output preparation.

| Sequence inside (W1) | Counts and individual marginals | Joint-state conclusion |
|---|---|---|
| $`\lambda_\alpha\to0`$ | Accurate | Nominal pure TMSV is accurate |
| $`\lambda_\alpha\to\lambda_0>0`$ | Accurate | Fixed purity and target-fidelity crossover |
| $`\lambda_\alpha\to\infty`$ | Accurate | Distance from every pure state tends to one |

The last row is established below. All three rows follow from the same
finite error bounds.

## 3. Count accuracy and the separate energy estimate

The physical-frame approximation is the established phase-averaged family

**Equation (W7).**

```math
\sigma_{ab}=\sum_{k,l\ge0}s_ks_l
 e^{-(k-l)^2/(8N)}|k,k\rangle\langle l,l|,
\qquad s_k=\mathrm{sech}r\,\tanh^kr,
\qquad D(\rho_{ab},\sigma_{ab})\le\eta_\alpha.
```

Its number distribution is exactly the nominal geometric law. Therefore
the complete pair-count distribution converges to the nominal prediction
in total variation under (W1), and each one-mode marginal converges to its
nominal thermal state in trace distance. Every POVM commuting with total
output photon number gives the same probabilities on $`\sigma_{ab}`$ and the
nominal pure TMSV, even when that POVM depends on $`\alpha`$.

The independent energy bound remains

**Equation (W8).**

```math
\frac{\langle n_a\rangle}{\alpha^2}
\le\frac{\exp[r+\alpha^2(e^{r/\alpha^2}-1)]}{4\alpha^2}.
```

Condition (W1) implies $`\lambda=o(\sqrt\alpha)`$ and $`r=O(\log\alpha)`$.
The right side of (W8) is

```math
\left(\frac{2\lambda}{\alpha}+\frac1{4\alpha^2}\right)
\exp\{\alpha^2(e^{r/\alpha^2}-1)-r\}=o(1).
```

Hence fractional pump depletion vanishes. When also
$`\alpha\lambda\to\infty`$,

**Equation (W9).**

```math
\boxed{\langle n_a\rangle\sim2\alpha\lambda,\qquad
\frac{N-\langle n_c\rangle}{N}\sim\frac{2\lambda}{\alpha}.}
```

For the lower bound, (W7) and (W6) give
$`k/(2\alpha\lambda)\Rightarrow\mathrm{Exp}(1)`$; bounded truncations imply
$`\liminf\langle k\rangle/(2\alpha\lambda)\ge1`$. Dividing (W8) by
$`2\lambda/\alpha`$ gives the matching upper bound, since
$`r^2/\alpha^2\to0`$. This is not an inference of an unbounded mean from
total variation alone. The absolute number of converted photons diverges
in (W9); only its fraction vanishes.

## 4. Accurate counts with distance one from every pure state

The exact pump and output purities coincide because the full state is pure.
The existing finite bound is

```math
|\mathrm{Tr}\rho_{ab}^2-\mathcal P(\lambda)|\le4\epsilon_\alpha.
```

For every pure state $`|\phi\rangle`$, its overlap with $`\rho_{ab}`$ is at
most $`\|\rho_{ab}\|_\infty\le\sqrt{\mathrm{Tr}\rho_{ab}^2}`$.
Projector discrimination therefore gives

**Equation (W10).**

```math
\boxed{\inf_{|\phi\rangle}
D(\rho_{ab},|\phi\rangle\langle\phi|)
\ge\left[1-\sqrt{\min\{1,\mathcal P(\lambda)+4\epsilon_\alpha\}}\right]_+.}
```

Because $`\mathcal P(\lambda)\sim\sqrt\pi/(2\lambda)`$, (W1) with
$`\lambda\to\infty`$ yields

**Equation (W11).**

```math
\boxed{\inf_{|\phi\rangle}
D(\rho_{ab},|\phi\rangle\langle\phi|)\longrightarrow1.}
```

The minimizing pure state may depend on $`N`$. This is much stronger than
failure of one nominal gain calibration. It is still not a distance-one
claim about every mixed Gaussian state.

### A single Gaussian also remains separated

The existing bounded characteristic-function argument applies at any
frequency, including $`\xi_\alpha=1/\lambda_\alpha`$. Its non-Gaussianity
contrast then simplifies to

```math
W_\lambda(1/\lambda)=\frac29e^{-1/\lambda^2}.
```

Thus for the set $`\mathcal G`$ of individual Gaussian states,

**Equation (W12).**

```math
\inf_{\gamma\in\mathcal G}D(\rho_{ab},\gamma)
\ge\left[\frac1{45}e^{-1/\lambda^2}-\epsilon_\alpha\right]_+,
\qquad
\liminf\inf_{\gamma\in\mathcal G}D(\rho_{ab},\gamma)\ge\frac1{45}.
```

The limit in (W12) assumes (W1) and $`\lambda\to\infty`$. The output still
approaches the **convex hull** of Gaussian states through (W7). These
statements are compatible: a mixture of Gaussian states need not itself
be Gaussian.

For completeness, the rescaled quadrature $`e^rX_-/\lambda`$ has limiting
characteristic function $`(1+2\xi^2)^{-1/2}`$, the law of $`\sqrt2`$ times a
product of two independent standard normals. The physical readout scale is
$`\lambda e^{-r}\sim\sqrt{\lambda/(8\alpha)}`$, which still shrinks here.
A phase reference and increasingly fine physical resolution remain
substantive requirements.

## 5. An explicit sequence and entanglement entropy

Take $`\lambda_\alpha=\alpha^{1/4}=N^{1/8}`$. Then

```math
r=\frac5{16}\log N+\frac12\log8+o(1),\qquad
\epsilon_\alpha,\eta_\alpha=O\!\left(\frac{\log N}{N^{1/4}}\right).
```

Equations (W7)–(W11) give correct complete pair counts together with

**Equation (W13).**

```math
\langle n_a\rangle\sim2N^{5/8},\qquad
\frac{N-\langle n_c\rangle}{N}\sim2N^{-3/8},\qquad
\mathrm{Tr}\rho_{ab}^2\sim\frac{\sqrt\pi}{2}N^{-1/8}.
```

The purity equivalence, rather than merely convergence to zero, follows
because the error in (W2) is $`o(N^{-1/8})`$. The pump/output second-Renyi
entanglement entropy consequently is

**Equation (W14).**

```math
S_2=-\log\mathrm{Tr}\rho_{ab}^2
=\frac18\log N-\log(\sqrt\pi/2)+o(1).
```

This is an entropy across **pump versus both outputs**, not a formula for
signal/idler entanglement or the von Neumann entropy. The physical quadrature
scale for (W12) is $`N^{-3/16}/\sqrt8`$. These exponents describe the specified
sequence. Other slowly growing sequences satisfying (W1) are also admissible.

## 6. Reproduction

The [checker](../scripts/check_manuscript_basis.py) verifies the exact algebra,
finite comparison-state identities, inequality constants, and evaluations of
the growing-window bounds. See [reproducibility](../REPRODUCIBILITY.md) for
the commands and [sources](SOURCES.md) for related validity criteria.
