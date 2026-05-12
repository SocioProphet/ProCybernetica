# ProCybernetica Program Status

## Status date

2026-05-12

## Program role

`SocioProphet/ProCybernetica` is the cybernetic security, governance, and resilience program for SocioProphet.

It is a sibling to `SocioProphet/superconscious`.

- `superconscious` produces interpretability certificates.
- `ProCybernetica` governs certificates, authority, actions, evidence, releases, monitoring, incidents, and public claims.

## Current state

```text
ProCybernetica:
  tier0:
    doctrine_complete: true
    runtime_executed: false
  tier1:
    doctrine_complete: true
    schema_ci: merged
    main_ci: green_via_ci_observation_ledger
    ci_observation_ledger_issue: #32
    ci_observation_receipt_commit: e639a4d0c1aaf94e0018ae0ae0e71609fb316a96
    ci_observation_receipt_run_id: 25714672871
    runtime_executed: false
  tier2:
    scope: governance_over_compositions
    doctrine_complete: planning_in_progress
    schema_ci: not_started
    runtime_executed: false
  workflow_dispatch_available: true
  production_governance_runtime: false
```

## Completed doctrine

Governance Fabric doctrine has landed under:

```text
docs/governance-fabric/
```

Current doctrine files:

```text
README.md
CONSTITUTIONAL_INVARIANTS.md
CYBERNETIC_GOVERNANCE_FABRIC.md
THREAT_MODEL.md
SEPARATION_OF_POWERS.md
BIRKHOFF_RELEASE_DELTA.md
MONITOR_NETWORK_AS_QEC.md
PCP_REPLAY_AUDIT.md
PRIVACY_PRESERVING_EVIDENCE.md
RESEARCH_RUNWAY_AI_QUANTUM.md
```

Tier 2 planning file on this branch:

```text
docs/governance-fabric/TIER2_COMPOSITION_GOVERNANCE_PLAN.md
```

## Key doctrine corrections landed

- Birkhoff language is now Birkhoff-style release-delta decomposition, not theorem-level claim.
- PCP language is now PCP-style replay audit, not formal PCP prover claim.
- Hypergraph composition is stated as a technical predicate pending formal Tier 2 proof.
- Frontier scoreboard is framed as absolute self-measurement, not competitor marketing.
- Tier 4 is explicitly research runway, not MVP surface.
- Privacy-preserving evidence is a Tier 1.5 bridge between retention and minimization.

## Tier 1 schema CI lane

PR #31 merged the first executable Governance Fabric schema lane into `main`.

Schema set:

```text
schemas/governance-fabric/authority_chain.v1.json
schemas/governance-fabric/agent_action_trace.v1.json
schemas/governance-fabric/tool_permission_scope.v1.json
schemas/governance-fabric/monitor_alert.v1.json
schemas/governance-fabric/safe_completion_decision.v1.json
schemas/governance-fabric/off_history_evidence.v1.json
schemas/governance-fabric/evidence_receipt.v1.json
schemas/governance-fabric/promotion_decision.v1.json
schemas/governance-fabric/cybernetic_safety_case.v1.json
schemas/composition/program-certificate.v1.json
```

Negative constitutional fixtures enforce:

1. no promotion by prose;
2. no hidden authority lane;
3. non-claims are load-bearing.

## Tier 2 planning lane

Tier 2 v0.1 scope is governance over compositions.

The Tier 2 planning document resolves:

- scope call: compositions, not meta-governance;
- Tier 2 invariants;
- negative-test plan;
- Tier 1 schema extension points;
- formal-methods in-scope/deferred split;
- Tier 2 CI passing definition;
- explicit doctrine-only deferrals;
- state block shape.

No Tier 2 schemas, fixtures, validators, or runtime behavior are implemented yet.

## CI status

Tier 1 has:

```bash
make governance-fabric-ci
```

This runs:

```bash
python -m pytest -q tests/test_governance_fabric_tier1.py
```

Observed CI state:

```text
PR #31 head CI: green
PR #31 merged: yes
CI Observation Ledger issue: #32
main push receipt observed: yes
receipt commit_sha: e639a4d0c1aaf94e0018ae0ae0e71609fb316a96
receipt workflow_run_id: 25714672871
receipt conclusion: success
receipt trigger: push
```

The CI Observation Ledger converts CI state into connector-visible evidence. Issue #32 contains a versioned JSON receipt posted by `github-actions[bot]` with `conclusion: success` for a `push` run on `main`.

## Runtime status

No governance runtime is claimed.

No cryptographic receipt system, monitor network, PCP-style replay prover, SNARK receipt implementation, or production approval flow is claimed.

## Funding / execution boundary

Current artifacts are doctrine and deterministic schema fixtures. They make the program structurally inspectable but do not execute governance.

The first fundable implementation milestone after schema CI is runtime integration of action traces, evidence receipts, promotion decisions, and safety cases.

## Non-claims

This repository currently does not claim:

- production governance runtime;
- formal hypergraph-category proof;
- mathematical Birkhoff factorization theorem;
- formal PCP prover;
- deployed monitor-network decoder;
- CP-SNARK evidence receipts;
- post-quantum receipt implementation;
- runtime integration with `superconscious` certificates;
- Tier 2 composition schemas or validators.

## Next bounded move

Review and merge the Tier 2 composition governance planning PR.

The first Tier 2 implementation PR should be limited to a composition-certificate schema, positive/negative deterministic fixtures, and a Tier 2 pytest harness.
