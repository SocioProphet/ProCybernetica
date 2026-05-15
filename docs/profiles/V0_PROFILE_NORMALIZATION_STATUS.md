# V0 Profile Normalization Status

Status: v0.1 validation record  
Issue: #7  
Runtime claim: none

## Purpose

This document records the v0 profile normalization state after the schema/profile reconciliation pass.

The four v0 profile files are present and validated by:

```text
tools/cybernetic_governance/validate_profiles.py
tests/test_profile_normalization.py
```

## Profile coverage

| Profile | Status | Coverage |
| --- | --- | --- |
| `profiles/controlplane_state_machine.yaml` | present and validated | Reconciled Fractal Node lifecycle, canonical transition events, alias preservation, evidence-required transitions. |
| `profiles/promotion_policy.example.yaml` | present and validated | ADR-0002 promotion decision vocabulary, authority budgets, evidence/replay/policy requirements, rollback/revoke governance boundary. |
| `profiles/bt_semantic_profile.yaml` | present and validated | Behavior-tree semantic expectations, replay/trace requirements, recovery policy, non-ownership of runtime execution. |
| `profiles/k3_bridge_lifecycle.yaml` | present and validated | Genesis/Inception/K3 lifecycle, domain-object reference pattern, HolographMe ownership boundary, evidence-required transitions. |

## Normalization decisions

- Generic Fractal Node lifecycle remains separate from twin/K3 lifecycle.
- `retired` and `finalized` both remain in the generic lifecycle.
- Source aliases are preserved through `transition_aliases` rather than expanded into schema enums.
- Rollback and revocation remain promotion/governance verdicts, not direct actuator commands.
- K3 references domain-owned objects instead of cloning HolographMe, agent-registry, SourceOS, or Prophet Platform schemas.

## Validation commands

```bash
make profiles-ci
python tools/cybernetic_governance/validate_profiles.py
python -m pytest -q tests/test_profile_normalization.py
```

## Non-claims

This profile validation tranche does not implement lifecycle runtime, promotion runtime, behavior-tree runtime, Genesis/Inception runtime, HolographMe runtime schemas, or upstream adapter execution. It records and validates public profile semantics only.
