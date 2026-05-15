# Schema and Profile Reconciliation

Status: estate-aware v0 reconciliation update

Turn: 10 / 20

This document reconciles the captured ProCybernetica blueprint with the active GitHub estate. It supersedes the initial schema seed posture by accounting for completed integration maps across AgentPlane, semantic-serdes/SHIR, ontogenesis, SourceOS/SociOS, Prophet Platform, HolographMe, Foundry/model-governance, and workstation/operator surfaces.

## Governing rule

ProCybernetica owns public constitutional semantics, doctrine-as-code, schema/profile interpretation, public conformance expectations, and reference-kit posture.

It does not own runtime/deployment services, model lifecycle ledgers, ontology release discipline, semantic-serdes contracts, SourceOS typed contracts, AgentPlane evidence artifacts, workstation runners, terminal products, browser runtimes, or product UI implementation.

## Sources reconciled

Primary source captures:

- `docs/source-captures/VOLUME_I_EXPANDED_MONOGRAPH_CAPTURE.md`
- `docs/source-captures/CONTROLPLANE_TECHNICAL_PAPER_CAPTURE.md`
- `docs/source-captures/GENESIS_INCEPTION_CAPTURE.md`
- `docs/source-captures/PROPHET_ARCHITECTURE_SPECIFICATION_CAPTURE.md`
- `docs/source-captures/EXECUTABLE_SPECIFICATION_PACK_CAPTURE.md`
- `docs/source-captures/REFERENCE_IMPLEMENTATION_KIT_CAPTURE.md`
- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`
- `docs/source-captures/VOLUME_VI_OPERATIONAL_MESH_CAPTURE.md`
- `docs/source-captures/VOLUME_VII_SECURE_COORDINATION_CAPTURE.md`
- `docs/source-captures/VOLUME_VIII_AUTONOMIC_CONSTITUTION_CAPTURE.md`

Estate maps:

- `docs/integration/agentplane-evidence-map.md`
- `docs/integration/semantic-serdes-shir-map.md`
- `docs/integration/ontogenesis-governance-map.md`
- `docs/integration/sourceos-socios-contract-map.md`
- `docs/integration/prophet-platform-record-map.md`
- `docs/integration/holographme-genesis-inception-map.md`
- `docs/integration/foundry-model-governance-map.md`
- `docs/integration/workstation-operator-surface-map.md`

## Source agreement

The captured corpus and estate maps agree on these requirements:

1. Every consequential participant should be representable as a node or referenced domain object.
2. Nodes expose identity, lifecycle, interfaces, memory, policy, and observability surfaces.
3. Commands and delegation are authority-bearing records, not informal messages.
4. Artifacts, claims, policies, model updates, release records, and operator actions need provenance.
5. Replay is constitutional evidence, not only debugging.
6. Proposal and promotion are distinct.
7. Learned, routed, inferred, or heuristic outputs stay soft-lane until validation and promotion.
8. Repositories are governed memory organs, not passive buckets.
9. Operator interventions must be typed and replayable.
10. Public implementation should publish public-safe schemas, examples, tests, methodology, and source-state summaries.
11. Existing upstream repos keep ownership of their concrete contract families.

## v0 schema disposition

### Keep in ProCybernetica v0

These schemas are appropriate public constitutional surfaces in this repository.

| Schema | Current status | Role |
| --- | --- | --- |
| `node_descriptor.schema.json` | present, reconciled | constitutional identity, lifecycle, and conformance surface for nodes |
| `artifact_envelope.schema.json` | present | generic public artifact/evidence wrapper |
| `policy_envelope.schema.json` | present | constitutional policy reference/summary surface |
| `command_envelope.schema.json` | present | authority-bearing command wrapper |
| `delegation_envelope.schema.json` | present | bounded handoff / scoped authority wrapper |
| `observation_envelope.schema.json` | present | information-plane observation wrapper |
| `status_envelope.schema.json` | present | node status and health report |
| `event_envelope.schema.json` | present | cross-plane event record with public release posture |
| `trace_event.schema.json` | present | causal/replay trace event |
| `transition_record.schema.json` | present | lifecycle transition evidence |
| `replay_envelope.schema.json` | present, reconciled | constitutional replay manifest |
| `evaluation_result.schema.json` | present, reconciled | evaluation / benchmark / conformance result summary |
| `promotion_decision.schema.json` | present, reconciled | constitutional admission, quarantine, rollback, or review verdict |
| `incident_report.schema.json` | present | review/remediation episode report |
| `claim.schema.json` | present | public claim object for Book XI practicum and scoring/evidence surfaces |
| `provenance_record.schema.json` | present | source/evidence lineage record |
| `capability_descriptor.schema.json` | present | high-level capability gateway descriptor |

### Keep as profiles, not schemas

| Contract | Current status | Reason |
| --- | --- | --- |
| `controlplane_state_machine.yaml` | present | lifecycle transition law belongs in profile layer |
| `promotion_policy.example.yaml` | present | threshold/promotion behavior belongs in profile layer |
| `bt_semantic_profile.yaml` | present | behavior-tree runtime semantics are profile-level |
| `k3_bridge_lifecycle.yaml` | present | Genesis/Inception transition profile, not full domain schema yet |

### Defer from v0

These remain valid blueprint concepts but should not be added to v0 until adapter and upstream maps stabilize.

| Deferred schema | Reason |
| --- | --- |
| `hologram.schema.json` | semantic-serdes/SHIR and ontogenesis own semantic object authority; add only after adapter design |
| `genesis_seed.schema.json` | needs HolographMe, Agent Registry, Policy Fabric, model/router, and SourceOS alignment first |
| `inception_request.schema.json` | same as above; should reference domain objects rather than duplicate them |
| `twin_runtime_descriptor.schema.json` | should likely use `domain_object_ref` and avoid cloning HolographMe |
| `policy_conflict_case.schema.json` | Volume VIII concept; wait until Policy Fabric / SourceOS policy mapping is complete |
| `stability_report.schema.json` | Volume VIII concept; wait for conformance plan and platform eval fabric mapping |
| `constitutional_verdict.schema.json` | may be needed later; currently `PromotionDecision` covers v0 decisions |
| `corpus_manifest.schema.json` | SHIR/ontogenesis/model-governance-ledger own relevant corpus/semantic artifacts |
| `operator_provenance_case.schema.json` | operator surfaces own concrete events; use EventEnvelope/ProvenanceRecord in v0 |
| `export_bundle.schema.json` | platform, SourceOS, semantic-serdes, and AgentPlane own concrete export/receipt surfaces |
| `attestation_statement.schema.json` | ontogenesis/AgentPlane/SourceOS/Prophet Platform own concrete attestation surfaces |
| `benchmark_corpus.schema.json` | model-governance-ledger / platform eval fabric own benchmark/eval records |
| `operator_record.schema.json` | covered in v0 by EventEnvelope, TraceEvent, TransitionRecord, and PromotionDecision |

## Upstream contract families ProCybernetica must not duplicate

| Upstream family | Owner | ProCybernetica action |
| --- | --- | --- |
| AgentPlane artifacts | `SocioProphet/agentplane` | reference RunArtifact, ReplayArtifact, PromotionArtifact, SessionArtifact, and related evidence |
| semantic-serdes primitives | `SocioProphet/semantic-serdes` | reference Event/Context/Surface, canonical enums, agent messages, decision artifacts, replay artifacts |
| SHIR object model | `SocioProphet/ontogenesis` and `semantic-serdes` | reference CandidateAssertion, Assertion, ProjectionLossReport, Receipt, and curation objects |
| ontology release discipline | `SocioProphet/ontogenesis` | reference SHACL reports, ledgers, signatures, SBOMs, module registry |
| SourceOS typed contracts | `SourceOS-Linux/sourceos-spec` | reference Policy, PolicyDecision, RunRecord, EventEnvelope, ProvenanceRecord, AgentSession, BootProofRecord, ReleaseReceipt, etc. |
| workstation conformance | `SociOS-Linux/workstation-contracts` | reference conformance fixtures and run receipts |
| Agent Machine runtime | `SourceOS-Linux/agent-machine` | reference AgentMachine, AgentPod, StorageReceipt, ActivationDecision, runtime evidence |
| Prophet Platform contracts | `SocioProphet/prophet-platform` | reference EventEnvelope, EvidenceReceipt, MembraneDecision, eval records, FogStack readiness records |
| HolographMe domain schemas | `SocioProphet/HolographMe` | reference HumanDigitalTwin, ConsentPolicy, Mission, projections, transition receipts |
| Foundry/model governance | `functional-model-surfaces`, `model-router`, `model-governance-ledger`, `guardrail-fabric`, `sourceos-model-carry` | reference manifest, route, governance, decision, carry, and ledger records |
| Operator products | `agent-term`, TurtleTerm, BearBrowser, source-os, socioprophet-web | reference operator/gateway events and receipts |

## Canonical v0 lifecycle

### Fractal Node lifecycle

Use:

- `unconfigured`
- `configured`
- `inactive`
- `active`
- `degraded`
- `recovery`
- `quarantined`
- `retired`
- `finalized`

Decision: keep both `retired` and `finalized`.

Rationale:

- `retired` means the node no longer has operational authority.
- `finalized` means archival closure or evidentiary finalization after retention/replay obligations are satisfied.

### Twin runtime lifecycle

Keep separate from generic node lifecycle:

- `draft`
- `candidate`
- `ready`
- `executing`
- `paused`
- `quarantined`
- `revoked`
- `archived`

Decision: do not encode this as a ProCybernetica v0 schema yet. Keep it in profile/mapping docs until Genesis/Inception schemas are designed around HolographMe and related domain objects.

## Lifecycle transition vocabulary

Use the existing `profiles/controlplane_state_machine.yaml` vocabulary for v0 implementation. Treat alternate names from source captures as aliases in docs, not schema enums.

Canonical node transition events for v0:

- `configure_ok`
- `admission_granted`
- `admission_denied`
- `activate_ok`
- `deactivate`
- `health_degraded`
- `recover_start`
- `recover_ok`
- `recover_failed`
- `quarantine`
- `remediation_ok`
- `revoke`
- `retire`
- `finalize`

Recommendation: add alias metadata to `controlplane_state_machine.yaml` in Turn 11 rather than expanding enum values in schemas.

## Promotion decision vocabulary

Current schema vocabulary is accepted for v0:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`
- `rollback-required`
- `revoke-authority`

