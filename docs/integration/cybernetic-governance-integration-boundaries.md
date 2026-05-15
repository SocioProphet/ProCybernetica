# Cybernetic Governance Integration Boundaries

Status: v0.1 integration-boundary record  
Issue: #28  
Publication state: public  
Runtime claim: none

## Purpose

This document records how the Cybernetic Governance Fabric doctrine, Tier 1 schemas, and defensive fixtures flow from ProCybernetica into the rest of the SocioProphet estate without moving runtime ownership into this repository.

The boundary is now concrete because:

- #26 landed the Tier 1 `schemas/cybernetic-governance/*` schema bundle;
- #27 landed defensive fixtures, a repository-local validator, pytest coverage, and Makefile targets;
- PR #76 recorded the schema/profile reconciliation decision that `schemas/cybernetic-governance/*` is the constitutional-governance object namespace while `schemas/governance-fabric/*` remains an executable validation lane.

## Ownership rule

ProCybernetica owns:

- public constitutional semantics;
- cybernetic-governance schemas;
- public-synthetic fixtures;
- repository-local validators;
- conformance vocabulary;
- doctrine and integration-boundary records.

ProCybernetica does not own:

- Prophet Platform runtime/eval-fabric services;
- SocioSphere workspace-governance runtime;
- AgentPlane execution runtime;
- Policy Fabric policy enforcement runtime;
- SourceOS/SociOS system or workstation runtime;
- Superconscious implementation;
- production telemetry pipelines.

## Stabilized ProCybernetica schema surface

The stabilized Tier 1 objects currently available for downstream consumption are:

- `authority_chain.v1.json`
- `instruction_conflict_case.v1.json`
- `agent_action_trace.v1.json`
- `tool_permission_scope.v1.json`
- `environment_delta.v1.json`
- `side_effect_assessment.v1.json`
- `off_history_evidence.v1.json`
- `monitor_alert.v1.json`
- `meta_monitor_report.v1.json`
- `evidence_receipt.v1.json`
- `promotion_decision.v1.json`
- `cybernetic_safety_case.v1.json`
- `release_delta_report.v1.json`
- `incident_record.v1.json`
- `privacy_evidence_classification.v1.json`
- `authority_graph_snapshot.v1.json`

The repository-local validation lane is:

```bash
make cybernetic-governance-fixtures
make cybernetic-governance-ci
```

## Prophet Platform boundary

Prophet Platform should consume ProCybernetica cybernetic-governance objects as runtime/eval-fabric evidence references, not redefine their constitutional semantics.

Downstream issue:

- `SocioProphet/prophet-platform#473` — consume ProCybernetica cybernetic governance evidence schemas.

Expected consumption pattern:

| ProCybernetica object | Prophet Platform use |
| --- | --- |
| `evidence_receipt.v1.json` | runtime/eval evidence reference or export object |
| `monitor_alert.v1.json` | platform monitor event reference |
| `meta_monitor_report.v1.json` | monitor health/calibration reference |
| `release_delta_report.v1.json` | release/readiness delta evidence |
| `cybernetic_safety_case.v1.json` | readiness or assurance evidence package reference |
| `authority_chain.v1.json` | governed runtime action authority reference |
| `tool_permission_scope.v1.json` | runtime tool/capability permission boundary reference |
| `agent_action_trace.v1.json` | agentic action trace evidence reference |

Prophet Platform remains the runtime owner. ProCybernetica provides the public constitutional semantics and validation artifacts.

## SocioSphere boundary

SocioSphere should consume ProCybernetica safety-case, promotion, evidence, privacy, incident, release, and authority objects for workspace governance and cross-repo promotion mapping.

Downstream issue:

- `SocioProphet/sociosphere#342` — consume ProCybernetica safety-case registry and promotion mapping.

Expected consumption pattern:

| ProCybernetica object | SocioSphere use |
| --- | --- |
| `cybernetic_safety_case.v1.json` | safety-case registry entry or workspace governance object |
| `promotion_decision.v1.json` | cross-repo promotion/hold/quarantine mapping |
| `authority_graph_snapshot.v1.json` | workspace separation-of-powers and authority-concentration view |
| `evidence_receipt.v1.json` | governance-board evidence reference |
| `privacy_evidence_classification.v1.json` | public/private evidence boundary display |
| `incident_record.v1.json` | incident/control-failure triage reference |
| `release_delta_report.v1.json` | release/change governance view |

