# Noetica Chat Surface — Triune Admission Candidate

**Candidate:** Noetica Chat Surface M2a (`noetica.chat.m2a`)
**Source repo:** SocioProphet/Noetica
**Current status:** `candidate` — not yet proposed, not yet approved, not yet admitted.
**Non-claim:** This document is a pending admission record. It does not prove Noetica is running in a Triune cluster.

---

## 1. Candidate identity

| Field                  | Value                                           |
|------------------------|-------------------------------------------------|
| `candidate_id`         | `noetica.chat.m2a`                              |
| `candidate_name`       | `Noetica Chat Surface M2a`                      |
| `candidate_status`     | `candidate`                                     |
| `execution_status`     | `synthetic_fixture`                             |
| `trust_domain`         | `lab_airgapped` (Triune lab scope only)         |
| `member_role`          | `faithful_candidate`                            |
| Source TRUST_SURFACE   | `SocioProphet/Noetica/TRUST_SURFACE.yaml`       |
| model-router entry     | `examples/model-catalog-entry.noetica-chat.synthetic.json` (model-router repo) |

---

## 2. Required gates before proposal

These must all pass before `candidate_status` may advance to `proposed`:

| Gate                                    | Current state         | Evidence required                                           |
|-----------------------------------------|-----------------------|-------------------------------------------------------------|
| Structural admission-pack validation    | Not run               | `tools/triune/validate-admission-pack.py` output + hash     |
| Policy dry-run (guardrail-fabric)       | Not run               | `dry_run_output_hash` + `dry_run_evidence_ref`              |
| Epsilon gate measurement                | Not measured          | `epsilon-gate` record with all 4 boundary axes              |
| model-router `AdmitEntry` pass          | Not run               | `AdmissionResult.evidenceRef` from model-router             |
| Triune deny-all NetworkPolicy active    | Not verified for Noetica node | `networkpolicy-default-deny.applied.json` evidence  |
| Cilium egress exceptions declared       | Not applied           | NetworkPolicy egress rules for each egress target           |
| Reversal plan exists and is documented  | Stub only (below)     | Executable revocation steps with evidence ref               |
| Host approval                           | Not issued            | `decision.host_approval` with `approved_by` + `approved_at` |

---

## 3. Egress requirements (from TRUST_SURFACE.yaml)

Noetica declares four egress targets, all currently `admitted: false` in its TRUST_SURFACE.
Each requires a Cilium `NetworkPolicy` egress rule as an exception to the Triune default-deny baseline.

### 3.1 `api.anthropic.com`

```yaml
purpose: standalone chat inference
credential_source: env:ANTHROPIC_API_KEY
grant_ref: call:anthropic
evidence_required: ExternalModelProviderRouteEvidence
```

Required NetworkPolicy exception:
```yaml
egress:
  - to:
      - namespaceSelector: {}
        podSelector: {}
    ports: []
  - to:
      - ipBlock:
          cidr: 0.0.0.0/0
    ports:
      - protocol: TCP
        port: 443
```
Scope: noetica namespace only, inference phase only.
guardrail-fabric grant: `call:anthropic` — must be admitted before Cilium rule applies.

### 3.2 `api.openai.com`

```yaml
purpose: standalone chat inference
credential_source: env:OPENAI_API_KEY
grant_ref: call:openai
evidence_required: ExternalModelProviderRouteEvidence
```

Same pattern as Anthropic. Distinct grant: `call:openai`.

### 3.3 `neuronpedia`

```yaml
purpose: SAE feature steering
credential_source: env:NEURONPEDIA_API_KEY (or loopback agent-machine stub)
grant_ref: call:neuronpedia:steer
gate: M2b real steering proof not closed
loopback_without_credential_allowed: true
```

Loopback (localhost agent-machine stub) requires no Cilium egress exception.
External Neuronpedia requires: `call:neuronpedia:steer` grant + egress rule + steering proof.
Current state: M2b gate not closed — loopback path only.

### 3.4 `superconscious`