Decision: keep rollback/revoke as promotion decision values for v0, but use governance phrasing (`rollback-required`, `revoke-authority`) to avoid confusing them with direct actuator commands.

Potential future split: `constitutional_verdict.schema.json` may later absorb rollback/revoke/stability verdicts after Volume VIII adapter work.

## Evaluation result vocabulary

Current schema vocabulary is accepted for v0:

- `pass`
- `conditional-pass`
- `warn`
- `fail`
- `drift`
- `inconclusive`
- `manual-review`

Promotion recommendations remain:

- `reject`
- `shadow-only`
- `limited-authority`
- `full-promotion`
- `quarantine`
- `manual-review`

## Conformance class reconciliation

Keep the Volume III ladder in v0:

- `C0-schema-conformant`
- `C1-supervised-node`
- `C2-replayable-node`
- `C3-production-node`
- `C4-safety-critical-embodiment`

Map later to:

- functional-model-surfaces M0-M5 maturity;
- SourceOS/SociOS conformance lanes;
- AgentPlane run/replay evidence;
- Prophet Platform eval fabric;
- ontogenesis SHACL/ledger gates.

Do not collapse these ladders yet. They measure adjacent but different things.

## Current v0 fixture coverage

Public synthetic fixtures currently validate through tests for:

- node descriptor
- policy envelope
- transition record
- artifact envelope
- claim
- provenance record
- event envelope
- trace event
- command envelope
- delegation envelope
- status envelope
- capability descriptor
- replay envelope
- evaluation result
- promotion decision

