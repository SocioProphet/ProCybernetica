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
    first_schema_pr: #37
    first_schema_merge_commit: 73d2320767eebf2df485bab94b857b15080ceff0
    first_schema_ci: green_via_ci_observation_ledger
    first_schema_ci_receipt: observed_by_exact_ledger_search
    evidence_receipt_integration_pr: #38
    evidence_receipt_integration_merge_commit: c3c288612a46167cb3b3a1c7f89f12faedb08962
    evidence_receipt_integration_ci: green_via_ci_observation_ledger
    evidence_receipt_integration_ci_receipt: observed_by_exact_ledger_search
    authority_scope_pr: #48
    authority_scope_merge_commit: 0b28e1fe66346b49554bbf51d62454008b42bce3
    authority_scope_ci: green_via_ci_observation_ledger
    authority_scope_ci_receipt: observed_by_exact_ledger_search
    nonclaim_analysis_pr: #54
    nonclaim_analysis_merge_commit: b6d1ad9bb13d812eb72baed2fff5bc7a8ce6641e
    nonclaim_analysis_ci: green_via_ci_observation_ledger
    nonclaim_analysis_ci_receipt: observed_by_exact_ledger_search
    monitor_independence_pr: #55
    monitor_independence_merge_commit: 9ed2983b7ccacccb10f0ec274359a97e31d2e4a9
    monitor_independence_ci: green_via_ci_observation_ledger
    monitor_independence_ci_receipt: observed_by_exact_ledger_search
    invariants_doctrine_pr: #56
    invariants_doctrine_merge_commit: a8e6b47648696658b8fd1d81239953fb2e8f11f0
    invariants_doctrine_ci: green_via_ci_observation_ledger
    invariants_doctrine_ci_receipt: observed_by_exact_ledger_search
    evidence_freshness_pr: #57
    evidence_freshness_merge_commit: 173fc92a21e4cf1b2a785365adc992f441910488
    evidence_freshness_ci: green_via_ci_observation_ledger
    evidence_freshness_ci_receipt: observed_by_exact_ledger_search
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
TIER2_SCHEMA_LANE.md
TIER2_COMPOSITION_INVARIANTS.md
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

## Tier 2 composition certificate schema lane

PR #37 merged the first Tier 2 implementation slice.

Implemented:

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

The schema implements flat v0.1 composition only:

```text
composition_order: 1
recursive_composition_allowed: false
```

## Tier 2 composition invariant lanes

The following Tier 2 flat-composition invariant lanes have merged green:

```text
PR #38 evidence receipt integration
PR #48 authority scope comparison
PR #54 structured non-claim analysis
PR #55 monitor independence
PR #57 evidence freshness
```

### Evidence receipt integration

Design posture:

```text
integration_mode: hash_bound_reference
runtime receipt-store lookup: deferred
embedded full receipt verification: deferred
recursive composition: false
```

New invariants enforce receipt binding coverage, no unknown receipt bindings, artifact-hash matching, and top-level receipt declaration.

### Authority scope comparison

Design posture:

```text
comparison_mode: declared_scope_lattice_v1
broader scope supports declared narrower scopes
narrower scope does not imply broader scope
runtime scope algebra: deferred
formal scope lattice proof: deferred
```

New invariant: composed authority scope must be supported by constituent-declared authority scopes under the declared scope lattice.

### Structured non-claim analysis

Design posture:

```text
analysis_mode: explicit_propagate_or_resolve_v1
every source non-claim must be propagated or resolved
resolutions must cite declared evidence receipts
runtime verification of resolution evidence: deferred
```

New invariants enforce source/non-claim alignment, propagate-or-resolve completeness, and evidence-bound resolution.

### Monitor independence

Design posture:

```text
analysis_mode: declared_monitor_independence_v1
distinct monitors when claimed
self-monitoring forbidden when claimed
acyclic monitor graph required when claimed
runtime monitor attestation: deferred
```

New invariants enforce monitor coverage, declared monitor evidence, distinct monitors, no self-monitoring, and acyclic monitor graphs.

### Evidence freshness

PR #57 merged declared evidence freshness analysis into composition certificates.

Implemented:

