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
schema_ci_complete: false
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

## Pending Tier 1 schema lane

Next executable work:

```text
schemas/governance-fabric/*.v1.json
tests/fixtures/governance-fabric/*.synthetic.json
make governance-fabric-ci
```

Initial schema set:

```text
authority_chain.v1.json
agent_action_trace.v1.json
tool_permission_scope.v1.json
monitor_alert.v1.json
safe_completion_decision.v1.json
off_history_evidence.v1.json
evidence_receipt.v1.json
promotion_decision.v1.json
cybernetic_safety_case.v1.json
```

Worked-example fixtures:

```text
allowed_action.synthetic.json
blocked_action.synthetic.json
transformed_safe_completion.synthetic.json
release_delta_promotion.synthetic.json
safety_case.synthetic.json
invalid_promotion_by_prose.synthetic.json
```

Composition schema pending:

```text
schemas/composition/program-certificate.v1.json
```

## CI status

No governance-fabric CI exists yet.

The next CI target should be:

```bash
make governance-fabric-ci
```

This should validate schemas and deterministic synthetic fixtures without claiming runtime execution.

## Runtime status

No governance runtime is claimed.

No cryptographic receipt system, monitor network, PCP-style replay prover, SNARK receipt implementation, or production approval flow is claimed.

## Funding / execution boundary

Current artifacts are doctrine-only. They make the program structurally inspectable but do not execute governance.

The first fundable implementation milestone is Tier 1 schema CI plus deterministic fixtures.

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

Add Tier 1 governance-fabric schemas, synthetic fixtures, and `make governance-fabric-ci`.

Do not add Tier 2+ formal machinery until Tier 1 schema CI is green.
