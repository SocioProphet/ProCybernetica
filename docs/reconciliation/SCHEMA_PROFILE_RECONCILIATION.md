# Schema and Profile Reconciliation

Status: estate-aware v0 reconciliation update

Turn: 10 / 20

This document reconciles the captured ProCybernetica blueprint with the active GitHub estate. It supersedes the initial schema seed posture by accounting for completed integration maps across AgentPlane, semantic-serdes/SHIR, ontogenesis, SourceOS/SociOS, Prophet Platform, HolographMe, Foundry/model-governance, and workstation/operator surfaces.

## Governing rule

ProCybernetica owns public constitutional semantics, doctrine-as-code, schema/profile interpretation, public conformance expectations, and reference-kit posture.

It does not own runtime/deployment services, model lifecycle ledgers, ontology release discipline, semantic-serdes contracts, SourceOS typed contracts, AgentPlane evidence artifacts, workstation runners, terminal products, browser runtimes, or product UI implementation.

## Sources reconciled

Primary source captures:

- `docs/source-captures/VOLUME_I_EXPANDED_MONOGRAPH_CAPTURE.md`
- `docs/source-captures/CONTROLPLANE_TECHNICAL_PAPER_CAPTURE.md`
- `docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`
- `docs/source-captures/PROPHET_ARCHITECTURE_SPECIFICATION_CAPTURE.md`
- `docs/source-captures/EXECUTABLE_SPECIFICATION_PACK_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
- `docs/source-captures/VOLUME_VI_OPERATIONAL_MESH_CAPTURE.md`
- `docs/source-captures/VOLUME_VII_SECURE_COORDINATION_CAPTURE.md`
- `docs/source-captures/VOLUME_VIII_AUTONOMIC_CONSTITUTION_CAPTURE.md`

Estate maps:

- `docs/integration/agentplane-evidence-map.md`
- `docs/integration/semantic-serdes-shir-map.md`
- `docs/integration/ontogenesis-governance-map.md`
- `docs/integration/sourceos-socios-contract-map.md`
- `docs/integration/prophet-platform-record-map.md`
- `docs/integration/holographme-genesis-inception-map.md`
- `docs/integration/foundry-model-governance-map.md`
- `docs/integration/workstation-operator-surface-map.md`

## Source agreement

The captured corpus and estate maps agree on these requirements:

1. Every consequential participant should be representable as a node or referenced domain object.
2. Nodes expose identity, lifecycle, interfaces, memory, policy, and observability surfaces.
3. Commands and delegation are authority-bearing records, not informal messages.
4. Artifacts, claims, policies, model updates, release records, and operator actions need provenance.
5. Replay is constitutional evidence, not only debugging.
6. Proposal and promotion are distinct.
7. Learned, routed, inferred, or heuristic outputs stay soft-lane until validation and promotion.
8. Repositories are governed memory organs, not passive buckets.
9. Operator interventions must be typed and replayable.
10. Public implementation should publish public-safe schemas, examples, tests, methodology, and source-state summaries.
11. Existing upstream repos keep ownership of their concrete contract families.

## v0 schema disposition

### Keep in ProCybernetica v0

These schemas are appropriate public constitutional surfaces in this repository.

| Schema | Current status | Role |
| --- | --- | --- |
| `node_descriptor.schema.json` | present, reconciled | constitutional identity, lifecycle, and conformance surface for nodes |
| `artifact_envelope.schema.json` | present | generic public artifact/evidence wrapper |
| `policy_envelope.schema.json` | present | constitutional policy reference/summary surface |
| `command_envelope.schema.json` | present | authority-bearing command wrapper |
| `delegation_envelope.schema.json` | present | bounded handoff / scoped authority wrapper |
| `observation_envelope.schema.json` | present | information-plane observation wrapper |
| `status_envelope.schema.json` | present | node status and health report |
| `event_envelope.schema.json` | present | cross-plane event record with public release posture |
| `trace_event.schema.json` | present | causal/replay trace event |
| `transition_record.schema.json` | present | lifecycle transition evidence |
| `replay_envelope.schema.json` | present, reconciled | constitutional replay manifest |
| `evaluation_result.schema.json` | present, reconciled | evaluation / benchmark / conformance result summary |
| `promotion_decision.schema.json` | present, reconciled | constitutional admission, quarantine, rollback, or review verdict |
| `incident_report.schema.json` | present | review/remediation episode report |
| `claim.schema.json` | present | public claim object for Book XI practicum and scoring/evidence surfaces |
| `provenance_record.schema.json` | present | source/evidence lineage record |
| `capability_descriptor.schema.json` | present | high-level capability gateway descriptor |

### Keep as profiles, not schemas

| Contract | Current status | Reason |
| --- | --- | --- |
| `controlplane_state_machine.yaml` | present | lifecycle transition law belongs in profile layer |
| `promotion_policy.example.yaml` | present | threshold/promotion behavior belongs in profile layer |
| `bt_semantic_profile.yaml` | present | behavior-tree runtime semantics are profile-level |
| `k3_bridge_lifecycle.yaml` | present | Genesis/Inception transition profile, not full domain schema yet |

### Defer from v0

These remain valid blueprint concepts but should not be added to v0 until adapter and upstream maps stabilize.

| Deferred schema | Reason |
| --- | --- |
| `hologram.schema.json` | semantic-serdes/SHIR and ontogenesis own semantic object authority; add only after adapter design |
| `genesis_seed.schema.json` | needs HolographMe, Agent Registry, Policy Fabric, model/router, and SourceOS alignment first |
| `inception_request.schema.json` | same as above; should reference domain objects rather than duplicate them |
| `twin_runtime_descriptor.schema.json` | should likely use `domain_object_ref` and avoid cloning HolographMe |
| `policy_conflict_case.schema.json` | Volume VIII concept; wait until Policy Fabric / SourceOS policy mapping is complete |
| `stability_report.schema.json` | Volume VIII concept; wait for conformance plan and platform eval fabric mapping |
| `constitutional_verdict.schema.json` | may be needed later; currently `PromotionDecision` covers v0 decisions |
| `corpus_manifest.schema.json` | SHIR/ontogenesis/model-governance-ledger own relevant corpus/semantic artifacts |
| `operator_provenance_case.schema.json` | operator surfaces own concrete events; use EventEnvelope/ProvenanceRecord in v0 |
| `export_bundle.schema.json` | platform, SourceOS, semantic-serdes, and AgentPlane own concrete export/receipt surfaces |
| `attestation_statement.schema.json` | ontogenesis/AgentPlane/SourceOS/Prophet Platform own concrete attestation surfaces |
| `benchmark_corpus.schema.json` | model-governance-ledger / platform eval fabric own benchmark/eval records |
| `operator_record.schema.json` | covered in v0 by EventEnvelope, TraceEvent, TransitionRecord, and PromotionDecision |

## Upstream contract families ProCybernetica must not duplicate

| Upstream family | Owner | ProCybernetica action |
| --- | --- | --- |
| AgentPlane artifacts | `SocioProphet/agentplane` | reference RunArtifact, ReplayArtifact, PromotionArtifact, SessionArtifact, and related evidence |
| semantic-serdes primitives | `SocioProphet/semantic-serdes` | reference Event/Context/Surface, canonical enums, agent messages, decision artifacts, replay artifacts |
| SHIR object model | `SocioProphet/ontogenesis` and `semantic-serdes` | reference CandidateAssertion, Assertion, ProjectionLossReport, Receipt, and curation objects |
| ontology release discipline | `SocioProphet/ontogenesis` | reference SHACL reports, ledgers, signatures, SBOMs, module registry |
| SourceOS typed contracts | `SourceOS-Linux/sourceos-spec` | reference Policy, PolicyDecision, RunRecord, EventEnvelope, ProvenanceRecord, AgentSession, BootProofRecord, ReleaseReceipt, etc. |
| workstation conformance | `SociOS-Linux/workstation-contracts` | reference conformance fixtures and run receipts |
| Agent Machine runtime | `SourceOS-Linux/agent-machine` | reference AgentMachine, AgentPod, StorageReceipt, ActivationDecision, runtime evidence |
| Prophet Platform contracts | `SocioProphet/prophet-platform` | reference EventEnvelope, EvidenceReceipt, MembraneDecision, eval records, FogStack readiness records |
| HolographMe domain schemas | `SocioProphet/HolographMe` | reference HumanDigitalTwin, ConsentPolicy, Mission, projections, transition receipts |
| Foundry/model governance | `functional-model-surfaces`, `model-router`, `model-governance-ledger`, `guardrail-fabric`, `sourceos-model-carry` | reference manifest, route, governance, decision, carry, and ledger records |
| Operator products | `agent-term`, TurtleTerm, BearBrowser, source-os, socioprophet-web | reference operator/gateway events and receipts |

## Canonical v0 lifecycle

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

Decision: keep both `retired` and `finalized`.

Rationale:

- `retired` means the node no longer has operational authority.
- `finalized` means archival closure or evidentiary finalization after retention/replay obligations are satisfied.

### Twin runtime lifecycle

Keep separate from generic node lifecycle:

- `draft`
- `candidate`
- `ready`
- `executing`
- `paused`
- `quarantined`
- `revoked`
- `archived`

Decision: do not encode this as a ProCybernetica v0 schema yet. Keep it in profile/mapping docs until Genesis/Inception schemas are designed around HolographMe and related domain objects.

## Lifecycle transition vocabulary

Use the existing `profiles/controlplane_state_machine.yaml` vocabulary for v0 implementation. Treat alternate names from source captures as aliases in docs, not schema enums.

Canonical node transition events for v0:

- `configure_ok`
- `admission_granted`
- `admission_denied`
- `activate_ok`
- `deactivate`
- `health_degraded`
- `recover_start`
- `recover_ok`
- `recover_failed`
- `quarantine`
- `remediation_ok`
- `revoke`
- `retire`
- `finalize`

Recommendation: add alias metadata to `controlplane_state_machine.yaml` in Turn 11 rather than expanding enum values in schemas.

## Promotion decision vocabulary

Current schema vocabulary is accepted for v0:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`
- `rollback-required`
- `revoke-authority`

