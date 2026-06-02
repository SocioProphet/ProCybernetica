# Repo Hardening Manifest Template

**Document ID:** `REPO-HARDENING-MANIFEST-TEMPLATE`
**Version:** 0.1.0
**Status:** Public-review template
**Parent:** `EFFECTIVE-AUTHORITY-ARCHITECTURE`

Every repo in the estate should eventually carry a `.prophet/hardening.yaml` manifest. The manifest declares what authority the repo creates, consumes, stores, delegates, or enforces.

This is a declaration surface, not a marketing label. Unknown or undeclared authority is non-compliant.

## Canonical YAML template

```yaml
schema_version: effective-authority/v0.1
repo: OWNER/NAME
zone: A
owner: TBD
maturity: draft

authority_classes: []
observation_channels: []
control_channels: []
egress_classes: []
background_workers: []
runtime_subjects: []
connector_surfaces: []
policy_sources: []
ledger_sinks: []
ci_validators: []
```

## Field rules

`repo` must be the GitHub repository full name.

`zone` must be one of:

- `A` — doctrine and standards;
- `B` — platform and workspace;
- `C` — agent/tool/model control plane;
- `D` — SourceOS/Bear local runtime;
- `E` — search, memory, world model, and semantic observers;
- `F` — packaging and distribution;
- `G` — research and proof estate.

`authority_classes` names the authority the repository can create or govern, such as `policy_evaluator`, `agent_runtime`, `browser_bridge`, `semantic_index`, `runtime_boundary`, `package_distribution`, or `proof_artifact_lineage`.

`observation_channels` lists local or connector-based surfaces that can observe user, project, device, semantic, or runtime state. Examples: `filesystem`, `semantic_index`, `browser_dom`, `terminal_pty`, `cloud_document`, `memory_store`.

`control_channels` lists channels that can carry commands or trigger actions. Examples: `mcp`, `ssh`, `browser_bridge`, `websocket`, `native_host`, `scheduler`, `ci_webhook`, `cloud_connector`, `agent_to_agent`.

`egress_classes` lists outbound payload classes the repo may produce or govern. Examples: `metadata`, `policy`, `schema`, `model_request`, `tool_input`, `file_content`, `semantic_index`.

`background_workers` lists timers, schedulers, daemons, event workers, sync loops, or recurring jobs.

`runtime_subjects` lists local processes, services, containers, VMs, extension hosts, plugin hosts, or model runtimes governed by this repo.

`connector_surfaces` lists external service connectors, such as GitHub, Google Drive, Gmail, cloud storage, browser extension stores, model providers, or ticketing systems.

`policy_sources` lists sources that may change runtime behavior, such as `repo`, `org`, `signed_config`, `user_grant`, `runtime_contract`, or `system_invariant`.

`ledger_sinks` lists where authority events must be recorded, usually `model-governance-ledger`, `policy-fabric`, `sourceos-syncd`, or a repo-local evidence ledger.

`ci_validators` lists CI lanes that validate the manifest or the authority records emitted by this repo.

`maturity` must be one of `draft`, `partial`, `enforced`, or `verified`.

## Zone examples

### Zone A — doctrine and standards

```yaml
schema_version: effective-authority/v0.1
repo: SocioProphet/ProCybernetica
zone: A
owner: ProCybernetica standards lane
maturity: draft
authority_classes:
  - doctrine
  - schema
  - validator
observation_channels: []
control_channels: []
egress_classes: []
background_workers: []
runtime_subjects: []
connector_surfaces: []
policy_sources:
  - repo
ledger_sinks:
  - model-governance-ledger
ci_validators:
  - effective-authority-ci
```

### Zone C — agent/tool/model control plane

```yaml
schema_version: effective-authority/v0.1
repo: SocioProphet/agentplane
zone: C
owner: AgentPlane runtime lane
maturity: draft
authority_classes:
  - agent_runtime
  - tool_invocation
  - session_execution
observation_channels:
  - filesystem
  - terminal_pty
  - memory_store
control_channels:
  - mcp
  - agent_to_agent
  - scheduler
egress_classes:
  - model_request
  - tool_input
  - tool_output
background_workers:
  - scheduled_agent_task
runtime_subjects:
  - native_process
  - agent_worker
connector_surfaces: []
policy_sources:
  - user_grant
  - signed_config
  - runtime_contract
ledger_sinks:
  - model-governance-ledger
  - policy-fabric
ci_validators:
  - effective-authority-ci
```

### Zone D — SourceOS/Bear local runtime

```yaml
schema_version: effective-authority/v0.1
repo: SourceOS-Linux/BearBrowser
zone: D
owner: Bear Browser runtime lane
maturity: draft
authority_classes:
  - browser_runtime
  - browser_bridge
  - local_observation_surface
observation_channels:
  - browser_dom
  - clipboard
  - filesystem
control_channels:
  - browser_bridge
  - native_host
egress_classes:
  - metadata
  - file_content
  - policy
background_workers:
  - extension_update_check
runtime_subjects:
  - browser_process
  - extension_host
connector_surfaces: []
policy_sources:
  - user_grant
  - signed_config
ledger_sinks:
  - sourceos-syncd
  - model-governance-ledger
ci_validators:
  - effective-authority-ci
```

## Compliance rule

A repo manifest does not prove safety. It creates the minimum declaration surface needed for validation. Runtime repos must later emit live authority records that conform to the Effective Authority schemas.
