# Privacy-Preserving Evidence

## Purpose

This document fills the Tier 1.5 gap between evidence retention and privacy protection.

The Cybernetic Governance Fabric requires digital evidence. It does not require maximal raw-data exposure.

## Core doctrine

Evidence minimization is not evidence deletion.

The goal is to preserve enough information to audit claims while avoiding unnecessary exposure of private, sensitive, proprietary, or security-relevant content.

## Evidence modes

### Raw evidence

Original trace, prompt, output, dataset row, artifact, or log.

Use only when required for audit and permitted by policy.

### Redacted evidence

Raw evidence with sensitive fields removed or masked.

Requires a redaction map describing what was removed and why.

### Hashed evidence

Content hash proves stable identity without exposing content.

Useful for source-locking, fixture validation, and privacy-preserving references.

### Committed evidence

Cryptographic commitment to evidence that may later be opened.

Useful when immediate disclosure is unnecessary but later auditability must be preserved.

### Aggregated evidence

Statistical summary over private rows.

Must record aggregation method and minimum cohort size.

### Zero-knowledge or succinct evidence

Proof that a property holds without revealing full witness data.

Tier 2/3 target. Not assumed in Tier 1 MVP.

### Sealed witness evidence

Evidence held in a restricted-access store with public hash and access policy.

Useful for safety-sensitive or privacy-sensitive material.

## Evidence minimization decision tree

1. Can the claim be audited from a hash? Use hash.
2. If not, can it be audited from aggregate statistics? Use aggregate.
3. If not, can it be audited from redacted content? Use redaction.
4. If not, can it be audited from a commitment plus restricted opening? Use commitment or sealed witness.
5. If raw evidence is required, record why no weaker mode suffices.

## Required metadata

Every privacy-preserving evidence object should record:

```text
evidence_mode
raw_available
redaction_policy
hash_algorithm
commitment_scheme
sealed_witness_policy
privacy_risk_class
audit_sufficiency_rationale
opening_conditions
retention_period
```

## Privacy risk classes

### P0 — Public

Safe to publish.

### P1 — Internal

Internal evidence, low privacy risk.

### P2 — Sensitive

Contains user, operational, security, or proprietary information.

### P3 — Sealed

High-risk evidence that may only be opened under declared authority.

### P4 — Non-retainable raw

Raw form must not be retained; only commitment, aggregate, or redacted form is allowed.

## Interaction with off-history retention

Off-history must be retained, but it may be retained as privacy-preserving evidence.

A blocked action involving sensitive data may preserve:

- action type;
- authority path;
- hash of input;
- redacted reason;
- monitor alert;
- blocked-output commitment;
- retention policy.

It need not preserve raw sensitive content unless audit requires it.

## Interaction with public claims

A public claim must not expose sealed evidence unless publication authority explicitly approves disclosure.

Public evidence bundles should prefer hashes, redactions, summaries, and non-sensitive fixtures.

## Non-claim boundary

This document defines evidence-minimization doctrine. It does not implement cryptographic proof systems, redaction engines, or sealed-witness storage.
