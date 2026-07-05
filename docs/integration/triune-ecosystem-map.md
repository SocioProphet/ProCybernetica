# Triune Ecosystem Integration Map

**Status:** execution scaffolding complete; live Triune not yet claimed.
**Non-claim:** This document describes intended integration architecture. It does not prove any live deployment, live cluster membership, or live admission decision.

---

## 1. Overview

The Triune lab execution layer sits within a four-layer admission stack. Each layer has its own gate, its own evidence record, and its own `evidenceRef` / `admission_pack_id`. Gates compose: a failure at any layer prevents admission at the layer above.

```
Layer 1 — Triune admission-pack (ProCybernetica)
  Cluster membership gate: epsilon, deny-all network, host approval, ledger.
  Schema: schemas/triune/admission-pack.v1.json
  Tool:   tools/triune/validate-admission-pack.py

Layer 2 — agent-machine PolicyAdmission (SourceOS-Linux/agent-machine)
  Node activation gate: AgentPod placement, PolicyAdmission, ActivationDecision.
  Schema: contracts/policy-admission.schema.json (agent-machine repo)

Layer 3 — model-router AdmitEntry (model-router)
  Artifact admission gate: ModelCatalogEntry, egress, observability, capability.
  Schema: schemas/model-catalog-entry.v0.1.schema.json (model-router repo)
  Contract: contracts/sourceos/model-catalog-entry.v0.1.ts (model-router repo)

Layer 4 — guardrail-fabric policy verdict
  Capability and policy grant surface (policy-fabric repo).
```

---

## 2. Cross-layer evidence chain

Each layer's evidence record feeds into the layer above as a cross-reference. The chain is:

```
Triune admission-pack.ledger_entry.evidence_refs
  ← agent-machine PolicyAdmission.decisionRef / planDigest
       ← model-router AdmissionResult.evidenceRef
            ← guardrail-fabric policy verdict ref
```

### Field mapping

| ProCybernetica (Triune)                         | agent-machine                                 | model-router                                   |
|-------------------------------------------------|-----------------------------------------------|------------------------------------------------|
| `cluster_member_id`                             | `request.agentMachineId`                      | —                                              |
| `admission-pack.admission_pack_id`                        | `PolicyAdmission.decisionRef`                 | `clusterAdmissionRef`                          |
| `policy.dry_run_output_hash`                    | `request.planDigest` (`sha256:<hex>`)         | `artifact.contentHash`                         |
| `policy.dry_run_evidence_ref`                   | `request.manifestDigest`                      | `attestation.hashChain[1]`                     |
| `reversal_plan.steps`                           | `requestType: teardown / wipe`                | `lifecycle.retentionPolicy.reapOrphanRows`     |
| `ledger_entry.evidence_refs`                    | `receiptSafety.evidenceRefs`                  | `AdmissionResult.evidenceRef`                  |
| `decision.host_approval`                        | `obligations.requiresHostApproval`            | (not a model-router concern)                   |
| `epsilon_gate.boundary_axes`                    | (not a model-router concern)                  | (not a model-router concern)                   |
| `non_claims`                                    | (TRUST_SURFACE non-production blocks)         | `evaluation.epistemicLevel = synthetic`        |

---

## 3. Layer 1 → Layer 2: Triune cluster-member ↔ agent-machine node

A Triune-admitted inception VM is an agent-machine node. Before any AgentPod may be placed on a Triune inception cluster:

1. The inception VM must hold an `admitted` `cluster-member` record in the Triune ledger.
2. Its `cluster_member_id` maps to `agentMachineId` in agent-machine's `PolicyAdmission`.
3. The Triune `admission-pack.admission_pack_id` is carried as `PolicyAdmission.decisionRef`.
4. The kubeconfig stored at `~/triune-lab/kubeconfigs/<cluster_member_id>` is the same
   kubeconfig referenced by agent-machine deployment receipts for that node.

### Failure mode prevented

Without this binding, a reachable node could receive `PolicyAdmission` without Triune cluster-level clearance. The `cluster_not_admitted` denial reason in `model-router` closes this at the artifact layer; the Triune epsilon gate closes it at the cluster layer.

---

## 4. Layer 2 → Layer 3: agent-machine ↔ model-router

When an AgentPod is placed on an admitted Triune node, model-router validates the artifact:

1. The `ModelCatalogEntry.clusterAdmissionRef` must point to the Triune `admission_pack_id` for that node.
2. An empty `clusterAdmissionRef` triggers `cluster_not_admitted` denial in model-router.
3. The model-router `AdmissionResult.evidenceRef` URI is written back into the Triune
   `ledger_entry.evidence_refs` as proof that artifact admission ran.

