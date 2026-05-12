# Tier 2 Composition Governance Plan

## Status

Planning artifact only.

This document defines the first Tier 2 scope for the Cybernetic Governance Fabric. It does not add schemas, fixtures, runtime behavior, or formal proofs.

Tier 2 planning is unblocked because Tier 1 schema CI is merged and connector-observed green through the CI Observation Ledger.

## 1. Scope call

Tier 2 v0.1 scope is:

```text
governance over compositions
```

Tier 1 governs individual governance artifacts: authority chains, action traces, tool scopes, evidence receipts, promotion decisions, safety cases, monitor alerts, off-history evidence, and cross-program certificates.

Tier 2 governs what happens when those artifacts are composed into larger governance objects.

The central question:

```text
When multiple governed artifacts compose, what authority, evidence, safety, monitoring, and non-claim properties survive composition, and what new risks appear at the boundary?
```

## Explicit deferrals

### Meta-governance deferred

Meta-governance is the governance of the governance fabric itself: who may change schemas, update constitutional invariants, issue authority roots, or change promotion rules.

It is deferred from Tier 2 v0.1 because composition governance should be proven on ordinary composed artifacts before turning self-referential.

Deferred target:

```text
Tier 2 v0.2 or Tier 3, depending on formal-methods readiness.
```

### Runtime orchestration deferred

Tier 2 v0.1 does not govern live multi-agent runtime orchestration.

It governs composition certificates and deterministic fixture evidence. Runtime traces remain Tier 1 evidence objects until runtime execution exists.

### Formal theorem claims deferred

Tier 2 v0.1 may use graph, hypergraph, and typed-boundary vocabulary. It does not claim a completed hypergraph-category theorem, formal model-checking proof, or Lean mechanization.

## 2. Tier 2 invariants

Tier 2 invariants are stated as things the system must reject. Each invariant should have at least one negative fixture in the Tier 2 schema CI lane.

### Invariant T2.1 — No implicit composition

A composite claim must cite a composition certificate.

A safety case that relies on multiple constituent certificates without a composition certificate is invalid.

Negative fixture:

```text
negative_composite_claim_without_composition_certificate.synthetic.json
```

Expected failure:

```text
missing composition_certificate_ref
```

### Invariant T2.2 — No authority widening across composition boundary

A composed artifact may not claim authority broader than the authority explicitly available in its constituents and composition rule.

Composition must not silently upgrade authority.

Negative fixture:

```text
negative_composition_authority_widening.synthetic.json
```

Expected failure:

```text
composed_authority_scope exceeds declared composition_rule.allowed_authority_scope
```

Schema-level v0.1 enforcement can require explicit fields for:

```text
constituent_authority_scopes
composition_rule.allowed_authority_scope
composed_authority_scope
```

A later static analyzer can compare scopes semantically. The v0.1 schema can enforce field presence and fixture-level deterministic comparisons.

### Invariant T2.3 — No evidence laundering

Composition cannot erase constituent evidence gaps, failed checks, off-history branches, or non-claims.

If a constituent has a non-claim, the composed certificate must either propagate it or explicitly override it with evidence.

Negative fixture:

```text
negative_composition_drops_constituent_non_claim.synthetic.json
```

Expected failure:

```text
constituent_non_claims not represented in propagated_non_claims or resolved_non_claims
```

### Invariant T2.4 — No synthetic-to-runtime promotion by composition

A composition of `synthetic_fixture` or `doctrine_only` artifacts cannot produce a `runtime_executed` composite.

Runtime status must be monotone under composition unless a runtime execution certificate explicitly exists.

Negative fixture:

```text
negative_composition_upgrades_execution_status.synthetic.json
```

Expected failure:

```text
composite execution_status runtime_executed unsupported by constituent runtime evidence
```

### Invariant T2.5 — Monitor independence cannot increase silently

A composed monitor claim may not report independence stronger than the weakest relevant constituent monitor unless a meta-monitor certificate justifies the improvement.

Negative fixture:

```text
negative_composition_inflates_monitor_independence.synthetic.json
```

Expected failure:

```text
composed_monitor_independence exceeds constituent_monitor_independence without meta_monitor_certificate_ref
```

## 3. Tier 2 negative tests

Tier 2 v0.1 should have three to five negative fixtures.

