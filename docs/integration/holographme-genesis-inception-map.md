# HolographMe / Genesis-Inception Map

Status: initial integration map

Turn: 7 / 20

Related issue: #13

## Purpose

This document maps `SocioProphet/HolographMe` to ProCybernetica Genesis/Inception/K3 planning.

The goal is to prevent ProCybernetica from inventing a parallel runtime-persona or worker-profile model before accounting for HolographMe's existing schemas, governance model, and operating model.

HolographMe owns the self-owned work-twin domain, its consent/projection discipline, mission-fit workflow, and domain schemas.

ProCybernetica owns the broader constitutional machinery: Genesis seed law, Inception runtime binding, K3 transition law, Fractal Node semantics, policy/replay/promotion doctrine, and public conformance expectations.

## Source basis

Primary HolographMe sources checked:

- `SocioProphet/HolographMe/README.md`
- `SocioProphet/HolographMe/docs/architecture.md`
- `SocioProphet/HolographMe/docs/governance.md`
- `SocioProphet/HolographMe/docs/operating-model.md`
- `SocioProphet/HolographMe/schemas/human-digital-twin.schema.json`
- `SocioProphet/HolographMe/schemas/consent-policy.schema.json`
- `SocioProphet/HolographMe/schemas/mission.schema.json`

Primary ProCybernetica sources:

- `docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`
- `profiles/k3_bridge_lifecycle.yaml`
- `schemas/policy_envelope.schema.json`
- `schemas/delegation_envelope.schema.json`
- `schemas/capability_descriptor.schema.json`
- `schemas/claim.schema.json`
- `schemas/artifact_envelope.schema.json`
- `schemas/provenance_record.schema.json`
- `schemas/promotion_decision.schema.json`

## Ownership boundary

| Surface | HolographMe owns | ProCybernetica owns |
| --- | --- | --- |
| Work-twin domain schema | HumanDigitalTwin schema and domain semantics | Genesis/Inception interpretation and constitutional lifecycle mapping |
| Consent and projection | ConsentPolicy schema, projection discipline, work-related view rules | PolicyEnvelope semantics, public-first conformance, and authority boundaries |
| Mission fit | Mission schema, mission-fit projection workflow, consulting/workgraph lifecycle | Command/Delegation/Capability/Promotion interpretation over mission events |
| Capability claims | capability claim structure, evidence attachments, confidence posture | Claim/evidence/promotion law and relation to SHIR/ontogenesis evidence |
| Transition receipts | domain transition receipts for twin state changes | ArtifactEnvelope, ProvenanceRecord, ReplayEnvelope, and PromotionDecision mapping |
| Delegated agents | domain authority bands and allowed action constraints | DelegationEnvelope and agent/repo governance semantics |
| Operating model | intake, assessment, projection, team formation, delivery, outcome update | Genesis seed, Inception binding, K3 lifecycle, replay, and lawful learning posture |

## Genesis/Inception mapping

HolographMe maps naturally into ProCybernetica's Genesis/Inception model.

| Genesis/Inception concept | HolographMe analogue | Mapping decision |
| --- | --- | --- |
| Genesis seed | reusable schema/governance profile for work-twin formation | HolographMe schemas can inform a future `genesis_seed` profile for work-twin use cases. |
| Inception request | intake event that binds subject, consent, mission context, and runtime | HolographMe intake/assessment workflow is a concrete Inception scenario. |
| Twin runtime descriptor | HumanDigitalTwin state plus runtime/projection context | Do not duplicate HolographMe schema; reference it as domain object. |
| K3 bridge | controlled progression from intake to verified runtime projection | Map state changes to K3 events and transition receipts. |
| Cognitive mesh | assessment, evidence, mission-fit reasoning, team matching | HolographMe domain services can be organs/capabilities under ProCybernetica law. |
| Policy envelope | consent policy, projection rules, delegation limits | HolographMe ConsentPolicy should map to PolicyEnvelope references, not be copied. |
| Provenance memory | evidence artifacts and transition receipts | Preserve as ArtifactEnvelope/ProvenanceRecord refs. |

## Schema mapping

| HolographMe schema/object | ProCybernetica analogue | Mapping decision |
| --- | --- | --- |
| `HumanDigitalTwin` | future `TwinRuntimeDescriptor`, `NodeDescriptor` only if participating as active node | HolographMe owns the domain schema. ProCybernetica should reference it. |
| `CapabilityClaim` | `Claim` plus evidence refs | Capability claims can map to ProCybernetica claims but keep HolographMe verification/status semantics. |
| `EvidenceArtifact` | `ArtifactEnvelope` / `ProvenanceRecord` | Evidence artifacts become evidence refs in ProCybernetica. |
| `ConsentPolicy` | `PolicyEnvelope` | ConsentPolicy remains HolographMe-owned; ProCybernetica references it as policy evidence. |
| `Projection` | semantic-serdes surface projection and ProCybernetica evidence surface | Projection should be treated as a bounded public/controlled surface, not raw record access. |
| `Mission` | `CommandEnvelope`, `DelegationEnvelope`, `CapabilityDescriptor`, or work-order equivalent | Mission requests can become bounded commands/delegations under policy. |
| `TransitionReceipt` | `ArtifactEnvelope`, `ProvenanceRecord`, `ReplayEnvelope` | Transition receipts are evidence for replay and promotion. |
| delegated agent record | `DelegationEnvelope` / authority grant refs | Use DelegationEnvelope only as constitutional bridge; HolographMe owns domain authority bands. |

