# Effective Authority Architecture

**Document ID:** `EFFECTIVE-AUTHORITY-ARCHITECTURE`
**Version:** 0.1.0
**Status:** Public-review proposal
**Owner:** ProCybernetica / Prophet Platform standards lane
**Scope:** SourceOS Linux, Bear Browser, Prophet Platform, AgentPlane, model/control-plane repos, workspace/search/world-model surfaces, and research/proof estate governance.

## 1. Thesis

Modern vendor systems fail the user when visible preferences do not equal effective runtime authority. The estate therefore treats user-facing settings as intent declarations, not as proof of enforcement.

The system must answer four questions for every repository, runtime, agent, connector, model, browser bridge, VM, background worker, and shared plane:

1. What can observe?
2. What can act?
3. What can leave the machine or workspace boundary?
4. What proves the machinery stopped?

The answer is the **Effective Authority Graph**: a signed, inspectable, local-first graph of actors, authorities, runtime subjects, observation channels, control channels, egress routes, policy sources, grants, background workers, semantic observers, and stop proofs.

## 2. Relation to Bear hardening invariants

This architecture consumes the Bear hardening invariant catalog. The controlling invariants are:

- consent gates machinery, not UI;
- egress self-reports destination, purpose, and payload class;
- policy provenance is signed and append-only;
- no undocumented behavioral flags;
- shared planes require signed membership and mutation logs;
- transparency requires locally checkable proofs;
- default deny is expressed as declarative data;
- update manifests are content-pinned and signed.

This document adds the missing operating architecture: all invariants emit into one effective-authority graph and one user-visible authority console.

## 3. Core objects

### 3.1 EffectiveAuthorityNode

A node is any entity capable of observing, acting, delegating, storing, indexing, executing, routing, or changing policy.

Required node classes:

- `human_user`
- `organization`
- `device`
- `daemon`
- `agent`
- `model_provider`
- `model_route`
- `plugin`
- `skill`
- `connector`
- `browser_bridge`
- `vm_guest`
- `container`
- `scheduled_task`
- `token`
- `filesystem_scope`
- `egress_route`
- `policy_flag`
- `semantic_index`
- `memory_store`
- `shared_plane`
- `conversation_branch`
- `runtime_grant`

### 3.2 AuthorityEdge

An edge records a concrete authority relationship.

Required edge classes:

- `can_observe`
- `can_act`
- `can_read`
- `can_write`
- `can_execute`
- `can_egress`
- `can_schedule`
- `can_mutate_policy`
- `can_spawn`
- `can_bridge`
- `can_impersonate`
- `can_index`
- `can_summarize`
- `can_retain_memory`

Every edge must trace to a signed policy source, a user grant, a system invariant, or a revocable runtime boundary contract. Unattributed authority is non-compliant.

## 4. Preference compiler

A preference is not enforcement. A preference must compile into low-level runtime state.

A disabled feature must compile to all of the following, as applicable:

- service stopped;
- timer disabled;
- background worker disabled;
- egress route removed;
- credential revoked or made unusable;
- plugin unloaded;
- connector grant revoked;
- browser bridge disconnected;
- VM/container boundary updated;
- semantic observer paused or deleted;
- stop proof emitted.

A preference compiler emits both a desired-state record and an observed-state verification result. Drift is a policy failure.

## 5. Proof of stopped machinery

A kill switch is insufficient. Every high-risk feature needs an attestable off-state.

A stop proof must include:

- feature identifier;
- prior authority edges;
- disabled services and timers;
- revoked grants and tokens;
- removed egress routes;
- unloaded plugins/connectors;
- stopped VMs/containers/bridges;
- semantic observers paused/deleted;
- timestamp;
- verifier identity;
- signed result.

Examples:

- Browser bridge disabled: no bridge process, no active socket, no paired extension, no cloud relay session, no active origin grant, no scheduled reconnect.
- AI inference disabled: no active provider, no active route, no remote fallback, no inference monitor, no scheduled model asset fetch.
- Remote control disabled: no SSH probe, no remote-device worker, no remote support session, no active token, no reconnect timer.

## 6. Fail-closed rule

If policy, grant, connector state, account/org state, model route, plugin state, or egress allow-set cannot be fetched and verified, the runtime must fail closed.

Fail-open behavior is non-compliant unless a signed emergency policy explicitly allows it, with user-visible banner and bounded expiry.

## 7. Required registries

The estate must maintain these registries as graph-backed ledgers:

