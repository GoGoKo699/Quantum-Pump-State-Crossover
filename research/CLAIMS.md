# Model and claims

## Model and scales

The pump $`c`$, signal $`a`$, and idler $`b`$ are bosonic modes governed by the
closed, lossless, resonant Hamiltonian

```math
H=i\hbar g(ca^\dagger b^\dagger-c^\dagger ab),\qquad
|\Psi(0)\rangle=|\alpha\rangle_c|0,0\rangle_{ab},\qquad g>0,\quad\alpha>0.
```

Write $`n_j=j^\dagger j`$, $`N=\alpha^2`$, $`\tau=gt`$, and
$`r=\alpha\tau`$. The nominal classical-pump prediction is the pure
two-mode squeezed vacuum (TMSV)

```math
|\mathrm{TMSV}_r\rangle=\sum_{k\ge0}s_k|k,k\rangle,
\qquad s_k=\mathrm{sech}r\,\tanh^k r.
```

The crossover coordinate is $`\lambda=(e^{2r}-1)/(8\alpha)\ge0`$. The
fixed-crossover theorem takes $`\alpha\to\infty`$ at
$`r=r_\alpha(\lambda)=\tfrac12\log(1+8\alpha\lambda)`$, uniformly on each
fixed compact interval $`\lambda\in[0,\Lambda]`$. Fixed gain, fixed physical
time, and fixed depletion specify different limits.

## Controlled state approximation

Remove the pump displacement and nominal output squeezing, and let $`d`$
annihilate the displaced pump. The exact residual state is within
$`O_\Lambda(\log\alpha/\alpha)`$ in vector norm of

```math
|\chi_\lambda\rangle=e^{\lambda(d-d^\dagger)R}|0,0,0\rangle,
\qquad R=1+n_a+n_b+a^\dagger b^\dagger+ab.
```

In the physical frame, the controlled approximation marks generated pair
number $`k`$ with pump amplitude $`\alpha-k/(2\alpha)`$. Tracing the pump gives

```math
\sigma_{ab}=\sum_{k,l\ge0}s_ks_l e^{-(k-l)^2/(8N)}
|k,k\rangle\langle l,l|.
```

The exact output $`\rho_{ab}`$ is within
$`O_\Lambda(\log\alpha/\alpha)`$ of this approximation in trace distance,
$`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. The
[state proof](THEOREM.md) gives explicit finite bounds for both comparisons.
The comparison state $`\sigma_{ab}`$ is a Gaussian phase average of the TMSV with phase variance
$`1/(4N)`$, derived from the initially pure pump. It describes the output
after tracing the pump; subsequent joint operations retaining that correlated
pump require the full state.

## Accuracy regimes

The finite estimates also control varying $`\lambda=\lambda_\alpha`$ in the
sufficient window

```math
\frac{(1+\lambda_\alpha^2)(1+r_\alpha)}{\alpha}\longrightarrow0.
```

Throughout this window, the complete pair-count distribution converges to the
nominal geometric law in total variation. Each individual output approaches
its nominal thermal marginal in trace distance. The joint output obeys a
stronger accuracy criterion:

| Crossover sequence | Joint-state conclusion |
|---|---|
| $`\lambda_\alpha\to0`$ | The nominal pure TMSV becomes accurate in trace distance. |
| $`\lambda_\alpha\to\lambda_0>0`$ | Purity and nominal-state fidelity approach finite crossover values. |
| $`\lambda_\alpha\to\infty`$ | The infimum of trace distance over every pure state tends to one. |

Within this window, nominal pure-state accuracy holds **if and only if**
$`\lambda_\alpha\to0`$, equivalently the nominal mean pair number
$`\bar n_{\mathrm{cl}}=\sinh^2r`$ is $`o(\sqrt N)`$. The
[validity-window proof](VALIDITY_WINDOW.md) derives these statements from the
finite inequalities, including nonconvergent crossover sequences.

## Energy, purity, and entanglement

A separate conserved-sector energy estimate proves vanishing fractional
pump depletion throughout the window. When also $`\alpha\lambda\to\infty`$,

```math
\langle n_a\rangle\sim2\alpha\lambda,\qquad
\frac{N-\langle n_c\rangle}{N}\sim\frac{2\lambda}{\alpha}.
```

In particular, for fixed $`\lambda>0`$ the mean pair number is asymptotic to
$`2\lambda\sqrt N`$. The energy proof uses conserved-number sectors and
bounded truncations of the count law; trace distance alone does not control
an unbounded mean.

Define

```math
\mathcal P(\lambda)=\int_0^\infty e^{-z-\lambda^2z^2}\,dz.
```

At each fixed finite $`\lambda\ge0`$, pump and joint-output purity tend to
$`\mathcal P(\lambda)`$, while squared target fidelity
$`\langle\mathrm{TMSV}_r|\rho_{ab}|\mathrm{TMSV}_r\rangle`$ tends to
$`\mathcal P(\lambda/\sqrt2)`$. Both are strictly below one for
$`\lambda>0`$ and equal one at $`\lambda=0`$. Global purity makes pump
mixedness an entanglement diagnostic across **pump versus both outputs**.
The [growing-window example](VALIDITY_WINDOW.md) also gives the second-Renyi
entropy for that partition along $`\lambda_\alpha=N^{1/8}`$.

## Measurement scope

Every POVM commuting with total output photon number has asymptotically the
nominal statistics throughout the controlled window. This includes passive
optics with vacuum ancillas followed by photon counting.

For fixed $`\lambda>0`$, a phase-referenced squeezed-quadrature distribution
separates the exact output from every individual Gaussian state, including
mixed states with adjusted parameters. The output nevertheless approaches
the convex Gaussian hull through $`\sigma_{ab}`$. These are different
comparison classes. The readout requires physical resolution on a scale
$`N^{-1/4}`$; fixed positive additive Gaussian resolution erases this
particular distinction. The [quadrature proof](THEOREM.md), Section 7, and
[varying-parameter extension](VALIDITY_WINDOW.md), Section 4, give the
bounded statistics and their measurement scales.

## First fixed-purity crossing

For a prescribed loss $`0<\delta<1`$, let $`\lambda_\delta>0`$ be the unique
solution of $`\mathcal P(\lambda_\delta)=1-\delta`$. The first time at which
the exact pump purity reaches $`1-\delta`$ satisfies

```math
gt_\delta=\frac{\log\alpha+\log(8\lambda_\delta)}{2\alpha}
+O_\delta(\log\alpha/\alpha^2).
```

The proof uses a uniform purity envelope without assuming monotonic exact
dynamics. [Finite first-crossing certificates](PROOF_REVIEW.md) provide
exact-arithmetic enclosures. The [source comparison](SOURCE_REVIEW.md)
explains how the leading large-$`\alpha`$ parts of the short-time coefficients
agree with Chinni–Quesada while
their fixed-degree polynomial has a different asymptotic root.

[Proof map](PROOF_MAP.md) · [Tutorial bridge](TUTORIAL_BRIDGE.md) ·
[Sources and attribution](SOURCES.md)
