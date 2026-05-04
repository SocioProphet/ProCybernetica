# Recent Contribution Alignment

Status: initial 21-day contribution audit

Window: 2026-04-13 through 2026-05-04

Author/login checked: `mdheller`

Purpose: prevent ProCybernetica from being developed in a vacuum by aligning the repository with both the current estate dossier and live contribution activity across SocioProphet, SourceOS-Linux, SociOS-Linux, and mdheller repositories.

## Source material

This alignment uses two inputs:

1. The current repository dossier snapshot uploaded as `socioprophet_repository_dossier_current_snapshot_2026-04-29(4).pdf`.
2. Live GitHub commit and repository checks through the connected GitHub estate for contributions by `mdheller` since 2026-04-13.

## Baseline from repository dossier

The dossier identifies 105 unique repositories across:

- SocioProphet: 68
- SourceOS-Linux: 7
- SociOS-Linux: 26
- mdheller: 4

It also provides the core agent operating rule used here:

- clone predictably under `~/dev/<repo-name>`;
- establish current state before editing;
- read README, maturity files, docs, schemas, examples, Makefile, and workflows first;
- respect repository planes;
- validate and leave evidence;
- branch narrowly and avoid collapsing multiple planes into one change.

## Workstream routing from dossier

The dossier says ProCybernetica sits in the contracts/standards workstream alongside:

- `SocioProphet/functional-model-surfaces`
- `SourceOS-Linux/sourceos-spec`
- `socioprophet-standards-*`
- `prophet-core-contracts`

It also identifies ProCybernetica as P0, canonical/control-plane, on the cybernetic doctrine/governance plane.

Dossier-provided adjacent surfaces for ProCybernetica include:

- `sociosphere`
- `workspace-inventory`
- `prophet-platform`
- relevant standards repositories

This means ProCybernetica should not become a runtime dumping ground. It should remain a public doctrine-as-code, schema/profile, conformance, and platform-integration repository.

## Repositories with visible recent contribution activity

### SocioProphet

Observed active/relevant repos in the 21-day contribution stream:

- `SocioProphet/ProCybernetica`
- `SocioProphet/prophet-platform`
- `SocioProphet/model-router`
- `SocioProphet/HolographMe`
- `SocioProphet/prophet-platform-fabric-mlops-ts-suite`
- `SocioProphet/functional-model-surfaces`
- `SocioProphet/workspace-inventory`
- `SocioProphet/semantic-serdes`
- `SocioProphet/ontogenesis`

Important alignment observations:

- `prophet-platform` has fresh identity, FogStack, AgentPlane, PolicyPlane, runtime-readiness, and evidence-parity work.
- `semantic-serdes` has fresh SHIR SerDes schema, fixture, and CI work.
- `ontogenesis` has fresh SHIR v0.1 semantic hyperknowledge spec work.
- `functional-model-surfaces` has Prophet Intelligence Foundry contract-spine work.
- `model-router` has Professional Intelligence routing decision examples.
- `workspace-inventory` has Prophet Intelligence Foundry estate alignment updates.
- `HolographMe` has human digital twin schema, governance, and operating-model work.

### SourceOS-Linux

Observed active/relevant repos in the 21-day contribution stream:

- `SourceOS-Linux/sourceos-spec`
- `SourceOS-Linux/agent-machine`
- `SourceOS-Linux/agent-term`
- `SourceOS-Linux/BearBrowser`
- `SourceOS-Linux/homebrew-tap`

Important alignment observations:

- `sourceos-spec` has fresh local-first service, shell receipt, browser history, redaction, ops history, and state-integrity contracts.
- `agent-machine` has deterministic release evidence bundle, supply-chain/digest/provenance strict mode, grant hardening, TopoLVM, AgentTerm, and Policy Fabric integration stubs.
- `agent-term` has a CI-backed local operator smoke path creating durable EventStore and Matrix state artifacts.
- `BearBrowser` has browser-history policy/event contracts, local-first design, Linux packaging and credential/build readiness helpers.
- `homebrew-tap` exposes validation and readiness commands for SourceOS/BearBrowser surfaces.

### SociOS-Linux

Observed active/relevant repos in the 21-day contribution stream:

- `SociOS-Linux/source-os`
- `SociOS-Linux/workstation-contracts`
- `SociOS-Linux/socios`
- `SociOS-Linux/cloudshell-fog`
- `SociOS-Linux/embeddinglab`
- `SociOS-Linux/graphlab`
- `SociOS-Linux/nlplab`
- `SociOS-Linux/timeserieslab`
- `SociOS-Linux/translationlab`