```text
composition_certificate.v1.json evidence_freshness_analysis field
positive_composition_evidence_freshness_all_fresh.synthetic.json
negative_composition_unanalyzed_receipt.synthetic.json
negative_composition_unbound_receipt_class.synthetic.json
negative_composition_stale_evidence_claimed_fresh.synthetic.json
negative_composition_refresh_without_evidence.synthetic.json
negative_composition_stale_acknowledged_without_propagation.synthetic.json
updated tests/test_governance_fabric_tier2.py evidence-freshness checks
```

Design posture:

```text
analysis_mode: declared_evidence_freshness_v1
receipt timestamps: declared values only
freshness windows: issuer-declared
receipt_class taxonomy: issuer-declared
runtime timestamp verification: deferred
transitive supersession traversal: deferred
```

New invariants enforced:

1. freshness analysis must cover every top-level evidence receipt;
2. freshness record classes must be declared in `freshness_windows`;
3. `fresh` receipts must be within their declared class window and have internally consistent `age_seconds`;
4. `refreshed` receipts must cite a declared refresh receipt;
5. `acknowledged_stale` receipts must cite propagated or resolved non-claims.

## Tier 2 composition invariants doctrine lane

PR #56 merged the canonical cross-repo reference document for the Tier 2 composition invariant family.

Implemented:

```text
docs/governance-fabric/TIER2_COMPOSITION_INVARIANTS.md
```

The document consolidates the six-element invariant pattern, current invariant catalog, future extension candidates, and cross-repo references for `superconscious`, `sociosphere`, `policy-fabric`, and `agentplane`.

## CI status

Tier 1 has:

```bash
make governance-fabric-tier1-ci
```

Tier 2 has:

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
PR #37 head CI: green
PR #37 merged: yes
Tier 2 composition main receipt: success observed through exact CI Observation Ledger search for commit 73d2320767eebf2df485bab94b857b15080ceff0
PR #38 head CI: green
PR #38 merged: yes
Tier 2 evidence receipt integration main receipt: success observed through exact CI Observation Ledger search for commit c3c288612a46167cb3b3a1c7f89f12faedb08962
PR #48 head CI: green
PR #48 merged: yes
Tier 2 authority-scope main receipt: success observed through exact CI Observation Ledger search for commit 0b28e1fe66346b49554bbf51d62454008b42bce3
PR #54 head CI: green
PR #54 merged: yes
Tier 2 non-claim analysis main receipt: success observed through exact CI Observation Ledger search for commit b6d1ad9bb13d812eb72baed2fff5bc7a8ce6641e
PR #55 head CI: green
PR #55 merged: yes
Tier 2 monitor-independence main receipt: success observed through exact CI Observation Ledger search for commit 9ed2983b7ccacccb10f0ec274359a97e31d2e4a9
PR #56 head CI: green
PR #56 merged: yes
Tier 2 composition-invariants doctrine main receipt: success observed through exact CI Observation Ledger search for commit a8e6b47648696658b8fd1d81239953fb2e8f11f0
PR #57 head CI: green
PR #57 merged: yes
Tier 2 evidence-freshness main receipt: success observed through exact CI Observation Ledger search for commit 173fc92a21e4cf1b2a785365adc992f441910488
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
- Tier 2 runtime behavior;
- runtime receipt-store lookup;
- embedded full receipt verification;
- full semantic authority lattice beyond declared fixture scopes;
- runtime verification of non-claim resolution evidence;
- runtime monitor independence attestation;
- runtime verification of timestamp authenticity;
- transitive supersession-chain traversal;
- policy-governed freshness windows;
- Tier 0 receipt-class taxonomy enforcement.

## Next bounded move

Tier 2 schema work that does not require new infrastructure is now substantially complete.

Next likely work should be one of:

1. cross-repo Tier 2 invariant bindings for `superconscious`, `sociosphere`, `policy-fabric`, and `agentplane`;
2. Tier 2 v2 mode design for runtime-backed verification modes;
3. wait for dependency resolution for remaining schema candidates:
   - constituent authority concentration requires signer/reputation substrate;
   - scope coverage requires a comparable scope lattice definition.
