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
| `TBD-GROT` | governance fibration | Theorem | Partially discharged theorem with open obligations | `procybernetica-governance-fibration-v0.1.md` defines the fibration standard and structural schema; full theorem status still requires downstream colimit/evidence-cocone tranche. | Keep open until cartesian lift, deterministic cleavage, canonical-form, and later evidence-cocone obligations are all discharged. | open |
| `TBD-CLEV` | deterministic cleavage | Theorem | Theorem with proof obligation | Deterministic cleavage requires a specified lift-selection rule and a structural witness that every admitted cleavage operation records its cartesian lift. | Discharge through deterministic-cleavage standard, cleavage-operation schema, valid fixture, and missing-lift rejection test. | open |
| `TBD-GNF` | governance-token normal form | Theorem | Theorem with uniqueness obligation | Canonical form is only theorem-like if uniqueness is claimed for normalized tokens after cleavage. | Discharge through canonical-forms standard and schema-level requirement that canonical tokens carry projection role, admissibility role, and cleavage version. | open |
| `TBD-COL` | evidence aggregate | Theorem | Deferred theorem | Cocone is not a colimit until universal property is witnessed. | Require colimit witness natural in target. | open |

## Explicit non-row: reindex coherence

No `TBD-REINDEX` row is opened in this tranche because `schemas/procybernetica/reindex-operation.v0.1.schema.json` is structural only. It requires `coherence_status: "not-asserted"` and does not claim functoriality, coherence, or composition law.

A future theorem-audit row is required before any document asserts reindex functoriality, cleavage compatibility, or compositional coherence.

## Acceptance rule

A formal document is not standards-grade until all theorem-like claims have audit rows and every open row has either a proof obligation, implementation obligation, or explicit deferral.