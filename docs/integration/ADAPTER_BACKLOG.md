# Adapter Backlog

Status: initial v0 adapter backlog

Turn: 12 / 20

Purpose: convert the completed estate maps into concrete adapter work without moving runtime ownership into ProCybernetica.

## Rule

Adapters in this backlog should reference upstream artifacts. They should not copy or reimplement upstream schemas.

ProCybernetica owns:

- public constitutional interpretation;
- public examples and fixtures;
- conformance expectations;
- mapping docs;
- reference validation behavior.

Upstream repos own their runtime, domain, evidence, and concrete contract surfaces.

## Priority scale

| Priority | Meaning |
| --- | --- |
| P0 | Required for v0 public-review coherence |
| P1 | Important for first implementation wave |
| P2 | Useful after v0 conformance and public review |

## P0 adapters

### 1. AgentPlane evidence refs

| Field | Value |
| --- | --- |
| Owner repo | `SocioProphet/agentplane` |
| ProCybernetica map | `docs/integration/agentplane-evidence-map.md` |
| Upstream artifacts | RunArtifact, ReplayArtifact, PromotionArtifact, ReversalArtifact, SessionArtifact, PlacementDecision, specialized evidence artifacts |
| ProCybernetica contracts | ArtifactEnvelope, ReplayEnvelope, EvaluationResult, PromotionDecision, ProvenanceRecord, TraceEvent |
| Fixture path | `examples/integrations/agentplane/` |
| Priority | P0 |

Deliver fixtures:

- `replay_artifact_ref.example.json`
- `promotion_artifact_ref.example.json`
- `run_receipt_ref.example.json`

Acceptance:

- fixtures reference AgentPlane artifacts by URI/ref/digest;
- no AgentPlane schema clones;
- fixtures validate through ProCybernetica wrapper or generic reference shape once added.

### 2. semantic-serdes / SHIR semantic refs

| Field | Value |
| --- | --- |
| Owner repos | `SocioProphet/semantic-serdes`, `SocioProphet/ontogenesis` |
| ProCybernetica map | `docs/integration/semantic-serdes-shir-map.md` |
| Upstream artifacts | SemanticCell, SurfaceProjection, SHIR CandidateAssertion, Assertion, ProjectionLossReport, Receipt |
| ProCybernetica contracts | Claim, EventEnvelope, TraceEvent, ObservationEnvelope, ReplayEnvelope, ProvenanceRecord |
| Fixture path | `examples/integrations/semantic-serdes/` |
| Priority | P0 |

Deliver fixtures:

- `claim_to_shir_candidate_assertion.example.json`
- `dashboard_surface_projection_ref.example.json`
- `replay_to_shir_receipt_ref.example.json`

Acceptance:

- fixtures explain truth-class and claim-status mapping;
- dashboard payloads are treated as surface projections;
- SHIR receipts/projection-loss reports are referenced, not cloned.

### 3. Ontogenesis validation and release refs

| Field | Value |
| --- | --- |
| Owner repo | `SocioProphet/ontogenesis` |
| ProCybernetica map | `docs/integration/ontogenesis-governance-map.md` |
| Upstream artifacts | SHACL reports, dist manifests, ledgers, signatures, SBOMs, module registry entries |
| ProCybernetica contracts | Claim, ProvenanceRecord, ArtifactEnvelope, EvaluationResult, PromotionDecision |
| Fixture path | `examples/integrations/ontogenesis/` |
| Priority | P0 |

Deliver fixtures:

- `claim_shacl_gate_ref.example.json`
- `ontology_release_evidence_ref.example.json`

Acceptance:

- validated claims reference ontology and validation evidence;
- no SHACL/ledger/SBOM schema clones;
- public claim examples preserve validation/provenance boundary.

### 4. SourceOS/SociOS contract refs

| Field | Value |
| --- | --- |
| Owner repos | `SourceOS-Linux/sourceos-spec`, `SociOS-Linux/workstation-contracts`, `SourceOS-Linux/agent-machine`, `SociOS-Linux/source-os` |
| ProCybernetica map | `docs/integration/sourceos-socios-contract-map.md` |
| Upstream artifacts | SourceOS EventEnvelope, PolicyDecision, CapabilityToken, ProvenanceRecord, RunRecord, AgentSession, BootProofRecord, ReleaseReceipt, WorkstationProfile, ActivationDecision |
| ProCybernetica contracts | NodeDescriptor, PolicyEnvelope, DelegationEnvelope, ArtifactEnvelope, ReplayEnvelope, EvaluationResult, PromotionDecision |
| Fixture path | `examples/integrations/sourceos/` |
| Priority | P0 |

Deliver fixtures:

- `sourceos_event_ref.example.json`
- `boot_proof_artifact_ref.example.json`
- `agent_machine_activation_ref.example.json`

Acceptance:

- fixtures reference SourceOS/SociOS records by URN/ref;
- no SourceOS schema clones;
- boot/release/workstation/agent-machine evidence is represented as external evidence.

### 5. Prophet Platform evidence refs

| Field | Value |
| --- | --- |
| Owner repo | `SocioProphet/prophet-platform` |
| ProCybernetica map | `docs/integration/prophet-platform-record-map.md` |
| Upstream artifacts | EventEnvelope, EvidenceReceipt, MembraneDecision, FogStack readiness record, eval-fabric run record, Office runtime records |
| ProCybernetica contracts | ArtifactEnvelope, ProvenanceRecord, ReplayEnvelope, EvaluationResult, PromotionDecision, PolicyEnvelope |
| Fixture path | `examples/integrations/prophet-platform/` |
| Priority | P0 |

