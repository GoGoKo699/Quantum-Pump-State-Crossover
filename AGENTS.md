# Repository maintenance

Work only in `GoGoKo699/Quantum-Pump-State-Crossover`. The user authorizes
modification and merge in this repository. Read `README.md`, `research/TUTORIAL_BRIDGE.md`,
`research/CLAIMS.md`, `research/THEOREM.md`, `research/PROOF_MAP.md`,
`research/SOURCES.md`, `research/VALIDITY_WINDOW.md`,
`research/PROOF_REVIEW.md`, `research/SOURCE_REVIEW.md`, and
`REPRODUCIBILITY.md` first.

## Scientific scope

Preserve the coherent pump, vacuum outputs, lossless resonant nondegenerate
three-mode Hamiltonian and compact-lambda growing-gain limit. Distinguish
norm/trace-distance control from unbounded moment estimates; use the separate
energy proof. Keep first-crossing, fixed-gain, and finite-time claims distinct. The
separate validity-window corollary uses the original finite inequalities; do
not extrapolate a fixed-lambda little-o to varying lambda or claim a maximal
undepleted window.

The Gaussian phase mixture is a reduced-state representation, not injected
technical noise or a Markovian channel. Separate individual Gaussian states
from their convex hull. No Wigner-negativity, device operating-window, or
failure of all photon-counting uses follows. State phase-reference and
shrinking-resolution requirements when discussing the quadrature signature.
Credit the model, Gaussian frames, historical high-gain limits, and prior
pump-noise mechanism. Source access failures are not novelty evidence.

## Preservation and presentation

`research/THEOREM.md` is the canonical, directly maintained theorem.
Scientific implementations live in `scripts/`; canonical reports live in
`verification/`. The hashes in `verification/integrity.json` protect the
core implementations, their reference reports, the theorem, and the license.
Do not regenerate references or relax assertions to make a check pass.
Changes to a protected file require explicit scientific justification and
an accompanying integrity-manifest update. Preserve equations and source terminology.
Present the complete scientific account. Keep development chronology and
work orders out of reader-facing pages; retain model assumptions and
measurement conditions that determine the meaning of a result.
Retain the owner's MIT license and Purpose and contact notice.

Preserve the one-source learning route through Yanagimoto et al. (2024),
arXiv:2311.13775v1, Section II and Boxes 1–3. The local tutorial bridge
translates the degenerate example to this nondegenerate model; it does not
replace the canonical proofs. Keep inherited Gaussian frames, amplified cubic
interactions, and onset-scale reasoning credited. Other literature supports
attribution and comparison rather than adding prerequisite tutorials.

## Verification and remote writes

Run `python scripts/verify.py --output-dir /absolute/new/path/outside/repository`.
All scientific assertions stay unchanged. Canonical byte differences are
reported separately, never hidden by overwriting a reference. Portability
mode admits only finite numeric report changes after every assertion passes;
review all differences explicitly before a merge.

Verify live repository identity and main before writing. Use a feature branch
and PR, check the actual published head and its CI receipt/source hashes,
merge with the expected head, then check merged main separately. Do not
force-push shared branches, add write-capable CI, or import another project's
code or agenda. Local verification is not hosted verification; neither is
external scientific peer review.
