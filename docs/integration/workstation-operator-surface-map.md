# Workstation and Operator Surface Map

Status: initial integration map

Turn: 9 / 20

## Purpose

This document maps SourceOS/SociOS workstation and operator surfaces to ProCybernetica's operator, gateway, host, process, and evidence-node doctrine.

The goal is to prevent ProCybernetica from becoming a UI shell, terminal product, browser runtime, workstation contract runner, or Linux realization repo. ProCybernetica should define public constitutional expectations for these surfaces: event discipline, delegated authority, receipts, replay, policy gates, promotion, and public conformance.

## Source basis

Primary sources checked:

- `SociOS-Linux/source-os/README.md`
- `SociOS-Linux/workstation-contracts/README.md`
- `SourceOS-Linux/agent-term/README.md`
- `SourceOS-Linux/TurtleTerm/README.md`
- `SourceOS-Linux/BearBrowser/README.md`
- `mdheller/socioprophet-web/README.md`

Prior maps used:

- `docs/integration/sourceos-socios-contract-map.md`
- `docs/integration/agentplane-evidence-map.md`
- `docs/integration/prophet-platform-record-map.md`

## Ownership boundary

| Surface | Owning repo/lane | ProCybernetica role |
| --- | --- | --- |
| Linux realization | `SociOS-Linux/source-os` | Host/gateway/operator node interpretation; no Linux image/profile ownership |
| Workstation/CI contracts | `SociOS-Linux/workstation-contracts` | Conformance evidence interpretation; no runner ownership |
| ChatOps/operator console | `SourceOS-Linux/agent-term` | Operator/gateway node doctrine and event/replay requirements |
| Terminal workbench | `SourceOS-Linux/TurtleTerm` | Trusted command execution receipts and agent delegation interpretation |
| Browser runtime | `SourceOS-Linux/BearBrowser` | Browser evidence/projection/automation policy interpretation |
| Product UI shell | `mdheller/socioprophet-web` and later SocioProphet product repos | Surface projection and operator dashboard semantics |
| Execution evidence | AgentPlane / SourceOS / Prophet Platform | ProCybernetica interprets and maps evidence; does not own runtime |

## SourceOS Linux realization mapping

`SociOS-Linux/source-os` is the Linux realization home for the SourceOS control-plane stack. It carries host roles, profiles, images, builders, and Linux-facing integration surfaces that realize the AgentPlane contract on Linux hosts.

ProCybernetica mapping:

| source-os surface | ProCybernetica analogue |
| --- | --- |
| host role | `NodeDescriptor` with host/service embodiment |
| profile/image/builder | `ArtifactEnvelope` / `ProvenanceRecord` / SourceOS release evidence |
| linux templates | `CapabilityDescriptor` / policy-scoped execution refs |
| mesh planning docs | integration evidence and topology context |
| agentplane integration docs | AgentPlane evidence map refs |

Rule: ProCybernetica should not define SourceOS Linux profiles or images. It should require evidence and replayability when those profiles become part of a cybernetic control loop.

## Workstation contracts mapping

`SociOS-Linux/workstation-contracts` owns workstation/CI contract and conformance lanes.

It validates workstation, Agent Machine, Office Plane, and IPC contract surfaces, including conformance fixtures for allowed and denied behavior.

ProCybernetica mapping:

| workstation-contracts surface | ProCybernetica analogue |
| --- | --- |
| conformance fixture | `EvaluationResult` evidence |
| contract JSON | `ArtifactEnvelope` / SourceOS contract ref |
| IPC transcript | `TraceEvent` / `ReplayEnvelope` evidence |
| run receipt | `ArtifactEnvelope` / `ProvenanceRecord` |
| denied fixture | `IncidentReport` or `EvaluationResult` failure case |

Rule: ProCybernetica should not implement workstation runners. It should interpret conformance outputs as evidence for node/runtime readiness.

## AgentTerm mapping