### Bootstrap-ordering alignment

Triune enforces: deny-all NetworkPolicy applied **before** workload admission.
model-router enforces: `sinkInitializesBeforeIO: true` — provenance sink and policy gate
come up **before** inference IO is reachable.

These are the same temporal ordering discipline at different layers.

---

## 5. Layer 3 → Layer 4: model-router ↔ guardrail-fabric

`ModelCatalogEntry.governance.guardrailPolicyRef` names the policy-as-code artifact that
guardrail-fabric evaluates during the Triune dry-run. The dry-run output is the artifact
that `tools/triune/hash-evidence.py` hashes, producing the `dry_run_output_hash` in the
admission pack.

The chain is:

```
guardrail-fabric dry-run output
  → hash-evidence.py → dry_run_output_hash
       → admission-pack.policy.dry_run_output_hash
            → Triune epsilon gate (gate_result: pass requires this hash)
```

---

## 6. Noetica as a faithful workload candidate

Noetica (SocioProphet/Noetica) is the first concrete workload candidate for Triune admission.

Its TRUST_SURFACE declares four un-admitted egress targets:

| Target                     | Phase declared  | grant_ref                    | Triune implication              |
|----------------------------|-----------------|------------------------------|---------------------------------|
| `api.anthropic.com`        | inference only  | `call:anthropic`             | Cilium egress exception required |
| `api.openai.com`           | inference only  | `call:openai`                | Cilium egress exception required |
| `neuronpedia`              | inference only  | `call:neuronpedia:steer`     | Cilium egress exception required |
| `superconscious`           | inference+shutdown | `sourceos:superconscious:submit-task` | Cilium egress exception required |

Each target requires:
1. An explicit Cilium `NetworkPolicy` egress rule (exception to default-deny).
2. A `ModelCatalogEntry.egress.targets[].permittedPhases` declaration matching the phase.
3. Admission in `guardrail-fabric` for the `call:*` grant.
4. A Triune admission pack with `policy.checked_policies` covering egress grants.

The synthetic `ModelCatalogEntry` for Noetica is at:
`examples/model-catalog-entry.noetica-chat.synthetic.json` (model-router repo)

The pending Triune admission pack for Noetica is at:
`docs/integration/noetica-admission-candidate.md` (this repo)

---

## 7. prophet-platform ↔ Triune substrate

prophet-platform hosts the substrate plane that runs on top of Triune clusters:

| prophet-platform component      | Triune layer                                           |
|---------------------------------|--------------------------------------------------------|
| Cilium / Hubble adapter         | Telemetry bridge on Triune's Cilium ClusterMesh         |
| Tetragon adapter                | Runtime security observability within Triune clusters   |
| KubeEdge adapter                | Edge-node faithful candidate admission surface          |
| Dashboard BFF                   | `genesys` herald/dashboard/ledger role                  |
| Identity Policy Service         | Maps to Triune `trust_domain` + `machine_identity_ref`  |
| OPA                             | Provides guardrail-fabric policy verdict surface         |

These are not independent services — they are a stack. The correct bring-up order is:

```
1. Triune inception clusters (i1, i2, i3) — sovereign k3s control planes
2. Cilium + default-deny NetworkPolicy baseline
3. Triune formation evidence
4. prophet-platform substrate services (admitted as Triune workloads)
5. prophet-platform Cilium/Hubble + Tetragon adapters
6. Workload admission (Noetica, agent-machine nodes, etc.)
```

---

## 8. Completion gate for this integration

This integration map is structurally complete when:

1. Triune `admission-pack` schema cross-references `clusterAdmissionRef` pattern used in model-router.
2. model-router `AdmissionResult.evidenceRef` is written into ProCybernetica ledger entries.
3. A real (non-synthetic) Noetica `ModelCatalogEntry` is admitted against a live Triune cluster.
4. guardrail-fabric policy ref for Noetica's egress grants is hash-bound in the admission pack.
5. The Triune epsilon gate dry-run hash covers the guardrail-fabric policy evaluation output.

Until those conditions are met, the status is:

```
integration map complete; live cross-layer evidence chain not yet claimed
```

---

## Non-claims

- This document does not prove any live Triune deployment.
- This document does not prove any live agent-machine node is admitted.
- This document does not prove Noetica is running in a Triune cluster.
- No production credentials, kubeconfigs, or private IPs appear in this document.
- Synthetic fixtures in examples/ are structural demonstrations, not operational evidence.
