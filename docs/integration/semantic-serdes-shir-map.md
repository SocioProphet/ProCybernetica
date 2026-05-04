# Semantic SerDes and SHIR Map

Status: initial integration map

Turn: 3 / 20

Related issue: #10

## Purpose

This document maps ProCybernetica v0 semantic contracts to `SocioProphet/semantic-serdes` and SHIR so ProCybernetica does not fork plane, truth-class, context, surface, projection, and semantic receipt vocabulary.

ProCybernetica owns cybernetic constitutional semantics, replay law, promotion law, public conformance posture, and reference-kit interpretation.

semantic-serdes owns semantics-aware serialization contracts for events, context, surfaces, agent messages, decisions, replay artifacts, canonical enums, and SHIR schema fixtures.

ontogenesis owns the SHIR semantic contract and ontology-governed semantic authority layer.

## Source basis

Primary upstream sources checked:

- `SocioProphet/semantic-serdes/README.md`
- `SocioProphet/semantic-serdes/canonical_enums.yaml`
- `SocioProphet/semantic-serdes/docs/shir-serdes-v0.1.md`
- `SocioProphet/ontogenesis/docs/specs/shir-v0.1.md`

Primary ProCybernetica sources:

- `docs/source-captures/PRELUDE_F_ONTOLOGY_CORPUS_SEMANTIC_CONTRACTS_CAPTURE.md`
- `schemas/claim.schema.json`
- `schemas/event_envelope.schema.json`
- `schemas/trace_event.schema.json`
- `schemas/observation_envelope.schema.json`
- `schemas/replay_envelope.schema.json`
- `schemas/provenance_record.schema.json`

## Ownership boundary

| Surface | Upstream owner | ProCybernetica role |
| --- | --- | --- |
| Event / Context / Surface primitives | semantic-serdes | Interpret as observation, memory, world model, replay, or promotion evidence. |
| Canonical enums | semantic-serdes | Map into node, claim, event, dashboard, and promotion semantics. |
| SHIR object model | ontogenesis + semantic-serdes | Reference SHIR objects as semantic evidence; do not redefine them. |
| Semantic projection | semantic-serdes / SHIR | Require projection-loss awareness when projections drive scoring, dashboards, or ML exports. |
| Ontology authority | ontogenesis | Reference ontology and curation artifacts; do not duplicate release discipline. |
| Cybernetic promotion law | ProCybernetica | Decide when semantic outputs may affect canonical truth or action. |
| Public conformance posture | ProCybernetica | Publish rules, examples, conformance checks, and integration expectations. |

## Canonical enum mapping

semantic-serdes canonical enums should guide ProCybernetica semantic integrations.

### Plane

| semantic-serdes plane | ProCybernetica interpretation |
| --- | --- |
| `RAW` | raw observation or immediate experience |
| `EVENT` | event envelope, trace event, lifecycle/event log |
| `ENTITY` | world-model entity or claim subject/object |
| `DERIVED` | derived claim, inferred output, evaluation result |
| `GLOBAL` | shared memory, ontology, policy, or corpus scope |
| `SURFACE` | dashboard, export, query, API, or operator projection |

### Truth class

| semantic-serdes truth class | ProCybernetica interpretation |
| --- | --- |
| `OBSERVED` | observation-backed claim or event |
| `ASSERTED` | asserted claim, curated assertion, or policy statement |
| `INFERRED` | derived or model-assisted claim |
| `REPUTED` | externally sourced claim with weaker authority |

## Claim status mapping

| ProCybernetica `Claim.status` | Upstream analogue | Rule |
| --- | --- | --- |
| `candidate` | SHIR CandidateAssertion / proposed tag | Not canonical truth. |
| `hypothesis` | inferred / provisional | Requires evidence and review. |
| `validated` | SHIR Assertion / governed or canonical tag | May support hard-lane use after policy and promotion. |
| `derived` | derived assertion | Must preserve derivation refs. |
| `stale` | superseded or deprecated semantic state | Do not silently delete. |
| `retracted` | curation or repair decision | Preserve reason and provenance. |

Recommendation: do not modify `Claim` again until all estate maps are complete. If needed, add a later adapter object for semantic-serdes truth class and admissibility tier.

## SHIR object mapping

