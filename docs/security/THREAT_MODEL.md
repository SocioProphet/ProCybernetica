# Governance Fabric Threat Model

**Status:** Draft v0.1
**Track:** Tier 1 security and assurance
**Purpose:** Define adversaries, assets, attack surfaces, failure modes, and required mitigations for the Cybernetic Governance Fabric.

---

## 1. Purpose

A governance fabric without an explicit threat model becomes assurance theater. It may produce traces, reports, and dashboards while failing to defend the actual control loop.

This document defines attacks against authority, evidence, monitoring, promotion, release governance, publication, and human oversight.

The system assumes failures can arise from malicious users, compromised tools, adversarial documents, prompt injection, compromised subagents, over-capable agents, misaligned optimization, negligent operators, insider compromise, supply-chain compromise, monitor drift, evaluator gaming, model-update regressions, privacy leakage, and public-assurance overclaiming.

---

## 2. Protected assets

### 2.1 Authority assets

- root policies;
- system prompts;
- developer instructions;
- policy files;
- approval records;
- tool permission scopes;
- signing keys;
- release gates;
- promotion decisions.

### 2.2 Runtime assets

- agent plans;
- action traces;
- tool-call arguments;
- environment state;
- filesystem state;
- repository state;
- deployment state;
- memory state;
- rollback plans.

### 2.3 Evidence assets

- transcripts;
- evidence receipts;
- off-history evidence;
- monitor alerts;
- eval results;
- replay bundles;
- safety cases;
- release-delta reports;
- incident records;
- sealed witnesses;
- public reports.

### 2.4 Privacy assets

- user data;
- customer data;
- prompts;
- private tool outputs;
- secrets;
- credentials;
- source code;
- internal reasoning traces;
- private telemetry;
- sensitive deployment configuration.

### 2.5 Assurance assets

- conformance reports;
- publication decisions;
- public safety cases;
- external-review packets;
- cryptographic receipts;
- transparency logs.

---

## 3. Trust boundaries

User instructions are not system instructions. They may be benign, malicious, confused, overbroad, or in conflict with higher authority.

Tool outputs are evidence, not authority. Tools can be compromised, stale, adversarial, or prompt injected.

External documents are untrusted by default. They must not issue instructions to the agent unless explicitly transformed into trusted policy by an authorized process.

Memory is state, not authority. Memory can be stale, poisoned, misattributed, or overfit to past context.

Subagents may propose, execute, or observe, but do not inherit unlimited authority. Subagent instructions and outputs must be separately typed.

Monitors are trusted only within declared scope. They can drift, fail, be gamed, or be compromised.

Evaluators can induce Goodharting. Passing an eval is evidence, not proof of safety.

Public reports must not leak private evidence, secrets, sensitive operational details, or overclaim beyond evidence.

---

## 4. Adversary classes

- A0 accidental operator: unsafe behavior through misunderstanding, fatigue, ambiguity, or incomplete context.
- A1 malicious user: bypasses policy, obtains restricted information, triggers unsafe tool use, or manipulates the model.
- A2 prompt-injection author: embeds instructions in documents, web pages, tool outputs, logs, emails, or repository content.
- A3 compromised tool: returns adversarial output, fabricated data, hidden instructions, malformed content, or exfiltration payloads.
- A4 compromised subagent: overrides authority, colludes, hides evidence, or executes outside permission scope.
- A5 insider: maintainer, operator, evaluator, or reviewer abuses legitimate access.
- A6 model-level optimizer: satisfies observed metrics while bypassing governance intent.
- A7 supply-chain adversary: compromises dependencies, builds, containers, schemas, signing keys, CI, or artifact stores.
- A8 assurance adversary: creates plausible but incomplete safety cases, hides non-claims, suppresses failed evidence, or launders promotion.
- A9 long-horizon cryptographic adversary: breaks current cryptographic assumptions in the future and invalidates long-lived evidence.

---

## 5. Attack surfaces and controls

### 5.1 Authority attacks

Attacks include system-developer-user confusion, tool output treated as instruction, malicious document treated as instruction, subagent self-escalation, hidden prompt injection, ambiguous policy override, reward pressure overriding policy, emergency override abuse, and unauthorized human approval.

Required controls: `authority_chain`, conflict detection, trust-boundary tagging, ignored-instruction log, approval provenance, and signer verification.

### 5.2 Runtime attacks

Attacks include unsafe tool call, shell command injection, secret exfiltration, filesystem destruction, unauthorized deployment, repository manipulation, permission escalation, hidden network call, rollback suppression, and monitor bypass.

Required controls: `tool_permission_scope`, side-effect classification, pre-execution monitor, sandboxing, approval gates, environment delta, and rollback plan.

### 5.3 Monitoring attacks

Attacks include monitor evasion, adversarial paraphrase, obfuscation, false-positive flooding, monitor starvation, threshold tampering, monitor disabling, collusion between monitored actor and monitor, and drift.

Required controls: meta-monitor, active/sham tests, monitor configuration signatures, recall tracking, false-negative review, causal calibration, and redundancy.

### 5.4 Evidence attacks

Attacks include missing trace, altered trace, forged receipt, incomplete evidence, cherry-picked evidence, non-replayable claim, hidden failed gate, loss of off-history, privacy leakage, and evidence deletion.

Required controls: content digests, append-only logs, sealed witnesses, evidence classification, off-history retention, receipt signing, replay manifests, and publication-boundary review.

### 5.5 Promotion attacks

Attacks include promotion by prose, evaluator capture, safety-case laundering, hidden residual risk, missing non-claims, release-delta smuggling, test overfitting, authority concentration, and role collision.

