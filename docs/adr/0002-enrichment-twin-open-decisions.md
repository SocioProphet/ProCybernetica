# ADR-0002: Enrichment Twin open decisions

**Date:** 2026-06-11  
**Status:** open — owner call required before agent build  
**Context:** Enrichment Twin Mission Spec v0.1 (see [`docs/architecture/enrichment-twin-mission-spec.md`](../architecture/enrichment-twin-mission-spec.md))

---

## Decision 1: Supersession vs retraction semantics

### Question

When a heavier model (e.g. a fog-run 3B vision model) produces a higher-confidence claim that supersedes an earlier edge-run claim, what is the status of the earlier claim?

- **Option A — `superseded`:** Earlier claim is retained, queryable, and visible to provenance queries. Hidden from the default scene projection (filtered by confidence rank). The `superseded_by` field on the old claim and `supersedes` on the new claim create a bidirectional provenance link.
- **Option B — `retracted`:** Earlier claim is retained for audit but hidden from all projection surfaces, not just the default one. Matches the `retracted` status in the base ProCybernetica claim schema.

### Recommendation

**Option A — `superseded` + confidence-ranked default projection.**

Rationale: retraction implies the earlier claim was wrong or harmful. Supersession implies a better source arrived. The enrichment case is the latter — the edge model's claim was correct given its capability; the fog model simply has more information. Retaining the earlier claim with `superseded` status preserves the full enrichment history and allows replay from any point in the locus progression. The canonical spec's merge rule ("merging claims must never destroy provenance") supports this.

### Owner call needed

Confirm Option A is acceptable for the sensitivity classes where retraction might be preferable (e.g. a `face_cluster` claim from an edge model that misidentified someone — should that be `superseded` or `retracted`?). A possible middle ground: `superseded` for all modalities except `face_cluster`, which gets `retracted` status on supersession.

---

## Decision 2: Scene persistence

### Question

Are enrichment world-scenes (the fused view of asset + retrieved context the twin constructs per enrichment step) persisted for audit, or reconstructed on demand from the event history + claim references?

- **Option A — On-demand reconstruction:** Only claims are persisted. Scenes are transient. Replay reconstructs the scene from the event log + claim store + memory-mesh state at the time of the run.
- **Option B — Scene persistence:** The world scene is serialized and stored alongside the run artifact. Replay reads the stored scene directly.

### Recommendation

**Option A — on-demand reconstruction; persist only the claims.**

Rationale: scenes contain fused context (memory refs, retrieved fragments, policy state) that duplicates data already in the event log and claim store. Persisting them creates a second source of truth with its own consistency burden. The K3 lifecycle event chain (`scene.built` event) already records enough to reconstruct. Replay fidelity should come from the event log, not from storing transient intermediate state.

### Owner call needed

Confirm that the event envelope captures enough scene state for replay. Specifically: is the `scene.built` event payload sufficient to reproduce the retrieval inputs (query hologram, memory refs, retrieval profile), or does the replay engine need additional structure?

---

## Decision 3: Host index writeback scope

### Question

Does the Enrichment Twin write enrichment claims back into System-Space search (the Spotlight-equivalent host index) as redacted projections, or does it stay in User/Inception Space and expose a query API that the host search layer calls?

- **Option A — Query API only:** The Enrichment Twin never touches System Space. The host search layer calls the twin's query API (or memory-mesh) to retrieve enrichment projections at query time. `GATED_HOST_UPDATE` gates query-API exposure, not a write into the immutable plane.
- **Option B — Redacted writeback:** The twin writes sensitivity-class-filtered claim projections into a System Space index segment. This requires a write path into the immutable plane, even if gated and append-only.

### Recommendation

**Option A — query-API only; never mutate System Space.**

Rationale: System Space is defined as immutable OSTree invariants. Writing into it — even with approval gates — violates the invariant that enrichment never mutates System Space, only reads it. The `GATED_HOST_UPDATE` approval gate in the seed becomes a gate on query-API activation (exposing enrichment results to the host search layer), not a write gate. This preserves the three-space invariant and keeps the immutability guarantee clean.

### Owner call needed

Confirm the host search layer (Spotlight-equivalent) has an integration path for calling an external query API rather than reading from an in-process index. If the host search architecture requires a local index write, this decision needs revisiting with a tighter scoping of what "System Space" means for the search index segment.

---

## Impact on spec

Once these three decisions are resolved:

1. Update `traits.superseded_by` / `traits.supersedes` semantics in `enrichment_claim_hologram.schema.json` if a face_cluster carve-out is added
2. Update `GATED_HOST_UPDATE` lifecycle step description in `enrichment-twin-mission-spec.md §7` to reflect Option A (query-API activation, not writeback)
3. Confirm `scene.built` event payload scope in `event_envelope.schema.json` extensions for enrichment

---

*Related: [`docs/architecture/enrichment-twin-mission-spec.md`](../architecture/enrichment-twin-mission-spec.md), [`docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`](../source-captures/GENESIS_INCEPTION_CAPTURE.md)*
