# ProCybernetica Colimit Witness Standard v0.1

Status: Draft standard  
Theorem-audit row: `TBD-COL`  
Runtime claim: none

## Purpose

This standard defines structural colimit-witness records for evidence cocones.

A witness record may assert a candidate universal-property posture, but only under an explicit evidence status. It must not silently convert a cocone into a proven colimit.

## Colimit candidate

A colimit candidate references:

- an evidence cocone;
- an apex evidence object;
- source objects;
- comparison target objects;
- mediator witnesses;
- uniqueness posture;
- naturality posture;
- theorem-audit references.

## Universal-property posture

The required field `universal_property_status` records the epistemic state of the universal-property claim.

Allowed values:

- `not_asserted` — no universal property is claimed;
- `structural_candidate` — the record has enough structure to review as a candidate;
- `review_required` — a human or formal review is required;
- `counterexample_found` — candidate failed;
- `proved_elsewhere` — proof is external and must be cited.

Only `proved_elsewhere` may be used to support a future theorem-audit closure, and only if the proof reference is present and independently reviewable.

## Mediator witness

A mediator witness records how a competing target receives a unique mediating map from the apex candidate.

This tranche requires mediator records to be explicit. It does not prove mediator uniqueness.

## Uniqueness posture

The required field `uniqueness_status` records whether uniqueness is not asserted, structurally claimed, review-required, counterexampled, or externally proved.

## Relation to `TBD-COL`

`TBD-COL` remains open after this tranche.

This standard discharges only the structural-documentation obligation: colimit witnesses are now representable, fixture-backed, and CI-validated. Full theorem closure still requires a proof or formal downgrade of the theorem claim.

## Schema anchor

```text
schemas/procybernetica/colimit-witness.v0.1.schema.json
```

## Non-claims

This standard does not prove a colimit, does not prove mediator uniqueness, does not assert naturality, does not implement runtime construction, does not discharge `TBD-COL`, and does not discharge `TBD-GROT`.
