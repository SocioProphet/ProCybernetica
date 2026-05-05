# SourceOS / SociOS Contract Map

Status: initial integration map

Turn: 5 / 20

Related issue: #11

## Purpose

This document maps ProCybernetica v0 schemas and evidence semantics to the active SourceOS/SociOS typed contract estate.

The goal is to prevent ProCybernetica from duplicating lower-level execution, provenance, policy, agent-plane, boot, workstation, and conformance contracts that are already owned by SourceOS-Linux and SociOS-Linux repositories.

ProCybernetica owns public constitutional semantics, replay/promotion law, node doctrine, and conformance interpretation.

SourceOS/SociOS repositories own typed runtime, host, workstation, boot, agent-machine, and conformance contracts.

## Source basis

Primary upstream sources checked:

- `SourceOS-Linux/sourceos-spec/README.md`
- `SourceOS-Linux/sourceos-spec/schemas/README.md`
- `SociOS-Linux/workstation-contracts/README.md`
- `SourceOS-Linux/agent-machine/README.md`

Recent contribution stream accounted for:

- SourceOS `ShellReceiptEvent`, `OpsHistoryEvent`, `OpsHistoryContextPackRef`, `RedactionTombstone`, `LocalFirstServiceManifest`, `BearHistoryEvent`, `BearHistorySyncPolicy` work.
- SociOS workstation/office conformance fixtures and installed command smoke paths.
- Agent Machine release evidence bundle, strict digest/provenance gate, policy/grant hardening, AgentTerm/TopoLVM/Policy Fabric stubs, and runtime evidence work.

## Ownership boundary

| Surface | SourceOS/SociOS owns | ProCybernetica owns |
| --- | --- | --- |
| Canonical typed contracts | `sourceos-spec` schemas, OpenAPI/AsyncAPI fragments, JSON-LD/Hydra overlay | Cybernetic interpretation and public conformance expectations |
| Policy and grants | SourceOS `Policy`, `PolicyDecision`, `CapabilityToken`, obligations, exceptions | PolicyEnvelope as constitutional summary/reference surface |
| Execution/provenance | `RunRecord`, `WorkflowSpec`, `WorkloadSpec`, `ProvenanceRecord`, `EventEnvelope`, `MappingSpec` | Replay, promotion, node, and evidence law over those records |
| Agent plane contracts | `AgentSession`, `ExecutionDecision`, `ExecutionSurface`, `SkillManifest`, `MemoryEntry`, `SessionReceipt`, `TelemetryEvent` | Agent node doctrine and authority/promotion semantics |
| Boot/release | `ReleaseSet`, `BootProofRecord`, `ReleaseReceipt`, `GitRefBuild`, `Fingerprint`, `ConfigSource` | Boot/update receipts as evidence in ArtifactEnvelope/ProvenanceRecord/ReplayEnvelope |
| Workstation/desktop | `WorkstationProfile`, `DesktopProfile`, launcher/package/validation surfaces | Operator/gateway node interpretation and conformance expectations |
| Workstation conformance | `workstation-contracts` fixtures and validators | References to conformance evidence; no duplicate runner |
| Agent Machine runtime | Agent Machine node substrate, AgentPod, provider lifecycle, receipts, activation decisions | Host/process/executor node semantics and evidence interpretation |
| Browser/terminal operator surfaces | BearBrowser, TurtleTerm, agent-term, source-os shell/operator flows | Gateway/operator node doctrine and public evidence expectations |

## Direct contract mapping

| ProCybernetica schema | SourceOS/SociOS surface | Mapping decision |
| --- | --- | --- |
| `NodeDescriptor` | `AgentSession`, `ExecutionSurface`, `WorkstationProfile`, `DesktopProfile`, Agent Machine node/profile concepts | ProCybernetica node describes constitutional role. SourceOS/SociOS contracts describe concrete runtime/host/workstation state. |
| `PolicyEnvelope` | `Policy`, `Rule`, `PolicyDecision`, `CapabilityToken`, `Obligation`, `Exception` | ProCybernetica should reference SourceOS policy objects; do not redefine policy language. |
| `CommandEnvelope` | `WorkOrder`, `WorkflowSpec`, `LauncherAction`, agent/session commands | CommandEnvelope is constitutional command wrapper; concrete execution commands live upstream. |
| `DelegationEnvelope` | `CapabilityToken`, `WorkOrder`, `AgentSession`, agent grant surfaces | Delegation should reference SourceOS token/grant/session records where applicable. |
| `CapabilityDescriptor` | `SkillManifest`, `ExecutionSurface`, `LauncherProvider`, Agent Machine provider/capability contracts | Do not duplicate provider/runtime schema; use CapabilityDescriptor as high-level capability statement. |
| `EventEnvelope` / `TraceEvent` | SourceOS `EventEnvelope`, `TelemetryEvent`, `ShellReceiptEvent`, `OpsHistoryEvent`, `BearHistoryEvent` | SourceOS owns concrete event contracts; ProCybernetica interprets them for replay/promotion/control loops. |
| `ProvenanceRecord` | SourceOS `ProvenanceRecord`, `GitRefBuild`, release evidence, state-integrity records | Prefer upstream provenance records; ProCybernetica can summarize or reference. |
| `ArtifactEnvelope` | `ReleaseReceipt`, `BootProofRecord`, `ArtifactCacheRecord`, `SessionReceipt`, Agent Machine release evidence bundle | Wrap/reference SourceOS artifacts as evidence; do not clone all record shapes. |
| `ReplayEnvelope` | `RunRecord`, `SessionReceipt`, `BootProofRecord`, OpsHistory/TopicEnvelope records | ReplayEnvelope points to upstream evidence needed for reconstruction. |
| `EvaluationResult` | SourceOS validation records, workstation conformance results, Agent Machine activation decisions | EvaluationResult may summarize validation outcomes. |
| `PromotionDecision` | release gate results, policy decisions, activation decisions, rollout policies | PromotionDecision is ProCybernetica constitutional verdict over upstream evidence. |
| `IncidentReport` | FrustrationSignal, failed run/session receipts, redaction tombstones, repair/rollback evidence | IncidentReport references upstream events; do not duplicate raw operational logs. |

