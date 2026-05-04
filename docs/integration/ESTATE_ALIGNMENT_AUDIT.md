# GitHub Estate Alignment Audit

Status: initial audit

Date: 2026-04-29

Purpose: ensure ProCybernetica is not built in a vacuum. This note captures relevant upstream repositories, recent work, and integration implications for the ProCybernetica v0 public standard and reference implementation.

## Summary

ProCybernetica should remain the public blueprint, doctrine, schema/profile, conformance, and reference-kit surface. It should not duplicate runtime ownership already established elsewhere in the estate.

The estate already contains active surfaces for:

- runtime and deployment: `SocioProphet/prophet-platform`;
- platform DevSecOps / CI / observability standards: `SocioProphet/prophet-platform-standards`;
- evidence-producing execution plane: `SocioProphet/agentplane`;
- agent identity and authority registry: `SocioProphet/agent-registry`;
- semantic event/context/surface contracts: `SocioProphet/semantic-serdes`;
- ontology governance and SHACL promotion gates: `SocioProphet/ontogenesis`;
- SourceOS/SociOS typed contracts: `SourceOS-Linux/sourceos-spec`;
- boot and recovery evidence surface: `SourceOS-Linux/sourceos-boot`;
- SourceOS execution/dev surfaces: `SourceOS-Linux/agent-machine`, `SourceOS-Linux/agent-term`, `SourceOS-Linux/sourceos-devtools`, `SourceOS-Linux/sourceos-shell`;
- SociOS substrate and Linux governance surfaces: `SociOS-Linux/socios`, `SociOS-Linux/source-os`.

## Relevant upstream surfaces

### SocioProphet/prophet-platform

Role observed: runtime and deployment hub for the SocioProphet platform.

Important repo posture:

- thin platform monorepo;
- `contracts/` contains platform-facing event, evidence, and receipt contracts;
- `apps/` owns deployable runtime services;
- `infra/` owns deployment wiring;
- `tools/` owns validation and smoke-test helpers;
- evaluation fabric lane owns platform-level ranking, replay, and intelligence work.

Implication for ProCybernetica:

- ProCybernetica defines public constitutional law and v0 standards.
- Prophet Platform implements production runtime services and consumes ProCybernetica contracts.
- Do not duplicate platform runtime in ProCybernetica.
- Add compatibility mapping between ProCybernetica `EventEnvelope`, `TraceEvent`, `ReplayEnvelope`, `EvaluationResult`, `PromotionDecision`, and platform contracts.

Recent upstream work to account for:

- identity contract consumption PRs #379, #380, #381;
- FogStack evidence/parity PRs #366 through #382;
- office runtime contract PR #378;
- AgentPlane/PolicyPlane linkage and live preflight evidence are now core platform patterns.

### SocioProphet/prophet-platform-standards

Role observed: canonical platform standards for DevSecOps, CI/CD, RBAC, audit, and observability.

Important standards:

- Tekton + ArgoCD + GitOps strategy;
- DevSecOps, RBAC, audit standards;
- OpenTelemetry observability and telemetry;
- cosign, SBOM, in-toto, Kyverno, Grafana dashboards.

Implication for ProCybernetica:

- ProCybernetica CI/conformance should align with these standards where practical.
- v0 should add a standards import note rather than inventing a parallel CI/security doctrine.
- Future conformance artifacts should map to audit/OTEL standards.

### SocioProphet/agentplane

Role observed: execution control plane for AI + hardware + state stack.

Core execution chain:

```text
Bundle -> Validate -> Place -> Run -> Evidence -> Replay
```

Important artifacts:

- ValidationArtifact;
- PlacementDecision;
- RunArtifact;
- ReplayArtifact;
- PromotionArtifact;
- ReversalArtifact;
- SessionArtifact;
- AgentMachineMountEvidence;
- OfficeArtifactEvidence;
- NetworkDoorPlanEvidence;
- ExternalModelProviderRouteEvidence;
- NativeAssistantBridgeEvidence.

Implication for ProCybernetica:

- ProCybernetica `ReplayEnvelope`, `EvaluationResult`, `PromotionDecision`, `CapabilityDescriptor`, and `ArtifactEnvelope` must map to AgentPlane artifacts.
- AgentPlane owns evidence-producing execution. ProCybernetica owns the public constitutional vocabulary and conformance law.
- Add an AgentPlane artifact mapping doc before expanding runtime code.

Recent upstream work to account for:

- PR #84 defines agentic PR control plane v0 with work-order schema and lifecycle from issue to merge ledger.
- This is directly relevant to ProCybernetica GitHub/repository-as-node governance and should be imported into the GitHub integration model.

### SocioProphet/agent-registry

Role observed: governed registry for agent specs, identities, sessions, memories, tool grants, revocation, and runtime authority.

Implication for ProCybernetica:

- ProCybernetica should not define a competing agent registry.
- ProCybernetica should define the public `AgentNode` contract and map it to `agent-registry` authority/session/memory/tool-grant records.

### SocioProphet/semantic-serdes

Role observed: canonical schema pack for semantics-aware event/context/surface serialization.

Important concepts:

- Event, Context, Surface primitives;
- canonical enum definitions for planes, truth classes, time models, merge models, scopes, and surfaces;
- agent message envelope;
- agent decision artifact;
- replay artifact;
- alias maps;
- validation tooling.

