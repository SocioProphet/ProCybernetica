# ADR-0002: Enrichment Twin open decisions

**Date:** 2026-06-11  
**Status:** decided — all three recommendations adopted 2026-06-11  
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

### Decision

**Option A adopted with carve-out:** `superseded` for all modalities. `face_cluster` claims that are superseded also get `superseded` (not `retracted`) — the misidentification case is handled by the confidence-ranked default projection hiding the lower-confidence claim, not by retraction. Retraction is reserved for claims that were affirmatively wrong due to a policy violation, not for claims that were outcompeted by a better model.

---

## Decision 2: Scene persistence

### Question

Are enrichment world-scenes (the fused view of asset + retrieved context the twin constructs per enrichment step) persisted for audit, or reconstructed on demand from the event history + claim references?

- **Option A — On-demand reconstruction:** Only claims are persisted. Scenes are transient. Replay reconstructs the scene from the event log + claim store + memory-mesh state at the time of the run.
- **Option B — Scene persistence:** The world scene is serialized and stored alongside the run artifact. Replay reads the stored scene directly.

### Recommendation

**Option A — on-demand reconstruction; persist only the claims.**

Rationale: scenes contain fused context (memory refs, retrieved fragments, policy state) that duplicates data already in the event log and claim store. Persisting them creates a second source of truth with its own consistency burden. The K3 lifecycle event chain (`scene.built` event) already records enough to reconstruct. Replay fidelity should come from the event log, not from storing transient intermediate state.

### Decision

**Option A adopted.** On-demand reconstruction from event log + claim store. The `scene.built` event payload must include: query hologram ref, memory refs used, retrieval profile applied, and the locus at which retrieval ran. If replay cannot reconstruct a scene from these, that is a gap in the event envelope to fix — not a reason to persist scenes.

---

## Decision 3: Host index writeback scope

### Question

Does the Enrichment Twin write enrichment claims back into System-Space search (the Spotlight-equivalent host index) as redacted projections, or does it stay in User/Inception Space and expose a query API that the host search layer calls?

- **Option A — Query API only:** The Enrichment Twin never touches System Space. The host search layer calls the twin's query API (or memory-mesh) to retrieve enrichment projections at query time. `GATED_HOST_UPDATE` gates query-API exposure, not a write into the immutable plane.
- **Option B — Redacted writeback:** The twin writes sensitivity-class-filtered claim projections into a System Space index segment. This requires a write path into the immutable plane, even if gated and append-only.

### Recommendation

**Option A — query-API only; never mutate System Space.**

Rationale: System Space is defined as immutable OSTree invariants. Writing into it — even with approval gates — violates the invariant that enrichment never mutates System Space, only reads it. The `GATED_HOST_UPDATE` approval gate in the seed becomes a gate on query-API activation (exposing enrichment results to the host search layer), not a write gate. This preserves the three-space invariant and keeps the immutability guarantee clean.

### Decision

**Option A adopted.** Query-API only; System Space is never written by the Enrichment Twin. `GATED_HOST_UPDATE` gates query-API activation (the host search layer is permitted to call the enrichment query endpoint), not a writeback path. If the host search layer requires a local index write in future, that requires a new ADR and a System Space immutability boundary review — it is not a silent change to this decision.

---

## Impact on spec

Once these three decisions are resolved:

1. Update `traits.superseded_by` / `traits.supersedes` semantics in `enrichment_claim_hologram.schema.json` if a face_cluster carve-out is added
2. Update `GATED_HOST_UPDATE` lifecycle step description in `enrichment-twin-mission-spec.md §7` to reflect Option A (query-API activation, not writeback)
3. Confirm `scene.built` event payload scope in `event_envelope.schema.json` extensions for enrichment

---

*Related: [`docs/architecture/enrichment-twin-mission-spec.md`](../architecture/enrichment-twin-mission-spec.md), [`docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`](../source-captures/GENESIS_INCEPTION_CAPTURE.md)*
