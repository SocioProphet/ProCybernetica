# Cybernetic Governance Gap Audit and Readiness Matrix

**Status:** Draft v0.1
**Track:** Post-capture hardening audit
**Applies to:** Cybernetic Governance Fabric doctrine bundle introduced in PR #25
**Purpose:** Convert the v0.1 doctrine capture into an executable hardening plan with explicit gaps, readiness levels, state transitions, enums, schema traceability, validation criteria, cross-repo boundaries, and merge gates.

---

## 1. Executive summary

The v0.1 doctrine capture is strategically correct but not yet an executable standard.

It captures the frontier direction:

- no hidden authority lane;
- no action without trace;
- no promotion by prose;
- digital, typed, digestible, privacy-classified evidence;
- off-history retention;
- monitor independence and monitor-of-monitors;
- separation of powers and authority concentration;
- release-delta decomposition;
- monitor networks as error-correcting systems;
- probabilistically checkable replay audit;
- public-first assurance with non-claims.

The remaining gap is operational precision. The fabric needs exact lifecycle states, canonical enums, schema-to-invariant traceability, machine-readable non-claims, disclosure profiles, supply-chain provenance, concrete MVP traces, validator semantics, readiness levels, and CI gates.

This document makes those gaps explicit and assigns them to doctrine, schema, validator, runtime, integration, or research lanes.

---

## 2. Audit classification

Each gap is classified into one of five lanes.

| Lane | Meaning |
|---|---|
| Doctrine | Needs additional normative text before schema work is stable |
| Schema | Needs JSON Schema or YAML contract |
| Validator | Needs executable validation and fixtures |
| Runtime | Needs Prophet Platform or AgentPlane implementation later |
| Integration | Needs SocioSphere, Prophet Platform, or future Superconscious coordination |
| Research | Captured runway; does not block MVP |

Each gap also has a readiness effect:

| Effect | Meaning |
|---|---|
| Blocks Tier 1 | Must be resolved before schema bundle can be called complete |
| Blocks validator | Must be resolved before fixtures can be meaningful |
| Blocks runtime | Must be resolved before platform integration |
| Blocks assurance | Must be resolved before public safety-case claims |
| Non-blocking runway | Important but not required for MVP |

---

## 3. Artifact lifecycle state machine

The doctrine currently names promotion discipline but does not fully define a cybernetic artifact lifecycle. The following lifecycle should be canonical for governance artifacts.

### 3.1 States

| State | Meaning |
|---|---|
| `draft` | Artifact exists but is not yet reconciled or schema-backed |
| `captured` | Artifact is preserved in repository with source context and non-claims |
| `reconciled` | Terminology, scope, and boundaries have been reconciled with existing ProCybernetica doctrine |
| `schema_defined` | Machine-readable schema or contract exists |
| `fixture_backed` | Valid and invalid examples exist |
| `validator_backed` | Executable validator checks the schema and fixtures |
| `cross_checked` | At least one independent or cross-repo check has passed |
| `runtime_consumed` | A runtime, monitor, eval service, or platform adapter consumes the artifact |
| `promoted` | Artifact is approved for its declared governance scope |
| `quarantined` | Artifact conflicts with a constitutional invariant, failed gate, or provenance rule |
| `archived` | Artifact retained for provenance but no longer active |

### 3.2 Allowed transitions

| From | To | Required evidence |
|---|---|---|
| `draft` | `captured` | Source context, non-claims, owner |
| `captured` | `reconciled` | Vocabulary review, scope review, conflict log |
| `reconciled` | `schema_defined` | Schema file, schema owner, invariant map |
| `schema_defined` | `fixture_backed` | Valid fixtures, invalid fixtures, fixture intent |
| `fixture_backed` | `validator_backed` | Validator command, pass/fail report, diagnosis output |
| `validator_backed` | `cross_checked` | Independent review, CI, or cross-repo check |
| `cross_checked` | `runtime_consumed` | Runtime adapter or consuming service receipt |
| `runtime_consumed` | `promoted` | Promotion decision, evidence receipts, non-claims |
| any active state | `quarantined` | Failed invariant, failed validator, provenance conflict, or incident |
| any active state | `archived` | Archive decision and replacement or deprecation reason |

### 3.3 Forbidden transitions

The following transitions are invalid:

