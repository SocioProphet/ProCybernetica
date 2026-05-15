# ProCybernetica Governance Canonical Forms Standard v0.1

Status: Draft standard  
Theorem-audit row: `TBD-GNF`  
Runtime claim: none

## Purpose

This standard defines governance-token canonical forms after deterministic cleavage.

It builds on:

- `procybernetica-governance-substrate-v0.1.md`;
- `procybernetica-governance-fibration-v0.1.md`;
- `procybernetica-deterministic-cleavage-v0.1.md`.

## Canonical token

A governance token is in canonical form only when it contains:

- `token_id`;
- `projection_role`;
- `admissibility_role`;
- `cleavage_version`;
- optional digest or source token reference.

The token-intersection invariant from the substrate remains mandatory:

```math
\mathcal T_{\mathrm{tokens}}\subseteq\Pi\cap\mathcal C.
```

`projection_role` witnesses the token's projection authority. `admissibility_role` witnesses its policy/admissibility constraint. `cleavage_version` identifies the deterministic normal-form rule applied.

## Normal-form rule

A canonical form is a versioned representative of a governance token after cleavage.

A normal-form record must not discard:

- source token identity;
- projection role;
- admissibility role;
- base context;
- cleavage version.

## Uniqueness posture

This standard does not by itself prove mathematical uniqueness. It records the required structure for a future uniqueness proof or accepted axiom.

`TBD-GNF` remains open until the deterministic-cleavage rule is proven or accepted to choose a unique representative for each admissible input under a fixed cleavage version.

## Schema anchors

Canonical tokens appear in:

- `schemas/procybernetica/governance-fibration.v0.1.schema.json`;
- `schemas/procybernetica/cleavage-operation.v0.1.schema.json`.

## Non-claims

This standard does not implement a canonicalization engine, does not claim uniqueness as a proven theorem, and does not provide evidence-cocone or colimit witnesses.
