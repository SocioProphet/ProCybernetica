# F4 Transition Observables Addendum

**Status:** Draft addendum to `docs/falsification/unified-falsification-v1.0.md`  
**Date:** May 12, 2026  
**Purpose:** Add the Cairnmark-to-Stele transition observables introduced by the transition doctrine.

---

## 1. Relationship to unified falsification v1.0

The unified falsification document v1.0 specifies F4.1 through F4.3 as reasoning-operations observables. The Cairnmark-to-Stele transition doctrine introduces three additional F4 observables that become monitorable after the v1.3 additive-field bump lands.

This addendum records F4.4, F4.5, and F4.6 until they are folded into the next unified falsification revision.

---

## 2. F4.4: Transition records absent for promoted Steles

**Condition:** If any `promoted_stele` artifact exists without a corresponding transition record referencing it, the audit chain is incomplete.

**Detection mechanism:** Schema and cross-reference validation. Every artifact with `promotion_state: promoted_stele` must resolve to a transition record whose subject points to that artifact and whose target state is `promoted_stele`.

**Revision direction:** Require transition-record generation as part of every candidate-to-Steele promotion path. Existing promoted artifacts without transition records must be backfilled or marked `superseded` until re-adjudicated.

**Severity:** S1.

**Fixture status:** Pending. Should be added with the transition-record schema.

---

## 3. F4.5: Adjudication outcome inconsistent with promotion_state

**Condition:** If a Stele's `reasoning_trace_ref` references an adjudication proofpack with outcome other than `admitted` or `partial`, the transition rules were violated.

**Detection mechanism:** Cross-field validation over `promotion_state`, `reasoning_trace_ref.adjudication_outcome`, and `reasoning_trace_ref.adjudication_authority_layer`.

**Revision direction:** Strengthen `promotion_state_requires_reasoning_trace` and the Cairnmark-to-Stele transition validator. Artifacts that violate the rule must be rejected or superseded.

**Severity:** S1.

**Fixture status:** Covered by positive and rejected transition fixtures plus a future negative fixture where `promotion_state: promoted_stele` references `adjudication_outcome: rejected`.

---

## 4. F4.6: Cairnmark composite promoted with Cairnmark fragments

**Condition:** If a composite artifact is in `promoted_stele` state but any referenced fragment is in `candidate` state, the composite-promotion rule is violated.

**Detection mechanism:** Cross-field validation over composite fragment references. Every fragment referenced by a `promoted_stele` composite must itself have `promotion_state: promoted_stele`.

**Revision direction:** Enforce `composite_fragments_match_promotion_state` in the v1.3 cross-field validator. Composite artifacts that violate the rule must fail validation.

**Severity:** S1.

**Fixture:** `tests/fixtures/transition/m1-composite-promoted-with-cairnmark-fragment.invalid.synthetic.json`.

---

## 5. Status impact

With this addendum, the falsification set becomes:

- F1.x: 3 observables;
- F2.x: 3 observables;
- F3.x: 2 observables;
- F4.x: 6 observables;
- F5.x: 3 observables;
- F6.x: 4 observables;
- F7.x: 4 observables;
- F8.x: 4 observables;
- M.x: 3 meta-observables.

Total: 23 falsification observables plus 3 meta-observables.

---

## 6. Non-claims

This addendum does not implement transition-record schemas or validators.

This addendum does not replace the unified falsification document. It is a focused supplement that should be folded into the next falsification revision.
