# Enrichment Twin — Mission Spec v0.1

**Status:** design synthesis — agent-implementable once platform is green  
**Date:** 2026-06-11  
**Design posture:** open-source first, local-first hard law, policy-gated, replayable, provenance-aware  
**Basis:** reconciles the Apple on-device enrichment baseline (photoanalysisd / mediaanalysisd / mobileassetd / spotlightknowledge) into the canonical SourceOS architecture defined in `cybernetic_agentic_genesis_inception_spec`, `SourceOS / SocioProphet Linux Image Generation and Validation Corpus`, and `Socios Linux Web v0.1 (three-plane model)`.

---

## 1. Purpose

Define enrichment (photo, media, document, and other per-asset analysis) as a **mission archetype** inside the existing platform — not as a new topology. The deliverable Apple ships as a closed, device-locked, opaque pipeline is reproduced here as a governed, legible, mesh-placeable Enrichment Twin.

Non-negotiable inheritance (from the canonical spec):

- No actuation before twin verification
- Every effect cites policy + memory + provenance
- Every twin revocable
- Every artifact attributable
- Every state transition evented and replayable

---

## 2. Reframe — what the enrichment "mesh" actually is

The three planes are spaces inside the host, not mesh tiers:

| Space | Role |
|---|---|
| **System Space** | Immutable OSTree invariants: root ontology, trust anchors, base policy, organ catalog. Enrichment pipeline never mutates this; reads invariants only, writes redacted governance-gated projections back for host-side search. |
| **User Space** | Workspace / build / local-first corpus (e.g. the photo library lives here). |
| **Inception Space** | Agent VM (~10%+ of host resources). The Enrichment Twin runs here. |

The mesh tiers are execution loci (existing doctrine): `local → trusted private → attested fog → burst cloud`. Burst cloud is forbidden unless explicitly policy-enabled.

The inter-node bridge is the K3 twin bridge: agent plane → home K3s bastion (if present) → cloud K3s bastion → triune mesh, transported via MQTT (mosquitto) + optional channels.

Enrichment = an Enrichment Twin executing the cybernetic loop (build query hologram → retrieve/fuse world scene → plan → act through organs under policy → observe → update memory → emit provenance), with the placement scheduler choosing the locus.

---

## 3. The Enrichment Genesis seed

Reuses the `GenesisSeed` schema (see `schemas/genesis_seed.schema.json`). One seed per enrichment class:

```json
{
  "seed_id": "seed:enrichment/photo-v1",
  "archetype": "enrichment_twin",
  "ontology_slice": ["Asset", "Person", "Scene", "Place", "Text", "Moment"],
  "goal_schema": "schema:enrichment_goal:v1",
  "organs_allowed": [
    "vision_analyzer", "ocr_analyzer", "face_cluster",
    "graph_retrieval", "model_invoke", "policy_check"
  ],
  "retrieval_profile": {
    "graph": true, "hybrid": true, "multimodal": true,
    "self_reflective": false, "recursive": false
  },
  "memory_profile": {
    "episodic": "read_write", "semantic": "read_write_scoped",
    "procedural": "read", "provenance": "append_only"
  },
  "policy_profile": [
    "policy:enrichment/base",
    "policy:data_access/sensitivity_tiered",
    "policy:placement/local_first_hard"
  ],
  "provider_profile": [
    "provider:model_router", "provider:memory_mesh",
    "provider:regis_entity_graph"
  ],
  "federation_profile": "same_domain_only",
  "approval_profile": {
    "burst_cloud_placement": "required",
    "host_index_writeback": "required"
  }
}
```

`burst_cloud_placement` and `host_index_writeback` are the two actuation classes where enrichment crosses a trust or immutability boundary — both require explicit approval.

---

## 4. The claim hologram (enriched output)

Every enrichment output is a claim hologram, not a fact. Reuses the enrichment claim hologram schema (see `schemas/enrichment_claim_hologram.schema.json`). A scene label is never `"beach"`; it is:

```json
{
  "id": "holo:claim:asset/<asset_hash>/scene-0007",
  "kind": "enrichment_claim",
  "archetypes": ["Claim", "EvidenceBearingObject"],
  "traits": {
    "label": "beach",
    "confidence": 0.83,
    "modality": "scene"
  },
  "relations": [
    { "type": "derived_from", "target": "holo:asset:<asset_hash>" },
    { "type": "produced_by",  "target": "holo:twin:enrichment/<twin_id>" },
    { "type": "governed_by",  "target": "holo:policy:enrichment/base" }
  ],
  "memories": { "provenance": ["prov:enrich:<run_id>"] },
  "policy_envelope": "policy:claims/<sensitivity>",
  "provenance_root": "prov:enrich:<run_id>",
  "state_projection": "state:claim/<id>@v1",
  "version": "v1"
}
```

The provenance root must record: analyzer id + version, model id + version (resolved by model-router), input `asset_hash`, execution locus, `scheduled_because`, and sensitivity class.

This is the deliberate inversion of Apple's `<private>` logging: Layer 2 (residual: what model was staged) and Layer 3 (behavioral: what actually ran where) are both recorded, not hidden.

**Merge rule (inherited):** merging claims must never destroy provenance; conflicting claims retain claim-level lineage + confidence.