## SourceOS typed contract families and ProCybernetica role

### Governance

SourceOS governance schemas include `Policy`, `Rule`, `PolicyDecision`, `CapabilityToken`, `Obligation`, and `Exception`.

ProCybernetica role:

- reference these records from `PolicyEnvelope` and `DelegationEnvelope`;
- use them as evidence for promotion/actuation decisions;
- avoid defining an alternate policy language in this repo.

### Execution / provenance

SourceOS execution/provenance schemas include `RunRecord`, `WorkflowSpec`, `WorkloadSpec`, `ProvenanceRecord`, `EventEnvelope`, and `MappingSpec`.

ProCybernetica role:

- use these as concrete execution evidence;
- map them to `TraceEvent`, `ReplayEnvelope`, `EvaluationResult`, and `ProvenanceRecord` where needed;
- keep constitutional semantics separate from runtime contract ownership.

### Agent plane

SourceOS agent-plane schemas include `AgentSession`, `ExecutionDecision`, `ExecutionSurface`, `SkillManifest`, `MemoryEntry`, `SessionReceipt`, `SessionReview`, `TelemetryEvent`, and `FrustrationSignal`.

ProCybernetica role:

- map agent sessions to `NodeDescriptor` or `TransitionRecord` when they are cybernetic nodes;
- map execution decisions to `EvaluationResult` / `PolicyEnvelope` evidence;
- map session receipts to `ArtifactEnvelope` and `ReplayEnvelope` refs.

### Release / boot / experiments

SourceOS release/boot schemas include `ReleaseSet`, `BootProofRecord`, `ReleaseReceipt`, `GitRefBuild`, `Fingerprint`, `ConfigSource`, `NLBootPlan`, and rollout/experiment records.

ProCybernetica role:

- treat these as boot/update/release evidence;
- use them in `ArtifactEnvelope`, `ProvenanceRecord`, `ReplayEnvelope`, and `PromotionDecision`;
- do not implement boot verification or release-set logic in ProCybernetica.

### Workstation and desktop

SourceOS/SociOS workstation schemas include launcher, desktop, package, workstation profile, and conformance surfaces.

ProCybernetica role:

- map workstation profiles to operator/gateway/host node embodiments;
- consume conformance outputs as evidence;
- avoid becoming a workstation runner or shell implementation.

### Fog layer

SourceOS fog-layer schemas include topics, topic envelopes, content refs, replication policy, offers, work orders, usage receipts, and settlement events.

ProCybernetica role:

- treat append-only fog events and receipts as evidence sources;
- map usage receipts and work orders into `ArtifactEnvelope` / `ReplayEnvelope` / `EvaluationResult` as needed;
- leave fog compute/vault runtime to SourceOS/Prophet Platform owners.

## Workstation-contracts mapping

`SociOS-Linux/workstation-contracts` is the workstation/CI contract and conformance lane.

It explicitly owns:

- contract validation;
- conformance fixtures;
- Pixi-first backend adapters;
- Agent Machine and Office Plane dry-run behavior checks;
- IPC v0 reference harness for conformance;
- semantic validation for scoped mounts, raw database boundaries, and evidence emission.

ProCybernetica role:

- reference these conformance outputs as `EvaluationResult` evidence;
- model the runner/adapter as process/executor nodes only at constitutional level;
- do not implement workstation contract runner inside this repo.

## Agent Machine mapping

`SourceOS-Linux/agent-machine` owns the Linux-first node substrate for local and clustered agent execution.

Important Agent Machine objects:

- `AgentMachine`
- `AgentPod`
- `InferenceProvider`
- `CacheTier`
- `StorageReceipt`
- `PolicyAdmission`
- `AgentRegistryGrant`
- `AgentPlaneRuntimeEvidence`
- `ActivationDecision`

ProCybernetica mapping:

