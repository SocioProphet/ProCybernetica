# Tier 2 Composition Invariants

**Status:** v1.0 doctrine. Consolidates the Tier 2 composition invariant family. Cross-repo reference document.

**Date:** May 12, 2026

**Scope:** Defines the structural pattern under which Tier 2 flat composition certificates enforce invariants on what compositions can and cannot silently do. Consumed by reference from `superconscious`, the interpretability harness, and any other plane that produces compositions of governed artifacts.

**Boundary:** Tier 2 only. Recursive composition is explicitly deferred to Tier 3+. Runtime semantic verification of invariant content is explicitly deferred and is not claimed by any v1 analysis mode here.

## 1. What this document is

This document is the canonical reference for the Tier 2 composition invariant family. It does three things:

1. Names the structural pattern under which Tier 2 invariants are defined, enforced, and versioned.
2. Catalogs the currently merged invariants as instances of that pattern.
3. Specifies how future invariants extend the catalog without breaking the existing fixture corpus.

Repos that produce Tier 2 compositions reference this document rather than re-deriving the pattern. The pattern is plane-agnostic; only the content of specific invariants is plane-specific.

## 2. Why consolidation matters

Without a single reference document, the invariant pattern would be re-derived in each repo that ships a Tier 2 composition. The re-derivation risks are:

- inconsistent invariant shapes;
- inconsistent boundary preservation;
- inconsistent fixture conventions;
- inconsistent versioning.

This document fixes all four by specifying the canonical pattern once and pointing planes at it.

## 3. The Tier 2 composition invariant pattern

A Tier 2 composition invariant is defined by six elements.

### 3.1 Analysis field

A named field on the composition certificate schema that, when present, asserts the invariant applies and provides the structural data the invariant checks operate on.

Naming convention:

```text
<concern>_analysis
```

Examples:

```text
non_claim_analysis
monitor_independence_analysis
```

### 3.2 Analysis mode

A required string field inside the analysis field declaring which version of the invariant family is being applied.

Naming convention:

```text
<descriptor>_<mechanism>_v<N>
```

Examples:

```text
explicit_propagate_or_resolve_v1
declared_monitor_independence_v1
```

The descriptor prefix carries boundary semantics:

- `explicit_` means the invariant operates on explicitly declared structure.
- `declared_` means the invariant operates on declarations, not verified runtime behavior.
- Future descriptors may include `verified_`, `behavioral_`, `probabilistic_`, or `time_windowed_` when their semantics differ.

### 3.3 Structural admission requirements

A set of constraints expressed in JSON Schema or cross-field validation rules.

Each constraint must be named, have a clear failure-mode statement, and be fixture-testable.

### 3.4 Positive fixtures

Synthetic fixtures that satisfy all of the invariant's constraints. These exercise the analysis field with valid data and confirm the schema admits the composition.

### 3.5 Negative fixtures

Synthetic fixtures that violate specific invariant constraints. Each negative fixture targets one named constraint failure.

Filename pattern:

```text
negative_composition_<violation>.synthetic.json
```

### 3.6 Explicit non-claims

A non-claims list documenting what the invariant analysis does not verify. Boundary statements distinguish structural-admission checks from runtime-semantic checks.

At minimum, each mode must state:

```text
No runtime verification of <invariant content> is claimed.
```

## 4. Catalog of merged Tier 2 invariants

### 4.1 Composition certificate baseline

**Status:** Merged in PR #37. Commit `73d2320767eebf2df485bab94b857b15080ceff0`.

**Concern:** A multi-artifact claim can otherwise present itself as a composition without carrying a load-bearing composition artifact.

**Core fields:**

```text
composition_order: 1
composition_kind: flat_agent_composition
recursive_composition_allowed: false
```

**Structural admission requirements:**

1. Composite claims require a composition certificate.
2. A composition cannot upgrade execution status beyond the weakest constituent.
3. Every constituent authority chain must be covered.
4. The composed authority scope must be bounded by the composition rule.
5. Constituent non-claims must be propagated or resolved.

**Negative fixtures:**

```text
negative_composite_claim_without_composition_certificate.synthetic.json
negative_composition_status_boundary.synthetic.json
negative_composition_missing_authority_coverage.synthetic.json
```

**Non-claims:**

- No recursive composition is claimed.
- No runtime orchestration is claimed.
- No formal hypergraph proof is claimed.

