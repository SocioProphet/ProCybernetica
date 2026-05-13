# Tier 2 Binding Fan-Out Status

**Status:** v1.0 status artifact.

**Date:** May 13, 2026

**Scope:** Records the estate-wide Tier 2 invariant binding fan-out after the active consumer planes were bound to the ProCybernetica Tier 2 composition invariant catalog.

**Canonical catalog:** `docs/governance-fabric/TIER2_COMPOSITION_INVARIANTS.md`

## Summary

The Tier 2 composition invariant catalog is now consumed by the active estate planes that currently expose composition surfaces.

Bound planes:

```text
superconscious   cognition / certificate / trust-surface compositions
sociosphere      estate authority-dependency graph composition
policy-fabric    cancellation / fail-closed composition
agentplane       evidence receipt / replay / execution evidence composition
```

Evaluated out-of-scope for now:

```text
sourceos-syncd   local state-integrity / repair / provenance consumer surface
```

Reason: `sourceos-syncd` currently exposes state-integrity, events, identity, process-provenance, policy-normalizer, service-graph, and Semantic Enterprise state-integrity mapping validation surfaces. No `schemas/composition` lane or composition-certificate / Tier 2 binding surface was found in the current repo state.

If `sourceos-syncd` later introduces composition-producing schemas, it should receive a Tier 2 binding PR using the same pattern as the active planes.

## Bound plane details

### superconscious

Binding state:

```text
PR #14  M1 composite binding                    merged
PR #15  M5 public note binding                  merged
PR #16  lawful-learning trust-surface binding   merged
```

Composition classes:

```text
superconscious.m1.composite
superconscious.m5.public_note
superconscious.lawful_learning.trust_surface
```

Boundary posture:

```text
doctrine-only bindings
opaque hash references
no runtime receipt lookup
no runtime monitor attestation
no timestamp authenticity
no runtime claim promotion
```

### sociosphere

Binding state:

```text
PR #332  authority-dependency graph binding      merged
merge_commit: 60a0bcf29d97ed8ae144d277d4cfa5d29c21c1ef
```

Composition class:

```text
sociosphere.authority_dependency_graph
```

Boundary posture:

```text
doctrine-only binding
no runtime authority resolution
no runtime cancellation propagation
no estate topology verification
no authority chain traversal
no cross-plane runtime attestation
```

### policy-fabric

Binding state:

```text
PR #76  cancellation binding                     merged
merge_commit: 0fe197da60e26b302215b79b179d031dc490313f
```

Composition class:

```text
policy_fabric.cancellation_binding
```

Boundary posture:

```text
doctrine-only binding
no runtime cancellation execution
no runtime break-glass resolution
no cross-plane cancellation runtime propagation
no fail-closed runtime attestation
no admission decision at composition time
```

### agentplane

Binding state:

```text
PR #158  evidence receipt composition            merged
merge_commit: 6b648d39744fede6058bbdfdcaa73b5bcf44f2fe
```

Composition class:

```text
agentplane.evidence_receipt_composition
```

Boundary posture:

```text
doctrine-only binding
no runtime replay execution
no runtime evidence validation
no runtime execution attestation
no bundle-to-run integrity check
no cross-plane evidence resolution
```

## sourceos-syncd evaluation

Repository evaluated:

```text
SourceOS-Linux/sourceos-syncd
main commit observed: c2110c41adf6d9b5467906b10d4c72f130215ed2
```

Observed validation surfaces:

```text
validate-json
validate-schemas
validate-control-plane
validate-eventctl
validate-event-store
validate-events
validate-identity
validate-process-provenance
validate-policy-normalizer
validate-service-graph
validate-semantic-enterprise-state-integrity
```

Search result:

```text
No schemas/composition lane found.
No composition_certificate surface found.
No Tier 2 binding surface found.
```

Conclusion:

```text
sourceos-syncd is currently a state-integrity / repair / provenance consumer surface, not a Tier 2 composition producer.
No binding PR is required at this time.
```

## Current closure state

```text
Tier 2 catalog:                         merged in ProCybernetica
Active same-plane consumers:            bound in superconscious
Active cross-repo consumers:            bound in sociosphere, policy-fabric, agentplane
sourceos-syncd:                         evaluated out-of-scope until composition schemas appear
Cross-repo binding fan-out:             complete for active composition-producing planes
Runtime execution:                      not claimed
Recursive composition:                  not claimed
Runtime semantic verification:          not claimed
```

## Next work after this closure

Recommended next substantive lane:

```text
lawful-learning Phase 2 framework cleanup
```

Reason:

```text
The Tier 2 catalog and active-plane binding fan-out are now structurally closed for v1 doctrine-only work. The lawful-learning capture pipeline has Phase 1 merged and trust-surface binding installed, so Phase 2 framework cleanup is unblocked.
```

Alternative lanes:

```text
- ProCybernetica PR #25 / PR #49 review and merge cleanup
- 14-fragment interpretability harness binding pre-stage
- Neuronpedia integration workstream
- Tier 2 v2 runtime-backed mode design
```
