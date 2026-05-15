# ProCybernetica Theorem-Status Taxonomy v0.1

Status: Draft standard.

This standard defines the allowed claim-status labels for ProCybernetica mathematical, empirical, schema, and governance documents.

## Claim classes

A ProCybernetica claim must be classified as exactly one of:

```math
\text{Axiom}\mid\text{Definition}\mid\text{Proposition}\mid\text{Theorem}\mid\text{Empirical Claim}\mid\text{Conjecture}.
```

## Axiom

An axiom is a load-bearing system commitment adopted without proof inside the current standard.

Use for commitments such as deterministic cleavage, canonical token intersection, and canonical-form requirements.

Example:

```math
\mathcal T_{\mathrm{tokens}}\subseteq\Pi\cap\mathcal C.
```

## Definition

A definition introduces terminology, structure, notation, or a construction. It is not proven true or false.

Use for reversibility distance `\rho`, evidence cocone definitions, substrate tuples, token roles, and schema object classes.

## Proposition

A proposition is a provable statement under stated assumptions, usually narrower than a theorem or dependent on a named regularity condition.

Use for monotonicity of `\rho` under monotone evidence arrival, dual-update convergence under convexity and Slater-type hypotheses, and approximation guarantees.

## Theorem

A theorem is a proof-grade universal or parametric result whose hypotheses and proof obligations are explicit.

Use only when all assumptions, ambient categories, universal properties, and proof dependencies are stated.

Examples requiring theorem-grade discipline:

- Grothendieck governance fibration after cartesian lifts / cleavage are verified.
- Evidence colimit only after the natural universal property is proven.
- Posterior consistency only with identifiability constraints.

## Empirical Claim

An empirical claim is measured on a named corpus, fixture, benchmark, runtime, or calibration set. It is not a theorem.

Use for ECE thresholds, detector pass rates, observed benchmark behavior, runtime performance, and corpus-level calibration results.

## Conjecture

A conjecture is a plausible claim not yet proven, measured, or adopted as an axiom.

Use when the standard wants to preserve a research direction without encoding it as a system commitment.

## Classification rule

If a claim affects runtime behavior but is not derived from weaker assumptions, classify it as `Axiom`, not as `Theorem`.

If a claim is checked by tests or measurements, classify it as `Empirical Claim`, not as `Theorem`.

If a claim introduces an object or quantity, classify it as `Definition`, not as `Theorem`.

If a claim depends on assumptions, state the assumptions in the proposition/theorem block.