Decision: keep rollback/revoke as promotion decision values for v0, but use governance phrasing (`rollback-required`, `revoke-authority`) to avoid confusing them with direct actuator commands.

Potential future split: `constitutional_verdict.schema.json` may later absorb rollback/revoke/stability verdicts after Volume VIII adapter work.

## Evaluation result vocabulary

Current schema vocabulary is accepted for v0:

- `pass`
- `conditional-pass`
- `warn`
- `fail`
- `drift`
- `inconclusive`
- `manual-review`

Promotion recommendations remain:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`

## Conformance class reconciliation

Keep the Volume III ladder in v0:

- `C0-schema-conformant`
- `C1-supervised-node`
- `C2-replayable-node`
- `C3-production-node`
- `C4-safety-critical-embodiment`

Map later to:

- functional-model-surfaces M0-M5 maturity;
- SourceOS/SociOS conformance lanes;
- AgentPlane run/replay evidence;
- Prophet Platform eval fabric;
- ontogenesis SHACL/ledger gates.

Do not collapse these ladders yet. They measure adjacent but different things.

## Current v0 fixture coverage

Public synthetic fixtures currently validate through tests for:

- node descriptor
- policy envelope
- transition record
- artifact envelope
- claim
- provenance record
- event envelope
- trace event
- command envelope
- delegation envelope
- status envelope
- capability descriptor
- replay envelope
- evaluation result
- promotion decision

Scoring/dashboard public sample fixtures exist for:

- lab scoring sample CSV
- evidence registry sample CSV
- monitoring deltas sample CSV
- dashboard export sample JSON

## Runtime scaffold status

`procyber/` remains a reference validation scaffold, not a production runtime.

Accepted v0 runtime scope:

- schema loading;
- JSON payload validation;
- public practicum report emission;
- CI fixture checks.

Rejected for v0 inside this repo:

- platform service runtime;
- AgentPlane execution;
- SourceOS runner;
- ontology release pipeline;
- model routing;
- guardrail runtime;
- UI implementation;
- browser/terminal runtime.

## Package naming decision

Current CLI/package name `procyber` may remain for v0 validation scaffold.

Open future decision: rename to `procybernetica` only if packaging/release work begins. Do not block v0 conformance docs on package naming.

## Schema changes still safe after estate maps

Only these schema-level changes are safe before adapter fixtures land:

1. Add optional `external_refs` style fields only if they are generic and do not encode upstream-specific schemas.
2. Add examples under `examples/integrations/*` referencing upstream artifact IDs.
3. Add documentation links from existing schemas to upstream maps.
4. Add public conformance checks that require references, not duplicated payloads.

Avoid adding new large schema families until adapter backlog and conformance plan complete.

## Recommended next-turn profile work

Turn 11 should update profiles, not schemas:

- add alias metadata to `controlplane_state_machine.yaml`;
- clarify `promotion_policy.example.yaml` against accepted decision values;
- ensure BT profile points to AgentPlane/SourceOS execution evidence rather than implementing BT runtime;
- ensure K3 profile references HolographMe and future domain-object refs without cloning domain schemas.

## Updated follow-up issues

1. Keep issue #6 open for remaining schema cleanup, but narrow it to fixtures/docs rather than new schema families.
2. Keep issue #7 open for profile alias and invariant normalization.
3. Keep issue #8 open for practicum validation/report flow only.
4. Use mapping follow-up issues #15, #16, #17 and adapter backlog later for integration fixtures.
5. Do not open more schema-family issues until Turn 12 adapter backlog.

## Current recommendation

The v0 schema surface is now sufficient for public review once profile reconciliation, adapter backlog, and conformance docs land.

Do not continue expanding schemas. Move to profiles, conformance, adapter refs, and public review checklist.
