# PCP-Style Replay Audit

## Purpose

This document defines the probabilistically checkable replay-audit doctrine for the Cybernetic Governance Fabric.

The naming is intentionally precise: this is a **PCP-style replay audit** discipline, not a claim that the current trace system implements a formal probabilistically checkable proof theorem, PCP compiler, or succinct proof system.

## Scope

PCP-style replay audit applies to:

- long agent action traces;
- release-delta evidence chains;
- safety-case subclaims;
- monitor logs;
- evidence-receipt chains;
- off-history branches.

## Core concepts

### Trace

A sequence of governed actions and evidence events.

### Trace commitment

A cryptographic commitment to the trace, usually via hash tree, transcript hash, or later SNARK/PCP receipt.

### Local constraint

A small checkable rule over a local portion of the trace.

Examples:

- every action has an authority reference;
- every irreversible action has approval;
- every promotion has evidence;
- every evidence reference resolves to a hash;
- every emergency action has after-action review.

### Probabilistic audit

A verifier samples trace locations and checks local constraints.

The audit does not prove every cell is correct. It gives a declared detection probability under declared sampling and adversary assumptions.

### Replay oracle

A component that can answer local trace queries without exposing the entire trace.

This may be implemented as raw trace lookup, Merkle proof, redacted evidence bundle, or future cryptographic proof.

## Technical predicate

A replay audit satisfies the PCP-style predicate when:

1. the trace is committed;
2. the constraint set is versioned;
3. the sampling method is declared;
4. sampled locations are recorded;
5. local checks return machine-readable pass/fail results;
6. detection probability is declared with assumptions;
7. redactions do not remove fields required for checked constraints.

This predicate is weaker than a formal PCP theorem but strong enough for Tier 1 governance CI.

## Why this matters

Governance must scale. Replaying every trace in full will fail under cost, privacy, and latency pressure.

PCP-style audit gives the assurance plane statistical replay teeth: small checks with explicit detection probability.

## Certificate fields

A PCP-style replay audit certificate should record:

```text
trace_commitment
constraint_set
sampling_seed
sampled_locations
local_check_results
detection_probability_claim
privacy_redactions
failure_locations
replay_oracle_ref
```

## Acceptance rule

A trace passes PCP-style replay audit when:

- all sampled local constraints pass;
- sampling seed is recorded;
- constraint set is versioned;
- detection probability is declared;
- privacy redactions do not remove fields needed for the checked constraints.

## Failure rule

If any sampled local constraint fails, the trace is not promotion-ready. The failed location becomes off-history evidence and must be retained.

## Relation to CP-SNARK receipts

PCP-style replay audit is an assurance stepping stone.

Late Tier 2 may add CP-SNARK evidence receipts. PCP-style replay remains useful even after cryptographic receipts because it is simpler, inspectable, and cheap to run during development.

## Non-claim boundary

This document does not implement a PCP theorem or cryptographic prover. It defines a governance audit discipline inspired by probabilistically checkable proof systems.
