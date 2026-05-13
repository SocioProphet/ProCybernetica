# Triune Bring-Up Runbook

Status: public-safe runbook draft  
Date: 2026-05-13  
Execution status: operator procedure draft; no live runtime is claimed

## Scope

This runbook brings up the Triune Inception VM lab pattern in a controlled, air-gapped or lab-isolated environment. It assumes `genesys` is the operator workstation, `k3-a` and `k3-b` are the twin bastion hosts, and each Inception VM runs a separate k3s control plane.

The default v0 federation path is Cilium ClusterMesh with Herald-Multi addressing each cluster through separate kubeconfigs. KubeFed remains an alternate placement-policy track.

## Preconditions

Do not begin unless these are true:

1. The lab network is isolated from production and customer systems.
2. No production credentials are present on Inception VMs.
3. Each Inception VM has a unique identity, hostname, and asset record.
4. The bastion has deny-by-default network policy material staged.
5. The operator has a rollback path for every cluster join.
6. Admission is host-approved only until delegated policy is explicitly created.

## Phase 0: prepare source records

Create one cluster-member record per expected node:

```text
genesys
k3-a
k3-b
inception-i1
inception-i2
inception-i3
```

For every record, capture:

```text
cluster_member_id
cluster_name
member_role
trust_domain
status
control_plane
networking
policy_baseline
governance_refs
safety_status
non_claims
ledger_entry
```

Use `schemas/triune/cluster-member.v1.json` as the shape.

## Phase 1: build each Inception VM as its own k3s cluster

The source blueprint uses k3s with Traefik, ServiceLB, flannel, and default network policy disabled so Cilium can own CNI and policy enforcement.

Baseline intent:

```bash
curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="server --disable traefik --disable servicelb --flannel-backend=none --disable-network-policy" \
  sh -
```

Productionized implementation should replace live internet curl with a pinned, mirrored, verified, air-gapped installer bundle.

## Phase 2: install Cilium and deny-all policy

Install Cilium from the lab-approved bundle. Then apply default-deny policy before workload admission.

Minimum policy posture:

```text
default deny ingress
default deny egress
no privileged pods
no hostPID
signed images required
resource limits required
```

Gatekeeper or Kyverno may enforce admission controls. The current schema permits either, but the source blueprint named Gatekeeper.

## Phase 3: form the Triune

Bring `inception-i1`, `inception-i2`, and `inception-i3` online as the first quorum.

Recommended v0 formation:

```text
federation_mode: cilium_clustermesh
orchestrator: herald_multi_kubeconfig
members: i1, i2, i3
```

The operator should verify:

1. Each cluster has its own API server and kubeconfig.
2. ClusterMesh identity is unique per cluster.
3. Cross-cluster service discovery is limited to the lab namespace.
4. Deny-all policy remains active by default.
5. No candidate cluster is admitted without an admission pack.

## Phase 4: load FPGL and epsilon gates

The source blueprint names the FPGL states:

```text
IDLE
ACCUM
LIMIT
ALIGN
CLEAR
```

The minimum v0 rule is:

```text
if epsilon gate passes and all boundary axes are below threshold:
  action may be allow or align
if epsilon gate warns:
  action must be damp or align
if epsilon gate fails:
  action must be freeze, revert, or reject
```

The structural validator under `tools/triune/validate-admission-pack.py` enforces the admission-pack case where the gate must pass before admission is proposed.

## Phase 5: evaluate faithful candidates

A candidate may be observed without being admitted.

A candidate may become proposed only if the admission pack contains:

```text
event_ir_snapshot_ref
proof_artifact_refs
sbom_ref
signature_refs
image_refs
network_policy_ref
policy_dry_run.result == pass
epsilon_gate.decision.gate_result == pass
reversal_plan
non_claims
ledger_entry
```

Run:

```bash
python tools/triune/validate-admission-pack.py examples/triune/admission-pack.synthetic.json
```

For a real candidate, replace the synthetic fixture with a generated admission pack and require host approval before `status: admitted`.

## Phase 6: admit or reject

Admission states:

```text
observed -> candidate -> dry_run -> proposed -> approved -> admitted
observed -> candidate -> rejected
admitted -> quarantined -> revoked
```

A proposed candidate is not a member. An approved candidate is not fully admitted until mesh/federation join has completed and the ledger records the join.

## Phase 7: revoke

A revocation must be executable from the admission pack:

1. Remove ClusterMesh peer or KubeFed member.
2. Revoke service credentials.
3. Restore deny-all egress.
4. Move workloads to quarantine namespace or stop them.
5. Record the ledger event.
6. Preserve evidence for replay.

## Acceptance checklist

The Triune bring-up is minimally acceptable when:

- all three Inception clusters have independent control planes;
- deny-all policy is active in the lab namespace;
- signed-image policy is active or explicitly marked as pending;
- synthetic admission-pack validation passes;
- no candidate is marked admitted without approval;
- reversal path is documented for every member;
- non-claims remain present in every public artifact.