```yaml
purpose: SourceOS mode task submission
credential_source: agent-registry grant resolution
grant_ref: sourceos:superconscious:submit-task
gate: M3 live SourceOS integration not wired
```

M3 gate not yet closed. This egress target is `proposed` at `shutdown` phase only until M3 lands.

---

## 4. Capability manifest (from model-catalog-entry)

Declared in `model-catalog-entry.noetica-chat.synthetic.json`:

```json
{
  "declaredCapabilities": [
    "inference.text",
    "net.egress:anthropic",
    "net.egress:openai",
    "net.egress:neuronpedia",
    "net.egress:superconscious"
  ],
  "requiredPermissions": [
    "net.egress:api.anthropic.com",
    "net.egress:api.openai.com",
    "net.egress:neuronpedia",
    "net.egress:superconscious"
  ],
  "highPrivilege": true
}
```

`highPrivilege: true` because the entry requires explicit external network egress grants.
guardrail-fabric requires an explicit policy grant for each `net.egress:*` capability.

---

## 5. Steering requirements

Noetica M2a declares `steeringTier: full` and `emitsSteeringDiff: true`.

This means:
- When steering is applied, the steered-vs-baseline diff MUST be surfaced to the operator.
- `saeFeatureDictRef` must point to a real Neuronpedia feature dictionary before `steeringTier` may be exercised at `full` tier in a live cluster.
- Until M2b real steering proof is closed, steeringTier is effectively `local` (loopback stub only).

---

## 6. Reversal plan (stub — must be completed before admission)

```
1. Remove Noetica from Triune ClusterMesh / KubeFed membership.
2. Revoke ANTHROPIC_API_KEY, OPENAI_API_KEY, NEURONPEDIA_API_KEY from the node.
3. Remove Cilium egress NetworkPolicy exceptions for noetica namespace.
4. Quarantine or stop Noetica workload pods.
5. Revoke agent-registry grant for superconscious task submission.
6. Record revocation ledger entry with timestamp and evidence refs.
7. Preserve all admission and revocation evidence artifacts for replay.
```

This plan must be tested and hash-bound before `candidate_status` advances to `admitted`.
Revocation evidence ref: `local://evidence/noetica/revocation-plan.json` (operator-local only).

---

## 7. Admission pack generation (pending)

When all gates above pass, generate the admission pack with:

```bash
python tools/triune/render-admission-pack.py \
  --candidate noetica.chat.m2a \
  --candidate-name "Noetica Chat Surface M2a" \
  --event-ir-ref local://evidence/noetica/event-ir.json \
  --proof-ref local://evidence/noetica/guardrail-policy-dry-run.json \
  --sbom-ref local://evidence/noetica/sbom.spdx.json \
  --signature-ref local://evidence/noetica/signatures/release.sig \
  --image-ref local://evidence/noetica/images/noetica-chat.sha256 \
  --network-policy-ref examples/triune/networkpolicy/default-deny.yaml \
  --dry-run-result pass \
  --dry-run-output ~/triune-lab/evidence/noetica/policy-dry-run.json \
  --dry-run-evidence-ref local://evidence/noetica/policy-dry-run.json \
  --revocation-ref local://evidence/noetica/revocation-plan.json \
  --output ~/triune-lab/admission-packs/noetica-chat.m2a.admission-pack.json
```

Then validate:
```bash
python tools/triune/validate-admission-pack.py \
  ~/triune-lab/admission-packs/noetica-chat.m2a.admission-pack.json
```

Expected result: `PASS` with `candidate_status: proposed`.
Advance to `approved` only after host approval is issued and recorded.

---

## 8. Non-claims

- This document is a pending admission record, not proof of admission.
- No host approval has been issued.
- No dry-run has been executed.
- No Cilium egress exceptions have been applied.
- No Triune cluster member record exists for Noetica yet.
- The synthetic `model-catalog-entry.noetica-chat.synthetic.json` is a structural fixture only.
- `epistemicLevel: synthetic` in the model catalog entry reflects the absence of live eval.
- Steering at `full` tier is not exercisable until M2b real steering proof is closed.
- M3 SourceOS integration (`superconscious` egress) is not wired.
