# SocioProphet Proof Pack Template

**Version:** 1.0
**Status:** Draft v0.1 capture
**Track:** Assurance, buyer review, procurement review, architecture review, and gate-review evidence packaging
**Purpose:** Assemble an evidence-backed buyer, analyst, procurement, architecture, or gate-review packet for the SocioProphet platform or for a specific governed agent capability.

---

## 1. Packet metadata

- Review name:
- Review date:
- Reviewer organization:
- Buyer segment or deployment context:
- Product / platform version under review:
- Documentation version under review:
- Weighting model used: default enterprise or regulated variant
- Primary use case or workflow class:
- Primary risks and constraints:

---

## 2. Executive summary

Provide a one-page summary answering the following:

- What is being evaluated?
- What problem does it solve?
- What deployment class is in scope?
- What level of autonomy is requested?
- What level of evidence and governance is available?
- What are the strongest proof points?
- What are the largest gaps?
- Recommended disposition: accept, conditional accept, hold, or reject.

---

## 3. Product efficacy evidence

Include the strongest evidence for whether the system works.

### Required or recommended artifacts

- benchmark report;
- scenario evaluation report;
- workflow completion export;
- latency and cost dashboard extracts;
- tool correctness or groundedness report.

### Summary prompts

- Which workflows were scored?
- What was the evaluation window?
- What are the measured success thresholds and actual values?
- Which results are production evidence versus pilot evidence?
- What is not yet measured?

---

## 4. Governance and control evidence

Include the strongest evidence for whether the system is bounded, auditable, and governable.

### Required or recommended artifacts

- policy package identifiers and policy decision exports;
- approval workflow samples;
- replay execution reports;
- audit export samples;
- rollback rehearsal report;
- provenance and SBOM bundle references.

### Summary prompts

- Which actions are policy-gated?
- Which actions require human approval?
- What percentage of privileged actions have complete evidence?
- Are replay and rollback successful for the scored workflow class?
- Which governance gaps remain?

---

## 5. Customer delivery and adoption evidence

Include the strongest evidence for whether customers can deploy and adopt the system quickly and repeatedly.

### Required or recommended artifacts

- deployment timeline summary;
- time-to-first-production record;
- time-to-first-value summary;
- support SLA report;
- operator or admin productivity-change summary;
- adoption depth summary.

### Summary prompts

- How long did deployment take?
- What was the first measured business value and when was it observed?
- What delivery friction was encountered?
- What roles adopted the system?
- What level of operational lift has been measured?

---

## 6. Market proof evidence

Include the strongest evidence for whether the vendor or platform is durable and trusted in market context.

### Required or recommended artifacts

- anonymized production customer count by segment;
- lighthouse reference summaries;
- partner or integration inventory;
- competitive win or positioning summary;
- retention or expansion indicators where available.

### Summary prompts

- What segments are already served?
- What reference proof is usable in this review?
- Which deployment and integration partners exist?
- What is the current market maturity of this offer?

---

## 7. Artifact manifest template

Use the following structure for every artifact included in the packet.

- Artifact ID:
- Lane:
- Artifact type:
- Title:
- Date or evaluation window:
- Owner:
- Location:
- Redaction status:
- Reviewer note:

---

## 8. Redaction and handling rules

- Remove or replace customer-identifying information unless explicitly approved for disclosure.
- Remove secrets, internal hostnames, and operationally sensitive implementation details.
- Preserve enough structure for reviewers to validate claims without exposing prohibited information.
- Mark all synthetic, illustrative, or anonymized examples clearly.

---

## 8.1 Upstream-aligned evidence exhibits

For SocioProphet / SourceOS / FogStack reviews, include the following exhibits when applicable.

### FogStack parity exhibit

- FogStackParityReadinessRecord:
- Command used:
- Evaluation window:
- Non-mutating proof boundary confirmed: yes / no
- Post-MVP gaps disclosed: yes / no

### Identity and authentication exhibit

- Standards lock reference:
- Identity contract schemas:
- Example validation report:
- Runtime target under review:
- Shadow-spec override present: yes / no

### Agent Machine release evidence exhibit

- ReleaseEvidenceBundle:
- SignedReleaseBundleEnvelope:
- Supply-chain strict-mode result:
- Digest/provenance evidence:
- Real signing verifier present: yes / no / not claimed

### Professional Intelligence routing and guardrail exhibit

- Routing decision schema/version:
- Routing decision examples:
- Guardrail pack version:
- Citation required: yes / no
- Policy decision required: yes / no
- Workroom scope required: yes / no
- Tool grant required: yes / no
- Low-confidence escalation required: yes / no

### SourceOS Door profile exhibit

- NetworkAccessProfile:
- FirewallBindingProfile:
- MeshBindingProfile:
- ExternalModelProviderProfile:
- NativeAssistantBridgeProfile:
- Prompt egress default: denied / allowed / not applicable
- Inline secret exposure present: yes / no

### AgentTerm operator evidence exhibit

- AgentTerm event-log export:
- Matrix posture evidence:
- Policy-gated dispatch proof:
- Agent Registry resolution/grant evidence:
- Local smoke path result:

### Prophet Intelligence Foundry lifecycle exhibit

- Data manifest:
- Eval report:
- Safety / guardrail review:
- Model governance ledger release decision:
- Model-router admission:
- sourceos-model-carry approved reference:
- Agent Machine runtime placement evidence:
- AgentPlane run capsule:
- Operator readout:

### Claim discipline exhibit

- Claimed level: demo readiness / MVP parity / deployment parity / production parity / regulated readiness
- Evidence level actually proven:
- Known excluded claims:
- Reviewer disposition:

---

## 9. Submission checklist

- Executive summary included.
- Product efficacy evidence attached.
- Governance and control evidence attached.
- Customer delivery and adoption evidence attached.
- Market proof evidence attached.
- Artifact manifest complete.
- Redactions complete.
- Reviewer worksheet or scorecard attached.
- Final disposition recorded.

---

## 10. Appendix: sample disposition narrative

### Accept

The reviewed capability demonstrates repeatable product efficacy, strong governance coverage, acceptable delivery maturity, and sufficient market proof for the target deployment class.

### Conditional accept

The reviewed capability is promising and may be deployed or advanced if the listed remediation items are completed within the agreed review window.

### Hold

The reviewed capability should not advance yet because required evidence is incomplete, thresholds are not met, or operational readiness is insufficient.

### Reject

The reviewed capability is not suitable for advancement in the current state because product, governance, delivery, or trust evidence is materially inadequate.

---

## 11. Relationship to the Cybernetic Governance Fabric

This template is the reviewer-facing packaging layer for evidence produced by the Cybernetic Governance Fabric.

It should consume, not replace, the lower-level governance artifacts:

- `authority_chain.v1.json`
- `agent_action_trace.v1.json`
- `tool_permission_scope.v1.json`
- `off_history_evidence.v1.json`
- `evidence_receipt.v1.json`
- `promotion_decision.v1.json`
- `cybernetic_safety_case.v1.json`
- `release_delta_report.v1.json`
- `privacy_evidence_classification.v1.json`
- `artifact_provenance.v1.json`
- `non_claim.v1.json`

The proof pack is not itself the evidence. It is the packet that organizes evidence for buyer, analyst, architecture, procurement, or gate review.

---

## 12. Non-claims

This template does not claim that evidence exists for every exhibit.

This template does not permit overstating demo, MVP, deployment, production, or regulated-readiness levels.

This template does not bypass privacy, redaction, or publication-boundary controls.

This template does not replace the cybernetic safety case. It packages selected claims and evidence for a specific review context.