| Agent Machine object | ProCybernetica analogue |
| --- | --- |
| `AgentMachine` | host/service/process `NodeDescriptor` embodiment |
| `AgentPod` | process/executor node or Workload evidence |
| `InferenceProvider` | `CapabilityDescriptor` and policy-scoped execution capability |
| `CacheTier` | memory/resource model reference |
| `StorageReceipt` | `ArtifactEnvelope` / `ProvenanceRecord` evidence |
| `PolicyAdmission` | `PolicyEnvelope` / `EvaluationResult` evidence |
| `AgentRegistryGrant` | `DelegationEnvelope` / authority grant reference |
| `AgentPlaneRuntimeEvidence` | `ArtifactEnvelope` / `TraceEvent` evidence |
| `ActivationDecision` | `PromotionDecision` or `EvaluationResult` depending on decision semantics |

## Recent SourceOS/SociOS additions ProCybernetica must account for

### sourceos-spec

Recent contracts that matter:

- `ShellReceiptEvent`
- `OpsHistoryEvent`
- `OpsHistoryContextPackRef`
- `RedactionTombstone`
- `LocalFirstServiceManifest`
- `BearHistoryEvent`
- `BearHistorySyncPolicy`

Implication:

- ProCybernetica event, replay, redaction, publication, and evidence docs should reference these as upstream surfaces.
- Do not invent separate shell/browser/history event shapes in ProCybernetica.

### BearBrowser / BearHistory

Recent BearBrowser work adds browser history events, sync policy, validation workflows, local-first design, and packaging/build readiness helpers.

Implication:

- Browser history and browser activity should flow through SourceOS/BearBrowser contract surfaces.
- ProCybernetica should treat browser/operator history as evidence, not define browser history schema.

### agent-term

Recent agent-term work adds local operator smoke path and durable EventStore/Matrix state artifacts.

Implication:

- AgentTerm can be an operator/gateway node.
- Its emitted artifacts/events should be evidence refs in ProCybernetica, not copied into new schemas.

### source-os

Recent source-os work covers office shell, Mac-on-Linux validation, workstation polish, shortcut/dock validation, and agent instructions.

Implication:

- SourceOS workstation/operator validation should feed `EvaluationResult` and `ArtifactEnvelope` references.
- ProCybernetica should not become product UI or shell runner.

## Required adapter posture

Future SourceOS/SociOS adapter refs should look like:

```json
{
  "artifact_ref": "srcos://release-receipt/<id>",
  "contract_kind": "ReleaseReceipt",
  "digest": "sha256:...",
  "procybernetica_contract": "ArtifactEnvelope",
  "provenance_ref": "srcos://prov/<id>",
  "policy_ref": "srcos://decision/<id>"
}
```

Do not copy complete SourceOS records into ProCybernetica unless creating a synthetic public fixture.

## ProCybernetica schema implications

### Keep

- `NodeDescriptor`
- `PolicyEnvelope`
- `CommandEnvelope`
- `DelegationEnvelope`
- `CapabilityDescriptor`
- `EventEnvelope`
- `TraceEvent`
- `ProvenanceRecord`
- `ArtifactEnvelope`
- `ReplayEnvelope`
- `EvaluationResult`
- `PromotionDecision`
- `IncidentReport`

### Do not add in ProCybernetica v0

- SourceOS `Policy` / `PolicyDecision` clone;
- SourceOS `RunRecord` clone;
- SourceOS `EventEnvelope` clone;
- SourceOS `AgentSession` clone;
- SourceOS `ReleaseReceipt` clone;
- SourceOS `BootProofRecord` clone;
- workstation contract runner schemas;
- Agent Machine AgentPod / StorageReceipt / ActivationDecision clones;
- BearHistory / OpsHistory / ShellReceipt clones.

### Consider later

- generic `ExternalEvidenceRef` after all estate maps are complete;
- `examples/integrations/sourceos/sourceos_event_ref.example.json`;
- `examples/integrations/sourceos/boot_proof_artifact_ref.example.json`;
- `examples/integrations/sourceos/agent_machine_activation_ref.example.json`.

## Open questions

1. Should ProCybernetica `NodeDescriptor` include a `sourceos_contract_ref` extension profile for Agent Machine and WorkstationProfile refs?
2. Should `PolicyEnvelope` accept explicit SourceOS `PolicyDecision` and `CapabilityToken` refs?
3. Should SourceOS `EventEnvelope` become the preferred concrete event carrier where both repos intersect?
4. Should SourceOS `RedactionTombstone` inform ProCybernetica public release and redaction records?
5. Should Agent Machine `ActivationDecision` map to `PromotionDecision` or a separate capability admission profile?

## Follow-up backlog

- Add SourceOS/SociOS adapter fixtures after all maps are complete.
- Update `docs/PUBLICATION_MATRIX.md` with SourceOS redaction/evidence refs if needed.
- Add conformance note: ProCybernetica must not clone SourceOS boot/release/workstation/agent-machine contract families.
- After Prophet Platform map, decide whether SourceOS event refs should be direct or platform-mediated.

## Current conclusion

SourceOS/SociOS owns typed execution, policy, provenance, workstation, boot, agent-machine, and operator contracts. ProCybernetica should provide constitutional interpretation and conformance expectations over those records, not duplicate their schemas or runners.
