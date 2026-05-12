# Tier 2 Schema Lane: Composition Certificate

## Status

This lane implements the first Tier 2 schema slice for Governance Fabric.

Tier 2 v0.1 scope is governance over flat compositions. Recursive composition and meta-governance remain deferred.

## Scope

Implemented schema:

```text
schemas/governance-fabric/composition_certificate.v1.json
```

Implemented fixtures:

```text
tests/fixtures/governance-fabric/tier2/composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composite_claim_without_composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_status_boundary.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_missing_authority_coverage.synthetic.json
```

Implemented test harness:

```text
tests/test_governance_fabric_tier2.py
```

Implemented operator targets:

```bash
make governance-fabric-tier2-ci
make governance-fabric-ci
```

## Composition algebra

Tier 2 v0.1 uses flat composition only:

```text
composition_order: 1
composition_kind: flat_agent_composition
recursive_composition_allowed: false
```

Higher-order composition is deferred to v0.2.

## Invariants enforced

### T2.1 — No implicit composition

A multi-artifact composite claim does not satisfy Tier 2 unless it has a composition certificate.

Negative fixture:

```text
negative_composite_claim_without_composition_certificate.synthetic.json
```

### T2.2 — No synthetic-to-runtime promotion by composition

A composition of synthetic or doctrine-only constituents cannot claim `runtime_executed`.

Negative fixture:

```text
negative_composition_status_boundary.synthetic.json
```

### T2.3 — No missing authority-chain coverage

Every constituent artifact's authority chain must be represented in the composition certificate.

Negative fixture:

```text
negative_composition_missing_authority_coverage.synthetic.json
```

### T2.4 — Non-claim propagation

All constituent non-claims must be propagated or explicitly resolved.

This is checked in the Tier 2 static invariant harness.

### T2.5 — Authority scope bounded by composition rule

The composed authority scope must be a subset of `composition_rule.allowed_authority_scope`.

This is checked in the Tier 2 static invariant harness.

## Runtime boundary

This lane is schema/fixture/static-check only.

It does not claim:

- runtime governance over live multi-agent systems;
- recursive composition semantics;
- meta-governance;
- formal hypergraph proof;
- TLA+/Alloy/Lean verification;
- cryptographic receipts.

## Next after merge

If this lane merges green, the next Tier 2 implementation slice should choose one of:

1. authority-scope semantic comparison;
2. non-claim propagation/resolution schema refinement;
3. monitor-independence composition checks;
4. composition-certificate evidence receipt integration.