- `draft` directly to `promoted`;
- `captured` directly to `runtime_consumed`;
- `schema_defined` directly to `promoted` without fixtures and validators;
- `validator_backed` to `promoted` without promotion decision;
- `quarantined` to `promoted` without remediation and fresh evidence.

### 3.4 Required schema

Add:

- `schemas/cybernetic-governance/artifact_lifecycle_state.v1.json`
- `schemas/cybernetic-governance/lifecycle_transition.v1.json`

### 3.5 Readiness effect

Blocks Tier 1 and blocks assurance.

---

## 4. Canonical enums

The doctrine currently uses terms such as high risk, irreversible, sealed, public, and promoted. These must become canonical enums.

### 4.1 Severity tier

`none`, `info`, `low`, `medium`, `high`, `critical`, `catastrophic`

### 4.2 Autonomy tier

`manual`, `assistive`, `supervised_agent`, `delegated_agent`, `bounded_autonomous`, `high_autonomy`, `frontier_autonomy`

### 4.3 Evidence tier

`E0_raw_occurrence`, `E1_typed_occurrence`, `E2_replayable_occurrence`, `E3_controlled_contrast`, `E4_interventional_support`, `E5_independent_cross_check`, `E6_governed_signal`, `E7_production_control`, `E8_public_assurance`

### 4.4 Reversibility class

`fully_reversible`, `mostly_reversible`, `partially_reversible`, `externally_visible`, `irreversible`, `legally_material`, `financially_material`, `privacy_material`, `security_material`, `physical_world_material`

### 4.5 Evidence disclosure class

`public`, `redacted`, `private`, `sealed`, `privileged`, `sensitive_ops`, `do_not_retain`

### 4.6 Promotion decision

`allow`, `allow_with_monitoring`, `allow_with_degraded_autonomy`, `require_more_evidence`, `quarantine`, `reject`, `archive`

### 4.7 Monitor output state

`pass`, `fail`, `missing`, `inconsistent`, `unknown`, `degraded`, `outage`

### 4.8 Release-delta gate color

`green`, `yellow`, `red`, `black`

### 4.9 Incident class

`near_miss`, `policy_violation`, `privacy_event`, `security_event`, `monitor_failure`, `evidence_failure`, `release_regression`, `publication_error`, `authority_failure`, `runtime_side_effect`

### 4.10 Required schema

Add:

- `schemas/cybernetic-governance/enums.v1.json`

### 4.11 Readiness effect

Blocks Tier 1.

---

## 5. Schema-to-invariant traceability

Every Tier 1 schema must declare which constitutional invariants it implements.

| Schema | Primary invariant(s) | Required traceability field |
|---|---|---|
| `authority_chain.v1.json` | No hidden authority lane | `implements_invariants` |
| `instruction_conflict_case.v1.json` | No hidden authority lane | `implements_invariants` |
| `agent_action_trace.v1.json` | No action without trace | `implements_invariants` |
| `tool_permission_scope.v1.json` | Irreversibility requires approval; separation of powers | `implements_invariants` |
| `environment_delta.v1.json` | No action without trace | `implements_invariants` |
| `side_effect_assessment.v1.json` | Irreversibility requires approval | `implements_invariants` |
| `off_history_evidence.v1.json` | Off-history is retained | `implements_invariants` |
| `monitor_alert.v1.json` | Monitor independence; monitors are monitored | `implements_invariants` |
| `meta_monitor_report.v1.json` | Monitors are monitored | `implements_invariants` |
| `evidence_receipt.v1.json` | Evidence digital, typed, digestible | `implements_invariants` |
| `promotion_decision.v1.json` | No promotion by prose | `implements_invariants` |
| `cybernetic_safety_case.v1.json` | Safety case before frontier promotion; claims require non-claims | `implements_invariants` |
| `release_delta_report.v1.json` | Release changes require delta governance | `implements_invariants` |
| `incident_record.v1.json` | No action without trace; evidence retention | `implements_invariants` |
| `privacy_evidence_classification.v1.json` | Privacy and evidence minimization | `implements_invariants` |
| `authority_graph_snapshot.v1.json` | Separation of powers; authority concentration | `implements_invariants` |

### Required rule

A schema without `implements_invariants` is incomplete.

### Readiness effect

Blocks schema readiness and assurance readiness.

---

## 6. Machine-readable non-claims

Non-claims must not remain free text only.

### 6.1 Required object

