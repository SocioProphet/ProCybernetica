# Foundry / Model Governance Map

Status: initial integration map

Turn: 8 / 20

## Purpose

This document maps ProCybernetica scoring, evaluation, promotion, lawful-learning, and conformance doctrine to the active Functional Model / Foundry / Model Router / Model Governance / Guardrail / SourceOS carry lane.

The goal is to prevent ProCybernetica from becoming a model governance ledger, router, guardrail runtime, model-carry repo, training workspace, or workspace inventory. ProCybernetica should provide the public constitutional semantics that make those surfaces coherent and inspectable.

## Source basis

Primary sources checked:

- `SocioProphet/functional-model-surfaces/README.md`
- `SocioProphet/model-router/README.md`
- `SocioProphet/model-governance-ledger/README.md`
- `SocioProphet/guardrail-fabric/README.md`
- `SourceOS-Linux/sourceos-model-carry/README.md`
- `SocioProphet/workspace-inventory/README.md`

Primary ProCybernetica sources:

- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/SCORING_METHODOLOGY_CAPTURE.md`
- `schemas/evaluation_result.schema.json`
- `schemas/promotion_decision.schema.json`
- `schemas/policy_envelope.schema.json`
- `schemas/capability_descriptor.schema.json`

## Ownership boundary

| Surface | Owning repo/lane | ProCybernetica role |
| --- | --- | --- |
| Functional AI surface contracts | `functional-model-surfaces` | Constitutional interpretation of service manifests, maturity gates, promotion law |
| Model routing | `model-router` | Policy/evaluation semantics for route decisions and fallback posture |
| Model lifecycle ledger | `model-governance-ledger` | Public promotion/revocation law and evidence interpretation |
| Guardrail runtime and decision ABI | `guardrail-fabric` | Policy decision semantics, fail-closed expectations, incident/promotion interpretation |
| Local model carry | `sourceos-model-carry` | Evidence/capability interpretation; no OS image authority for mutable model lifecycle |
| Local runtime/placement | `agent-machine` and AgentPlane | Execution evidence and runtime placement references |
| Workspace/estate maturity | `workspace-inventory`, `sociosphere` | Maturity evidence, repo/node conformance interpretation |
| Labs | `SociOS-Linux/*lab` | Functional service manifest producers and evidence sources |

## Functional Model Surfaces mapping

`functional-model-surfaces` is the standards spine for governed model, adapter, dataset, evaluation, guardrail, tool, agent, routing, promotion, and SourceOS carry contracts.

It owns:

- repository maturity schema;
- functional service manifest schema;
- Prophet Foundry contract spine;
- maturity gates M0-M5;
- contract boundaries for model/data/training/eval/release/runtime surfaces.

ProCybernetica mapping:

| Functional Model surface | ProCybernetica surface |
| --- | --- |
| repo maturity record | `EvaluationResult` / public conformance status |
| functional service manifest | `CapabilityDescriptor` / `ArtifactEnvelope` refs |
| Foundry contract spine | constitutional map to promotion/replay/evidence law |
| maturity gates M0-M5 | ProCybernetica conformance ladder alignment |
| lab functional manifests | `ArtifactEnvelope`, `ProvenanceRecord`, `EvaluationResult` |
| promotion flow | `PromotionDecision` and lawful-learning policy |

Rule: ProCybernetica should not redefine Foundry contract spine. It should map its constitutional v0 contracts to Foundry surfaces.

## Model Router mapping

`model-router` decides where a request should go. It explicitly does not own model lifecycle, local model carry profiles, or per-user personalization consent.

Router invariants include:

- local-first routing by default;
- prompt egress denied by default;
- hosted fallback requires policy approval;
- personalization requires consent and model-governance-ledger contract;
- route decisions preserve runtime health and governance refs;
- prompt evidence should be hash-only by default.

ProCybernetica mapping:

| Model Router object/concept | ProCybernetica surface |
| --- | --- |
| route binding | `CapabilityDescriptor`, `PolicyEnvelope`, `EvaluationResult` |
| local fallback | policy/evaluation evidence for route selection |
| hosted fallback | `CommandEnvelope` / `PolicyEnvelope` / `PromotionDecision` evidence if consequential |
| route decision evidence | `ArtifactEnvelope`, `TraceEvent`, `ProvenanceRecord` refs |
| personalization boundary | `PolicyEnvelope`, `DelegationEnvelope`, `PromotionDecision` refs |

Rule: ProCybernetica should not define runtime route-binding schemas. It should define the constitutional expectations route bindings must satisfy.

## Model Governance Ledger mapping

`model-governance-ledger` owns model, adapter, dataset, eval, promotion, factsheet, rollback, and revocation records.

It owns personal tuning contracts because those contracts define consent, data boundaries, evaluation requirements, promotion posture, and revocation semantics.

ProCybernetica mapping:

| Ledger record | ProCybernetica surface |
| --- | --- |
| model lifecycle record | `ArtifactEnvelope` / `ProvenanceRecord` |
| dataset lineage | `ProvenanceRecord` / SHIR/ontogenesis refs |
| eval receipt | `EvaluationResult` / `ReplayEnvelope` refs |
| promotion record | `PromotionDecision` ref or evidence input |
| rollback/revocation record | `PromotionDecision` with `rollback-required` / `revoke-authority` or IncidentReport |
| factsheet | `ArtifactEnvelope` / public scoring evidence |
| personal tuning contract | `PolicyEnvelope` / `DelegationEnvelope` / HolographMe or consent-aware refs |

Rule: ProCybernetica should not become the model-governance ledger. It should define public constitutional criteria and map to ledger records.

## Guardrail Fabric mapping

`guardrail-fabric` owns deterministic guardrail decisions and the SourceOS Agent Reliability Control Plane decision ABI.

It provides:

- decision ABI;
- dataclasses/enums for decisions, evidence, effects, severity, scope, action class;
- local JSONL decision logging;
- policy simulation CLI;
- fail-closed behavior;
- JSON Schema for decision artifact;
- baseline deterministic policy packs;
- agent hook adapter;
- CI-backed tests.

ProCybernetica mapping:

| Guardrail Fabric object/concept | ProCybernetica surface |
| --- | --- |
| guardrail decision | `PolicyEnvelope`, `EvaluationResult`, `TraceEvent` evidence |
| deny/defer/quarantine decision | `PromotionDecision` or `IncidentReport` depending scope |
| policy simulation result | `EvaluationResult` |
| decision log | `ArtifactEnvelope` / `ProvenanceRecord` refs |
| action class | `CapabilityDescriptor.side_effect_class` alignment |
| fail-closed behavior | constitutional invariant and conformance check |

Rule: ProCybernetica should not create a competing guardrail decision ABI. It should reference Guardrail Fabric decisions and express what they mean constitutionally.

## SourceOS Model Carry mapping

`sourceos-model-carry` defines the on-device carriage layer for governed AI services.

It may carry:

- service clients;
- launch profiles;
- signed service references;
- local cache policy;
- fallback references;
- ReleaseSet and BootReleaseSet bindings;
- evidence collectors;
- workstation integration hints;
- Local Model Door profiles.

It must not become the authority for model promotion, model lifecycle state, or personal tuning authorization.

ProCybernetica mapping:

| SourceOS Model Carry concept | ProCybernetica surface |
| --- | --- |
| local model profile | `CapabilityDescriptor` / SourceOS evidence ref |
| signed service reference | `ArtifactEnvelope` / `ProvenanceRecord` |
| launch profile | `CommandEnvelope` / `CapabilityDescriptor` evidence |
| cache policy | `PolicyEnvelope` / memory/resource model refs |
| fallback ref | route/evaluation evidence |
| ReleaseSet binding | SourceOS boot/release evidence refs |
| evidence collector | `TraceEvent` / `ArtifactEnvelope` refs |
| Local Model Door | capability and policy-governed route profile |

Rule: ProCybernetica should not define local model carry schemas or mutable OS model update authority.

## Workspace Inventory mapping

`workspace-inventory` is the canonical index of repositories in the SocioProphet org and adjacent cross-org authorities. It records repo roles, integration contracts, canonical responsibility, status, and wiring hints.

ProCybernetica mapping:

| Workspace Inventory field | ProCybernetica use |
| --- | --- |
| repo status | node/repository maturity evidence |
| authority_role | owner boundary in integration maps |
| boundary_notes | non-duplication guardrail |
| related_repos | adapter/dependency graph |
| canonical_source_ref | provenance for contract ownership |
| optional_layer | conformance profile scoping |

Rule: ProCybernetica integration docs should be cross-checked against workspace-inventory to avoid stale or invented ownership.

## Professional Intelligence / Foundry lane mapping

Recent estate activity points to a Professional Intelligence / Prophet Intelligence Foundry lane spanning:

- `functional-model-surfaces`
- `model-router`
- `model-governance-ledger`
- `guardrail-fabric`
- `agent-registry`
- `sourceos-model-carry`
- `agent-machine`
- `agentplane`
- `workspace-inventory`
- `socioprophet-web`
- `prophet-platform-fabric-mlops-ts-suite`

ProCybernetica should use this as the concrete model-governance/evaluation use case for lawful learning and promotion.

Recommended mapping:

```text
Functional service manifest
  -> model governance ledger record
  -> model-router route binding
  -> guardrail decision evidence
  -> SourceOS model carry profile
  -> Agent Machine placement/evidence
  -> AgentPlane run/replay evidence
  -> Prophet Platform eval fabric record
  -> ProCybernetica EvaluationResult / PromotionDecision interpretation
```

## ProCybernetica schema implications

### Keep

- `EvaluationResult`
- `PromotionDecision`
- `PolicyEnvelope`
- `CapabilityDescriptor`
- `ArtifactEnvelope`
- `ProvenanceRecord`
- `ReplayEnvelope`
- `TraceEvent`
- `EventEnvelope`

### Do not add in ProCybernetica v0

- functional service manifest clone;
- Foundry contract spine clone;
- local-personal route binding clone;
- personal tuning contract clone;
- guardrail decision ABI clone;
- local model profile clone;
- repo maturity schema clone;
- model lifecycle ledger schema clone;
- training/eval runtime schemas.

### Consider later

- generic `ExternalEvidenceRef` after all maps complete;
- `examples/integrations/foundry/functional_service_ref.example.json`;
- `examples/integrations/model-router/route_decision_ref.example.json`;
- `examples/integrations/model-governance/promotion_record_ref.example.json`;
- scoring/dashboard synthetic examples for Foundry maturity and model-route evidence.

## Open questions

1. Should ProCybernetica conformance levels align directly with functional-model-surfaces M0-M5 or remain a separate cybernetic ladder?
2. Should route decisions be modeled as `EvaluationResult`, `PromotionDecision`, or both depending side-effect level?
3. Should guardrail quarantine decisions map directly to ProCybernetica `PromotionDecision.decision = quarantine`?
4. Should personal tuning contracts be mapped through HolographMe-style projection/consent semantics where person-owned data is involved?
5. Should ProCybernetica scoring dashboard include Foundry maturity as a first-class score slice?

## Follow-up backlog

- Add Foundry/model-governance adapter fixtures after all maps complete.
- Update scoring/dashboard docs to include Foundry maturity and model-route evidence as candidate public score slices.
- Decide conformance-ladder relation to M0-M5 in Turn 13 conformance plan.
- Revisit `EvaluationResult` and `PromotionDecision` examples after platform and Foundry adapters are defined.

## Current conclusion

The Foundry/model-governance lane already has a distributed ownership model. ProCybernetica should not absorb it. ProCybernetica should provide the public constitutional interpretation: what counts as evidence, when evaluation is sufficient, when promotion is lawful, when rollback or revocation is required, and how these facts become inspectable in public.
