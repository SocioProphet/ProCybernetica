# Prophet Platform Record Map

Status: initial integration map

Turn: 6 / 20

Related issue: #12

## Purpose

This document maps ProCybernetica v0 contracts to `SocioProphet/prophet-platform` runtime, FogStack, identity, office runtime, evaluation, and evidence records.

The goal is to prevent ProCybernetica from becoming a second runtime/deployment hub. Prophet Platform owns concrete runtime services, deployment wiring, platform contracts, datastores, eval-fabric APIs, FogStack parity records, and platform evidence receipts.

ProCybernetica owns the public constitutional semantics, conformance law, schema/profile interpretation, and reference-kit posture.

## Source basis

Primary Prophet Platform sources checked:

- `SocioProphet/prophet-platform/README.md`
- `SocioProphet/prophet-platform/docs/PLATFORM_EVAL_FABRIC.md`
- `SocioProphet/prophet-platform/docs/FOGSTACK_PACKS.md`
- `SocioProphet/prophet-platform/contracts/README.md`
- `SocioProphet/prophet-platform/adr/ADR-033-canonical-receipts-and-event-envelopes.md`

Primary ProCybernetica sources:

- `docs/integration/ESTATE_ALIGNMENT_AUDIT.md`
- `docs/integration/RECENT_CONTRIBUTION_ALIGNMENT.md`
- `docs/decisions/0002-v0-contract-scope.md`
- `schemas/`

## Ownership boundary

| Surface | Prophet Platform owns | ProCybernetica owns |
| --- | --- | --- |
| Runtime hub | deployable services in `apps/`, gateway/API/search/execution services | constitutional interpretation of runtime records |
| Platform contracts | repo-local platform-facing event/evidence/receipt contracts in `contracts/` | mapping to public constitutional envelopes and conformance expectations |
| Deployment | `infra/`, Kustomize, ArgoCD, namespaces, local/cluster wiring | public integration law, not deployment implementation |
| Evaluation fabric | score schemas, local/cluster wiring, datastores, API routes, dashboard inputs | scoring doctrine, promotion law, replay/evidence interpretation |
| FogStack | product pack catalog, parity readiness record, local evidence graph, pack maturity | constitutional classification and evidence mapping |
| Evidence receipts | `EvidenceReceipt`, `EventEnvelope`, `MembraneDecision`, platform domain events | `ArtifactEnvelope`, `TraceEvent`, `EventEnvelope`, `ProvenanceRecord`, `ReplayEnvelope`, `EvaluationResult` semantics |
| Office runtime | office runtime records, WOPI/open office boundaries, workspace execution surfaces | capability/policy/evidence interpretation |
| AgentPlane/PolicyPlane linkage | platform-side integration links and runtime readiness records | constitutional integration requirements and non-duplication rule |

## Platform contracts mapping

Prophet Platform contracts currently include:

- `CarrierIngested`
- `EventEnvelope`
- `MembraneDecision`
- `EvidenceReceipt`
- `TopicAssigned`
- `EmbeddingComputed`
- `LensOutput`
- `ExportApproved`
- `ExportDenied`

ADR-033 establishes the platform rule:

- every runtime service emits an `EventEnvelope`;
- every materially completed action emits an `EvidenceReceipt`;
- policy/membrane services emit `MembraneDecision`;
- service-specific events reference canonical receipts.

ProCybernetica mapping:

| Platform contract | ProCybernetica analogue | Mapping decision |
| --- | --- | --- |
| `EventEnvelope` | `EventEnvelope` / `TraceEvent` | Platform owns concrete runtime event envelope. ProCybernetica uses event semantics for replay/control interpretation. |
| `EvidenceReceipt` | `ArtifactEnvelope` / `ProvenanceRecord` | EvidenceReceipt should be referenced as public evidence, not duplicated. |
| `MembraneDecision` | `PolicyEnvelope` / `EvaluationResult` / `PromotionDecision` | Membrane decisions are policy evidence and may inform promotion/quarantine verdicts. |
| `CarrierIngested` | `ObservationEnvelope` / `ArtifactEnvelope` | Ingest events are observations/artifacts in ProCybernetica terms. |
| `TopicAssigned` | `EventEnvelope` / repository node event | Topic assignment is event evidence for routing/indexing. |
| `EmbeddingComputed` | `ArtifactEnvelope` / `ProvenanceRecord` | Embeddings are derived artifacts; retain provenance and replay refs. |
| `LensOutput` | `ArtifactEnvelope` / dashboard or surface projection | Lens outputs are derived artifacts/surfaces. |
| `ExportApproved` | `PromotionDecision` or policy/evaluation evidence | Export approval is a policy-promotion decision input. |
| `ExportDenied` | `PromotionDecision` / IncidentReport if material | Export denial is governance evidence; not necessarily an incident. |

## Evaluation fabric mapping

Prophet Platform eval fabric owns:

- metric and score schemas used by platform services;
- local and cluster datastore wiring;
- API surfaces for dashboards;
- replay/provenance hooks;
- ranking logic for internal decision support;
- frontier, dossier, radar, and health routes.

ProCybernetica mapping:

| Eval fabric object | ProCybernetica surface |
| --- | --- |
| metric definition | scoring methodology / future scoring schema docs |
| metric fact | `ArtifactEnvelope` or evaluation fact evidence |
| context slice | `ObservationEnvelope` / semantic-serdes context / SHIR refs |
| eval run | `EvaluationResult` plus `ReplayEnvelope` refs |
| competitor snapshot | `ArtifactEnvelope` / scoring evidence row |
| profile score | scoring/dashboard public payload |
| replay artifact | `ReplayEnvelope` / `ProvenanceRecord` refs |
| dashboard route | public surface projection |

