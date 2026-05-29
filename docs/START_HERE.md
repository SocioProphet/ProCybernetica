# Start Here

This repository is the public codification surface for the existing ProCybernetica blueprint.

The repository has reached a stable v0 public-review state after the bounded 20-turn integration lane. Capture and reconciliation remain preserved, but the repo now also exposes executable public conformance lanes.

## Public-first rule

This repository exists so the blueprint can be inspected, criticized, reproduced, and trusted in public.

Publish by default. Sanitize only for specific narrow reasons: secrets, credentials, customer/user-private data, live private telemetry, sensitive deployment configuration, legally restricted third-party material, or evidence requiring redaction.

Read:

- `docs/decisions/0001-public-first-transparency.md`
- `docs/PUBLICATION_BOUNDARY.md`
- `docs/PUBLICATION_MATRIX.md`

## Public-review read order

Start here:

1. `docs/INTEGRATION_STATUS.md`
2. `docs/PUBLIC_REVIEW_CHECKLIST.md`
3. `docs/conformance/README.md`
4. `docs/implementation/VERTICAL_SLICE_PLAN.md`
5. `docs/BLUEPRINT_POSITIONING.md`
6. `docs/BLUEPRINT_PROVENANCE.md`
7. `docs/CAPTURE_STATUS.md`
8. `docs/CORPUS_INDEX.md`
9. `AGENTS.md`

Then read the source captures by layer:

### Lineage and doctrine

- `docs/source-captures/VOLUME_I_EXPANDED_MONOGRAPH_CAPTURE.md`
- `docs/source-captures/CONTROLPLANE_TECHNICAL_PAPER_CAPTURE.md`

### Architecture law

- `docs/source-captures/PROPHET_ARCHITECTURE_SPECIFICATION_CAPTURE.md`
- `docs/source-captures/EXECUTABLE_SPECIFICATION_PACK_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`

### Genesis, Inception, and twin runtime

- `docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`

### Mesh, coordination, and stabilization

- `docs/source-captures/VOLUME_VI_OPERATIONAL_MESH_CAPTURE.md`
- `docs/source-captures/VOLUME_VII_SECURE_COORDINATION_CAPTURE.md`
- `docs/source-captures/VOLUME_VIII_AUTONOMIC_CONSTITUTION_CAPTURE.md`

### Constitutional control and lawful learning

- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`

### Frontier cybernetic governance doctrine

- `docs/cybernetic-governance/CAPTURE_INDEX.md`
- `docs/cybernetic-governance/PROGRAM_CAPTURE.md`
- `docs/constitutional/CONSTITUTIONAL_INVARIANTS.md`
- `docs/foundations/CYBERNETIC_GOVERNANCE_FABRIC.md`
- `docs/security/THREAT_MODEL.md`
- `docs/constitutional/SEPARATION_OF_POWERS.md`
- `docs/release/BIRKHOFF_RELEASE_DELTA.md`
- `docs/monitor/MONITOR_NETWORK_AS_QEC.md`
- `docs/assurance/PCP_REPLAY_AUDIT.md`

### Capability doctrine

- `docs/capabilities/fraud-decision-intelligence-control-plane.md`

### Implementation practicum

- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
- `docs/implementation/VERTICAL_SLICE_PLAN.md`
- `tests/fixtures/book-xi/slice-a-ingest-to-claims.synthetic.json`

### Mathematical and semantic runway

- `docs/source-captures/PRELUDE_B_LINEAR_ALGEBRA_CAPTURE.md`
- `docs/source-captures/PRELUDE_C_DYNAMICS_FEEDBACK_CAPTURE.md`
- `docs/source-captures/PRELUDE_F_ONTOLOGY_CORPUS_SEMANTIC_CONTRACTS_CAPTURE.md`

### Scoring and dashboard program

- `docs/source-captures/SCORING_METHODOLOGY_CAPTURE.md`
- `docs/source-captures/DASHBOARD_ARTIFACT_INVENTORY_CAPTURE.md`
- `docs/scoring/README.md`
- `docs/dashboard/README.md`
- `docs/assurance/CIVIC_STACK_ASSURANCE_BINDING.md`

## Current repository mode

The repository is in v0 public-review mode.

The main blueprint corpus is captured. The v0 schema/profile surface is normalized. Public-synthetic fixtures and validators are in CI. Remaining runtime implementation belongs in the owning upstream repositories.

## What not to do first

Do not begin by expanding runtime code.

Do not treat public-review readiness as production readiness.

Do not hide public-safe material because it is incomplete or still being improved.

Do not ingest raw scoring/dashboard data without classification, but do publish schemas, methodology, summaries, validation checks, and public-safe fixtures.

Do not overwrite source ambiguity with invented certainty.

Do not implement Superconscious runtime coupling from this doctrine branch while `SocioProphet/superconscious` is under construction; open dependency issues there only if a concrete integration requirement appears.

## Correct next work

1. Keep CI and fixture validation green.
2. Use `docs/PUBLIC_REVIEW_CHECKLIST.md` before publishing or claiming conformance.
3. Extend Book XI after Slice A only through bounded public-safe slices.
4. Treat G7+ theorem/colimit/evidence-cocone work as a separate theorem-audit tranche.
5. Push downstream runtime adapters into the owning repositories.
6. Publish public-safe scoring/dashboard artifacts or substitutes under the publication matrix.
7. Leave the CI Observation Ledger open by design.