| SHIR object | ProCybernetica analogue | Decision |
| --- | --- | --- |
| `Node` | semantic object; sometimes a `NodeDescriptor` only when it is also a control node | Do not collapse semantic nodes and cybernetic nodes. |
| `Anchor` | source/evidence reference | Reference through `ProvenanceRecord` or `ArtifactEnvelope`. |
| `Connector` / `RoleBinding` / `Link` | relation model | Owned by SHIR; ProCybernetica references connector/link IDs. |
| `Context` | memory, replay, policy, or world-model context | Reference context IDs; do not fork context schema. |
| `Assertion` | validated/governed claim | Treat as semantic evidence for promotion/evaluation. |
| `Evidence` | evidence source | Reference through `ArtifactEnvelope` and `ProvenanceRecord`. |
| `TemporalScope` | valid/observation/replay timing | Preserve bitemporal semantics where available. |
| `Projection` | dashboard/export/retrieval/ML lowering | Require projection-loss reporting when material. |
| `Receipt` | transform or projection receipt | Reference as provenance/evidence artifact. |
| `CandidateAssertion` | `Claim.status = candidate` | Candidate claims do not become truth without validation. |
| `ProjectionLossReport` | evidence for semantic loss | Reference from replay/evaluation when projection changes meaning. |
| `CurationDecision` | promotion/retraction/repair decision | Map to `PromotionDecision`, `IncidentReport`, or future curation adapter. |

## Event and trace mapping

semantic-serdes owns general event/context/surface serialization. ProCybernetica owns the cybernetic role of an event.

| ProCybernetica field | Upstream relation |
| --- | --- |
| `EventEnvelope.event_family` | semantic-serdes plane/surface/context classification |
| `EventEnvelope.public_release_state` | publication matrix / surface visibility bridge |
| `TraceEvent.correlation_id`, `trace_id`, `span_id` | replayability and causal ordering |
| `ObservationEnvelope.modality` | raw/event/surface intake classifier |
| `ProvenanceRecord.source_refs` | SHIR Evidence / Anchor / Receipt refs |

## Dashboard/export mapping

ProCybernetica dashboard payloads are surface projections.

| Dashboard element | Upstream mapping |
| --- | --- |
| leaderboard | `SURFACE` / dashboard projection |
| evidence registry | surface projection over assertions/evidence refs |
| drift view | temporal projection over snapshots or query windows |
| contradiction view | semantic diagnostic / curation signal in future |
| subject profile | entity-context projection |
| export JSON | surface projection payload with public visibility and replay refs |

Requirement: scoring/dashboard aggregations should preserve enough summary/projection metadata to explain what was lost, summarized, or approximated.

## Replay mapping

ProCybernetica `ReplayEnvelope` is a constitutional replay manifest. It should reference semantic-serdes or SHIR receipts when semantic transforms are involved.

Example reference pattern:

```json
{
  "replay_id": "replay:...",
  "artifact_refs": ["shir-receipt:..."],
  "trace_refs": ["semantic-serdes:event:..."],
  "version_pins": {
    "semantic_serdes_schema": "v0.1",
    "shir_schema": "v0.1",
    "ontology_profile": "..."
  }
}
```

## ProCybernetica schema implications

### Keep

- `Claim`
- `EventEnvelope`
- `TraceEvent`
- `ObservationEnvelope`
- `ReplayEnvelope`
- `ProvenanceRecord`
- `ArtifactEnvelope`
- `EvaluationResult`
- `PromotionDecision`

### Do not add in ProCybernetica v0

- `SemanticCell`
- `SurfaceProjection`
- `ContextMergePolicy`
- `AgentMessage`
- `AgentDecisionArtifact`
- `SHIRCandidateAssertion`
- `SHIRAssertion`
- `SHIRProjectionLossReport`
- `SHIRReceipt`

These belong upstream in semantic-serdes and ontogenesis.

### Consider later

- `ExternalEvidenceRef` after all estate maps are complete.
- semantic-serdes adapter fixtures under `examples/integrations/semantic-serdes/`.
- a `Claim` extension profile for truth class, admissibility tier, and curation refs.

## Open questions

1. Should ProCybernetica `Claim` include `truth_class` in v0.1, or should that remain an adapter mapping?
2. Should dashboard export payloads be recast as semantic-serdes `SurfaceProjection` examples?
3. Should `public_release_state` stay ProCybernetica-specific or map directly to surface visibility?
4. Should SHIR `Receipt` be represented as `ArtifactEnvelope`, `ProvenanceRecord`, or both?
5. Should projection-loss reporting be mandatory for all scoring/dashboard aggregates or only for semantic graph/ML lowerings?

## Follow-up backlog

- Add `examples/integrations/semantic-serdes/claim_to_shir_candidate_assertion.example.json`.
- Add `examples/integrations/semantic-serdes/dashboard_surface_projection.example.json`.
- Add `examples/integrations/semantic-serdes/replay_to_shir_receipt.example.json`.
- Update scoring/dashboard docs to state that dashboard payloads are surface projections.
- Revisit `Claim` schema only after all estate maps are complete.

## Current conclusion

semantic-serdes and SHIR are upstream semantic contract authorities. ProCybernetica should reference them, interpret their governance role, and enforce constitutional expectations around promotion, replay, public evidence, and semantic preservation. It should not duplicate their schemas.