Deliver fixtures:

- `evidence_receipt_ref.example.json`
- `fogstack_readiness_ref.example.json`
- `eval_fabric_run_ref.example.json`

Acceptance:

- fixtures make platform runtime ownership explicit;
- ProCybernetica only interprets platform evidence constitutionally;
- no platform contract clones.

## P1 adapters

### 6. HolographMe Genesis/Inception refs

| Field | Value |
| --- | --- |
| Owner repo | `SocioProphet/HolographMe` |
| ProCybernetica map | `docs/integration/holographme-genesis-inception-map.md` |
| Upstream artifacts | HumanDigitalTwin, ConsentPolicy, Mission, projection, transition receipt |
| ProCybernetica contracts | PolicyEnvelope, DelegationEnvelope, CapabilityDescriptor, Claim, ArtifactEnvelope, ProvenanceRecord, ReplayEnvelope, PromotionDecision, K3 profile |
| Fixture path | `examples/integrations/holographme/` |
| Priority | P1 |

Deliver fixtures:

- `twin_ref.example.json`
- `projection_receipt_ref.example.json`
- `k3_holographme_transition_ref.example.json`

Acceptance:

- fixtures use domain object refs;
- no HolographMe schema clones;
- K3 profile is shown as lifecycle interpretation layer.

### 7. Foundry/model governance refs

| Field | Value |
| --- | --- |
| Owner repos | `functional-model-surfaces`, `model-router`, `model-governance-ledger`, `guardrail-fabric`, `sourceos-model-carry` |
| ProCybernetica map | `docs/integration/foundry-model-governance-map.md` |
| Upstream artifacts | functional service manifest, route binding, governance ledger record, guardrail decision, model carry profile |
| ProCybernetica contracts | EvaluationResult, PromotionDecision, PolicyEnvelope, CapabilityDescriptor, ArtifactEnvelope, ProvenanceRecord, ReplayEnvelope |
| Fixture path | `examples/integrations/foundry/` |
| Priority | P1 |

Deliver fixtures:

- `functional_service_ref.example.json`
- `route_decision_ref.example.json`
- `model_governance_promotion_ref.example.json`
- `guardrail_decision_ref.example.json`

Acceptance:

- fixtures preserve repo ownership;
- route/governance/guardrail/carry objects remain upstream;
- ProCybernetica shows lawful-learning interpretation.

### 8. Workstation/operator surface refs

| Field | Value |
| --- | --- |
| Owner repos | `source-os`, `workstation-contracts`, `agent-term`, `TurtleTerm`, `BearBrowser`, product UI repos |
| ProCybernetica map | `docs/integration/workstation-operator-surface-map.md` |
| Upstream artifacts | AgentTerm event, TurtleTerm receipt, BearBrowser event/history evidence, workstation conformance result, UI dashboard projection |
| ProCybernetica contracts | NodeDescriptor, CommandEnvelope, DelegationEnvelope, CapabilityDescriptor, EventEnvelope, ArtifactEnvelope, ReplayEnvelope, EvaluationResult |
| Fixture path | `examples/integrations/operator/` |
| Priority | P1 |

Deliver fixtures:

- `agentterm_event_ref.example.json`
- `turtleterm_receipt_ref.example.json`
- `bearbrowser_event_ref.example.json`
- `workstation_conformance_ref.example.json`

Acceptance:

- fixtures model operator/gateway node evidence;
- no terminal/browser/UI runtime schemas are duplicated;
- approval and replay posture are visible.

## P2 adapters

### 9. Generic ExternalEvidenceRef

| Field | Value |
| --- | --- |
| Owner repo | ProCybernetica |
| Depends on | P0 and P1 fixture patterns |
| Proposed contract | `external_evidence_ref.schema.json` or embedded object pattern |
| Priority | P2 |

Decision rule:

Do not add this schema until at least three adapter fixture families demonstrate repeated structure. If repeated fields stabilize, add a generic reference object with:

- `source_repo`
- `contract_kind`
- `external_ref`
- `digest`
- `version`
- `procybernetica_contract`
- `public_release_state`
- `notes`

### 10. Full scoring/dashboard publication adapter

| Field | Value |
| --- | --- |
| Owner repos | ProCybernetica plus platform/eval fabric as applicable |
| Depends on | scoring/dashboard publication plan, platform eval-fabric map |
| Priority | P2 |

Deliver:

- full public or sanitized scoring bodies;
- dashboard export payload schema or semantic-serdes surface projection mapping;
- validation checks for full row counts.

## Issue fanout plan

After Turn 12:

- Create adapter fixture issues for P0 groups if not already covered.
- Keep P1/P2 as backlog until public conformance plan lands.
- Do not create schema-family issues for upstream-owned contracts.

## v0 stop criteria for adapter backlog

For the 20-turn stop point, adapter backlog is sufficient when:

1. This document exists.
2. P0/P1 adapter families are named with owner repo and fixture path.
3. Downstream issues exist for P0 adapter fixtures.
4. `SCHEMA_PROFILE_RECONCILIATION.md` says no more schema expansion before adapter refs/conformance.

## Current conclusion

The next work is not more schemas. It is public adapter fixtures and conformance checks that prove ProCybernetica can reference the estate cleanly without absorbing upstream ownership.