1. Control-channel registry: SSH, browser bridge, MCP, WebSocket, native host, local socket, vsock, extension bridge, BLE/nearby transport, scheduler, CI webhook, cloud connector, agent-to-agent channel.
2. Observation-channel ledger: microphone, camera, screen, clipboard, accessibility, file index, semantic embedding, browser DOM, terminal PTY, shell history, notifications, contacts, calendar, location, cloud documents.
3. Egress ledger: every outbound request records destination, purpose, payload class, actor, process, account/org, feature, policy decision, and response class.
4. Tool grant ledger: every tool call traces to scope, approval mode, input hash, expiry, and revocation handle.
5. Token injection ledger: every token/secret injection records target runtime, scope, purpose, expiry, and revocation.
6. Background worker registry: every scheduler/timer/sync/daemon job records owner, purpose, next run, last run, egress class, data class, and disable proof.
7. Runtime boundary registry: every VM/container/guest declares rootfs/image digest, mounts, egress, CA bundle, token injection, file scopes, clipboard/browser/SSH bridging, process tree, and teardown proof.
8. Conversation integrity ledger: turns, tool calls, branches, deletions, summaries, and compactions are hash-chained and tombstoned.
9. Shared-plane membership log: every workspace, memory plane, sync namespace, group container, or collaborative surface logs membership and mutations in-plane.

## 8. Repo estate zones

The 122-repo estate is governed by zone profiles rather than bespoke one-off controls.

### Zone A — Doctrine and standards

Repos: `ProCybernetica`, `prophet-platform-standards`, `policy-fabric`, `model-governance-ledger`.

Responsibilities: invariant catalog, schemas, validators, signed policy provenance, evidence taxonomy, transparency instruments.

### Zone B — Platform and workspace

Repos: `prophet-platform`, `prophet-workspace`, `socioprophet`, `sociosphere`.

Responsibilities: active authority APIs, authority console, workroom integration, dashboarding, user-visible controls.

### Zone C — Agent/tool/model control plane

Repos: `agentplane`, `agent-registry`, `guardrail-fabric`, `model-router`, `functional-model-surfaces`, `holmes`.

Responsibilities: agent manifests, tool grants, model route records, fail-closed policy, memory governance, provider manifests.

### Zone D — SourceOS/Bear local runtime

Repos: `sourceos-spec`, `sourceos-boot`, `sourceos-syncd`, `sourceos-shell`, `sourceos-devtools`, `agent-machine`, `agent-term`, `BearBrowser`, `librewolf-source-mirror`, `homebrew-tap`.

Responsibilities: boot/update trust, sync membership logs, VM/container boundary contracts, browser bridge containment, local observation-channel ledger.

### Zone E — Search, memory, world model, and semantic observers

Repos: `sherlock-search`, `gaia-world-model`, memory/Lampstand surfaces, Holmes/lab repos.

Responsibilities: inspectable indexes, embedding provenance, semantic observer inventory, topology identity/fingerprint separation, local-first matching.

### Zone F — Packaging and distribution

Repos: `homebrew-prophet`, SourceOS taps, `lattice-forge`, `sourceos-model-carry`, CLI/devtools repos.

Responsibilities: content-pinned manifests, signed packages, provenance, rollback, runtime install surfaces.

### Zone G — Research and proof estate

Repos: Heller-Winters, BSD, Yang-Mills, Heller-Gödel, Hodge, Heller-Dirac, and related proof program repos.

Responsibilities: claim-grade provenance, proof artifact lineage, computational diagnostic evidence classes, authorship preservation, import-by-commit discipline.

## 9. Minimum repo manifest

Every repo must eventually include `.prophet/hardening.yaml` with:

```yaml
schema_version: effective-authority/v0.1
repo: OWNER/NAME
zone: A|B|C|D|E|F|G
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
owner: TBD
maturity: draft|partial|enforced|verified
```

## 10. Product requirement

The user must be able to open one console and answer:

- What is active now?
- What can observe me?
- What can act on my behalf?
- What can leave the machine or workspace?
- What is scheduled?
- What tokens exist?
- What browser bridges are paired?
- What VMs or containers are running?
- What semantic indexes and memories exist?
- What policies changed?
- What proves this feature is off?

## 11. Non-goals

This document does not assert compromise. It defines a hardening architecture derived from observed vendor and agent-client failure modes.

This document does not ingest private logs, tokens, payloads, or user data. It is schema-first and public-safe.

This document does not move runtime implementation into ProCybernetica. Downstream repos own their runtime adapters.

## 12. Next tranche

1. Add JSON schemas for `EffectiveAuthorityNode`, `AuthorityEdge`, `EgressEvent`, `PolicyLedgerEntry`, `ToolGrant`, `RuntimeBoundaryContract`, `BackgroundWorkerRecord`, and `StopProof`.
2. Add `.prophet/hardening.yaml` schema.
3. Add fixtures for each estate zone.
4. Add validator and CI lane.
5. Seed manifests into top tranche repos.
6. Build Prophet Workspace authority console against fixture data.
7. Wire live egress and tool-grant events in `agentplane`, `guardrail-fabric`, and `model-router`.
