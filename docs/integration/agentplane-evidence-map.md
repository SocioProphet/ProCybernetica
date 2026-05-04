# AgentPlane Evidence Map

Status: initial integration map

Turn: 2 / 20

Related issue: #9

## Purpose

This document maps ProCybernetica v0 contracts to `SocioProphet/agentplane` evidence artifacts and receipt lifecycle surfaces.

The goal is to prevent duplication. AgentPlane already owns governed execution, placement, run evidence, replay artifacts, promotion/reversal artifacts, session records, and receipt assembly. ProCybernetica owns the public constitutional semantics, envelope vocabulary, conformance expectations, and reference-kit posture.

## Source basis

Primary AgentPlane sources checked:

- `SocioProphet/agentplane/README.md`
- `SocioProphet/agentplane/schemas/README.md`
- `SocioProphet/agentplane/docs/receipt-lifecycle.md`
- `SocioProphet/agentplane/docs/agentic-pr-control-plane-v0.md`

Primary ProCybernetica sources:

- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
- `docs/decisions/0002-v0-contract-scope.md`
- `schemas/`

## Ownership boundary

| Surface | AgentPlane owns | ProCybernetica owns |
| --- | --- | --- |
| Execution unit | Bundle, BrokerExecutionBundle, executor inventory, runner backends | Constitutional interpretation of execution as Fractal Node process |
| Validation | Bundle validation and ValidationArtifact-style evidence | Public validation-envelope semantics and conformance rules |
| Placement | PlacementDecision and executor selection | Authority / value-judgment semantics for placement decision evidence |
| Run | RunArtifact, runtime execution evidence, status, exit code | Artifact and event semantics for consequential execution |
| Replay | ReplayArtifact and deterministic replay input bundle | ReplayEnvelope and replay-law semantics |
| Promotion | PromotionArtifact and ReversalArtifact | PromotionDecision, lawful-learning, promotion/quarantine semantics |
| Session | SessionArtifact, session lifecycle refs | Node lifecycle / state transition / policy semantics |
| Receipt | MAIPJ run receipt assembly from normalized event stream | Constitutional interpretation of receipt as evidence and replay law |
| Agentic PR lifecycle | AgenticPRWorkOrder and evidence-producing PR control lifecycle | Repository/process/agent node doctrine and merge/promotion law |

## Direct schema/artifact mapping

| ProCybernetica contract | AgentPlane surface | Mapping note |
| --- | --- | --- |
| `NodeDescriptor` | Bundle metadata, Executor, SessionArtifact, Agent Machine binding | A bundle executor or agent session can be represented as a ProCybernetica node, but AgentPlane owns the concrete execution identity and artifact schema. |
| `ArtifactEnvelope` | RunArtifact, ReplayArtifact, PromotionArtifact, ReversalArtifact, SessionArtifact, specialized evidence artifacts | ProCybernetica `ArtifactEnvelope` is the public outer evidence classification. AgentPlane artifact schemas are concrete execution evidence payloads. |
| `CommandEnvelope` | Bundle execution request, AgenticPRWorkOrder, runner invocation | ProCybernetica command semantics can wrap or reference AgentPlane work orders, but must not replace their schema. |
| `DelegationEnvelope` | AgenticPRWorkOrder, issue-to-task lifecycle, session policy refs | Delegation maps to bounded issue/work-order execution authority. |
| `CapabilityDescriptor` | Bundle backend intent, executor, tool surfaces, native assistant / model route / network evidence surfaces | CapabilityDescriptor describes the constitutional capability. AgentPlane owns executor/tool-specific evidence. |
| `TraceEvent` / `EventEnvelope` | MAIPJ receipt event stream | ProCybernetica events should be compatible with AgentPlane receipt event requirements and trace IDs. |
| `TransitionRecord` | SessionArtifact status changes, agentic PR lifecycle transitions | TransitionRecord captures constitutional lifecycle evidence; AgentPlane owns session/PR lifecycle artifacts. |
| `ReplayEnvelope` | ReplayArtifact | ReplayEnvelope is constitutional replay manifest; ReplayArtifact is AgentPlane’s concrete replay input record. |
| `EvaluationResult` | ValidationArtifact, RunArtifact status, ReplayArtifact validation, benchmark/eval records | EvaluationResult can summarize or reference AgentPlane validation/run/replay outcomes. |
| `PromotionDecision` | PromotionArtifact, ReversalArtifact | PromotionDecision is the constitutional verdict; AgentPlane promotion/reversal artifacts are execution-plane evidence. |
| `IncidentReport` | failed run evidence, reversal artifact, session status, receipt assembly failure | IncidentReport should reference AgentPlane artifacts rather than duplicate them. |
| `ProvenanceRecord` | receipt evidence block, artifact digests, replay manifest refs | ProCybernetica provenance can point to AgentPlane sealed evidence and receipts. |

## AgentPlane artifact inventory relevant to ProCybernetica

From AgentPlane schema/docs, current public evidence types include:

- `ValidationArtifact`
- `PlacementDecision`
- `RunArtifact`
- `ReplayArtifact`
- `PromotionArtifact`
- `ReversalArtifact`
- `SessionArtifact`
- `AgentMachineMountEvidence`
- `OfficeArtifactEvidence`
- `NetworkDoorPlanEvidence`
- `ExternalModelProviderRouteEvidence`
- `NativeAssistantBridgeEvidence`