Scoring/dashboard public sample fixtures exist for:

- lab scoring sample CSV
- evidence registry sample CSV
- monitoring deltas sample CSV
- dashboard export sample JSON

## Runtime scaffold status

`procyber/` remains a reference validation scaffold, not a production runtime.

Accepted v0 runtime scope:

- schema loading;
- JSON payload validation;
- public practicum report emission;
- CI fixture checks.

Rejected for v0 inside this repo:

- platform service runtime;
- AgentPlane execution;
- SourceOS runner;
- ontology release pipeline;
- model routing;
- guardrail runtime;
- UI implementation;
- browser/terminal runtime.

## Package naming decision

Current CLI/package name `procyber` may remain for v0 validation scaffold.

Open future decision: rename to `procybernetica` only if packaging/release work begins. Do not block v0 conformance docs on package naming.

## Schema changes still safe after estate maps

Only these schema-level changes are safe before adapter fixtures land:

1. Add optional `external_refs` style fields only if they are generic and do not encode upstream-specific schemas.
2. Add examples under `examples/integrations/*` referencing upstream artifact IDs.
3. Add documentation links from existing schemas to upstream maps.
4. Add public conformance checks that require references, not duplicated payloads.

Avoid adding new large schema families until adapter backlog and conformance plan complete.

