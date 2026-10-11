# Analytical figures

The figures visualize the limiting crossover curves and finite error bounds.
Render them with

```bash
python manuscript/render_figures.py --output-dir /absolute/new/figure-directory
```

Rendering additionally uses Matplotlib, whose executed version is recorded
in `figures/generation.json`. It is not required for the scientific check
suite. The CSV files preserve the plotted values; their floating-point
format is a data convenience, not certified interval arithmetic.

## Figure 1: fixed crossover

[SVG](figures/crossover.svg) · [data](figures/crossover.csv)

**Caption.** Pump and joint-output purity $\mathcal P(\lambda)$ and squared
fidelity $\mathcal P(\lambda/\sqrt2)$ with the nominal two-mode squeezed
vacuum in the fixed-$\lambda$ large-pump limit. At every displayed finite
crossover coordinate, complete pair-count error and fractional depletion
tend to zero. The curves are limiting formulas, not finite-brightness
numerical propagation. The purity loss diagnoses entanglement across the pump
versus both outputs jointly.

## Figure 2: a controlled growing-window sequence

[SVG](figures/growing_window.svg) · [data](figures/growing_window.csv)

**Caption.** Evaluations of the finite inequalities along
$\lambda_\alpha=\alpha^{1/4}=N^{1/8}$. The lower bound on trace distance from
every pure output state tends to one, while the upper bound on the total-
variation error of the nominal geometric pair-count law tends to zero.
The curves use the explicit state error, not a bare extrapolation of the
limiting state. Bounds exceeding a trivial probability range are clipped to
that range. The brightness values illustrate the asymptotic bounds of the
closed three-mode Hamiltonian. The CSV also includes the energy bound and
the single-Gaussian separation bound.
