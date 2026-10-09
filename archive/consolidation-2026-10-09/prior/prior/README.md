# Quantized-pump crossover pilot

A fresh, independent calculation for resonant nondegenerate down-conversion
with an initially coherent pump. At a controlled growing-gain crossover, pump
purity has a nontrivial limiting curve while fractional depletion tends to zero.
The model and broad quantum-pump mechanism have direct predecessors. The
candidate contribution is the complete limiting state and uniform error bound.

Read [the derivation and allocation decision](PILOT.md), then the
[source-reading record](SOURCES.md). This is a pilot record, not an initialized
scientific repository or a publication-priority certificate.

## Reproduce the five check groups

The recorded environment is in `RUN_RECORD.json`. With the listed dependencies:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python check_pilot.py --output /absolute/path/to/a/new/report.json
```

Use a new filename: the checker refuses to overwrite evidence. Numerical
truncations test identities and the exact-frame equations; the asymptotic claims
rest on the proof, not on extrapolating these simulations. The two supplied runs
pass all assertions, but one state-distance field differs by approximately
1.18e-16. Report identity and scientific assertion success are separate facts.
No old project's code, original article PDF, or external figure is imported.