## Recommended next-turn profile work

Turn 11 should update profiles, not schemas:

- add alias metadata to `controlplane_state_machine.yaml`;
- clarify `promotion_policy.example.yaml` against accepted decision values;
- ensure BT profile points to AgentPlane/SourceOS execution evidence rather than implementing BT runtime;
- ensure K3 profile references HolographMe and future domain-object refs without cloning domain schemas.

## Updated follow-up issues

1. Keep issue #6 open for remaining schema cleanup, but narrow it to fixtures/docs rather than new schema families.
2. Keep issue #7 open for profile alias and invariant normalization.
3. Keep issue #8 open for practicum validation/report flow only.
4. Use mapping follow-up issues #15, #16, #17 and adapter backlog later for integration fixtures.
5. Do not open more schema-family issues until Turn 12 adapter backlog.

## Current recommendation

The v0 schema surface is now sufficient for public review once profile reconciliation, adapter backlog, and conformance docs land.

Do not continue expanding schemas. Move to profiles, conformance, adapter refs, and public review checklist.

---

## 2026-05-15 branch and schema-family reconciliation addendum

Status: post-falsification-CI branch-audit addendum  
Issue: #2  
Scope: retained branch disposition, schema-family unblock criteria, and supersession decisions

### Purpose

This addendum records reconciliation findings from the branch cleanup and post-#45 validation pass. It prevents cleanup and implementation work from erasing branch-local schema work that is not yet represented by the current v0 reconciliation surface.

The addendum does not implement new schemas, validators, profiles, runtime services, or integration adapters. It records what is captured, what is superseded, what remains stranded, and what decisions are required before blocked schema issues can move.

### Branch disposition as schema evidence

| Branch | Disposition | Reconciliation meaning |
| --- | --- | --- |
| `work/falsification-ci-45` | safe delete after merge | Falsification coverage registry, owners registry, validators, fixtures, tests, and Makefile targets are on `main`. |
| `work/evidence-escalation-standard-58` | safe delete after merge | Evidence and escalation standard, coordinated-compromise schema, and public-synthetic example are on `main`. |
| `work/unified-falsification-v1-44` | safe delete after merge | Unified falsification doctrine is on `main`. |
| `work/epistemic-governance-binding-42` | safe delete after merge | Epistemic Governance doctrine binding is on `main`. |
| `work/triune-default-deny-networkpolicy-69` | safe delete after merge | Triune default-deny NetworkPolicy example is on `main`. |
| `work/oai-pmh-lawful-harvest` | safe delete after content-equivalence audit | PR #59 landed the lawful metadata harvesting contract; all changed files audited as content-equivalent to `main`. |
| `work/interpretability-tier2-composition-v0-1-clean` | safe delete after content-equivalence audit | Standalone interpretability composition manifest schema, fixtures, and tests are on `main`. |
| `capture/triune-inception-lab-v0-1-clean` | safe delete after content-equivalence audit | Clean Triune capture is on `main`; `Makefile` is superseded by newer `main` additions while retaining `triune-ci`. |
| `capture/triune-inception-lab` | superseded by clean Triune branch | Older fixture used local-looking paths and a not-yet-present network-policy path. Clean branch intentionally replaced those with opaque `synthetic://` references and explicit synthetic non-claims. |
| `cybernetic-governance-tier1-schemas` | retain | Contains unique #26-relevant schemas under `schemas/cybernetic-governance/`; not equivalent to merged `schemas/governance-fabric/` Tier 1 lane. |
| `work/interpretability-tier2-composition` | retain | Closed-unmerged PR #53 branch mutates `composition_certificate.v1.json` directly with interpretability artifact kinds and domain annotations. Not equivalent to standalone manifest path on `main`. |
| `work/interpretability-tier2-composition-v0` | retain | Same design family as PR #53: direct `composition_certificate.v1.json` mutation. Must be resolved together with PR #53 branch. |
| `cybernetic-governance-doctrine-v0-1` | retain until full audit completes | Multiple high-risk samples are content-equivalent on `main`, but the branch has a 71-commit surface and requires file-by-file equivalence before deletion. |