ProCybernetica should not recreate those schemas unless a narrow constitutional wrapper is required. The preferred pattern is reference-by-URI/hash/digest plus ProCybernetica-level interpretation.

## Receipt lifecycle mapping

AgentPlane receipt assembly uses a normalized event stream and is fail-closed when required events are missing.

Required AgentPlane receipt events:

- `workspace.locked`
- `context.pack.selected`
- `context.pack.fetched`
- `policy.evaluated`
- `placement.selected`
- `run.started`
- `run.completed`
- `evidence.sealed`

ProCybernetica mapping:

| Receipt event | ProCybernetica interpretation |
| --- | --- |
| `workspace.locked` | Node/process admission context and risk class |
| `context.pack.selected` | Memory/context input and policy-scoped observation |
| `context.pack.fetched` | Artifact/context retrieval evidence |
| `policy.evaluated` | PolicyEnvelope evaluation and authority gate |
| `placement.selected` | Value judgment / resource allocation / executor selection |
| `run.started` | TransitionRecord or TraceEvent for execution start |
| `run.completed` | EvaluationResult / ArtifactEnvelope / TraceEvent |
| `evidence.sealed` | ProvenanceRecord, ReplayEnvelope, promotion evidence bundle |

## Agentic PR control plane mapping

AgentPlane’s agentic PR control plane defines this lifecycle:

```text
Issue -> Task Planner -> Repo Snapshot -> Sandbox Runner -> Patch Producer -> Diff Hygiene Gate -> CI Runner -> Review Agent -> PR Publisher -> Merge Gate -> Post-merge Ledger
```

ProCybernetica mapping:

| AgentPlane stage | ProCybernetica concept |
| --- | --- |
| Issue | CommandEnvelope / DelegationEnvelope source |
| Task Planner | Planner node / behavior generation |
| Repo Snapshot | Repository node observation and provenance baseline |
| Sandbox Runner | Executor node with scoped authority |
| Patch Producer | Agent/process node output artifact |
| Diff Hygiene Gate | PolicyEnvelope and EvaluationResult |
| CI Runner | EvaluationResult and TraceEvent |
| Review Agent | Operator/agent node status and review observation |
| PR Publisher | ArtifactEnvelope and repository-side actuation |
| Merge Gate | PromotionDecision |
| Post-merge Ledger | ProvenanceRecord / ReplayEnvelope / receipt refs |

Important rule: ProCybernetica should use this AgentPlane lifecycle as the concrete execution-plane model for repository-as-node governance. Do not define a second unbounded PR-agent lifecycle in ProCybernetica.

## Required adapter posture

A future AgentPlane adapter should not copy AgentPlane artifacts into new ProCybernetica schemas.

It should emit or derive lightweight references:

```json
{
  "artifact_ref": "agentplane://run-artifact/<id>",
  "artifact_kind": "RunArtifact",
  "digest": "sha256:...",
  "procybernetica_contract": "ArtifactEnvelope",
  "provenance_ref": "agentplane://receipt/<id>",
  "replay_ref": "agentplane://replay-artifact/<id>"
}
```

## ProCybernetica schema implications

### Keep

- `ArtifactEnvelope`
- `ReplayEnvelope`
- `EvaluationResult`
- `PromotionDecision`
- `TraceEvent`
- `EventEnvelope`
- `ProvenanceRecord`
- `CapabilityDescriptor`

### Do not expand yet

- Do not add a separate `RunArtifact` schema in ProCybernetica.
- Do not add a separate `PlacementDecision` schema in ProCybernetica.
- Do not add a separate `AgenticPRWorkOrder` schema in ProCybernetica.
- Do not add separate Network/BYOM/native assistant evidence schemas in ProCybernetica.

Those are AgentPlane surfaces.

### Needed bridge later

- `agentplane_artifact_ref.schema.json` or equivalent reference object may be useful if repeated mappings become verbose.
- Adapter fixtures can live under `examples/integrations/agentplane/` after this map stabilizes.

## Open questions

1. Should ProCybernetica v0 add a generic `ExternalEvidenceRef` schema used across AgentPlane, SourceOS, Prophet Platform, and ontogenesis mappings?
2. Should `PromotionDecision` reference AgentPlane `PromotionArtifact` directly through `approval_refs` or a dedicated `evidence_refs` entry?
3. Should AgentPlane MAIPJ receipts become first-class `ArtifactEnvelope` examples in ProCybernetica fixtures?
4. Should issue/PR governance use AgentPlane `AgenticPRWorkOrder` as the only concrete work-order schema?

## Follow-up backlog

- Add `examples/integrations/agentplane/replay_artifact_ref.example.json`.
- Add `examples/integrations/agentplane/promotion_artifact_ref.example.json`.
- Add adapter docs after SourceOS/SociOS and Prophet Platform mappings are complete.
- Consider a generic `ExternalEvidenceRef` only after all estate maps are complete.

## Current conclusion

AgentPlane is the execution evidence plane. ProCybernetica is the constitutional semantics and conformance plane. The correct integration pattern is reference, summarize, and govern AgentPlane artifacts rather than duplicating their schemas.
