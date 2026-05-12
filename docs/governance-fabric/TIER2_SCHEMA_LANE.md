# Tier 2 Schema Lane: Composition Certificate

## Status

This lane implements the first Tier 2 schema slice for Governance Fabric and five follow-up integration slices.

Tier 2 v0.1 scope is governance over flat compositions. Recursive composition and meta-governance remain deferred.

## Scope

Implemented schema:

```text
schemas/governance-fabric/composition_certificate.v1.json
```

Implemented fixtures include the positive composition certificate fixture and negative fixtures for status, authority, receipt binding, authority-scope, non-claim, monitor-independence, and evidence-freshness failures.

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

## Authority scope comparison

Composition certificates include:

```text
authority_scope_analysis
comparison_mode: declared_scope_lattice_v1
```

The static harness computes supported scope from constituent declarations plus the declared lattice. A broader scope supports narrower scopes declared by the lattice. Narrower scopes do not automatically support broader scopes.

## Structured non-claim analysis

Composition certificates may include:

```text
non_claim_analysis
analysis_mode: explicit_propagate_or_resolve_v1
```

When present, the static harness requires every source non-claim to be explicitly propagated or resolved. Resolutions must cite declared evidence receipts.

## Monitor-independence analysis

Composition certificates may include:

```text
monitor_independence_analysis
analysis_mode: declared_monitor_independence_v1
```

When present, the static harness checks monitor coverage, monitor evidence receipts, distinct monitor requirements, self-monitoring prohibition, and acyclic monitor graphs.

## Evidence freshness analysis

Composition certificates may include:

```text
evidence_freshness_analysis
analysis_mode: declared_evidence_freshness_v1
```

When present, the static harness checks that every declared evidence receipt has a freshness record, each receipt class is bound to a declared window, fresh receipts are within their declared windows, refreshed receipts cite declared refresh receipts, and stale acknowledgments cite propagated or resolved non-claims.

This is declared freshness only. Receipt timestamps, receipt classes, and freshness windows are issuer-declared in v1.

## Invariants enforced

### T2.1 — No implicit composition

A multi-artifact composite claim does not satisfy Tier 2 unless it has a composition certificate.

### T2.2 — No synthetic-to-runtime promotion by composition

A composition of synthetic or doctrine-only constituents cannot claim `runtime_executed`.

### T2.3 — No missing authority-chain coverage

Every constituent artifact's authority chain must be represented in the composition certificate.

### T2.4 — Non-claim propagation

All constituent non-claims must be propagated or explicitly resolved.

### T2.5 — Authority scope bounded by composition rule

The composed authority scope must be a subset of `composition_rule.allowed_authority_scope`.

### T2.6 — Receipt coverage for every constituent artifact

Every constituent artifact must have at least one receipt binding.

### T2.7 — No unknown receipt bindings

Receipt bindings must not reference artifacts outside the constituent set.

### T2.8 — Receipt binding hash must match constituent artifact hash

The hash in each receipt binding must match the referenced constituent artifact hash.

### T2.9 — Declared receipt list must include all receipt bindings

The top-level `evidence_receipt_refs` list must include all hash-bound constituent receipt bindings and the composition certificate's own receipt reference.

### T2.10 — Composed authority scope must be constituent-supported

The composed authority scope must be supported by constituent-declared scopes under the declared scope lattice.

### T2.11 — Every source non-claim must be handled

When `non_claim_analysis` is present, every source non-claim must be propagated or resolved.

### T2.12 — Non-claim resolutions require declared evidence

A resolution record must cite an evidence receipt that appears in the top-level `evidence_receipt_refs` list.

### T2.13 — Distinct monitor requirement

When `monitor_independence_analysis.independence_claim.requires_distinct_monitors` is true, distinct constituent artifacts must not share the same monitor.

### T2.14 — No self-monitoring

When `monitor_independence_analysis.independence_claim.forbids_self_monitoring` is true, a monitor may not monitor an artifact with the same identifier.

### T2.15 — Acyclic monitor graph

When `monitor_independence_analysis.independence_claim.requires_acyclic_monitor_graph` is true, monitor relationships must form an acyclic graph.

### T2.16 — Freshness coverage completeness

When `evidence_freshness_analysis` is present, every top-level `evidence_receipt_refs` entry must have a corresponding freshness record.

Negative fixture:

```text
negative_composition_unanalyzed_receipt.synthetic.json
```

### T2.17 — Freshness window class binding

Every freshness record's `receipt_class` must be declared in `freshness_windows`.

Negative fixture:

```text
negative_composition_unbound_receipt_class.synthetic.json
```

### T2.18 — Fresh evidence must be within its declared freshness window

A receipt with status `fresh` must have a declared age within the class freshness window, and `age_seconds` must match the claim-time minus receipt-creation-time calculation.

Negative fixture:

```text
negative_composition_stale_evidence_claimed_fresh.synthetic.json
```

### T2.19 — Refreshed evidence requires declared refresh evidence

A receipt with status `refreshed` must cite a refresh receipt present in top-level `evidence_receipt_refs`.

Negative fixture:

```text
negative_composition_refresh_without_evidence.synthetic.json
```

### T2.20 — Stale acknowledgments require propagated or resolved non-claims

A receipt with status `acknowledged_stale` must cite a non-claim present in top-level `propagated_non_claims` or `resolved_non_claims`.

Negative fixture:

```text
negative_composition_stale_acknowledged_without_propagation.synthetic.json
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
- runtime verification of non-claim resolution evidence;
- runtime monitor independence attestation;
- runtime verification of timestamp authenticity;
- transitive supersession-chain traversal;
- policy-governed freshness windows;
- Tier 0 receipt-class taxonomy enforcement.

## Next after merge

If the evidence-freshness composition slice merges green, the next Tier 2 implementation work that does not require new infrastructure is likely complete. The remaining documented candidates require dependency resolution:

```text
constituent authority concentration: reputation or signer-weight substrate
scope coverage: scope lattice definition
```