Add `non_claim.v1.json` with fields:

- `non_claim_id`
- `subject_ref`
- `excluded_claim`
- `excluded_scope`
- `reason`
- `risk_if_misread`
- `related_claim_ids`
- `review_status`

### 6.2 Required use

The following artifacts must include non-claims:

- cybernetic safety case;
- release-delta report;
- public assurance report;
- interpretability claim;
- monitor promotion claim;
- frontier readiness claim;
- incident closure claim.

### 6.3 Example

A monitor claim may state: this monitor detects a declared fixture class. Its non-claim must state that it does not prove absence of all prompt injection, all tool misuse, or all collusion.

### 6.4 Readiness effect

Blocks assurance.

---

## 7. Evidence disclosure profiles

Evidence classification must be explicit before any public assurance claim.

### 7.1 Profiles

| Profile | Meaning | Publication behavior |
|---|---|---|
| `public` | Safe to publish in full | Publishable by default |
| `redacted` | Publishable after removal of sensitive fields | Publish redacted artifact and reason |
| `private` | Internal evidence | Do not publish raw content |
| `sealed` | Committed evidence with restricted witness access | Publish commitment or summary only |
| `privileged` | Legal or privileged evidence | Restricted handling |
| `sensitive_ops` | Operational security sensitive | Publish only sanitized summary |
| `do_not_retain` | Should not be stored after immediate use | Store only deletion receipt or minimal audit record |

### 7.2 Required object

Add `privacy_evidence_classification.v1.json` with fields:

- `evidence_ref`
- `disclosure_class`
- `classification_reason`
- `allowed_audiences`
- `retention_policy`
- `redaction_policy`
- `publication_decision_ref`

### 7.3 Readiness effect

Blocks public assurance.

---

## 8. Supply-chain and artifact provenance

The evidence fabric must cover itself.

### 8.1 Required provenance for governance artifacts

Schemas, validators, fixtures, reports, receipts, and safety cases must record:

- artifact ID;
- version;
- digest;
- signer or committer;
- source repository;
- source path;
- dependency list;
- generation tool if generated;
- validation command;
- validation result;
- timestamp.

### 8.2 Required object

Add:

- `artifact_provenance.v1.json`
- `validator_run_receipt.v1.json`

### 8.3 Readiness effect

Blocks assurance and runtime promotion.

---

## 9. Readiness levels

Each plane gets readiness levels.

| Level | Name | Meaning |
|---|---|---|
| R0 | named | Concept is named but not captured |
| R1 | captured | Doctrine exists in repository |
| R2 | reconciled | Vocabulary and non-claims are reconciled |
| R3 | schema-ready | Schema exists and maps to invariants |
| R4 | fixture-ready | Valid and invalid fixtures exist |
| R5 | validator-ready | Executable validator passes and fails correctly |
| R6 | integration-ready | Consumer boundary is defined |
| R7 | runtime-ready | Runtime or platform service consumes artifact |
| R8 | assurance-ready | Safety case and public/private evidence boundary exist |
| R9 | promoted | Artifact promoted for declared scope |

### Current readiness estimate

| Plane | Current readiness | Reason |
|---|---:|---|
| Constitutional | R1 | Doctrine captured |
| Authority | R1 | Doctrine captured, schema pending |
| Runtime | R1 | Doctrine captured, implementation pending |
| Evidence | R1 | Doctrine captured, schema pending |
| Promotion | R1 | Doctrine captured, schema pending |
| Release delta | R1 | Doctrine captured, decomposition schema pending |
| Monitor network | R1 | Doctrine captured, schema pending |
| Replay audit | R1 | Doctrine captured, schema pending |
| Assurance/publication | R1 | Doctrine captured, profiles pending |
| Integration | R1 | Boundary captured, cross-repo issues pending |

### Readiness effect

Blocks any frontier claim beyond doctrine capture.

---

## 10. Concrete MVP trace example requirement

The next implementation PR must add one end-to-end trace that shows:

1. authority resolution;
2. instruction conflict status;
3. action plan;
4. tool permission scope;
5. side-effect assessment;
6. monitor alert;
7. control decision;
8. action trace or off-history evidence;
9. evidence receipt;
10. promotion decision;
11. non-claims;
12. replay status.

### Required fixtures

