# Reproducibility

Use Python 3.13 with the pinned dependencies:

```bash
python -m pip install -r requirements.txt
python scripts/build_reading.py --check
python scripts/verify.py --output-dir /absolute/path/to/new-results
```

The output directory must be new and outside the repository. The verifier
runs **25 scientific groups and 8 infrastructure tests**, checks local links
and source integrity, and compares all five numerical reports with their
canonical references.

## Scientific checks

| Component | What it checks |
|---|---|
| State and measurement checks | Residual generators, finite-state evolution, number marking, count laws, purity, fidelity, quadrature statistics, and cutoff refinement |
| `scripts/check_proof_review.py` | Continuous-coordinate remainder norms, energy identities, exact first-crossing certificates, source expansions, and phase-mixture formulas |
| `scripts/check_manuscript_basis.py` | Finite error domination, count identities, source conventions, changing-frequency witnesses, and the growing-parameter sequence |

The analytical proofs establish the infinite-dimensional statements.
The numerical and symbolic checks verify identities, finite examples, and
the implementation of the stated bounds.

The first-crossing certificates use rational sign comparisons: alternating
Taylor bounds for purity, integer square-root bounds, and exponential Taylor
sums with a geometric remainder. Their exact witnesses are in
[proof-review.json](verification/proof-review.json). The symbolic checker
runs with `PYTHONHASHSEED=0` for reproducibility. Growing-window examples
evaluate the proved inequalities at high precision; their decimal values
are distinct from the rational interval certificates.

## Verification receipt

`verification.json` records the tested commit and tree, the complete source
hash inventory, assertion outcomes, and every canonical report difference.
The `scientific/` directory contains three reports and their logs;
`proof_review.json` and `manuscript_basis.json` are compared with the two
references under `verification/`.

Strict mode requires byte-identical canonical reports. The explicit option
`--allow-numeric-report-differences` permits finite numerical changes with
identical types and structure after every assertion passes. Such a run is
labeled `PASS_REQUIRES_NUMERIC_REVIEW` and lists every changed field.
Source changes, missing reports, nonnumeric changes, and failed assertions
are errors in either mode. Hosted CI uses this portability option; inspect
the receipt to distinguish assertion success from report byte identity.

## Figures

[Figure data and captions](manuscript/FIGURES.md) identify the limiting curves
and finite error bounds. Render the SVGs with

```bash
python manuscript/render_figures.py --output-dir /absolute/new/figure-directory
```

Rendering additionally requires Matplotlib. The CSV files store plotted
values, and `manuscript/figures/generation.json` records rendering versions.

## Source integrity

`research/THEOREM.md` is generated from the reference theorem through
`scripts/build_reading.py`. The transformation ledger in
`provenance/READING.json` hashes the source, output, and every display
equation. Edit the generation rules and regenerate to update this page.
Other research pages are maintained directly.

The verifier checks the 60-file reference package under
`archive/consolidation-2026-10-09/`, its three manifests, and the owner's
license. `provenance/IMPORT.json` records the package and archive hashes.
Reference reports and scientific tolerances are preserved; execution
receipts for a PR head and merged main are recorded separately in the PR.

[Sources and attribution](research/SOURCES.md) · [Proof map](research/PROOF_MAP.md)