Important alignment observations:

- `source-os` has active workstation-v0, office shell, Mac-on-Linux, shortcut map, dock validation, aggregate polish, and agent instruction work.
- `workstation-contracts` has Agent Machine and Office Plane conformance fixtures, plus TritRPC frame-pack operation work.
- `socios` has opt-in personalization orchestration contract work.
- lab repos were created or seeded for embedding, graph, NLP, time-series, and translation work.

### mdheller

Observed active/relevant repos in the 21-day contribution stream:

- `mdheller/socioprophet-web`
- `mdheller/economic-prophet`
- `mdheller/m2-env-bootstrap`
- `mdheller/profit-mpcc`

Important alignment observations:

- `socioprophet-web` has SourceOS lifecycle control-plane UI, Professional Intelligence dashboard MVP, and GAIA map workbench work.
- `economic-prophet` has schema-first economic-profit reference implementation, object graph, lineage, audit, and runtime validation work.
- `m2-env-bootstrap` has local bootstrap hardening and environment verification work.
- `profit-mpcc` has MPCC export classification and lineage/overlap witness work.

## Corrections this imposes on ProCybernetica

### 1. Treat the dossier as routing law

The dossier is now the estate navigation baseline. ProCybernetica docs and agent instructions should continue to respect the separation between standards, runtime services, boot/install behavior, SourceOS workstation work, agent execution, model governance, and product/UI repositories.

### 2. Do not duplicate SourceOS contracts

SourceOS/SociOS typed contract work is active and recent. ProCybernetica must map to `sourceos-spec`, `workstation-contracts`, `agent-machine`, `sourceos-boot`, and relevant SourceOS/SociOS surfaces rather than invent lower-level host/workstation/agent-machine contracts in isolation.

### 3. Do not duplicate AgentPlane evidence

AgentPlane and Prophet Platform are already producing evidence artifacts, run/replay records, runtime dry-run records, parity readiness records, node inventories, and policy decision links. ProCybernetica should define constitutional semantics and conformance expectations, not replace their runtime evidence surfaces.

### 4. Align with semantic-serdes and SHIR immediately

The SHIR work in `semantic-serdes` and `ontogenesis` is directly relevant to ProCybernetica `Claim`, `ProvenanceRecord`, `EventEnvelope`, `TraceEvent`, and dashboard/export semantics.

ProCybernetica should add compatibility maps before expanding its claim/event schemas further.

### 5. Fold HolographMe into Genesis/Inception and twin lifecycle

Recent HolographMe work on human digital twin schema, governance, and operating model is directly relevant to the Genesis/Inception/K3 twin bridge and `TwinRuntimeDescriptor` backlog.

ProCybernetica should not invent a separate human/twin model without mapping HolographMe first.

### 6. Recognize Professional Intelligence / Foundry lane

Recent `functional-model-surfaces`, `model-router`, `workspace-inventory`, `socioprophet-web`, and `prophet-platform-fabric-mlops-ts-suite` work points to a Professional Intelligence / Prophet Intelligence Foundry lane.

ProCybernetica scoring, promotion, and model-governance docs should incorporate this as a concrete use case.

### 7. Treat mdheller incubation repos as source examples, not authority

`economic-prophet`, `profit-mpcc`, and `socioprophet-web` contain useful patterns: schema-first runtime validation, audit-pack writing, object graph lineage, export classification, and control-plane UI. They should inform examples and product integration, but canonical standards should graduate into SocioProphet/SourceOS/SociOS repos.

## Immediate issues/actions

Already opened:

- AgentPlane evidence map.
- semantic-serdes / SHIR map.
- ontogenesis governance map.

Additional required issues:

- Map ProCybernetica v0 schemas to SourceOS/SociOS typed contracts.
- Map SourceOS boot/agent-machine/workstation evidence into ProCybernetica envelopes.
- Map Prophet Platform FogStack/eval/identity records into ProCybernetica constitutional loop.
- Map HolographMe into Genesis/Inception/Twin lifecycle.
- Map Professional Intelligence / Foundry lane into ProCybernetica scoring and promotion law.

## Working conclusion

The live contribution stream confirms that ProCybernetica should be the public constitutional standard and reference-kit layer for a large, already-moving estate. It should not act as an isolated runtime project. The next safe move is compatibility mapping before further schema expansion.
