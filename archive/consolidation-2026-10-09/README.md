# Quantum pump state crossover

**Right photon counts, non-Gaussian joint state.** In a closed coherent-pump down-converter, a controlled growing-gain regime makes the full pair-count distribution agree with the deterministic-pump prediction while the joint quantum state remains finitely different. Its fractional pump depletion vanishes. An explicit non-Gaussian quadrature distribution distinguishes that state from every single Gaussian model when a suitable phase reference and resolution are available.

Read the [self-contained theorem](THEOREM.md), then the [contribution assessment](REVIEW.md) and [primary-source comparison](SOURCES.md). The [workspace handoff](PROJECT_HANDOFF.md) defines the bounded next task and protected-project separation. No repository has been created or checked.

The theorem combines a uniform state-norm limit, an independent energy estimate, complete number-statistics control, a fixed-purity onset law, and a bounded phase-sensitive measurement consequence. It is an ideal three-mode theoretical result, not a device operating-window guarantee. The limiting signal state is a Gaussian mixture, not a state outside the convex Gaussian hull.

## Reproduction

Use NumPy, SciPy, and SymPy, then run:

```bash
python verify.py --output-dir /absolute/new/path/outside/package
```

The wrapper runs all fifteen current and preserved scientific check groups, verifies the incoming files and manifests, and lists any canonical-report difference. A failed numerical assertion is separate from a last-bit report change. Neither is hidden by editing source tolerances or reference reports.

The 33-file incoming record in `prior/` is unchanged, including its original failed convergence check and pilot repeat-report difference. It supplies detailed historical derivations and computational evidence, but is not the first reading path. Current check source is `check_consolidation.py`; all new outputs are in `evidence/`. No external paper PDF is redistributed.