### 4.2 Evidence receipt integration

**Status:** Merged in PR #38. Commit `c3c288612a46167cb3b3a1c7f89f12faedb08962`.

**Analysis field:** `receipt_integration`

**Integration mode:** `hash_bound_reference`

**Concern:** A composition can otherwise reference constituent artifacts while leaving their evidence chain implicit.

**Structural admission requirements:**

1. Every constituent artifact must have at least one receipt binding.
2. Receipt bindings must not reference unknown constituent artifacts.
3. Receipt binding hashes must match referenced constituent artifact hashes.
4. Top-level `evidence_receipt_refs` must include all hash-bound constituent receipts and the composition certificate receipt.

**Negative fixtures:**

```text
negative_composition_missing_receipt_binding.synthetic.json
negative_composition_unknown_receipt_binding.synthetic.json
negative_composition_receipt_hash_mismatch.synthetic.json
```

**Non-claims:**

- No runtime receipt-store lookup is claimed.
- No embedded full receipt verification is claimed.

### 4.3 Authority scope comparison

**Status:** Merged in PR #48. Commit `0b28e1fe66346b49554bbf51d62454008b42bce3`.

**Analysis field:** `authority_scope_analysis`

**Analysis mode:** `declared_scope_lattice_v1`

**Concern:** A composition rule can otherwise permit a broad scope that no constituent artifact actually supports.

**Structural admission requirements:**

1. Scope analysis must bind every constituent artifact.
2. Scope analysis must not reference unknown constituent artifacts.
3. The composed authority scope must be supported by constituent-declared scopes under the declared scope lattice.
4. A broader scope supports declared narrower scopes.
5. A narrower scope does not imply a broader scope.

**Negative fixture:**

```text
negative_composition_unsupported_authority_scope.synthetic.json
```

**Non-claims:**

- No runtime scope algebra is claimed.
- No formal scope-lattice proof is claimed.
- No full semantic authority lattice beyond declared fixture scopes is claimed.

### 4.4 Non-claim propagation

**Status:** Merged in PR #54. Commit `b6d1ad9bb13d812eb72baed2fff5bc7a8ce6641e`.

**Analysis field:** `non_claim_analysis`

**Analysis mode:** `explicit_propagate_or_resolve_v1`

**Concern:** Compositions can silently narrow the non-claim surface of their constituents.

If artifact A has non-claim X and artifact B has non-claim Y, the composition of A and B must address both X and Y, either by propagating them upward into the composition's non-claims or resolving them with explicit evidence.

**Structural admission requirements:**

1. `source_non_claims` must match constituent non-claims.
2. Every source non-claim must appear in `propagated_non_claims` or `resolved_non_claims`.
3. Propagation records must appear in `propagated_non_claims`.
4. Resolution records must appear in `resolved_non_claims`.
5. Resolution records must cite evidence receipts declared in `evidence_receipt_refs`.

**Negative fixtures:**

```text
negative_composition_unhandled_non_claim.synthetic.json
negative_composition_resolution_missing_evidence.synthetic.json
```

**Non-claims:**

- No runtime verification of non-claim resolution evidence is claimed.
- A cited evidence receipt is structurally required but not semantically verified.

**Future v2 direction:**

A `verified_propagate_or_resolve_v2` mode could require evidence receipts cited in resolution to carry a `resolves_claim_refs` array enumerating which claims they assert resolution of.

### 4.5 Monitor independence

**Status:** Merged in PR #55. Commit `9ed2983b7ccacccb10f0ec274359a97e31d2e4a9`.

**Analysis field:** `monitor_independence_analysis`

**Analysis mode:** `declared_monitor_independence_v1`

**Concern:** Compositions can silently consolidate monitoring authority.

If artifact A is monitored by M_A and artifact B is monitored by M_B, a composition of A and B that claims independent monitoring requires declared structural distinctness between M_A and M_B.

**Structural admission requirements:**

1. Monitor analysis must cover every constituent artifact.
2. Monitor attestations must cite declared evidence receipts.
3. Distinct monitors are required when claimed.
4. Self-monitoring is forbidden when claimed.
5. Monitor graph must be acyclic when claimed.

**Negative fixtures:**

```text
negative_composition_shared_monitor.synthetic.json
negative_composition_self_monitoring.synthetic.json
negative_composition_monitor_cycle.synthetic.json
```

