# PCP Replay Audit

**Status:** Draft v0.1
**Track:** Tier 3 assurance extension, Tier 1/Tier 2 replay discipline
**Purpose:** Define probabilistically checkable replay artifacts for long agent traces and safety-case evidence.

---

## 1. Purpose

Full replay is expensive, sometimes impossible, and often privacy-sensitive.

A serious governance fabric needs more than trusting the log and less than rerunning everything every time. It needs replay artifacts that support efficient audit with statistical guarantees.

This document defines PCP-style replay audit: transforming long action traces and evidence bundles into probabilistically checkable objects that allow auditors to inspect small portions while retaining bounded confidence about the whole trace.

---

## 2. Scope

Applies to:

- long agent action traces;
- tool-call sequences;
- repository-change workflows;
- deployment workflows;
- monitor-alert histories;
- release-delta evidence;
- safety-case evidence bundles;
- incident timelines;
- off-history branch trees;
- public assurance claims.

---

## 3. Core concepts

### 3.1 Trace

A sequence or graph of governed events.

Examples include authority resolution, action proposal, monitor alert, tool call, environment delta, evidence receipt, and promotion decision.

### 3.2 Trace commitment

A cryptographic or digest-based commitment to the trace.

### 3.3 Local constraint

A condition that can be checked on a small part of the trace.

Examples:

- every action has authority chain;
- every tool call has permission scope;
- every promotion has evidence receipt;
- every public claim has non-claims;
- every monitor configuration change has release delta.

### 3.4 Probabilistic audit

A verifier samples trace locations and checks local constraints. Failure probability is bounded if the trace is invalid in more than a threshold fraction of locations.

### 3.5 Replay oracle

A service or artifact that answers audit queries without revealing more evidence than necessary.

---

## 4. Why this matters

Without PCP replay audit:

- long traces are rarely reviewed;
- public assurance claims become too expensive to verify;
- privacy-sensitive evidence is overexposed;
- agents can hide failure in large logs;
- auditors must choose between blind trust and full replay.

With PCP replay audit:

- long traces are compressed into checkable commitments;
- auditors can sample constraints;
- privacy-sensitive witnesses can remain sealed;
- public reports can state audit confidence;
- replay scales to large systems.

---

## 5. Audit object structure

A probabilistically checkable trace includes:

- `trace_id`
- `trace_type`
- `trace_length`
- `event_commitments`
- `constraint_set`
- `sampling_policy`
- `audit_queries`
- `audit_responses`
- `soundness_error`
- `privacy_policy`
- `evidence_receipt_ids`
- `non_replayable_segments`

---

## 6. Constraint families

### 6.1 Authority constraints

- every decision has `authority_chain_id`;
- no tool output is treated as higher authority;
- ignored lower-authority instructions are recorded;
- conflict cases are preserved.

### 6.2 Runtime constraints

- every tool call has permission scope;
- every environment mutation has delta record;
- irreversible actions have approval or stronger gate;
- rollback plan exists where required.

### 6.3 Evidence constraints

- every claim has receipt;
- every receipt has digest;
- every evidence object has privacy class;
- every off-history action is retained.

### 6.4 Promotion constraints

- no promotion by prose;
- every promotion references prior state and target state;
- every promotion includes non-claims;
- failed gates are not omitted.

### 6.5 Release constraints

- material changes have release-delta reports;
- counter-terms are recorded where detected;
- non-renormalizable changes block ordinary promotion.

### 6.6 Publication constraints

- public claims reference public-safe or redacted evidence;
- sealed evidence is not leaked;
- non-claims are included.

---

## 7. Sampling policy

Sampling policy depends on risk.

Low risk uses random sampling, low sample count, and after-the-fact audit.

Medium risk uses stratified sampling by event type, targeted sampling around gates, and periodic audit.

High risk uses dense sampling around irreversible actions, all promotions checked, all publication claims checked, and pre-promotion audit.

Critical risk may not use probabilistic-only approval. Critical risk requires full check of constitutional constraints; PCP audit supplements full review.

---

## 8. Soundness and confidence

A PCP replay audit should declare:

- fraction of trace assumed corrupted if invalid;
- sample count;
- probability of detecting corruption;
- residual soundness error;
- constraints covered;
- constraints not covered.

