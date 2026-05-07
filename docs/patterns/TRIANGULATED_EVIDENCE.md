# Triangulated Evidence Pattern

Status: candidate pattern
Turn: 3 / 28
Owner repository: `SocioProphet/ProCybernetica`
Expected downstream owner: `SocioProphet/prophet-platform-standards`

## Purpose

Triangulated evidence is the minimum stabilization rule for consequential claims and actions.

The pattern translates triangulation as structural stabilization into evidence practice. Assertion alone is not stable. A serious claim or action needs at least three mutually reinforcing points.

## Canonical triads

Use one or more of these triads depending on artifact type:

| Context | Required triad |
| --- | --- |
| Claim | assertion + evidence + independent witness |
| Code change | implementation + test + provenance |
| Runtime action | actor + policy + receipt |
| Artifact | content + hash + replay/build path |
| Model output | model output + source + verifier |
| Dataset | source + schema + validation report |
| Public doctrine | source capture + operational definition + conformance implication |
| Agent action | work order + policy decision + evidence artifact |
| Release | build + signature/SBOM + promotion decision |

## Minimal record

```yaml
triangulated_evidence:
  subject_ref: required
  evidence_class: claim | code | runtime | artifact | model_output | dataset | doctrine | agent_action | release | other
  assertion_ref: required
  evidence_refs:
    - required
  witness_refs:
    - required
  provenance_refs:
    - optional
  replay_refs:
    - optional
  validation_refs:
    - optional
  missing_points: []
  promotion_allowed: boolean
```

## Promotion rule

A consequential claim or action cannot promote to hard-lane authority unless triangulation is complete or a named exception is recorded.

```text
no triad -> candidate only
partial triad -> manual review or shadow-only
complete triad -> eligible for evaluation and promotion
complete triad + replay + policy -> eligible for operational authority
```

## Examples

### Source-derived doctrine

```yaml
triangulated_evidence:
  subject_ref: procybernetica:doctrine:dictionary_doctrine
  evidence_class: doctrine
  assertion_ref: claim:dictionary_doctrine_candidate
  evidence_refs:
    - source_capture:FULLER_SYNERGETICS_COMPLETION_CAPTURE
    - source_confidence:source-card-ledger-v0.2
  witness_refs:
    - reviewer:manual_review_required
  missing_points:
    - independent_bibliographic_verification
  promotion_allowed: false
```

### AgentPlane action

```yaml
triangulated_evidence:
  subject_ref: agentplane:operation:agent.patch.propose
  evidence_class: agent_action
  assertion_ref: work_order:agent.patch.propose
  evidence_refs:
    - policy_decision:allow
    - run_artifact:example
  witness_refs:
    - replay_artifact:example
  promotion_allowed: true
```

## Anti-patterns prevented

- untriangulated claim fallacy;
- source laundering;
- analogy-as-proof;
- false dashboard confidence;
- runtime side effect without receipt;
- agent self-promotion.

## Downstream integration

### Platform Standards

Should become a standard PR/release template and CI/release-gate pattern.

### Ontogenesis

Should express triads in SHACL for promoted concepts and validated claims.

### Sherlock

Should expose whether a result is triangulated or only asserted.

### AgentPlane

Should map work order, policy decision, and evidence artifact into this pattern.

### SourceOS

Should map event, policy decision, and operator narrative into this pattern.

## Current status

Candidate pattern. It becomes validated after profiles, examples, and downstream issue fanout land.