SocioSphere remains the workspace-governance and registry owner. ProCybernetica provides the public constitutional semantics and validation artifacts.

## AgentPlane boundary

AgentPlane owns execution. ProCybernetica objects may be referenced by AgentPlane run capsules, tool grants, action dispatches, operator readouts, and proof-pack exhibits, but ProCybernetica must not implement AgentPlane runtime behavior.

Current boundary:

- AgentPlane owns run execution, replay execution, session artifacts, and runtime evidence production.
- ProCybernetica owns public governance semantics around authority, action traces, side effects, evidence receipts, safety cases, and promotion decisions.
- Future AgentPlane adapter work should reference ProCybernetica schema IDs and validator outputs rather than forking object names.

No new AgentPlane issue is created from #28 because this repository already has a separate AgentPlane governance binding track (#39) that should consume the stabilized Tier 1 schemas.

## Policy Fabric boundary

Policy Fabric owns policy enforcement and admission decisions. ProCybernetica may provide policy-relevant evidence objects and conformance vocabulary, but it must not become the policy runtime.

Expected references:

- `authority_chain.v1.json` for authority evidence;
- `tool_permission_scope.v1.json` for permission boundaries;
- `promotion_decision.v1.json` for promotion/hold/quarantine semantics;
- `off_history_evidence.v1.json` for blocked or transformed action evidence.

## SourceOS and SociOS boundary

SourceOS/SociOS own system, workstation, event, provenance, and operator-runtime surfaces. ProCybernetica may define constitutional expectations for authority, evidence, replay, side effects, and public assurance.

Expected references:

- SourceOS/SociOS events and receipts may point to ProCybernetica evidence receipts or authority-chain objects;
- ProCybernetica should reference SourceOS/SociOS runtime receipts rather than reimplement system event capture;
- workstation/operator conformance artifacts should remain owned by their source repositories and be cited as evidence.

## Superconscious boundary

Superconscious is under construction and receives no implementation changes from this work.

No Superconscious issue is created from #28 because no concrete dependency has emerged. A future issue is appropriate only if a specific dependency appears, such as:

- required `agent_action_trace.v1.json` envelope consumption;
- required `off_history_evidence.v1.json` record consumption;
- required safety-case or promotion-decision registry consumption.

Until then, ProCybernetica should not couple this lane to Superconscious.

## Integration non-duplication rules

Downstream repositories must not silently fork ProCybernetica cybernetic-governance object names.

Allowed patterns:

- reference ProCybernetica schema IDs;
- wrap ProCybernetica objects in downstream adapter metadata;
- add downstream runtime-specific fields outside the ProCybernetica object;
- emit public-safe fixtures that cite ProCybernetica validation output.

Disallowed patterns:

- redefine `authority_chain`, `evidence_receipt`, `promotion_decision`, or `cybernetic_safety_case` with incompatible semantics;
- treat ProCybernetica schemas as runtime implementation ownership;
- publish private telemetry as public evidence;
- collapse safety-case claims into production-readiness claims;
- bypass non-claim, redaction, and evidence-tier semantics.

## Follow-on status

| Target | Follow-on | Status |
| --- | --- | --- |
| Prophet Platform | `SocioProphet/prophet-platform#473` | opened |
| SocioSphere | `SocioProphet/sociosphere#342` | opened |
| AgentPlane | ProCybernetica #39 owns AgentPlane governance binding schemas | existing track |
| Policy Fabric | future policy-admission bridge issue if needed | not opened here |
| SourceOS/SociOS | future event/provenance adapter issue if needed | not opened here |
| Superconscious | only if concrete dependency emerges | not opened |

## Non-claims

This document does not implement any downstream adapter, runtime service, production telemetry pipeline, registry runtime, policy runtime, or AgentPlane executor. It records boundaries and follow-on anchors so future work consumes ProCybernetica artifacts without silently moving ownership or forking semantics.
