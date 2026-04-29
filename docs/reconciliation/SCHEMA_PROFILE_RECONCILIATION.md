# Schema and Profile Reconciliation

Status: initial reconciliation seed for Codex/agent review.

This document compares the captured blueprint sources and recommends a canonical v0 contract surface. It is intentionally conservative: source variation is recorded before final decisions are made.

## Sources reconciled

Primary source captures:

- `docs/source-captures/PROPHET_ARCHITECTURE_SPECIFICATION_CAPTURE.md`
- `docs/source-captures/EXECUTABLE_SPECIFICATION_PACK_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/CONTROLPLANE_TECHNICAL_PAPER_CAPTURE.md`
- `docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`
- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
- `docs/source-captures/VOLUME_VI_OPERATIONAL_MESH_CAPTURE.md`
- `docs/source-captures/VOLUME_VII_SECURE_COORDINATION_CAPTURE.md`
- `docs/source-captures/VOLUME_VIII_AUTONOMIC_CONSTITUTION_CAPTURE.md`

## Source agreement

The captured corpus consistently agrees on these architectural requirements:

1. Every consequential participant must be represented as a node.
2. Nodes must expose identity, lifecycle, interfaces, memory, policy, and observability surfaces.
3. Commands and delegation are authority-bearing events, not informal messages.
4. Artifacts, claims, policies, and model updates require provenance.
5. Replay is constitutional evidence, not only debugging.
6. Proposals and promotions are distinct.
7. Learned or heuristic outputs stay soft-lane until validated and promoted.
8. Repositories are governed memory organs, not passive buckets.
9. Human/operator interventions must be typed and replayable.
10. Public implementation must avoid private data and operational secrets.

## Canonical v0 envelope family

Recommended v0 schema family:

| Canonical schema | Source basis | Purpose |
| --- | --- | --- |
| `node_descriptor.schema.json` | Vol II, Vol III, Vol IV, controlplane paper | constitutional identity and admission contract |
| `artifact_envelope.schema.json` | Vol II, Vol III, Vol IV | durable artifact/evidence record |
| `policy_envelope.schema.json` | Vol II, Vol III, Book VIII, Vol VII | policy bundle, constraint, obligation, and activation metadata |
| `command_envelope.schema.json` | Vol II, Vol III | typed authority-bearing command |
| `delegation_envelope.schema.json` | Vol II, Vol III | bounded handoff token / scoped authority transfer |
| `observation_envelope.schema.json` | Vol II, Vol III, controlplane paper | information-plane observation |
| `status_envelope.schema.json` | Vol II, Vol III, Vol IV | node status and health report |
| `trace_event.schema.json` | Vol IV, Book XI, Vol VI/VII | normalized causal event |
| `transition_record.schema.json` | Vol IV, Vol III | lifecycle transition evidence |
| `replay_envelope.schema.json` | Vol III, Vol IV, Book VIII | replay manifest and reconstruction contract |
| `evaluation_result.schema.json` | Vol III, Vol IV, Book VIII | evaluation, benchmark, conformance, replay result |
| `promotion_decision.schema.json` | Vol IV, Book VIII | constitutional admission/quarantine/rejection verdict |
| `incident_report.schema.json` | Vol III, Vol IV, Volume VIII | safety, policy, epistemic, runtime, or operator incident |
| `claim.schema.json` | Book XI, Prelude F | canonical claim object for ingest/query slices |
| `provenance_record.schema.json` | Book XI, Book VIII, Volume VI/VII/VIII | evidence chain and source lineage |
| `capability_descriptor.schema.json` | Book XI, Vol II | typed gateway for side effects |
| `operator_record.schema.json` | Vol I, Vol II, Book XI | explicit state-transforming operator choice |
| `genesis_seed.schema.json` | Genesis/Inception capture | reusable compile-time twin seed |
| `twin_runtime_descriptor.schema.json` | Genesis/Inception capture | live runtime twin descriptor |
| `event_envelope.schema.json` | Genesis/Inception, Book XI, Vol VI/VII | cross-plane event record |
| `policy_conflict_case.schema.json` | Volume VIII | typed cross-domain policy conflict |
| `stability_report.schema.json` | Volume VIII | mesh stability metrics and verdict basis |
| `constitutional_verdict.schema.json` | Volume VIII | stable/watch/constrain/quarantine governor verdict |
| `corpus_manifest.schema.json` | Volume VIII | governed corpus/data admission object |
| `operator_provenance_case.schema.json` | Volume VIII | human intervention provenance |
| `export_bundle.schema.json` | Volume VI/VII | signed export artifact and chain-of-custody |
| `attestation_statement.schema.json` | Volume VII, Book VIII | threshold/in-toto-style statement |
| `benchmark_corpus.schema.json` | Volume VI/VII, Book VIII | benchmark suite / learning admission corpus |

