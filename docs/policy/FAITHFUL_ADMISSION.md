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

## Non-claims

Admission policy does not imply production authorization. The Triune lab is a controlled substrate for governed experimentation, defensive validation, and cybernetic infrastructure hardening. Attaching production systems, customer systems, or third-party networks requires a separate policy and explicit authorization.
