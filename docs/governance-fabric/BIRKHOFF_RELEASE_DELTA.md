# Birkhoff-Style Release-Delta Governance

## Purpose

This document defines the operational release-delta doctrine for the Cybernetic Governance Fabric.

The naming is intentionally precise: this is a **Birkhoff-style release-delta decomposition**, not a claim that governance releases admit a literal mathematical Birkhoff factorization, Connes-Marcolli renormalization proof, or Hopf-algebraic theorem.

The doctrine imports the discipline of decomposition, residue tracking, and recomposition. It does not import theorem status.

## Scope

A release delta is any change between two governed states:

```text
state_before -> state_after
```

Examples:

- model checkpoint update;
- policy update;
- prompt/system-message update;
- tool permission change;
- schema version bump;
- monitor configuration change;
- runtime dependency update;
- public claim update.

## Core intuition

A release diff is not a single object.

It decomposes into semi-independent components:

- capability delta;
- safety delta;
- authority delta;
- privacy delta;
- evidence delta;
- monitor delta;
- supply-chain delta;
- publication delta;
- rollback delta.

Promotion decisions must inspect these components separately before recomposing the release case.

## Technical predicate

A release-delta report satisfies the Birkhoff-style predicate when:

1. each declared component has a source-state and target-state reference;
2. each component has evidence or a declared evidence gap;
3. unresolved residues are named explicitly;
4. recomposition preserves component limitations and non-claims;
5. the release decision cites the component decomposition rather than only aggregate pass/fail status.

This predicate is machine-checkable at Tier 1 and formally refinable at Tier 2.

## Release-delta object

A release-delta report records:

```text
release_id
state_before_ref
state_after_ref
delta_components
evidence_refs
risk_class
rollback_plan
approval_chain
non_claims
residue_summary
```

## Component decomposition

### Capability delta

What the system can now do that it could not do before.

### Safety delta

What safety behavior changed: refusal, compliance, tool use, monitoring, policy adherence, off-target behavior.

### Authority delta

What authority paths changed: new roles, new delegations, new emergency routes, new promotion permissions.

### Privacy delta

What data exposure, retention, logging, redaction, or evidence-minimization behavior changed.

### Evidence delta

What evidence is newly available, newly missing, superseded, or invalidated.

### Monitor delta

What monitors were added, removed, weakened, strengthened, or retuned.

### Supply-chain delta

What code, model, dataset, prompt, dependency, schema, or infrastructure artifact changed.

### Publication delta

What external claims, docs, demos, releases, or public commitments changed.

### Rollback delta

What rollback path exists, and what state cannot be rolled back.

## Birkhoff-style discipline

The doctrine is:

1. decompose the release into components;
2. evaluate each component separately;
3. record irreducible risk residues;
4. recompose into a release decision;
5. preserve the decomposition in evidence.

A single green test suite cannot approve a release if one component has an unresolved high-risk residue.

## Release approval rule

A release may be promoted only if:

- each delta component has evidence;
- each high-risk component has evaluator review;
- authority changes are explicit;
- irreversible actions are approved;
- rollback or forward-fix path is declared;
- non-claims are preserved;
- off-history is retained;
- residues are explicitly accepted, rejected, or assigned follow-up ownership.

## Relation to M1-M5 interpretability certificates

An interpretability certificate is one evidence type for a release delta.

It may support the safety delta, monitor delta, or publication delta, but it does not automatically approve the release.

## Non-claim boundary

This document defines operational release-delta doctrine. It does not claim a mathematical Birkhoff factorization theorem for governance systems. Any future theorem-level claim must be placed in a formal methods lane and cited separately.
