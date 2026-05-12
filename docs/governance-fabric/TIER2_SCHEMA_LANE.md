# Tier 2 Schema Lane: Composition Certificate

## Status

This lane implements the first Tier 2 schema slice for Governance Fabric and three follow-up integration slices.

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
tests/fixtures/governance-fabric/tier2/negative_composition_missing_receipt_binding.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_unknown_receipt_binding.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_receipt_hash_mismatch.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_unsupported_authority_scope.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_unhandled_non_claim.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_resolution_missing_evidence.synthetic.json
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

## Evidence receipt integration

Composition certificates use hash-bound receipt references.

Design decision:

```text
integration_mode: hash_bound_reference
```

The certificate names receipt IDs and hashes. It does not embed full receipt payloads or perform runtime receipt-store lookup.

This closes the audit seam between constituent artifacts and the composition certificate without introducing runtime dependency.

The schema supports future recursion by allowing receipt references of kind:

```text
evidence_receipt
composition_certificate
```

v0.1 uses the shape without enabling recursive composition.

## Authority scope comparison

Composition certificates include:

```text
authority_scope_analysis
comparison_mode: declared_scope_lattice_v1
```

The static harness computes supported scope from constituent declarations plus the declared lattice. A broader scope supports narrower scopes declared by the lattice. Narrower scopes do not automatically support broader scopes.

This closes the laundering path where a composition rule allows a broad scope but no constituent artifact actually supports it.

## Structured non-claim analysis

Composition certificates may include:

```text
non_claim_analysis
analysis_mode: explicit_propagate_or_resolve_v1
```

When present, the static harness requires every source non-claim to be explicitly propagated or resolved. Resolutions must cite declared evidence receipts.

This turns non-claim propagation from a string-list comparison into a source-bound trace of what happened to each constituent limitation.

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

### T2.6 — Receipt coverage for every constituent artifact

Every constituent artifact must have at least one receipt binding.

Negative fixture:

```text
negative_composition_missing_receipt_binding.synthetic.json
```

### T2.7 — No unknown receipt bindings

Receipt bindings must not reference artifacts outside the constituent set.

Negative fixture:

```text
negative_composition_unknown_receipt_binding.synthetic.json
```

### T2.8 — Receipt binding hash must match constituent artifact hash

The hash in each receipt binding must match the referenced constituent artifact hash.

Negative fixture:

```text
negative_composition_receipt_hash_mismatch.synthetic.json
```

### T2.9 — Declared receipt list must include all receipt bindings

The top-level `evidence_receipt_refs` list must include all hash-bound constituent receipt bindings and the composition certificate's own receipt reference.

This is checked in the Tier 2 static invariant harness.

### T2.10 — Composed authority scope must be constituent-supported

The composed authority scope must be supported by constituent-declared scopes under the declared scope lattice.

Negative fixture:

```text
negative_composition_unsupported_authority_scope.synthetic.json
```

### T2.11 — Every source non-claim must be handled

When `non_claim_analysis` is present, every source non-claim must be propagated or resolved.

Negative fixture:

```text
negative_composition_unhandled_non_claim.synthetic.json
```

### T2.12 — Non-claim resolutions require declared evidence

A resolution record must cite an evidence receipt that appears in the top-level `evidence_receipt_refs` list.

Negative fixture:

```text
negative_composition_resolution_missing_evidence.synthetic.json
```

## Runtime boundary

This lane is schema/fixture/static-check only.

It does not claim:

- runtime governance over live multi-agent systems;
- recursive composition semantics;
- meta-governance;
- formal hypergraph proof;
- TLA+/Alloy/Lean verification;
- cryptographic receipts;
- runtime receipt-store lookup;
- full semantic authority lattice beyond declared fixture scopes;
- runtime verification of non-claim resolution evidence.

## Next after merge

If the structured non-claim analysis slice merges green, the next Tier 2 implementation slice should be:

```text
monitor-independence composition checks
```