- `fixtures/cybernetic-governance/mvp_trace_allowed.json`
- `fixtures/cybernetic-governance/mvp_trace_blocked.json`
- `fixtures/cybernetic-governance/mvp_trace_transformed.json`

### Readiness effect

Blocks validator readiness.

---

## 11. CI checks

Once Tier 1 schema implementation begins, CI should fail if:

- docs reference a schema path that does not exist;
- a schema lacks `implements_invariants`;
- a schema lacks required enum imports;
- a fixture claims to be valid but fails validation;
- an invalid fixture passes validation;
- a safety case lacks non-claims;
- a promotion decision lacks evidence receipt;
- a public assurance example includes unclassified evidence;
- a release-delta report lacks gate color;
- an authority graph lacks role-collision assessment.

### Required tool

Add:

- `tools/validate_cybernetic_governance.py`

### Readiness effect

Blocks validator readiness.

---

## 12. Cross-repo dependency map

### 12.1 ProCybernetica

Owns doctrine, schemas, fixtures, validators, conformance vocabulary, and safety-case standards.

### 12.2 Prophet Platform

Consumes schemas after stabilization for runtime services, eval fabric, monitor API, evidence API, release-delta API, and dashboards.

### 12.3 SocioSphere

Consumes stabilized safety-case, promotion, authority graph, and registry objects for workspace-level governance and cross-repo promotion mapping.

### 12.4 Superconscious

No direct implementation dependency yet. Open only a dependency issue if a concrete contract is required, such as a required agent action trace envelope or off-history evidence record.

### 12.5 SourceOS

Future consumer for local-first evidence, replay receipts, provenance, and tamper-evident state integrity.

### 12.6 Readiness effect

Blocks runtime and integration readiness.

---

## 13. Gap table

| Gap | Lane | Effect | Next artifact |
|---|---|---|---|
| Lifecycle state machine | Doctrine + Schema | Blocks Tier 1 | `artifact_lifecycle_state.v1.json` |
| Canonical enums | Schema | Blocks Tier 1 | `enums.v1.json` |
| Schema-to-invariant traceability | Schema + Validator | Blocks schema readiness | `implements_invariants` field |
| Machine-readable non-claims | Schema + Assurance | Blocks assurance | `non_claim.v1.json` |
| Evidence disclosure profiles | Schema + Assurance | Blocks public assurance | `privacy_evidence_classification.v1.json` |
| Supply-chain provenance | Schema + Validator | Blocks assurance | `artifact_provenance.v1.json` |
| Readiness matrix | Doctrine + Validator | Blocks frontier claims | this document + validator |
| MVP trace example | Fixture + Validator | Blocks validator readiness | MVP trace fixtures |
| CI schema/doc consistency | Validator | Blocks validator readiness | `validate_cybernetic_governance.py` |
| Cross-repo map | Integration | Blocks runtime integration | integration issue/registry map |
| Monitor/evaluator calibration | Doctrine + Validator | Blocks monitor promotion | calibration fixtures |
| Release-delta gate color semantics | Schema + Validator | Blocks release readiness | release schemas |
| Role-collision metric | Schema + Validator | Blocks assurance | authority graph validator |

---

## 14. Merge criteria for moving beyond doctrine capture

The doctrine capture may merge as v0.1 draft if it clearly records non-claims and follow-on issues.

The work may not be called executable v0 until:

1. Tier 1 schemas exist;
2. canonical enums exist;
3. schemas map to invariants;
4. fixtures exist;
5. validators pass and fail correctly;
6. MVP trace examples exist;
7. public/private evidence profiles exist;
8. non-claim objects exist;
9. readiness matrix is updated;
10. integration boundaries are recorded.

The work may not be called frontier-ready until runtime consumption, monitor calibration, release-delta gates, safety cases, and public assurance reports are validated.

---

## 15. Non-claims

This audit does not implement the missing schemas, fixtures, validators, runtime services, or cross-repo adapters.

It also does not claim that the research runway has been reduced to production-grade form.

It claims only that the gaps are now explicit, assigned, and measurable.

---

## 16. Immediate next PR sequence

1. Add canonical enums and lifecycle schemas.
2. Add core Tier 1 schemas with invariant traceability.
3. Add MVP trace fixtures.
4. Add validator harness.
5. Add evidence disclosure and non-claim schemas.
6. Add release-delta and authority-graph validator fixtures.
7. Add Prophet Platform and SocioSphere integration issues after schema names stabilize.
