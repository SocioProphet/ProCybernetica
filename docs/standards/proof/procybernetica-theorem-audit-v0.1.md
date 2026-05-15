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
| `TBD-GROT` | governance fibration | Theorem | Theorem with proof obligation | Fibration requires lift and cleavage proof or axiom. | Discharge through governance-fibration and deterministic-cleavage standards. | open |
| `TBD-COL` | evidence aggregate | Theorem | Deferred theorem | Cocone is not a colimit until universal property is witnessed. | Require colimit witness natural in target. | open |

## Acceptance rule

A formal document is not standards-grade until all theorem-like claims have audit rows and every open row has either a proof obligation, implementation obligation, or explicit deferral.