### Namespace conflict: `governance-fabric` versus `cybernetic-governance`

The repository currently has two adjacent schema families that must not be silently merged by assumption:

| Family | Current status | Meaning |
| --- | --- | --- |
| `schemas/governance-fabric/*` | merged executable lane | Existing Tier 1/Tier 2 validation surface, Makefile targets, fixtures, and CI coverage. |
| `schemas/cybernetic-governance/*` | partial and branch-retained | Constitutional-governance schema namespace tied to #26 and the PR #25 doctrine bundle. |

Decision for now: keep both concepts distinct until #26 is reconciled.

The `governance-fabric` lane is the current executable validation lane. The `cybernetic-governance` lane is the candidate constitutional-governance object namespace requested by #26. The branch `cybernetic-governance-tier1-schemas` must be retained because it contains the exact #26 file family, but those schemas must not be promoted merely by branch existence.

#### Required #26 decision

#26 must choose one of these paths before implementation continues:

1. Promote `schemas/cybernetic-governance/*` as the canonical Tier 1 constitutional-governance namespace and map it to `governance-fabric` fixtures.
2. Retire `schemas/cybernetic-governance/*` in favor of `schemas/governance-fabric/*`, with an explicit supersession note for every #26 schema name.
3. Keep both namespaces but define a stable mapping: `cybernetic-governance` for constitutional object law, `governance-fabric` for executable test harness and composition lanes.

Default recommendation: choose path 3 unless a maintainer decides the namespace split is too costly. It preserves source intent while avoiding a destructive rename of the already-working validation lane.

### Interpretability composition fork

Two retained branches preserve an unresolved design alternative:

- `work/interpretability-tier2-composition`
- `work/interpretability-tier2-composition-v0`

Both directly mutate `schemas/governance-fabric/composition_certificate.v1.json` to admit interpretability artifact kinds such as `model_artifact`, `sae_artifact`, `feature_artifact`, `feature_explanation`, `feature_activation_set`, `steering_intervention`, `causal_triad`, `attribution_graph`, `off_target_audit`, `manifold_baseline`, `implementability_curve`, `robustness_certificate`, `benchmark_result`, and `public_interpretability_note`.

The later clean lane on `main` instead adds a standalone schema:

```text
schemas/governance-fabric/interpretability_composition_manifest.v1.json
```

Decision for now: the standalone manifest path is the active path on `main`; the direct `composition_certificate.v1.json` mutation is not adopted.

The retained branches should not be deleted until a supersession decision is recorded. The needed decision is whether interpretability composition should remain a domain-specific manifest that can be cited by composition certificates, or whether the base composition certificate must be generalized to include interpretability artifact kinds directly.

Default recommendation: retain the standalone manifest path. Do not widen `composition_certificate.v1.json` until a concrete consumer proves that a single base certificate must enumerate interpretability artifact kinds directly.

### Certificate-family status after #47 audit

#47 remains blocked for schema-bump work. The issue names M0-M5 certificate-family schemas and asks for additive v1.3 fields:

- `authority_layer`
- `promotion_state`
- `reasoning_trace_ref`
- `cadence_classification`

Current status:

- transition fixtures with v1.3-style fields exist under `tests/fixtures/transition/`;
- the named base certificate-family schemas are not yet discoverable as canonical schema files on `main`;
- F4.1-F4.3 falsification observables are now registered by #45, but F4.2 cannot become schema-testable until certificate-family schemas exist or are explicitly deferred.

Decision for now: #47 doctrine can proceed separately, but the schema bump remains blocked until the certificate-family schema locations and owner boundaries are resolved.

Default recommendation: create or update a certificate-family index before mutating schemas. That index should identify whether M0-M5 belong primarily to ProCybernetica, functional-model-surfaces, model-governance-ledger, or a bridge layer.

### Capability-tier and bridge status

#43 and #46 remain blocked by certificate-family and bridge-path uncertainty.

#43 references `docs/bridges/BRIDGE_SCHEMAS_V1_EXECUTION_PLAN.md`, but that path was not present when the unified falsification document was drafted. #46 depends on certificate and bridge schemas that are not all present as stable schema files.

Decision for now: do not add SHACL companion shapes or bridge validators until the schema locations are known. Add explicit deferred status where a schema or bridge plan is missing.

