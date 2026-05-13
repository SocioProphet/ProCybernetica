# Cybernetic Governance Hardening Audit

Status: Draft v0.1  
Issue: #29  
Track: Cybernetic governance hardening

## Purpose

This audit converts the post-capture review of the v0.1 cybernetic governance doctrine into an implementation checklist. The doctrine is now captured. The next requirement is operational hardening: exact states, enums, traceability, evidence profiles, fixture discipline, and CI gates.

## Summary

The v0.1 doctrine is strong enough to support schema work, but it is not implementation-complete. The main risks are ambiguous lifecycle terms, prose-only evidence expectations, missing schema-to-invariant traceability, and insufficient invalid-fixture coverage.

## Hardening checklist

| Gap | Lane | Required artifact | Blocks |
|---|---|---|---|
| Lifecycle states and transitions | profile/schema | canonical governance lifecycle profile | promotion schemas |
| Severity, autonomy, evidence, and reversibility enums | schema | shared enum definitions or schema fragments | Tier 1 schema bundle |
| Schema-to-invariant traceability | schema/conformance | invariant coverage matrix | validator coverage |
| Machine-readable non-claims | schema | non-claim object shape | safety cases and public reports |
| Evidence profiles and redaction rules | schema/profile | evidence classification profile | evidence receipts |
| Supply-chain provenance for schemas and fixtures | assurance | artifact provenance requirements | release bundles |
| Readiness levels | profile | readiness-level profile across doctrine, schema, validator, runtime, monitor, release, and assurance | milestone claims |
| Cross-repo dependency map | integration | ProCybernetica to Prophet Platform to SocioSphere to Superconscious dependency map | downstream implementation |
| Monitor and evaluator calibration | validation | active, sham, and held-out fixture rules | monitor claims |
| Concrete MVP trace example | example | authority-to-trace-to-evidence-to-promotion example | schema implementation review |
| Doctrine-to-schema acceptance criteria | conformance | merge checklist for #26 and #27 | schema PR review |
| CI checks for missing referenced schemas | CI | doctrine reference checker or manifest check | implementation phase |

## Required lifecycle baseline

Use a small lifecycle first:

```text
draft
captured
reconciled
schema_ready
validated
cross_checked
promoted
quarantined
archived
```

Promotion into `promoted` requires evidence receipt references, non-claims, authority chain, and validator pass. Unresolved Tier 0 invariant violations may only move into `draft`, `captured`, `diagnosed`, `quarantined`, or `archived` states.

## Required enum baseline

The first schema bundle should define stable values for:

```text
severity: info | low | medium | high | critical
autonomy_tier: manual | assisted | supervised | delegated | autonomous | frontier
evidence_tier: assertion | fixture | replayable | cross_checked | signed | independently_reviewed
reversibility: reversible | partially_reversible | externally_visible | irreversible
readiness: doctrine | schema | fixture | validator | integration | runtime | assurance
privacy_class: public | redacted | private | sealed | privileged | do_not_retain
```

These are starter values. Schema work in #26 may refine names, but the schemas must not leave these concepts as prose-only fields.

## Schema-to-invariant traceability

Every Tier 1 schema should declare which constitutional invariants it protects. Minimum expected coverage:

| Schema | Required invariant coverage |
|---|---|
| `authority_chain.v1.json` | no hidden authority lane |
| `agent_action_trace.v1.json` | no action without trace |
| `tool_permission_scope.v1.json` | no hidden authority lane; irreversibility gate |
| `side_effect_assessment.v1.json` | irreversibility gate; release-delta governance |
| `off_history_evidence.v1.json` | off-history retained |
| `evidence_receipt.v1.json` | digital typed digestible evidence |
| `promotion_decision.v1.json` | no promotion by prose alone |
| `cybernetic_safety_case.v1.json` | safety case before frontier promotion; non-claims |
| `release_delta_report.v1.json` | release changes require delta governance |
| `privacy_evidence_classification.v1.json` | privacy and evidence minimization |
| `authority_graph_snapshot.v1.json` | separation of powers; authority concentration |

## Merge acceptance criteria for #26

A Tier 1 schema PR is not complete unless:

1. every schema has `$id`, title, description, required fields, and strict additional-properties posture;
2. every schema includes invariant refs;
3. every promotion-bearing schema requires non-claims or an explicit statement that non-claims are not applicable;
4. every evidence-bearing schema requires digest, schema id, source, and evidence class;
5. every action-bearing schema requires actor, authority chain, side-effect class, and replay or non-replay reason;
6. examples are public-safe and marked synthetic unless runtime evidence exists.

## Merge acceptance criteria for #27

A fixture/validator PR is not complete unless:

1. valid and invalid fixtures exist for each Tier 1 schema family;
2. invalid fixtures fail for the intended reason;
3. validator output includes machine-readable status and human-readable diagnosis;
4. fixture coverage maps back to Tier 0 invariants;
5. at least one fixture demonstrates failed or blocked action retained as off-history evidence;
6. at least one fixture rejects promotion by prose;
7. at least one fixture rejects a safety case without non-claims.

## MVP trace target

The first executable example should cover:

```text
authority_chain
  -> agent_action_trace
  -> tool_permission_scope
  -> side_effect_assessment
  -> monitor_alert
  -> off_history_evidence or evidence_receipt
  -> cybernetic_safety_case
  -> promotion_decision
```

The example should include both a clean path and a blocked path.

## CI expectations

Once #26 begins implementation, CI should fail when:

- a doctrine file references a required schema path that does not exist;
- a schema is missing invariant refs;
- a fixture claims runtime evidence while using synthetic data;
- a promotion decision lacks evidence receipt refs;
- a safety case lacks non-claims.

## Integration note

Superconscious should remain untouched unless a concrete contract dependency appears after #26 and #27. The existing Superconscious evidence map gives a governance interpretation path, not a runtime integration requirement.
