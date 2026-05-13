# Triune Inception VM Lab Capture

Status: public-safe source capture and reconciliation note  
Date: 2026-05-13  
Lane: ProCybernetica lab substrate, federation governance, admission control  
Source state: user-supplied Triune/Inception VM blueprint captured from the working chat as `Pasted text(177).txt`  
Execution status: doctrine and schema capture only; no live cluster runtime is claimed

## Purpose

This document captures the Triune Inception VM lab pattern as a ProCybernetica governance surface.

The blueprint defines a controlled multi-cluster laboratory in which `genesys` acts as the herald, dashboard, ledger, and proof-gate workstation; `k3-a` and `k3-b` act as the twin bastion; each Inception VM runs its own k3s control plane; three Inception clusters form the initial Triune; and later clusters, pods, or nodes are admitted only after proof-pack, dry-run, policy, signature, and epsilon/boundary checks.

The operational point is not merely nested Kubernetes. The pattern is a cybernetic admission machine:

```text
source proof -> dry-run simulation -> epsilon/boundary gate -> host approval -> federation join -> ledgered reversal path
```

## Canonical implementation reading

The symbolic language is retained, but every symbol must carry an operational meaning before implementation.

| Blueprint term | ProCybernetica implementation meaning |
| --- | --- |
| `genesys` | Operator workstation and control-plane console for dashboards, ledger, Herald scheduling, and proof-gate review. |
| Twin bastion | `k3-a` / `k3-b` secured runway for lab networking, observation, policy bundles, and controlled access. |
| Inception VM | One VM with its own k3s control plane and no shared fate with other Inception clusters. |
| Triune | Initial three-cluster quorum, normally `I1`, `I2`, and `I3`, governed as a unit while preserving cluster sovereignty. |
| Faithful | Additional cluster/pod/node candidate that passes admission evidence and is accepted into the governed lab mesh. |
| Herald-Multi | Orchestrator that applies schedules, checks gates, and coordinates cluster-by-cluster actions through kubeconfigs. |
| FPGL | Finite policy-governed loop with states such as `IDLE`, `ACCUM`, `LIMIT`, `ALIGN`, and `CLEAR`. |
| EvalAngelica | Read-only evaluator/emissary that scores resonance, safety margin, policy fitness, and boundary trend. |
| epsilon gate | Numeric safety gate over `epsilon`, `epsilon_hat`, and `epsilon_eff` at micro/meso/macro scales. |
| boundary axes | Bounded risk dimensions such as network escape, privilege drift, identity ambiguity, and accumulated boundary charge. |
| FROST / host signoff | Approval surface. Until delegated policy exists, host approval remains required for admission. |

## Architecture spine

```text
genesys
  ├─ dashboards
  ├─ ledger
  ├─ Herald-Multi
  └─ admission review

twin bastion
  ├─ k3-a
  ├─ k3-b
  ├─ Cilium / policy bundles
  └─ deny-all baseline

Triune
  ├─ inception-i1: k3s control plane
  ├─ inception-i2: k3s control plane
  └─ inception-i3: k3s control plane

faithful candidates
  └─ join only through proof pack + dry run + gates + host approval + rollback plan
```

Each Inception VM is its own k3s cluster. This intentionally prevents a single broken experiment from bricking the bastion or contaminating the whole lab. The first production-grade implementation should preserve that no-shared-fate property.

## Default federation decision

The default v0 path should be Cilium ClusterMesh plus Herald-Multi managing each member through separate kubeconfigs.

Rationale:

1. It preserves sovereignty of each Inception control plane.
2. It makes failure domains clearer than an early KubeFed-first design.
3. It keeps admission/revocation concrete: add or remove a mesh peer and revoke the relevant service credentials.
4. KubeFed can remain an example track for placement-policy experiments, but not the default until the schemas and evidence adapters are stable.

## Admission contract

A candidate does not become faithful because it is reachable. It becomes faithful only after a signed admission pack records:

1. candidate identity and role;
2. Event-IR or equivalent snapshot;
3. proof artifact references;
4. SBOM reference;
5. image and signature references;
6. deny-all NetworkPolicy baseline;
7. policy dry-run result;
8. epsilon gate result;
9. boundary-axis result;
10. requested role;
11. approval record;
12. reversal/quarantine plan;
13. ledger entry;
14. explicit non-claims.

The initial schema set is under `schemas/triune/`.

## Safety invariants

The source blueprint states the key thresholds as:

```text
micro <= alpha
meso <= 2 alpha
macro median <= 3 alpha
macro p95 <= 4 alpha
boundary axes < 1
```

The v0 validator enforces those invariants structurally for admission packs. It does not verify signatures, interrogate clusters, or prove the runtime state.

Boundary axes are intentionally schema-flexible because the active risk axes may change by lab, but every axis must have a numeric `value` and positive `threshold`.

## Estate alignment

ProCybernetica owns the public doctrine, schemas, synthetic fixtures, and conformance law for this lab substrate.

Runtime ownership should remain mapped rather than duplicated:

- `SocioProphet/agentplane` should own evidence-producing execution artifacts where work orders, runs, replay, reversals, and promotion receipts are produced.
- `SocioProphet/prophet-platform` should consume the contracts as platform runtime and dashboard services mature.
- `SocioProphet/ontogenesis` should own ontology/SHACL promotion gates when Triune vocabulary is formalized into ontology modules.
- `SourceOS-Linux/sourceos-syncd` and SourceOS typed contracts should own lower-level substrate, local-first synchronization, provenance, and host-state replication.
- `SocioProphet/sociosphere` should consume the admission and safety state as orchestration/project/issue-board surface.

## Non-claims

This capture does not claim that:

- a live Triune lab has been deployed;
- FROST signing is implemented;
- Cilium ClusterMesh is configured;
- KubeFed is configured;
- Herald-Multi exists as production code;
- epsilon values are scientifically calibrated beyond the source blueprint;
- boundary axes are complete;
- admission packs are cryptographically verified;
- production or customer systems may be attached.

## Open decisions

1. Whether `alpha = 0.00730` remains the canonical default or becomes a per-lab policy value.
2. Which boundary axes become mandatory in v1.
3. Whether `EvalAngelica` becomes a first-class evaluator schema or maps to AgentPlane evaluation artifacts.
4. Whether Triune admission should require one host approval or host plus independent monitor approval.
5. Whether KubeFed examples remain documentation-only or become CI-validated manifests.
