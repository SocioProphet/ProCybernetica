# Faithful Admission Policy

Status: public-safe policy draft  
Date: 2026-05-13  
Scope: admission of additional clusters, pods, or nodes into the Triune lab mesh

## Policy statement

No candidate joins the Triune mesh merely because it is reachable. A candidate is admitted only when a complete admission pack passes structural validation, dry-run policy checks, epsilon gates, boundary-axis gates, and host approval.

Until a delegated approval policy exists, host approval is mandatory. Automation may propose admission; it may not unilaterally approve or admit.

## Admission states

```text
observed
candidate
dry_run
proposed
approved
admitted
quarantined
revoked
rejected
```

Only `admitted` members may receive the faithful-member role. `proposed` and `approved` are not runtime membership states.

## Required admission pack

A valid pack must include:

1. candidate identity;
2. candidate role request;
3. Event-IR or equivalent state snapshot;
4. proof artifact references;
5. SBOM reference;
6. image references;
7. signature references;
8. network policy reference;
9. policy dry-run result;
10. epsilon gate result;
11. boundary-axis readings;
12. authority-chain reference;
13. approval record when approved or admitted;
14. reversal plan;
15. non-claims;
16. ledger entry.

## What faithful admission means structurally

Faithful admission is not administrative recording. An admission pack is faithful if and only if:

1. **Epsilon gate result is hash-bound.** When `epsilon_gate_passed` is `true`, or when `decision.gate_result` is `pass`, the admission pack must carry `dry_run_output_hash`: a content hash of the actual dry-run output that produced the pass result. An epsilon gate claimed as passed without this hash is an administrative record, not a faithful admission.

2. **Dry-run evidence is referenced.** `dry_run_evidence_ref` must point to the evidence artifact produced by the dry-run policy check. The reference is opaque at admission time; it is not resolved during structural validation. It must still be present and non-empty.

3. **Host approval is traceable.** Approved or admitted packs must carry a host approval record through `admission_decision.approvals`. The approval record must be verifiable independently of the admission pack by the later authority-verification layer.

## The failure mode this prevents

A component that passes an administrative gate, where an operator records `epsilon_gate_passed: true` or `decision.gate_result: pass` without the system having actually executed the dry-run policy check, would be admitted without faithful basis. The hash-binding requirement makes this structurally impossible: without the dry-run output hash and dry-run evidence reference, the validator rejects the admission pack regardless of what the epsilon-gate claim says.

This follows the same discipline as Tier 2 evidence freshness invariants: evidence receipts cited in a composition must declare their creation time and class; an admission pack's epsilon-gate claim must declare its dry-run hash. In both cases, the structural requirement prevents claims from floating free of the evidence that grounds them.

## Minimum policy checks

The policy dry-run must check at least:

```text
default-deny-networkpolicy
signed-images-required
no-privileged-pods
no-host-pid
resource-limits-required
```

Any violation blocks admission unless a documented exception policy exists. The current v0 policy has no exception lane.

## Epsilon and boundary gates

The default v0 thresholds are:

```text
micro epsilon_eff <= alpha
meso epsilon_eff <= 2 alpha
macro median epsilon_eff <= 3 alpha
macro p95 epsilon_eff <= 4 alpha
each boundary axis value < threshold
```

The default alpha from the source blueprint is:

```text
alpha = 0.00730
```

Alpha may become a per-lab policy value in later versions, but must be explicitly recorded in each epsilon gate object.

## Approval rule

Approval must be explicit.

For `approved` or `admitted` decisions, `admission_decision.approvals` must contain at least one approval with:

```text
approval_kind: host
approved_by: <operator or host authority>
approved_at: <date-time>
```

The structural validator enforces this rule for approved/admitted states.

## Revocation rule

Every admission pack must include a reversal plan. A member that cannot be revoked should not be admitted.

Minimum reversal plan:

1. remove mesh/federation membership;
2. revoke service credentials;
3. restore deny-all egress;
4. quarantine or stop workloads;
5. record the revocation ledger entry;
6. preserve evidence for replay.

## What faithful admission does not claim

Faithful admission is a structural gate, not a semantic verification engine. These non-claims name the boundary:

- It does not verify that the dry-run output hash is cryptographically authentic. Hash authenticity verification is deferred to runtime infrastructure.
- It does not verify that the dry-run evidence artifact exists or is accessible. The reference is structurally required but not resolved at admission time.
- It does not verify that host approval was granted by the right authority for the admission class. Authority verification is a separate governance concern.
- It does not imply production authorization. The Triune lab is a controlled substrate for governed experimentation, defensive validation, and cybernetic infrastructure hardening. Attaching production systems, customer systems, or third-party networks requires a separate policy and explicit authorization.
