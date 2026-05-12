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
    doctrine_complete: planning_merged
    planning_pr: #35
    planning_merge_commit: a9ee2d5b9d536986f1be9308ff6c2a6396cc5ec3
    planning_ci: green_via_ci_observation_ledger
    planning_ci_receipt_run_id: 25715320769
    first_schema_branch: governance-fabric-tier2-composition-certificate
    schema_ci: implementation_pr_pending
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
TIER2_COMPOSITION_GOVERNANCE_PLAN.md
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

PR #35 merged the Tier 2 planning artifact.

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

## Tier 2 composition certificate branch

The first Tier 2 implementation branch is:

```text
governance-fabric-tier2-composition-certificate
```

Implemented on that branch:

```text
schemas/governance-fabric/composition_certificate.v1.json
tests/fixtures/governance-fabric/tier2/composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composite_claim_without_composition_certificate.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_status_boundary.synthetic.json
tests/fixtures/governance-fabric/tier2/negative_composition_missing_authority_coverage.synthetic.json
tests/test_governance_fabric_tier2.py
docs/governance-fabric/TIER2_SCHEMA_LANE.md
make governance-fabric-tier2-ci
```

The branch implements flat v0.1 composition only:

```text
composition_order: 1
recursive_composition_allowed: false
```

No recursive composition, meta-governance, runtime orchestration, or formal proof is claimed.

## CI status

Tier 1 has:

```bash
make governance-fabric-tier1-ci
```

Tier 2 branch adds:

```bash
make governance-fabric-tier2-ci
```

Full governance fabric CI target:

```bash
make governance-fabric-ci
```

Observed CI state:

```text
PR #31 head CI: green
PR #31 merged: yes
Tier 1 main receipt: success, run_id 25714672871
PR #35 head CI: green
PR #35 merged: yes
Tier 2 planning main receipt: success, run_id 25715320769
CI Observation Ledger issue: #32
```

The CI Observation Ledger converts CI state into connector-visible evidence. Issue #32 contains versioned JSON receipts posted by `github-actions[bot]` with `conclusion: success` for the relevant pull-request and push runs.

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
- recursive Tier 2 composition;
- Tier 2 runtime behavior.

## Next bounded move

Open and review the first Tier 2 implementation PR.

Merge only after PR-head CI is green and then close the main-branch CI observation through the CI Observation Ledger.