**Non-claims:**

- No runtime monitor independence attestation is claimed.
- The structural checks verify the declared monitor graph only.

**Future v2 directions:**

A `verified_monitor_independence_v2` mode could require runtime-backed monitor attestation evidence. A `behavioral_monitor_independence_v2` mode could add statistical independence checks across monitor outputs.

## 5. Pattern guarantees

Each catalog entry provides four operational guarantees.

### 5.1 Schema-level enforcement

The invariant is encoded in the composition certificate schema and static validation harness.

### 5.2 Negative-fixture coverage

Every named failure mode has at least one negative fixture. The negative fixtures are not documentation; they are CI-asserted failure modes.

### 5.3 Mode versioning

The `analysis_mode` field locks the composition to a specific version of the invariant family. Future modes can land alongside existing modes without breaking the existing fixture corpus.

### 5.4 Explicit boundary

Every analysis mode includes non-claims about what is not verified. The boundary between structural checks and runtime semantic verification is documented per mode.

## 6. How new Tier 2 invariants enter the catalog

A new Tier 2 invariant is added when:

1. A composition failure mode is identified that the existing catalog does not address.
2. A PR lands a schema field, analysis mode, structural admission requirements, positive fixtures, negative fixtures, and explicit non-claims.
3. This document is updated with the new invariant under Section 4.

The pattern is the contract. The content varies per concern.

## 7. Cross-repo references

Repos that produce Tier 2 compositions should reference this document rather than re-derive the pattern.

### 7.1 superconscious

The certificate program produces Tier 2 compositions at multiple levels:

- M1 composite: source-lock, witness card, causal triad, off-target audit, and related fragments.
- M5 public note: upstream certificates composed into a publication surface.
- Interpretability harness release bundles: multiple interpretability artifacts composed into a public claim surface.

Non-claim propagation applies directly. Monitor independence applies when the composition claims independent review or monitoring.

### 7.2 sociosphere

The estate authority-dependency graph is structurally a Tier 2 composition. Non-claim propagation applies to each plane's authority limits. Monitor independence applies to AuthorityDependency monitor edges.

### 7.3 policy-fabric

Cancellation bindings that compose across multiple cancellation sources are Tier 2 compositions. Non-claim propagation applies. Monitor independence applies where cancellation monitors are claimed independent from cancellation targets.

### 7.4 agentplane

Evidence receipt compositions that aggregate evidence from multiple runs are Tier 2 compositions. Non-claim propagation applies. Monitor independence may apply when evidence aggregation involves multiple independent witnesses.

## 8. What this document does not commit to

This document does not commit to:

- recursive composition;
- meta-governance;
- runtime semantic verification;
- formal proof machinery;
- cross-tier composition involving Tier 3+ recursive composition.

## 9. Open extensions

Three Tier 2 invariants are plausible next slices.

### 9.1 Evidence freshness analysis

**Concern:** Compositions can silently consolidate stale evidence.

**Proposed analysis mode:** `declared_evidence_freshness_v1`

Probable invariants:

- receipts must declare creation time;
- freshness windows per receipt class must be declared;
- receipts older than their window must be refreshed or acknowledged in non-claims;
- supersession chains must resolve to the latest non-superseded receipt.

### 9.2 Constituent authority concentration analysis

**Concern:** Authority chains across constituents may concentrate around a single signer.

**Proposed analysis mode:** `declared_authority_concentration_v1`

Probable invariants:

- distinct signers across constituents must be counted;
- concentration index must be computed and declared;
- shared signers must be enumerated;
- concentration above threshold must become a non-claim or require additional evidence.

### 9.3 Scope coverage analysis

**Concern:** Compositions can claim coverage that exceeds the union of constituent scopes.

**Proposed analysis mode:** `declared_scope_coverage_v1`

Probable invariants:

- composition scope must be a subset of constituent scope union unless excess scope is independently justified;
- scope expressions must use a declared comparable lattice;
- excess scope must be explicitly declared and evidence-bound.

## 10. Status

```text
Document version:                v1.0
Merged invariants in catalog:    5
Future invariants documented:    3
Pattern definition:              Complete for v1 declared/explicit modes
Boundary preservation:           Explicit per invariant
Cross-repo references:           4
Recursive composition:           Deferred
Meta-governance:                 Deferred
Runtime semantic verification:   Deferred
Formal proof integration:        Deferred
```