## Current repo schema delta

Current repository schemas are partial:

- `node_descriptor.schema.json` exists but includes some extensions not yet reconciled with Volume III's stricter enum set.
- `evaluation_result.schema.json` exists and is broadly aligned, but verdict and promotion recommendation enums differ from Volume III and Book VIII.
- `promotion_decision.schema.json` exists and includes `rollback` and `revoke`, which are useful but should be checked against the promotion law versus lifecycle law boundary.
- `replay_envelope.schema.json` exists and is broadly aligned.

Current repository is missing many canonical envelopes listed above.

Recommendation: keep current schemas as provisional until a v0 schema cleanup issue normalizes enums and file coverage.

## Lifecycle state reconciliation

Source variants:

- Controlplane paper: `unconfigured`, `inactive`, `active`, `degraded`, `recovery`, `finalized` plus quarantine in transition notes.
- Volume II: `unconfigured`, `inactive`, `active`, `degraded`, `recovery`, `quarantined`, `finalized`.
- Volume III: `unconfigured`, `configured`, `inactive`, `active`, `degraded`, `recovery`, `quarantined`, `retired`.
- Volume IV: `unconfigured`, `configured`, `inactive`, `active`, `degraded`, `recovery`, `quarantined`, `retired`.
- Genesis/Inception twin lifecycle: `draft`, `candidate`, `ready`, `executing`, `paused`, `quarantined`, `revoked`, `archived`.

Recommended v0 split:

### Fractal Node lifecycle

Use:

- `unconfigured`
- `configured`
- `inactive`
- `active`
- `degraded`
- `recovery`
- `quarantined`
- `retired`
- `finalized`

Rationale: this preserves the Volume III/IV executable sequence while retaining `finalized` from the controlplane paper as terminal archival/closure state.

### Twin runtime lifecycle

Use a separate profile:

- `draft`
- `candidate`
- `ready`
- `executing`
- `paused`
- `quarantined`
- `revoked`
- `archived`

Rationale: Twin/Inception lifecycle is related but not identical to generic node lifecycle. Do not collapse them prematurely.

## Lifecycle transition event reconciliation

Recommended v0 node transition events:

- `configure_ok`
- `admission_granted`
- `admission_denied`
- `activate_ok`
- `deactivate`
- `health_degraded`
- `contract_violation_or_health_drop`
- `recover_start`
- `recovery_started`
- `recover_ok`
- `recovery_verified`
- `recover_failed`
- `quarantine`
- `quarantine_imposed`
- `remediation_ok`
- `revoke`
- `retire`
- `never_admitted`
- `retirement_approved`
- `finalize`

Open decision: collapse synonymous pairs (`recover_start` vs `recovery_started`, `recover_ok` vs `recovery_verified`, `quarantine` vs `quarantine_imposed`) or preserve them as source-derived aliases.

Recommendation for v0 implementation: choose one canonical term per action and list aliases in profile metadata.

## Promotion decision reconciliation

Source variants:

