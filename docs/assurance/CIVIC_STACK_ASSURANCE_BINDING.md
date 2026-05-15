# Civic-Stack Assurance Binding

Status: v0.1 assurance binding  
Issue: #40  
Runtime claim: none

## Purpose

This document binds ProCybernetica to the Seven-Model Civic Operating Architecture as the cybernetic security, resilience, control, and evidence-pack layer.

Ontogenesis owns civic ontology and semantic terms. ProCybernetica owns public assurance doctrine, risk/control bindings, incident/control-failure evidence, audit completeness signals, and forensic evidence-pack posture.

## Upstream semantic anchors

- `SocioProphet/ontogenesis#80` — seven-model civic organizational alignment.
- `SocioProphet/ontogenesis#81` — RationalGRL and OQL/OAC semantics.

Related implementation anchors:

- `SocioProphet/sociosphere#323` — governance object model.
- `SocioProphet/delivery-excellence#28` — audit/compliance scoring.
- `SocioProphet/policy-fabric#72` — policy guardrails.
- `SocioProphet/agentplane#154` — runtime evidence.

## Civic object families

ProCybernetica binds assurance evidence for these civic-stack object families:

| Civic family | ProCybernetica binding |
| --- | --- |
| Risk | `civic_risk_control_binding.v1.json` records risk/control attachment and severity. |
| Control | `civic_risk_control_binding.v1.json` records control objective, owner, and evidence references. |
| IncidentEvent | `civic_incident_control_event.v1.json` records incident and control-failure events. |
| AttestationEvent | `civic_evidence_pack.v1.json` and `civic_assurance_trace.v1.json` cite attestations. |
| EvidencePack | `civic_evidence_pack.v1.json` packages service/dataset/runtime/policy/artifact evidence. |
| AuditFinding | `civic_audit_signal.v1.json` records audit completeness and scoreability signals. |
| ThreatModel | `civic_risk_contribution.v1.json` records threats as negative contributions, blockers, or defeaters. |
| ResilienceTarget | `civic_risk_control_binding.v1.json` records resilience target and control coverage. |

## Seven-model attachment rule

Controls may attach to civic model layers as follows:

| Layer | Meaning | Control attachment |
| --- | --- | --- |
| CGRM | Civic governance/risk model | policy, authority, accountability, redress, oversight controls |
| SRM | Service reference model | service dependency, service continuity, service-level control evidence |
| DRM | Data reference model | dataset provenance, data minimization, data quality, privacy controls |
| TRM | Technical/runtime reference model | runtime attestation, supply-chain verification, dependency controls |
| OAC | Organizational artifact catalog | artifact release, proof-pack, policy, certificate, and provenance controls |

## Evidence-pack requirements

Every civic evidence pack must classify its decision target:

- `service_decision`
- `dataset_decision`
- `runtime_decision`
- `policy_decision`
- `artifact_decision`

Minimum evidence references:

- evidence receipt or equivalent governed evidence reference;
- risk/control binding reference;
- audit signal reference;
- provenance, attestation, or proof-pack reference where applicable.

## Incident and control-failure events

Incident/control-failure events must identify:

- affected civic layer;
- affected object reference;
- event kind;
- severity;
- control references;
- evidence pack reference;
- SocioSphere consumption status;
- remediation or review status.

## Audit completeness signals

Audit signals should be scoreable by Delivery Excellence. Required dimensions:

- evidence completeness;
- control coverage;
- provenance completeness;
- redaction status;
- runtime attestation coverage;
- policy decision coverage;
- open gaps.

## RationalGRL negative contributions and defeaters

Threats and risks are expressed as:

- `negative_contribution` — weakens goal satisfaction;
- `blocker` — prevents admission or promotion;
- `defeater` — defeats a claim or assurance conclusion;
- `conflict` — creates unresolved control or policy conflict.

These references remain semantic-facing and should be aligned with Ontogenesis. ProCybernetica records the assurance/control interpretation.

## Worked trace

The first public-synthetic worked trace is:

```text
artifact deployed
  -> policy checked
    -> runtime attested
      -> control verified
        -> evidence pack emitted
          -> score updated
```

This trace is represented by:

- `tests/fixtures/civic-stack/civic-stack-assurance.synthetic.json`
- `tools/cybernetic_governance/validate_civic_stack.py`
- `tests/test_civic_stack_assurance.py`

## Non-claims

ProCybernetica does not own the civic ontology, runtime execution, public-value scoring, SocioSphere governance runtime, Delivery Excellence scoring runtime, Policy Fabric guardrail runtime, AgentPlane runtime evidence production, or Ontogenesis semantic release discipline. ProCybernetica supplies assurance evidence, risk/control doctrine, validation fixtures, and public conformance expectations.