`SourceOS-Linux/agent-term` is a terminal-native ChatOps console for Matrix rooms, registered agents, GitHub bots, CI systems, MCP tools, Agent Registry identities, Sociosphere workspaces, Prophet Workspace, Slash Topics, Memory Mesh, New Hope, Holmes, Sherlock, MeshRush, cloudshell-fog, AgentPlane, Policy Fabric, and local SourceOS services.

AgentTerm doctrine says the event log is the control plane and terminal UI is only the operator surface.

ProCybernetica mapping:

| AgentTerm surface | ProCybernetica analogue |
| --- | --- |
| Matrix room/channel | operator/gateway node context |
| slash command | `CommandEnvelope` or `EventEnvelope` |
| approval / human action | operator node `TransitionRecord` / `PromotionDecision` evidence |
| durable event log | `TraceEvent` / `ReplayEnvelope` source |
| plane registry | node registry / integration topology refs |
| Office command event | `CapabilityDescriptor` / `PolicyEnvelope` / AgentPlane evidence refs |
| shell request | cloudshell-fog / SourceOS shell evidence refs |
| agent resolution | Agent Registry refs / `DelegationEnvelope` |

Rule: ProCybernetica should not define AgentTerm command grammar. It should define what makes those commands lawful: identity, scope, policy, evidence, replay, and approval posture.

## TurtleTerm mapping

`SourceOS-Linux/TurtleTerm` is the SourceOS policy-aware, agent-addressable terminal workbench for trusted command execution, terminal receipts, agent delegation, and reproducible operator workflows.

ProCybernetica mapping:

| TurtleTerm surface | ProCybernetica analogue |
| --- | --- |
| command wrapper | `CommandEnvelope` evidence source |
| agent gateway | `DelegationEnvelope` / Agent Registry refs |
| terminal receipt | `ArtifactEnvelope` / `ProvenanceRecord` / `ReplayEnvelope` |
| skill manifest | `CapabilityDescriptor` / SourceOS skill refs |
| release artifacts / SBOM / attestations | `ArtifactEnvelope` / `ProvenanceRecord` |
| tmux bridge | operator/gateway node event source |

Rule: ProCybernetica should not become TurtleTerm or define terminal product behavior. It should define how terminal commands become governed evidence in cybernetic control loops.

## BearBrowser mapping

`SourceOS-Linux/BearBrowser` is a LibreWolf-derived SourceOS browser product for humans and agents.

It has two major modes:

1. Human Secure Browser.
2. Agent Browser Runtime.

BearBrowser owns browser overlays, settings profiles, enterprise/browser policies, agent-runtime policy contracts, downloads/workspace mount declarations, packaging manifests, AgentPlane registration, Prophet Workspace integration, and parity/maintenance scripts.

ProCybernetica mapping:

| BearBrowser surface | ProCybernetica analogue |
| --- | --- |
| human browser profile | operator/gateway node embodiment |
| agent browser runtime | executor/gateway node embodiment |
| browser policy | `PolicyEnvelope` / SourceOS contract ref |
| downloads/workspace mount declaration | SourceOS/AgentPlane evidence refs |
| Playwright/Stagehand action | `CommandEnvelope` / `CapabilityDescriptor` evidence |
| browser history/sync policy | SourceOS `BearHistoryEvent` / evidence refs |
| packaging/verification | `ArtifactEnvelope` / `ProvenanceRecord` |

Rule: ProCybernetica should not define browser automation schemas. It should require browser actions to preserve policy, evidence, projection, and replay semantics.

## SocioProphet web mapping

`mdheller/socioprophet-web` is a UI skeleton with mockable pages and TriRPC service wiring.

Recent estate notes identify it as a product UI shell with SourceOS lifecycle control-plane UI, Professional Intelligence dashboard, and GAIA map workbench work.

ProCybernetica mapping:

| UI surface | ProCybernetica analogue |
| --- | --- |
| dashboard | semantic-serdes surface projection / ProCybernetica public dashboard methodology |
| control-plane UI | operator/gateway node projection |
| GAIA map workbench | world-model projection and evidence surface |
| Professional Intelligence dashboard | scoring/evaluation/promotion surface |
| TriRPC service wiring | transport/adapter boundary, not ProCybernetica ownership |

Rule: ProCybernetica should not own product UI implementation. It should specify what evidence, replay, projection-loss, and public conformance data a UI surface must show.

## Unified operator/gateway node model

ProCybernetica should treat workstation and operator surfaces through these node classes:

| Surface type | Node class | Primary actuation | Primary evidence |
| --- | --- | --- | --- |
| AgentTerm room/thread | operator / gateway | commands, approvals, routing | event log, approvals, receipts |
| TurtleTerm shell/workbench | operator / executor / gateway | command execution, delegation | terminal receipt, command evidence |
| BearBrowser runtime | gateway / executor | browser navigation/extraction/automation | browser policy/event evidence |
| SourceOS workstation | host / service | profile activation, package/desktop posture | workstation profile, conformance result |
| SocioProphet web UI | gateway / operator | projection, review, dashboarding | surface projection, dashboard export |
| cloudshell-fog | gateway / executor | session placement, shell attach | shell session evidence |

## Cross-surface invariants

Every operator/workstation surface participating in ProCybernetica must preserve:

1. Actor or agent identity.
2. Command or event scope.
3. Policy refs.
4. Evidence refs.
5. Replay or receipt path.
6. Human approval when authority requires it.
7. Public-safe projection or redaction posture.
8. Ownership boundary to upstream repo.

## ProCybernetica schema implications

### Keep

- `NodeDescriptor`
- `CommandEnvelope`
- `DelegationEnvelope`
- `CapabilityDescriptor`
- `EventEnvelope`
- `TraceEvent`
- `ArtifactEnvelope`
- `ProvenanceRecord`
- `ReplayEnvelope`
- `EvaluationResult`
- `PromotionDecision`

### Do not add in ProCybernetica v0

- AgentTerm command schemas;
- Matrix room/message schemas;
- TurtleTerm receipt schemas;
- BearBrowser automation/history schemas;
- SourceOS workstation profile schemas;
- workstation contract runner schemas;
- web UI route/component schemas;
- cloudshell-fog session schemas.

### Consider later

- generic `ExternalEvidenceRef` after all maps complete;
- `examples/integrations/operator/agentterm_event_ref.example.json`;
- `examples/integrations/operator/turtleterm_receipt_ref.example.json`;
- `examples/integrations/operator/bearbrowser_event_ref.example.json`;
- dashboard surface projection fixture.

## Open questions

1. Should ProCybernetica conformance require every operator command to have a replay/receipt reference?
2. Should `CommandEnvelope` include an optional `operator_surface_ref` in v0.1?
3. Should `NodeDescriptor.node_class = gateway` become the preferred class for UI, browser, terminal, and ChatOps surfaces?
4. Should dashboard/public review surfaces require semantic-serdes `SurfaceProjection` refs?
5. Should BearBrowser and TurtleTerm receipts be represented through SourceOS contracts or direct evidence refs?

## Follow-up backlog

- Add operator/workstation adapter fixtures after all maps complete.
- Update public conformance plan to include operator/gateway surface invariants.
- Update scoring/dashboard docs to treat dashboards as operator review surfaces.
- Revisit `CommandEnvelope` and `CapabilityDescriptor` only after all maps complete.

## Current conclusion

The workstation/operator estate already has clear ownership: Linux realization in `source-os`, contracts in `workstation-contracts` and `sourceos-spec`, ChatOps in `agent-term`, trusted terminal workbench in TurtleTerm, governed browser runtime in BearBrowser, and UI surfaces in SocioProphet web/product repos. ProCybernetica should provide constitutional expectations over these surfaces, not implement them.