---

## 5. Placement contract

The Enrichment Twin emits a placement request per analysis unit. Locus eligibility is gated **before** cost optimization (governance precedes resources):

| Sensitivity class | Eligible loci |
|---|---|
| public / non-identifying (perceptual hash, generic scene) | local, trusted private, attested fog, burst cloud (if enabled) |
| internal (object/scene specifics) | local, trusted private, attested fog |
| sensitive (faces, OCR of documents, location) | local, trusted private only |

Scheduler objective (existing doctrine):

```
maximize  expected_progress_value
minus     weighted_total_cost(cash, energy, trust, latency, governance, opportunity)
minus     trust_risk_penalty
minus     governance_complexity_penalty
subject to: local_first_ordering, policy constraints, attestation constraints,
            sensitivity-class → eligible-loci mapping, evidence requirements
```

Burst cloud always requires the `burst_cloud_placement` approval from the seed. Content-addressing (`asset_hash`) lets a fog/cloud node operate without identity binding; the claim references the hash, so provenance survives relocation.

---

## 6. Derived-view / enrichment cache contract

Canonical truth (the asset) stays distinct from derived indexes. The enrichment cache is a registered derived view with lineage (Noria-style incremental maintenance):

- **Key:** `(asset_hash, analyzer_version, model_version)` → claim hologram
- **Compute-once:** any node populates; any node reads; enrichment computed once across the mesh
- **`path_content_conflict` primitive:** content-addressing makes "the file moved" vs "the content changed" deterministic — re-enrichment fires only on `asset_hash` change, not on path change
- **Supersession is append-only:** a higher-confidence claim from a heavier model (e.g. fog-run 3B) references and supersedes the edge-run claim; the earlier claim is retained

---

## 7. K3 lifecycle binding

An enrichment run is a mission through the existing K3 twin bridge:

```
INIT_SESSION (mission = enrich corpus delta)
→ PROBE_ACCEPT (negotiate organs, model classes, eligible loci)
→ INJECT_SEED (photo-v1)
→ SEED_PUBLISH
→ VERIFY_TWIN (identity, policy, memory bindings)
→ TWIN_READY (organs active)
→ [per-asset analysis → claim writes]
→ GATED_HOST_UPDATE (writeback to host search index — approval-gated)

Failure lanes: QUARANTINE / REVOKE / ROLLBACK
```

Each transition emits a signed event (`twin.verified`, `scene.built`, `memory.appended`, `actuation.requested/executed`) using the existing `event_envelope.schema.json`.

---

## 8. Repo landing map

| Component | Target repo |
|---|---|
| Enrichment Twin runtime / actuation | `agentplane` |
| Genesis seed registry entry | `prophet-core-catalog` / genesis registry |
| Genesis seed schema | `ProCybernetica/schemas/genesis_seed.schema.json` |
| Claim hologram serde | `semantic-serdes` |
| Enrichment claim hologram schema | `ProCybernetica/schemas/enrichment_claim_hologram.schema.json` |
| Claim store / memory fabric | `memory-mesh` (memory-mesh-upstream) |
| Knowledge graph (claim edges + provenance) | `regis-entity-graph` |
| Placement scheduler | SourceOS scheduler + `cloudshell-fog` (loci bridge) |
| Model catalog / adapter resolution | `model-router` |
| Placement + actuation policy (OPA) | `policy-fabric` / `guardrail-fabric` |
| Claim/evidence ledger | `prophet-core-ledger` (Exodus governance) |
| Three-plane host contract | `sourceos-spec` / `workstation-contracts` |

---

## 9. Open decisions

See [`docs/adr/`](../adr/) for the ADR tracking these. All three require owner call before agent build:

1. **Supersession vs retraction semantics.** When a heavier model supersedes an edge claim, is the old claim marked `superseded` (retained, queryable) or `retracted` (retained, hidden from default scene)? Recommendation: `superseded` + confidence-ranked default projection.

2. **Scene persistence.** Are enrichment world-scenes persisted for audit, or reconstructed on demand from event + claim references? Recommendation: on-demand reconstruction; persist only the claims.

3. **Host index writeback scope.** Does the Enrichment Twin write claims back into System-Space search as redacted projections, or stay in User/Inception Space and expose a query API the host calls? This determines whether `GATED_HOST_UPDATE` touches the immutable plane at all. Recommendation: query-API only, never mutate System Space.

---

## 10. Definition of done (architecture phase)

- [ ] `seed:enrichment/photo-v1` validates against the frozen `genesis_seed.schema.json`
- [ ] Enrichment claim hologram validates against `enrichment_claim_hologram.schema.json`; sample fixtures compile
- [ ] Placement scheduler returns an eligible-loci set for each sensitivity class and refuses burst-cloud without approval
- [ ] One asset enriched end-to-end on `local` locus, claim written to memory-mesh with full provenance, replayable from event history
- [ ] `path_content_conflict` correctly distinguishes move from change on a test corpus
- [ ] Open decisions 1–3 above have owner decisions recorded in ADRs

---

*Cross-reference: [`docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`](../source-captures/GENESIS_INCEPTION_CAPTURE.md), `schemas/genesis_seed.schema.json`, `schemas/enrichment_claim_hologram.schema.json`*