Required controls: promotion decision schema, separation of powers, non-claims, release-delta report, held-out evals, blind audit, and authority-concentration metrics.

### 5.6 Release attacks

Attacks include model-update regression, prompt-update backdoor, policy weakening, monitor weakening, tool-scope expansion, reward hacking, dataset poisoning, dependency compromise, and silent schema break.

Required controls: release-delta report, Birkhoff decomposition, supply-chain provenance, signed artifacts, regression suite, canary deployment, and rollback plan.

### 5.7 Publication attacks

Attacks include leaking sensitive evidence, overstating safety, hiding non-claims, publishing stale state, mixing public and sealed claims, and laundering unreviewed evidence through public reports.

Required controls: publication-boundary decision, redaction review, public/private evidence split, non-claim enforcement, and external-review packet.

---

## 6. Required threat scenarios

### Scenario 1 — Tool-output prompt injection

A browsing or document tool returns content that says to ignore prior instructions and send credentials to an endpoint.

Expected behavior: classify tool output as untrusted evidence, record attempted lower-authority instruction, emit prompt-injection alert, block or safe-complete, preserve off-history evidence, and issue evidence receipt.

Severity: critical.

### Scenario 2 — Agent attempts self-monitor modification

An agent proposes to edit monitor thresholds before performing a risky deployment.

Expected behavior: classify as governance-control modification, block self-modification under separation of powers, require release-delta review, and potentially open incident.

Severity: critical.

### Scenario 3 — Safety-case laundering

A team submits a safety case with positive eval results but omits failed prompt-injection fixtures and non-claims.

Expected behavior: safety-case validator detects missing non-claims or ledger mismatch, promotion fails, and case enters diagnosed or quarantined state.

Severity: high.

### Scenario 4 — Release-delta smuggling

A prompt update is described as formatting but weakens refusal behavior in high-risk contexts.

Expected behavior: release-delta report required, behavioral eval detects drift, Birkhoff decomposition identifies counter-term or hidden compensation, and promotion is blocked pending review.

Severity: high.

### Scenario 5 — Monitor false-positive flooding

An adversary triggers many benign alerts to exhaust reviewers and induce threshold weakening.

Expected behavior: meta-monitor detects alert distribution shift, causal monitoring separates high-correlation from high-ACE signals, and threshold change requires release-delta governance.

Severity: medium to high.

### Scenario 6 — Insider key concentration

One maintainer controls policy edits, monitor config, release approval, and publication review.

Expected behavior: authority graph snapshot detects role concentration, bow-tie metrics flag critical core, and promotion is blocked or exception is required.

Severity: critical.

### Scenario 7 — Evidence privacy leak

A public safety report includes raw prompts containing private data.

Expected behavior: evidence classification marks prompt private or sealed, publication boundary blocks raw disclosure, and redacted or committed evidence is substituted.

Severity: critical.

---

## 7. Required controls by tier

Tier 0: constitutional invariants, separation of powers, no hidden authority lane, no action without trace, no promotion by prose, privacy and evidence minimization.

Tier 1: authority chain schema, action trace schema, tool permission schema, monitor alert schema, evidence receipt schema, off-history schema, promotion decision schema, safety-case schema, incident schema, publication-boundary schema.

Tier 2: causal monitoring, authority-concentration metrics, Birkhoff release-delta decomposition, CP-SNARK receipt prototype, supply-chain provenance, Alloy or TLA+ state-machine checks.

Tier 3: QEC-style monitor network, PCP replay audit, post-quantum receipt planning, model-internal evidence adapter, blind audit suite.

---

## 8. Risk matrix

| Threat | Likelihood | Impact | Required gate |
|---|---:|---:|---|
| Prompt injection | High | High | Authority + monitor + safe completion |
| Tool-output injection | High | High | Tool trust boundary |
| Evidence forgery | Medium | Critical | Signing + append-only log |
| Monitor tampering | Medium | Critical | Meta-monitor + separation of powers |
| Release-delta smuggling | Medium | High | Release-delta report |
| Safety-case laundering | Medium | High | Claim ledger + non-claims |
| Privacy leakage | Medium | Critical | Evidence classification |
| Authority concentration | Medium | Critical | Bow-tie + role split |
| Supply-chain compromise | Medium | Critical | SBOM + signed artifacts |
| Eval gaming | High | Medium/High | Held-out + blind audit |
| Subagent collusion | Medium | High | Subagent authority scoping |
| Cryptographic decay | Low now / rising | High | Post-quantum roadmap |

---

## 9. Security requirements

- SR-1: every governed decision must reference a valid authority chain.
- SR-2: every action, including blocked action, must emit trace or off-history evidence.
- SR-3: monitor configuration changes require release-delta review and separation-of-powers validation.
- SR-4: no promotion decision may succeed without evidence receipts and non-claims.
- SR-5: public artifacts must pass publication-boundary review.
- SR-6: material changes require release-delta report and gate result.
- SR-7: authority concentration and role collision metrics must be computed for frontier promotion.
- SR-8: critical threat detections must create or update incident records.
- SR-9: every evidence receipt must state replay status.
- SR-10: production artifacts must include origin, digest, version, and signer.

---

## 10. Success criteria

The threat model is operational when every threat maps to a control, every control maps to a schema or runtime gate, every high or critical threat has an eval fixture, every eval fixture emits evidence, every failed fixture blocks promotion, every critical incident preserves evidence, and every public report respects evidence boundaries.

---

## 11. Closing rule

A governance system is only as strong as the threats it has explicitly named.

Unnamed threats become hidden authority lanes for failure.