Example statement:

With 200 sampled constraints over a 10,000-event trace, under the assumption that any invalid trace violates at least 2% of covered constraints, the audit detects invalidity with a declared probability computed from the sampling model.

The implementation should compute this exactly for the chosen sampling model.

---

## 9. Privacy-preserving audit

Replay audit must support selective disclosure.

Techniques include hashed event commitments, Merkle proofs, redacted payloads, sealed witnesses, zero-knowledge proof targets, differential disclosure by role, and private/public trace split.

The audit should be able to prove that an event existed, satisfied a constraint, was signed by the expected actor, and linked to the correct receipt without necessarily revealing raw private content.

---

## 10. Schema obligations

### `probabilistically_checkable_trace.v1.json`

Minimum fields:

- `trace_id`
- `trace_type`
- `trace_length`
- `event_commitment_root`
- `constraint_set_id`
- `sampling_policy_id`
- `soundness_claim`
- `privacy_policy_id`
- `non_replayable_segments`

### `audit_query.v1.json`

Minimum fields:

- `query_id`
- `trace_id`
- `sample_index`
- `constraint_id`
- `requested_disclosure`

### `audit_response.v1.json`

Minimum fields:

- `query_id`
- `result`
- `proof_ref`
- `evidence_receipt_id`

---

## 11. Audit protocol

### Step 1 — Commit trace

Build a commitment tree over all events.

### Step 2 — Declare constraints

Select constraint set based on trace type and risk tier.

### Step 3 — Generate sampling plan

Define random, stratified, or targeted sampling.

### Step 4 — Issue audit queries

Verifier requests proofs for sampled events and constraints.

### Step 5 — Respond with proofs

Replay oracle returns proof, redacted evidence, sealed proof, or private-reviewer-only artifact.

### Step 6 — Compute result

Verifier computes pass/fail and residual soundness error.

### Step 7 — Attach to safety case

Audit result becomes evidence in safety case or promotion decision.

---

## 12. Example

Trace: 5,000-event agent coding session.

Risk: high.

Constraints:

- all shell commands have permission scope;
- all file writes have environment delta;
- all blocked commands have off-history;
- all monitor alerts have evidence receipts;
- all PR changes have release-delta classification.

Audit:

- all promotions checked;
- all irreversible actions checked;
- 300 random low-risk events sampled;
- 100 stratified monitor events sampled.

Result:

- one missing off-history record found;
- trace fails until remediated;
- safety case cannot promote.

---

## 13. Relationship to cryptographic receipts

PCP replay audit and cryptographic receipts are complementary.

PCP replay audit checks long traces efficiently, samples local constraints, and supports statistical assurance.

Cryptographic receipts prove specific relations under commitments, support selective disclosure, and support stronger cryptographic assurance.

Long-term target: PCP object identifies sampled constraints, while a zero-knowledge proof verifies constraint satisfaction without revealing private witness.

---

## 14. Relationship to public assurance

A public report may include:

- trace commitment root;
- constraint set;
- sampling policy;
- audit confidence;
- failed constraints count;
- non-claims;
- redaction policy.

It should not expose private raw trace unless publication-boundary review permits it.

---

## 15. Tests

- PCP-1 missing authority: a trace omits authority chain from 5% of actions. Expected: probabilistic audit detects with high probability under declared sample count.
- PCP-2 promotion by prose: one promotion lacks evidence receipt. Expected: targeted promotion audit detects with certainty.
- PCP-3 private evidence: audit query requests private prompt. Expected: response gives sealed proof or redacted artifact according to policy.
- PCP-4 hidden failed gate: safety case omits failed gate. Expected: constraint comparing claim ledger and safety case detects mismatch.

---

## 16. Implementation roadmap

Phase 1: commitment tree over event logs.

Phase 2: constraint registry.

Phase 3: sampling policy engine.

Phase 4: audit query/response API.

Phase 5: safety-case integration.

Phase 6: selected constraints backed by stronger cryptographic proofs.

---

## 17. Closing rule

Replay is not a binary choice between rerunning everything and trusting everything.

A frontier governance fabric makes long traces probabilistically checkable, privacy-preserving, and promotion-relevant.