## K3 lifecycle mapping

| K3 state | HolographMe lifecycle example |
| --- | --- |
| `INIT_SESSION` | intake starts, subject context and requested projection scope established |
| `PROBE_ACCEPT` | governance, mission, assessment, and projection capability compatibility checked |
| `INJECT_SEED` | HolographMe schema/governance profile selected for the work-twin slice |
| `SEED_PUBLISH` | initial record, consent policy, and evidence package persisted with hashes/receipts |
| `VERIFY_TWIN` | schema validation, policy validation, evidence checks, and projection checks run |
| `TWIN_READY` | bounded mission-fit or assessment projection can be produced |
| `GATED_HOST_UPDATE` | controlled update to capability, consent, delegation, reputation, or mission state |
| `QUARANTINE` | governance or evidence failure blocks projection/update path |
| `REVOKE` | consent or authority withdrawn |
| `ROLLBACK` | reversible state transition compensated or restored from receipt trail |

## Policy and delegation mapping

HolographMe authority bands map to ProCybernetica delegation posture:

| HolographMe authority band | ProCybernetica delegation interpretation |
| --- | --- |
| observe | read/use only inside allowed projection scope |
| recommend | produce suggestions with explanation and reviewability |
| represent | respond or schedule within explicit delegated limits |
| negotiate | propose terms but require stronger review unless pre-authorized |
| commit | highest authority band; requires explicit receipt and strong approval posture |

ProCybernetica should not encode domain-specific employment/workflow rules. It should enforce the general rule that high-authority delegation requires policy refs, expiry, evidence, and replayability.

## Claim and evidence mapping

HolographMe capability claims and evidence artifacts should be mapped carefully:

```text
capability claim
  -> Claim candidate / asserted capability
  -> evidence artifact refs
  -> assessment or verification event
  -> transition receipt
  -> promotion/evaluation decision if used for matching or mission authority
```

Rules:

1. A capability claim without evidence must not be treated as verified.
2. Evidence and confidence posture must remain visible.
3. Mission-fit projection must not expose the full underlying record.
4. Outcome updates require transition receipts.
5. Corrections, disputes, revocations, and stale evidence must remain inspectable.

## Projection and surface mapping

HolographMe's projection discipline should map to semantic-serdes surface projections and ProCybernetica public/evidence posture.

| Projection type | ProCybernetica / semantic interpretation |
| --- | --- |
| mission-fit projection | surface projection over claims/evidence/policy refs |
| assessment projection | bounded context for interview or evaluation workflow |
| client delivery projection | role/capability/evidence surface for a specific engagement |
| agent delegate projection | delegation-specific view with authority limits |

Projection outputs should be treated as `ArtifactEnvelope` or dashboard/surface artifacts when persisted.

## ProCybernetica schema implications

### Keep

- `PolicyEnvelope`
- `DelegationEnvelope`
- `CapabilityDescriptor`
- `Claim`
- `ArtifactEnvelope`
- `ProvenanceRecord`
- `ReplayEnvelope`
- `PromotionDecision`
- `EventEnvelope`
- `TraceEvent`

### Do not add in ProCybernetica v0

- HumanDigitalTwin clone
- ConsentPolicy clone
- Mission clone
- capability-claim clone with HolographMe semantics
- projection-template schema specific to HolographMe
- workgraph/staffing schema

These belong to HolographMe or downstream workgraph repositories.

### Consider later

- future `genesis_seed.schema.json`
- future `inception_request.schema.json`
- future `twin_runtime_descriptor.schema.json`
- HolographMe adapter fixtures under `examples/integrations/holographme/`

## Required adapter posture

A future adapter should reference HolographMe artifacts instead of copying them:

```json
{
  "domain_ref": "holographme://human-digital-twin/<id>",
  "policy_ref": "holographme://consent-policy/<id>",
  "projection_ref": "holographme://projection/<id>",
  "receipt_ref": "holographme://transition-receipt/<id>",
  "procybernetica_contract": "ProvenanceRecord"
}
```

## Open questions

1. Should future `TwinRuntimeDescriptor` allow `domain_object_ref` for HolographMe and other twin-like domain objects?
2. Should HolographMe transition receipts become `ArtifactEnvelope` examples in ProCybernetica?
3. Should K3 bridge lifecycle include a domain-specific mapping profile for work-twin use cases?
4. Should `DelegationEnvelope.authority` align with HolographMe authority bands in v0.1?
5. Should public scoring/dashboard examples include HolographMe-style projection receipts as synthetic fixtures?

## Follow-up backlog

- Add `examples/integrations/holographme/twin_ref.example.json` after all maps complete.
- Add `examples/integrations/holographme/projection_receipt_ref.example.json` after all maps complete.
- Revisit future Genesis/Inception schemas after Functional Model/Foundry and Workstation maps are complete.
- Consider `domain_object_ref` pattern in future `TwinRuntimeDescriptor`.

## Current conclusion

HolographMe is the domain owner for self-owned work-twin governance. ProCybernetica should use it as the concrete Genesis/Inception/Twin use case, not replace it. The correct integration is to reference HolographMe schemas, policies, projections, and receipts while applying ProCybernetica's general constitutional rules for identity, delegation, policy, replay, promotion, and evidence.
