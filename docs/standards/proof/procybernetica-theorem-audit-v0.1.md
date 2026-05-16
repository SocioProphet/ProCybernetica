# ProCybernetica Theorem-Audit Register v0.1

Status: Draft audit register.

## Purpose

This register prevents definitions, empirical measurements, assumptions, approximations, and research conjectures from being mislabeled as theorems.

## Audit row schema

| Field | Meaning |
|---|---|
| `block_id` | Stable identifier for the claim block. |
| `source` | Manuscript, standard, schema, or repo path where the claim appears. |
| `original_label` | Claimed status before audit. |
| `audited_label` | Correct status after audit. |
| `rationale` | Reason for downgrade, upgrade, or confirmation. |
| `obligation` | Required citation, hypothesis, benchmark, schema invariant, or proof obligation. |
| `status` | `open`, `accepted`, `implemented`, or `deferred`. |

## Initial audit rows

| block_id | source | original_label | audited_label | rationale | obligation | status |
|---|---|---:|---:|---|---|---|
| `TBD-DUAL` | dual update | Theorem | Proposition | Convergence requires explicit regularity hypotheses. | Add convexity, boundedness, and duality assumptions. | open |
| `TBD-HB` | hierarchical Bayes | Theorem | Theorem with constraints | Component consistency requires identifiability constraints. | Add sum-to-zero or equivalent constraints. | open |
| `TBD-ECE` | detector calibration | Theorem | Definition plus empirical claim | Calibration threshold is measured, not universal. | Name corpus, bins, detector list, and measurement. | open |
| `TBD-SEL` | selection algorithm | Theorem | Approximation proposition | Greedy selection is not generally exact. | State approximation ratio or exact solver condition. | open |
| `TBD-RHO-E` | reversibility distance | Theorem | Definition | Existence is constructional. | Define formula, units, and domain. | open |
| `TBD-RHO-M` | reversibility monotonicity | Theorem | Proposition | Monotonicity needs monotone-arrival assumptions. | State event-arrival hypothesis. | open |
| `TBD-COP` | detector dependence | Theorem | Proposition under model assumption | Model-family assumptions affect dependence claims. | State model family and limits. | open |
| `TBD-IG` | information-gain selector | Theorem | Definition relative to criterion | Optimality needs a named objective. | Name the information-gain criterion. | open |
| `TBD-GROT` | governance fibration | Theorem | Partially discharged theorem with open obligations | G5/G6 define the governance fibration, deterministic cleavage, and canonical form structures; G7 now defines structural evidence-cocone and colimit-witness records. These artifacts support review but still do not prove full fibration law, cleavage uniqueness, canonical-form uniqueness, or universal property. | Keep open until a reviewed proof or explicit downgrade addresses cartesian lift, deterministic cleavage, canonical-form uniqueness, evidence-cocone compatibility, and colimit/universal-property obligations. | open |
| `TBD-CLEV` | deterministic cleavage | Theorem | Theorem with proof obligation | Deterministic cleavage requires a specified lift-selection rule and a structural witness that every admitted cleavage operation records its cartesian lift. | Discharge through deterministic-cleavage standard, cleavage-operation schema, valid fixture, and missing-lift rejection test plus proof or accepted axiom that the selected lifts are cartesian. | open |
| `TBD-GNF` | governance-token normal form | Theorem | Theorem with uniqueness obligation | Canonical form is only theorem-like if uniqueness is claimed for normalized tokens after cleavage. | Discharge through canonical-forms standard and schema-level requirement that canonical tokens carry projection role, admissibility role, and cleavage version plus proof or accepted axiom of uniqueness under fixed cleavage version. | open |
| `TBD-COL` | evidence aggregate | Theorem | Structural candidate with open theorem obligation | `procybernetica-evidence-cocone-v0.1.md` and `procybernetica-colimit-witness-v0.1.md` define cocone and colimit-witness records. Fixtures validate structural candidates but do not prove a universal property. | Require proof or formal review showing universal property, mediator existence, mediator uniqueness, and naturality in target; otherwise retain as structural candidate or downgrade. | open |

## G7 structural implementation note

G7 adds structural artifacts for evidence cocones and colimit witnesses:

- `docs/standards/governance/procybernetica-evidence-cocone-v0.1.md`
- `docs/standards/governance/procybernetica-colimit-witness-v0.1.md`
- `schemas/procybernetica/evidence-cocone.v0.1.schema.json`
- `schemas/procybernetica/colimit-witness.v0.1.schema.json`

These artifacts satisfy representation and validation obligations only. They do not close `TBD-GROT`, `TBD-CLEV`, `TBD-GNF`, or `TBD-COL`.

## Explicit non-row: reindex coherence

No `TBD-REINDEX` row is opened in this tranche because `schemas/procybernetica/reindex-operation.v0.1.schema.json` remains structural only. It requires `coherence_status: "not-asserted"` and does not claim functoriality, coherence, or composition law.

A future theorem-audit row is required before any document asserts reindex functoriality, cleavage compatibility, or compositional coherence.

## Acceptance rule

A formal document is not standards-grade until all theorem-like claims have audit rows and every open row has either a proof obligation, implementation obligation, or explicit deferral.