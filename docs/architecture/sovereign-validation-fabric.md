# Sovereign Validation Fabric

Status: proposal-candidate for policy-fabric codification  
Issue: #100  
Plane: ProCybernetica / policy fabric  
Runtime owner: downstream repositories, primarily Sociosphere and Prophet Platform

## Purpose

Sovereign Validation Fabric (SVF) defines governed inner-loop validation for agentic development across the Prophet estate. It internalizes the useful pattern of agent-runnable validation plans without adopting a vendor adapter or making any one execution environment the root abstraction.

SVF treats validation as a typed, policy-bounded, receipt-producing capability. A coding agent, workspace runner, CI lane, or platform service may request validation, but it may execute only registered `ValidationAction` records through a declared `ValidationPlan` under an admitted `ValidationCapabilityPolicy`.

## Non-goals

SVF is not a vendor integration.

SVF is not a generic arbitrary-command runner.

SVF is not a replacement for CI. CI remains an adjudication and regression surface; SVF supplies agent-invokable validation primitives that can run before a PR is opened or before a promotion request is made.

SVF is not a production runtime service in ProCybernetica. ProCybernetica defines the contracts and conformance semantics. Downstream repositories implement runners, adapters, plans, and product surfaces.

## Plane ownership

### ProCybernetica / policy fabric

ProCybernetica owns the authority vocabulary:

- `ValidationAction`
- `ValidationPlan`
- `ValidationCapabilityPolicy`
- `ValidationRun`
- `ValidationReceipt`
- side-effect taxonomy
- claim-scope taxonomy
- receipt overclaim rules
- public-safe conformance fixtures

### Sociosphere

Sociosphere owns workspace discovery and execution routing:

- repo-to-plan registry
- changed-path plan selection
- local runner contract
- receipt verification entrypoint
- workspace-level dogfood plans

Sociosphere consumes ProCybernetica policy contracts. It does not define validation authority independently.

### Agent plane / Prophet Platform

The agent plane owns invocation and user/product experience:

- `validate_change` skill/tool contract
- closed-loop patch/rerun flow
- PR-readiness summary
- validation catalog and receipt display

The agent plane may not invent commands, bypass blocking failures, mutate policy to make validation pass, or promote claims without receipts.

### Specialist repos

SCOPE-D owns defensive and assurance validation plans. Ontogenesis owns semantic validation plans. SourceOS and SociOS own OS/distribution validation plans.

### Model router

The model router consumes receipt state, risk class, repo criticality, and unresolved failures to adjust autonomy and verifier depth. It does not define plan validity, authorize actions, or certify receipts.

### Subconscious / memory mesh

Subconscious may learn from failure histories, repeated repair patterns, flaky plans, and plan usefulness. It does not authorize execution, mutate policy, or certify results.

## Core doctrine

1. Validation is a governed capability, not an arbitrary shell command.
2. Agents execute only registered Actions.
3. Plans compose only approved Actions.
4. Capability policies bind execution before an Action runs.
5. Receipts certify only declared, executed, evidence-backed claims.
6. Receipts must explicitly record non-certified claims where overclaim risk is natural.
7. Natural-language authored plans are drafts only; the canonical artifact is typed and schema-validated.
8. Production-environment execution is forbidden by default.
9. Runtime adapters are downstream implementation details, not policy authority.
10. Vendor adapters are out of scope for the canonical SVF primitive.

## Schema family

The first public schema tranche lives under `schemas/cybernetic-governance/` to match existing repository convention:

- `svf_validation_action.v1.json`
- `svf_validation_plan.v1.json`
- `svf_validation_capability_policy.v1.json`
- `svf_validation_run.v1.json`
- `svf_validation_receipt.v1.json`

## Side-effect taxonomy

Initial side-effect classes:

- `read_only`: may read declared inputs only.
- `write_temp`: may write to temporary output directories only.
- `write_workspace`: may mutate declared workspace paths.
- `write_repo`: may mutate repository files; must be explicitly authorized.
- `network_none`: no network use.
- `network_allowlisted`: network use only to declared allowlist.
- `cluster_sandbox`: may use a sandbox cluster.
- `qemu_sandbox`: may run virtualized OS/image validation.
- `browser_sandbox`: may run browser automation against declared test targets.
- `credential_none`: no credential access.
- `credential_read_scoped`: may read declared scoped credentials.

## Claim-scope taxonomy

Initial claim scopes:

- `schema_conformant`
- `fixtures_validated`
- `tests_passed`
- `semantic_roundtrip_preserved`
- `policy_boundary_preserved`
- `non_production_only`
- `runtime_smoke_passed`
- `artifact_integrity_verified`
- `receipt_integrity_verified`

A claim scope is not a global truth claim. It is a bounded assertion about the executed Plan, the declared inputs, and the evidence recorded in a Receipt.

## Receipt overclaim rule

A `ValidationReceipt` may certify a claim only if all of the following are true:

1. the claim appears in the referenced Plan's declared claim scope;
2. every Action needed for the claim completed successfully or the Plan declares an accepted inconclusive mode;
3. the input and output artifact digests are present;
4. the CapabilityPolicy admits the execution context;
5. the Receipt records the Plan and Policy digests;
6. the Receipt lists adjacent claims that are not certified when confusion is likely.

Examples of non-certified claims:

- schema validation does not certify runtime safety;
- a synthetic assurance fixture does not certify field behavior;
- a QEMU smoke test does not certify full hardware compatibility;
- an ontology roundtrip does not certify domain truth beyond declared shapes;
- a passing advisory plan does not certify merge readiness unless a blocking profile says so.

## Default production boundary

Production-environment execution is forbidden by default. The v1 public SVF primitive should fail closed for production-environment claims unless a future explicit policy extension defines stronger admission and evidence requirements.

## First conformance expectations

The initial conformance lane must reject:

- unregistered command bindings;
- Actions without owners;
- unsupported side-effect classes;
- unsupported network modes;
- undeclared credential access;
- Plans referencing unknown Actions;
- Plans declaring unsupported claim scopes;
- Receipts referencing unknown Plans;
- Receipts missing input digests;
- Receipts missing Plan or Policy digests;
- Receipts certifying claims outside Plan scope;
- Receipts claiming production-environment assurance without an explicit policy profile.

## Downstream implementation order

1. ProCybernetica defines and validates the schema family.
2. Sociosphere implements registry, changed-path selection, local runner, and receipt verifier.
3. Sociosphere dogfoods a workspace self-validation Plan.
4. ProCybernetica self-validates the SVF schema/fixture lane through Sociosphere once available.
5. SCOPE-D adds assurance validation Plans.
6. Ontogenesis adds semantic validation Plans.
7. SourceOS and SociOS add OS/distribution validation profiles.
8. Prophet Platform exposes `validate_change` to agents.
9. Model router consumes receipt state.
10. Subconscious consumes failure summaries with no authority semantics.
