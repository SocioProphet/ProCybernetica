# Governance Fabric Tier 1 Schema Lane

## Status

This lane implements the first executable slice of the Cybernetic Governance Fabric.

It is schema/fixture/CI complete, not runtime complete. All examples are deterministic synthetic fixtures.

## Scope

Tier 1 adds ten schema contracts:

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

The composition schema is the bridge between `SocioProphet/superconscious` and ProCybernetica. It allows Superconscious certificates to enter a ProCybernetica safety case as one evidence type.

## Fixture set

Valid fixtures:

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

Negative fixtures:

```text
tests/fixtures/governance-fabric/invalid_promotion_by_prose.synthetic.json
tests/fixtures/governance-fabric/invalid_action_missing_authority.synthetic.json
tests/fixtures/governance-fabric/negative_safety_case_empty_non_claims.synthetic.json
```

## Constitutional invariants enforced in CI

The negative fixtures assert three Tier 0 invariants:

1. **No promotion by prose.** Promotion decisions require non-empty `evidence_receipt_refs`.
2. **No hidden authority lane.** Action traces require `authority_chain_ref`.
3. **Non-claims are load-bearing.** Safety cases require non-empty `non_claims`.

## CI target

```bash
make governance-fabric-ci
```

This runs:

```bash
python -m pytest -q tests/test_governance_fabric_tier1.py
```

The repository’s normal GitHub Actions CI also runs `pytest -q`, so Tier 1 validation is part of the default CI path.

## Runtime boundary

No production governance runtime is claimed.

This lane validates schema structure, deterministic fixtures, negative invariant enforcement, and the cross-program composition shape.

## Non-claims

This lane does not claim:

- deployed governance runtime;
- cryptographic receipts;
- monitor network decoder;
- formal hypergraph proof;
- formal PCP prover;
- production promotion workflow;
- runtime integration with Superconscious certificates.
