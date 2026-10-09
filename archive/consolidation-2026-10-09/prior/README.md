# Coherent-pump crossover: source audit and reduced-state form

Read [the follow-up](FOLLOWUP.md) for the trace-controlled phase-averaged state, the distinction between accurate photon counts and inaccurate joint-state predictions, and the matched purity-onset comparison. [SOURCES.md](SOURCES.md) records primary passages and access boundaries. The initial pilot remains byte-preserved under [prior](prior/README.md).

Run the new five-group checks with NumPy, SciPy, SymPy and mpmath available:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python check_comparison.py --output /absolute/new/report.json
```

The argument for the infinite-system statement is analytical. Numerical cutoffs and quadrature refinements are diagnostics. The first convergence-check failure and its explicitly larger-amplitude continuation are preserved; no pilot tolerance or reference was altered. No repository is created by this package.