Default recommendation: before #43 implementation, create a small reconciliation note that either restores `docs/bridges/BRIDGE_SCHEMAS_V1_EXECUTION_PLAN.md` or records the corrected canonical path.

### Dependency-control calculus status

#41 remains blocked on core governance object stability. Its dependency-control schemas should reference core objects rather than replace them:

- authority chains;
- agent action traces;
- tool permission scopes;
- off-history evidence;
- monitor alerts;
- release-delta reports;
- evidence receipts;
- cybernetic safety cases;
- AgentPlane run capsules;
- proof-pack exhibits.

Decision for now: #41 must wait for #26 namespace disposition or explicitly reference both candidate namespaces with deferred status.

Default recommendation: implement #41 only after #26 chooses the `cybernetic-governance` / `governance-fabric` mapping. Otherwise dependency-control schemas will hard-code an unstable namespace.

### Agentic Ops status

#50 depends on three artifacts already present on `main`:

- `docs/integrations/AGENTIC_OPS_CMDP_UCO_PERSONA_POLICY.md`
- `schemas/cybernetic-governance/agentic_persona_policy.v1.yaml`
- `tools/cybernetic_governance/agentic_persona_substrategy_chooser.py`

Decision for now: #50 can move as a fixture/validation tranche, but should avoid creating another broad schema family until #26/#41 settle the core object namespace.

Default recommendation: split #50 into two phases:

1. validate existing persona-policy YAML and substrategy chooser behavior with fixtures;
2. defer new `agentic_*` telemetry schemas until the core governance namespace decision is made.

### MFEL status

#52 is independent enough to proceed before full schema freeze if it keeps its own namespace:

```text
schemas/mfel/*
```

Decision for now: MFEL can proceed as a public-safe standard tranche because it is a case-analysis and evidence-layer standard, not a replacement for core controlplane envelopes.

Constraint: MFEL examples must remain sanitized or synthetic and must preserve the standard rule separating observed fact, derived fact, interpretation, hypothesis, and prohibited conclusion.

### Updated unblock matrix

| Issue | Current status | Unblock condition |
| --- | --- | --- |
| #26 | blocked: reconciliation | Decide `cybernetic-governance` versus `governance-fabric` namespace relationship. |
| #27 | blocked behind #26 | Add fixtures and validators only after target schema namespace is fixed. |
| #28 | blocked behind #26 | Define integration boundaries after schema namespace and object ownership are fixed. |
| #41 | blocked behind #26 | Dependency-control schemas must reference stable governance objects. |
| #43 | blocked by bridge/certificate paths | Restore or correct bridge execution-plan path; confirm certificate-family schema locations. |
| #46 | blocked by #43/#47 | Add SHACL only after certificate and bridge schemas exist or are explicitly deferred. |
| #47 | partially blocked | Doctrine may proceed; schema bump waits for certificate-family schema index. |
| #50 | partially unblocked | Existing persona-policy and chooser fixtures may proceed; new telemetry schema family waits. |
| #52 | unblocked | May proceed as independent MFEL namespace if public-safe examples and non-attribution constraints are preserved. |

### Human decisions required

| ID | Decision | Default recommendation |
| --- | --- | --- |
| HD-1 | Should `schemas/cybernetic-governance/*` become canonical, be retired, or map to `schemas/governance-fabric/*`? | Keep both with explicit mapping. |
| HD-2 | Should interpretability artifact kinds be added to `composition_certificate.v1.json` or remain in standalone `interpretability_composition_manifest.v1.json`? | Keep standalone manifest until a concrete consumer requires base-certificate widening. |
| HD-3 | Where do M0-M5 certificate-family schemas live? | Create a certificate-family index before any v1.3 schema mutation. |
| HD-4 | Should #52 MFEL land before full schema freeze? | Yes, if isolated under `schemas/mfel/*` and public-safe. |
| HD-5 | Can `cybernetic-governance-doctrine-v0-1` be deleted after sampled equivalence? | Not yet. Complete file-by-file audit first. |

### Updated recommendation

The v0 core envelope surface is sufficient for public review work, but the governance-extension surface is not fully reconciled.

Do not delete retained schema branches or mutate broad schema families until the namespace and certificate-family decisions above are resolved. Proceed next with one of two safe tracks:

1. close #2 by merging this reconciliation addendum and using it as the decision frame for #26/#47/#50; or
2. implement #52 as an isolated MFEL standard tranche that does not depend on the unsettled governance schema namespace.