- Volume IV: `reject`, `shadow-only`, `limited-authority`, `full-promotion`, `quarantine`.
- Book VIII: proposal versus promotion; hard/soft boundary; quarantine; rollback and lawful learning.
- Volume III: `reject`, `shadow-only`, `limited-authority`, `full-promotion`; replay verdicts include `manual-review`.
- Current schema: `reject`, `shadow-only`, `limited-authority`, `full-promotion`, `quarantine`, `rollback`, `revoke`.

Recommended v0 `PromotionDecision.decision`:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `rollback-required`
- `revoke-authority`
- `manual-review`

Rationale: `rollback` and `revoke` should remain expressible, but naming should clarify they are governance decisions, not direct actuator commands.

Open decision: whether rollback/revoke belong in `promotion_decision` or in a separate `constitutional_verdict` / `incident_response` schema.

## Evaluation result reconciliation

Recommended v0 `EvaluationResult.verdict`:

- `pass`
- `conditional-pass`
- `warn`
- `fail`
- `drift`
- `inconclusive`
- `manual-review`

Recommended `promotion_recommendation`:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`

## Conformance class reconciliation

From Volume III:

- C0 schema conformant;
- C1 supervised node;
- C2 replayable node;
- C3 production node;
- C4 safety-critical embodiment.

Recommendation: preserve exactly as v0 conformance ladder.

## BT semantic profile reconciliation

Volume III pins:

- `root_to_leaf_sequential` tick model;
- explicit halt required;
- subtree-local blackboard default;
- shared keys require declaration;
- idempotent leaf reentry;
- leaf status events;
- recovery action policy refs;
- recovery retry budget;
- tick trace required;
- leaf action correlation ID required.

Recommendation: create `profiles/bt_semantic_profile.yaml` from Volume III before implementation expands.

## Genesis/Inception/K3 reconciliation

Genesis/Inception source defines:

- semantic hologram substrate;
- Genesis seed;
- Inception binding;
- K3 bridge states;
- twin lifecycle;
- cognitive mesh;
- provider/organ adapters;
- state-plane separation.

Recommended v0 artifacts:

- `schemas/hologram.schema.json`
- `schemas/genesis_seed.schema.json`
- `schemas/inception_request.schema.json`
- `schemas/twin_runtime_descriptor.schema.json`
- `profiles/k3_bridge_lifecycle.yaml`

Open decision: whether `Hologram` belongs in `schemas/` as canonical v0 or in a later semantic package after Prelude F/ontology alignment.

## Provisional runtime scaffold status

The `procyber/` package should be considered provisional.

It may be retained as a seed, but implementation should pause until:

1. schema family is reconciled;
2. lifecycle aliases are resolved;
3. package naming is decided (`procyber` vs `procybernetica` vs `prophet_reference_kit`);
4. fixtures are generated from captured examples.

Recommendation: do not expand runtime implementation until issue #2 completes review.

## Open decisions for human review

1. Package name: `procyber`, `procybernetica`, or `prophet_reference_kit`?
2. Should source-derived examples use `Prophet` or `ProCybernetica` names in JSON titles?
3. Should `finalized` and `retired` both exist in node lifecycle?
4. Should rollback/revoke be promotion decisions or incident/constitutional verdict decisions?
5. Should `Hologram` be a v0 schema or a v0.2 semantic package?
6. Should public repo include only schemas/docs first, with runtime in a later package, or keep reference runtime here?
7. Which artifacts need Apache-2.0 license headers versus markdown provenance notices?

## Recommended follow-up issues

1. Normalize v0 schema family and remove provisional enum drift.
2. Add missing core envelope schemas from Volume III.
3. Add BT semantic profile from Volume III.
4. Add K3 bridge lifecycle profile from Genesis/Inception.
5. Add Book XI claim/event/provenance/capability schemas.
6. Add Volume VI/VII/VIII mesh/coordination/autonomic schemas.
7. Decide package naming and runtime location.
8. Generate public-safe fixtures from captured examples.

## Current recommendation

Proceed with capture-complete, reconciliation-first posture.

Do not treat runtime code as canonical until the schema/profile cleanup is complete.