Implication for ProCybernetica:

- ProCybernetica `Claim`, `EventEnvelope`, `TraceEvent`, `ObservationEnvelope`, and dashboard/export semantics should align with semantic-serdes enums and surface model.
- Do not create conflicting truth-class or plane vocabulary.
- Add a semantic-serdes compatibility map.

Recent upstream work to account for:

- PR #7 added SHIR SerDes v0.1 schemas and fixtures;
- PR #8 added CI validation for SHIR fixtures.

### SocioProphet/ontogenesis

Role observed: auditable, policy-gated ontology engineering framework for RDF/OWL/JSON-LD assets.

Important mechanisms:

- layered ontology modules: Upper, Middle, Lower, Domains, Platform, prophet, epi;
- SHACL gates;
- JSON-LD roundtrip checks;
- deterministic dist builds;
- ledger generation and verification;
- detached signatures;
- SPDX SBOM generation.

Implication for ProCybernetica:

- ProCybernetica claim, ontology, and hard-lane promotion docs should map to ontogenesis SHACL and ledger gates.
- ProCybernetica should not invent a separate ontology release discipline.
- Add an ontology governance mapping from Prelude F / Claim schema to ontogenesis modules.

Recent upstream work to account for:

- PR #27 adds SHIR v0.1 semantic hyperknowledge spec;
- SHIR defines Node, Anchor, Connector, RoleBinding, Assertion, Evidence, Projection, Receipt, CurationDecision, ProjectionLossReport, and related objects.

### SourceOS-Linux/sourceos-spec

Role observed: canonical machine-readable typed contracts for SourceOS metadata governance platform and SociOS agent plane.

Important families:

- Governance: Policy, Rule, CapabilityToken, Obligation, Exception;
- Execution / Provenance: Dataset, RunRecord, WorkflowSpec, WorkloadSpec, ProvenanceRecord, EventEnvelope, MappingSpec;
- Agent Plane: AgentSession, ExecutionDecision, ExecutionSurface, SkillManifest, MemoryEntry, SessionReceipt, SessionReview, TelemetryEvent, FrustrationSignal;
- Release / Experiments and Fog Layer contracts.

Implication for ProCybernetica:

- ProCybernetica v0 schemas overlap deliberately with SourceOS typed contracts. We must map, not fork, these shapes.
- SourceOS/SociOS may own lower-level operational contract implementations; ProCybernetica owns cybernetic constitutional semantics.
- Add SourceOS contract mapping issue before changing schema names further.

### SourceOS-Linux/sourceos-boot

Role observed: boot, recovery, and secure live-provisioning surface for SourceOS.

Important concepts:

- BootReleaseSet;
- boot manifest;
- recovery/live environment;
- verified install/update/rollback;
- evidence records: device claim, manifest hash, boot mode, selected release set, verification result.

Implication for ProCybernetica:

- Boot and update receipts should become `ArtifactEnvelope` / `ProvenanceRecord` / `ReplayEnvelope` compatible evidence.
- ProCybernetica should add a SourceOS boot evidence adapter spec, not implement boot runtime.

### SourceOS-Linux/agent-machine and agent-term

Role observed: Agent Machine and terminal/agent interaction surfaces.

Implication for ProCybernetica:

- These should map to `host`, `process`, `agent`, `operator`, and `gateway` node classes.
- Agent-term/TurtleTerm/SourceOS shell can provide operator/gateway embodiments for ProCybernetica control loops.

### SociOS-Linux/socios and source-os

Role observed: SociOS/SourceOS substrate and Linux distribution surfaces.

Implication for ProCybernetica:

- Treat these as substrate and host/node implementation surfaces.
- ProCybernetica should publish schemas/adapters that let host evidence flow into the constitutional replay/promotion layer.

## Immediate required corrections to ProCybernetica work

1. Add estate alignment before further schema expansion.
2. Add mapping docs rather than duplicate AgentPlane, semantic-serdes, ontogenesis, SourceOS, and Prophet Platform contracts.
3. Treat AgentPlane evidence artifacts as upstream execution evidence.
4. Treat semantic-serdes as upstream semantic event/context/surface vocabulary.
5. Treat ontogenesis as upstream ontology governance and SHACL promotion gate lane.
6. Treat SourceOS spec/boot as upstream substrate, execution, provenance, and boot evidence contracts.
7. Treat Prophet Platform as production runtime consumer, not a secondary place to define doctrine.

## Follow-up issues to create

- Map ProCybernetica v0 schemas to AgentPlane evidence artifacts.
- Map ProCybernetica events/claims to semantic-serdes and SHIR.
- Map ProCybernetica claim/ontology gates to ontogenesis SHACL/ledger discipline.
- Map ProCybernetica v0 schemas to SourceOS/SociOS typed contracts.
- Map boot/update receipts to ProCybernetica evidence envelopes.
- Map Prophet Platform identity/eval/fogstack contracts to ProCybernetica constitutional loop.

## Current conclusion

The estate already contains strong pieces of the ProCybernetica implementation environment. ProCybernetica should become the public constitutional standard and reference-kit layer that makes those pieces coherent, not an isolated runtime or competing contract library.
