# F2.2 SHACL Companion Coverage Addendum

Status: v0.1 falsification cross-reference addendum  
Issue: #46  
Parent registry: `docs/falsification/observable-cross-reference.md`  
Runtime claim: none

## Purpose

This addendum records the #46 update to F2.2 after certificate-family v1.3 and bridge schemas became stable.

The parent cross-reference registry remains machine-checked by `scripts/validate_falsification_coverage.py`. This addendum is a focused status update for the F2.2 certificate/bridge companion-shape tranche.

## F2.2 observable

Parent observable:

```text
F2.2 — A certificate, bridge, or governance schema lacks companion validation coverage or explicit deferred status.
```

## Status after #46

F2.2 is now covered for the certificate and bridge surfaces by:

```text
shacl/certificates/certificate-family-v1.3.shacl.ttl
shacl/bridges/bridge-schemas-v1.shacl.ttl
docs/shacl/CERTIFICATE_AND_BRIDGE_SHACL_COVERAGE.md
tools/cybernetic_governance/validate_shacl_companions.py
tests/test_shacl_companions.py
tests/fixtures/falsification/f2-2-shacl-companion-coverage.synthetic.json
```

## Coverage interpretation

The new status is:

```text
covered-with-SHACL-plus-non-SHACL-fallback
```

Meaning:

- SHACL companion shapes exist for all #46 certificate kinds.
- SHACL companion shapes exist for all #46 bridge schemas.
- SHACL-expressible structural fields are declared in Turtle companion files.
- Cross-field and threshold rules remain in repository-local Python validators or future Rego/non-SHACL validation.

## Required fallback rules

The non-SHACL layer remains required for:

- `composite_fragments_match_promotion_state`
- `human_actor_requires_consent_for_reputation_microbeat`
- `promotion_state_strict_inheritance`
- `verifier_scores_consistent_with_verdict`
- `undecided_fails_closed_to_deny`
- `pattern_c_always_denies`
- CI-9 authority-concentration threshold enforcement

## Non-claims

This addendum does not claim runtime SHACL enforcement, production RDF validation, Rego implementation, Atlas runtime admission, Masonmark adjudication, or certificate promotion authority. It records companion-shape coverage and the fallback validation boundary for F2.2.
