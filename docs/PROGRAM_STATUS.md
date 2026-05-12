# ProCybernetica Program Status

## Status date

2026-05-11

## Program role

`SocioProphet/ProCybernetica` is the cybernetic security, governance, and resilience program for SocioProphet.

It is a sibling to `SocioProphet/superconscious`.

- `superconscious` produces interpretability certificates.
- `ProCybernetica` governs certificates, authority, actions, evidence, releases, monitoring, incidents, and public claims.

## Current state

```text
doctrine_complete: Tier 0 + Tier 1 doctrine spine
tier1_schema_ci_branch: governance-fabric-tier1-schema-ci
schema_ci_complete: pending PR/CI confirmation
runtime_executed: false
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

## Key doctrine corrections landed

- Birkhoff language is now Birkhoff-style release-delta decomposition, not theorem-level claim.
- PCP language is now PCP-style replay audit, not formal PCP prover claim.
- Hypergraph composition is stated as a technical predicate pending formal Tier 2 proof.
- Frontier scoreboard is framed as absolute self-measurement, not competitor marketing.
- Tier 4 is explicitly research runway, not MVP surface.
- Privacy-preserving evidence is a Tier 1.5 bridge between retention and minimization.

## Tier 1 schema CI branch

The branch `governance-fabric-tier1-schema-ci` implements the first executable Governance Fabric schema lane.

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

Valid fixture set:

```text
tests/fixtures/governance-fabric/authority_chain.synthetic.json
tests/fixtures/governance-fabric/tool_permission_scope.synthetic.json
tests/fixtures/governance-fabric/evidence_receipt.synthetic.json
tests/fixtures/governance-fabric/off_history_evidence.synthetic.json
tests/fixtures/governance-fabric/monitor_alert.synthetic.json
tests/fixtures/governance-fabric/allowed_action.synthetic.json
tests/fixtures/governance-fabric/blocked_action.synthetic.json
tests/fixtures/governance-fabric/transformed_safe_completion.synthetic.json
tests/fixtures/governance-fabric/release_delta_promotion.synthetic.json
tests/fixtures/governance-fabric/safety_case.synthetic.json
tests/fixtures/governance-fabric/program-certificate.synthetic.json
```

Negative constitutional fixture set:

```text
tests/fixtures/governance-fabric/invalid_promotion_by_prose.synthetic.json
tests/fixtures/governance-fabric/invalid_action_missing_authority.synthetic.json
tests/fixtures/governance-fabric/negative_safety_case_empty_non_claims.synthetic.json
```

The negative fixtures enforce:

1. no promotion by prose;
2. no hidden authority lane;
3. non-claims are load-bearing.

## CI status

Tier 1 adds:

```bash
make governance-fabric-ci
```

This runs:

```bash
python -m pytest -q tests/test_governance_fabric_tier1.py
```

The repository's normal GitHub Actions CI runs `pytest -q`, so Tier 1 validation is part of the default PR path.

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
- runtime integration with `superconscious` certificates.

## Next bounded move

Merge the Tier 1 schema CI branch after CI review.

Do not add Tier 2+ formal machinery until Tier 1 schema CI is green on GitHub Actions.