Minimum set:

1. no implicit composition;
2. no authority widening;
3. no evidence laundering;
4. no synthetic-to-runtime promotion;
5. no monitor-independence inflation.

If implementing all five makes the first schema PR too broad, the first PR may land three and defer two. Deferrals must be explicit in the lane document.

## 4. Tier 1 schemas extended by Tier 2

Tier 2 v0.1 extends these Tier 1 surfaces:

### `schemas/composition/program-certificate.v1.json`

Primary extension point.

Tier 2 will likely add a dedicated composition certificate schema rather than mutating the v1 program certificate immediately.

Candidate schema:

```text
schemas/governance-fabric/composition_certificate.v1.json
```

### `schemas/governance-fabric/authority_chain.v1.json`

Used to define and bound composed authority.

Tier 2 may reference authority-chain fragments in constituent lists.

### `schemas/governance-fabric/cybernetic_safety_case.v1.json`

Used to ensure composed safety cases propagate non-claims, residual risks, and off-history evidence.

### `schemas/governance-fabric/evidence_receipt.v1.json`

Used to represent composition certificates as evidence receipts.

### `schemas/governance-fabric/off_history_evidence.v1.json`

Used to preserve failed composition attempts and rejected composite claims.

## 5. Formal methods in scope now vs deferred

### In scope for Tier 2 v0.1

- JSON Schema validation.
- Deterministic synthetic fixtures.
- Negative fixtures that must fail validation.
- Simple static checks implemented in pytest where schema alone cannot express the invariant.
- Explicit state-block separation for Tier 1 and Tier 2.

### Deferred

- TLA+ models of governance-state transitions.
- Alloy models of authority graph constraints.
- Lean proofs of composition invariants.
- Hypergraph-category formalization.
- Runtime trace execution.
- Cryptographic receipts.
- SNARK or PCP proof systems.

Reason for deferral:

Tier 2 v0.1 must keep the same property as Tier 1: CI passes in seconds on deterministic fixtures without runtime dependencies.

## 6. Tier 2 CI passing definition

Tier 2 CI passes when:

1. all Tier 2 schemas are syntactically valid JSON Schema;
2. all positive Tier 2 fixtures validate;
3. all negative Tier 2 fixtures fail for the intended reason;
4. cross-tier integration fixtures compose Tier 1 artifacts through the Tier 2 composition certificate;
5. `make governance-fabric-ci` includes Tier 1 and Tier 2 checks;
6. the CI Observation Ledger records green on `main` after merge.

Candidate targets:

```text
make governance-fabric-tier2-ci
make governance-fabric-ci
```

`governance-fabric-ci` should compose Tier 1 and Tier 2 once Tier 2 lands.

## 7. Doctrine-only deferrals

Tier 2 v0.1 explicitly does not claim:

- runtime governance over live multi-agent systems;
- meta-governance over constitutional change;
- formal proof of hypergraph composition;
- semantic authority-scope comparison beyond deterministic fixture checks;
- deployed monitor network;
- cryptographic receipts;
- production promotion workflow.

These remain doctrine-only until schemas, fixtures, validators, and CI gates exist.

## 8. State block shape

The program status should split Tier 1 and Tier 2 explicitly:

```text
ProCybernetica:
  tier1:
    doctrine_complete: true
    schema_ci: merged
    main_ci: green_via_ci_observation_ledger
    runtime_executed: false
  tier2:
    scope: governance_over_compositions
    doctrine_complete: planning_in_progress
    schema_ci: not_started
    runtime_executed: false
```

This avoids collapsing all governance maturity into a single field.

## 9. First implementation PR after this plan

The next Tier 2 implementation PR should be small.

Recommended first schema:

```text
schemas/governance-fabric/composition_certificate.v1.json
```

Recommended first fixtures:

```text
tests/fixtures/governance-fabric/tier2/composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composite_claim_without_composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_upgrades_execution_status.synthetic.json
```

Recommended validator:

```text
tests/test_governance_fabric_tier2.py
```

Keep authority-widening and monitor-independence inflation for the second Tier 2 implementation PR if needed.

## Non-claim boundary

This document is a planning artifact. It does not implement Tier 2 schemas, fixtures, validators, runtime behavior, or formal proofs.