Rule: Platform eval fabric owns executable ranking, API, datastore, and dashboard wiring. ProCybernetica owns the scoring doctrine, public trust posture, and promotion/replay interpretation.

## FogStack mapping

FogStack parity readiness is currently platform-owned and local MVP, not production parity.

Prophet Platform FogStack docs say the local evidence graph proves:

- release;
- registry;
- deploy;
- GitOps;
- runtime dry-run;
- Agent Machine node inventory;
- immutable/declarative update readiness;
- TurtleTerm / BearBrowser use surfaces;
- AgentPlane run linkage;
- PolicyPlane decision linkage;
- one-command parity validation.

ProCybernetica mapping:

| FogStack evidence category | ProCybernetica interpretation |
| --- | --- |
| release evidence | `ArtifactEnvelope`, `ProvenanceRecord`, `PromotionDecision` |
| registry evidence | repository node / artifact-store node evidence |
| deploy evidence | `ReplayEnvelope`, `EvaluationResult`, transition evidence |
| GitOps evidence | repository/process node provenance |
| runtime dry-run | `EvaluationResult` / `CapabilityDescriptor` evidence |
| Agent Machine inventory | `NodeDescriptor` refs / SourceOS adapter evidence |
| immutable update readiness | SourceOS boot/release evidence refs |
| TurtleTerm/BearBrowser surface evidence | operator/gateway node evidence |
| AgentPlane linkage | AgentPlane evidence map refs |
| PolicyPlane linkage | policy/evaluation evidence refs |
| parity readiness record | `ArtifactEnvelope` / `EvaluationResult` summary |

Rule: ProCybernetica should not split FogStack packs or define FogStack runtime. It should interpret FogStack readiness records as evidence for constitutional claims.

## Identity and trust mapping

Recent platform work includes identity and platform standards locking. ProCybernetica should treat these as runtime identity/evidence inputs, not as a reason to invent identity services.

Mapping:

| Platform identity/trust record | ProCybernetica surface |
| --- | --- |
| identity contract schema/example | `NodeDescriptor`, `PolicyEnvelope`, Genesis/Inception backlog |
| identity standards lock | `ProvenanceRecord` / `ArtifactEnvelope` evidence |
| runtime identity check | `EvaluationResult` / `TraceEvent` evidence |
| trust/release graph | `ReplayEnvelope` / `PromotionDecision` evidence input |

## Office runtime mapping

Platform office/runtime records and WOPI/open office boundaries should map as follows:

| Platform office runtime surface | ProCybernetica surface |
| --- | --- |
| office artifact generation | `ArtifactEnvelope` |
| inspection/conversion/review | `EvaluationResult` / `ArtifactEnvelope` |
| send/publish/calendar-style side effect | `CommandEnvelope`, `CapabilityDescriptor`, `PolicyEnvelope`, `PromotionDecision` |
| runtime boundary record | `ProvenanceRecord` / `TraceEvent` |
| OfficeArtifactEvidence via AgentPlane | AgentPlane evidence reference |

Rule: ProCybernetica should define side-effect and promotion law, not implement office runtime.

## Platform/runtime non-duplication rules

Do not add the following to ProCybernetica v0:

- Platform `EvidenceReceipt` clone.
- Platform datastore schemas for Postgres/ClickHouse eval fabric.
- FogStack pack schemas.
- Platform runtime dry-run record schema.
- Office runtime record schema.
- Platform API route contracts.
- Platform deployment/Kustomize/ArgoCD contracts.
- Identity service contracts already owned by platform/standards surfaces.

Keep in ProCybernetica:

- public constitutional interpretation;
- envelope semantics;
- promotion/replay law;
- scoring doctrine;
- conformance expectations;
- adapter references.

## Required adapter posture

Future platform adapter refs should look like:

```json
{
  "artifact_ref": "prophet-platform://evidence-receipt/<id>",
  "contract_kind": "EvidenceReceipt",
  "event_ref": "prophet-platform://event/<id>",
  "procybernetica_contract": "ArtifactEnvelope",
  "replay_ref": "prophet-platform://eval-run/<id>",
  "policy_ref": "prophet-platform://membrane-decision/<id>"
}
```

Do not copy complete platform records into ProCybernetica unless creating public synthetic fixtures.

## Open questions

1. Should ProCybernetica define `ExternalEvidenceRef` after all estate maps complete?
2. Should platform `EvidenceReceipt` become the canonical concrete evidence object for Prophet Platform adapters?
3. Should `EvaluationResult` include explicit platform eval-fabric run refs?
4. Should FogStack parity readiness record become a public ProCybernetica scoring/evidence example?
5. Should platform `MembraneDecision` be treated as policy evidence or promotion evidence in v0.1?

## Follow-up backlog

- Add `examples/integrations/prophet-platform/evidence_receipt_ref.example.json` after all maps complete.
- Add scoring/dashboard bridge to platform eval fabric after conformance plan lands.
- Add FogStack readiness record fixture if public-safe.
- Revisit `PromotionDecision` after PolicyPlane and Prophet Platform mappings are both reviewed.

## Current conclusion

Prophet Platform is the runtime and deployment hub. ProCybernetica should not become a platform runtime or eval service. The right integration is to reference platform event/evidence/receipt records and interpret them through ProCybernetica constitutional law, replay law, scoring law, and public conformance expectations.
