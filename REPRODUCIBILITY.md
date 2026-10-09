# Reproducibility and source preservation

Use Python 3.13 with the pinned environment in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
python scripts/build_reading.py --check
python scripts/verify.py --output-dir /absolute/path/to/new-results
```

The output directory must be new and outside this repository. The wrapper
checks the full 60-file archive and its three manifests, the owner's license,
three generated reading pages, and relative links. It runs eight infrastructure
tests and all fifteen original scientific groups: five consolidation, five
comparison, and five pilot groups. No archived script, assertion, reference
report, or numerical tolerance is modified.

## Reading the receipt

`verification.json` records the tested commit and tree when Git metadata is
available, the source hash inventory, assertion outcomes, and every canonical
report difference. The original wrapper's receipt and logs are under
`scientific/`. Source integrity, passing assertions, and byte identity are
separate facts.

Strict mode requires all canonical report bytes to match. The explicit option
`--allow-numeric-report-differences` allows only finite numerical value changes
with identical types and structures after every original assertion passes.
Such a run is labeled `PASS_REQUIRES_NUMERIC_REVIEW` and lists every changed
field. This option changes report policy, not scientific tolerances. Missing
reports, changed sources, nonnumeric changes, and failed assertions are fatal.
The initial local baseline passed all fifteen groups with one approximately
$4.03\times10^{-16}$ difference in a physical-count diagnostic; that historical
report was not replaced.

Hosted CI uses the explicit portability mode to retain inspectable evidence
across numerical stacks. A green job does not establish canonical byte
identity. Inspect every difference and the source/commit hashes before merge.
A PR-head run is not a merged-main run; each must be verified separately.
Exact run evidence belongs in the PR discussion and artifacts.

## Scientific meaning

The proofs establish the infinite-dimensional asymptotic statements. Finite
cutoff evolution, refinement, symbolic core identities, and source-expansion
comparisons are checks, not external peer review or a novelty certificate.
Norm convergence does not by itself control unbounded moments. The source
record's older access boundaries remain explicit.

## Current reading pages

`scripts/build_reading.py` selects the supplied theorem, assessment, and source
sections and applies only recorded literal presentation changes. Its ledger
in `provenance/READING.json` hashes sources, outputs, and all selected display
equations. Edit the generation rule and regenerate rather than independently
editing those current pages. The complete originals remain unchanged in
`archive/consolidation-2026-10-09/`.

`provenance/IMPORT.json` records the exact supplied ZIP hash, initial repository
revision, archive root hash and unchanged license. Only this authorized research
package was imported; unrelated project files and external PDFs were excluded.

The continuation is [Chat-based](CURRENT.md), not dependent on a workspace.
