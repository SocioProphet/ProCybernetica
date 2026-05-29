# WallGuard Information Barriers

**Status:** Draft v0.1  
**Track:** ProCybernetica frontier governance doctrine  
**Scope:** Doctrine and conformance vocabulary only; downstream runtime implementation remains in owning repositories.  
**Parent issues:** `SocioProphet/ProCybernetica#102`, `SocioProphet/sociosphere#392`

## Purpose

WallGuard defines professional-workroom information barriers for the Prophet ecosystem.

A WallGuard barrier is not generic role-based access control. It is a confidentiality topology that governs whether a human, agent, tool, model, memory store, retrieval system, connector, artifact, workroom, or destination may participate in a client, matter, engagement, or restricted knowledge context.

The doctrine exists because agentic professional work changes the meaning of an ethical wall. A wall is no longer only a document-access rule or a human staffing restriction. It must also govern retrieval, memory writes, embeddings, agent-to-agent collaboration, model-context assembly, tool invocation, generated artifacts, clean-room release, and audit receipts.

This document establishes doctrine only. It does not implement runtime services, schemas, validators, APIs, product UI, storage, model routing, memory services, retrieval services, or live policy enforcement.

## Source and estate posture

WallGuard is a new doctrine slice derived from the existing ProCybernetica control doctrine and the current WallGuard planning program.

The relevant ProCybernetica anchors are:

- `docs/constitutional/CONSTITUTIONAL_INVARIANTS.md`
- `docs/constitutional/SEPARATION_OF_POWERS.md`
- `docs/foundations/CYBERNETIC_GOVERNANCE_FABRIC.md`
- `docs/security/THREAT_MODEL.md`
- `docs/integrations/AGENTPLANE_CYBERNETIC_GOVERNANCE_BINDING.md`
- `docs/cybernetic-governance/RECIPROCAL_CHANNEL_GOVERNANCE.md`
- `docs/source-captures/VOLUME_VI_OPERATIONAL_MESH_CAPTURE.md`
- `docs/source-captures/VOLUME_VII_SECURE_COORDINATION_CAPTURE.md`
- `docs/source-captures/CONSTITUTIONAL_CONTROL_CAPTURE.md`
- `docs/source-captures/BOOK_XI_IMPLEMENTATION_PRACTICUM_CAPTURE.md`

Runtime and product ownership remains downstream:

- `policy-fabric` owns WallPolicy and WallDecision semantics.
- `api-contracts` owns service/API contracts once issue tracking is enabled or routed elsewhere.
- `agent-registry` owns agent identity, session scope, recusal, and wall-membership metadata.
- `agentplane` owns agent collaboration and execution enforcement.
- `guardrail-fabric` owns model, tool, RAG, connector, and artifact-release guardrail binding.
- `memory-mesh` owns compartmented memory read/write enforcement.
- `sherlock-search` and `prophet-core-query` own pre-exposure retrieval and query enforcement.
- `holmes` owns clean-room synthesis behavior.
- `prophet-platform` owns Professional Workroom product surfaces.
- `prophet-core-ledger` owns WallDecisionReceipt and WallEvent ledgering.
- `sociosphere` and `workspace-inventory` own cross-repo topology and estate compliance tracking.

Explicitly excluded implementation dependencies:

- `cascade` is reference-only because no explicit license was found.
- `presidio` is not part of this workstream.
- `OrchestraOS` is not part of this workstream.
- Placeholder/demo or unrelated research repos must not become WallGuard authority by proximity.

## Core thesis

Professional work requires two distinct permissions:

1. **Access permission:** whether a subject may see or retrieve a resource.
2. **Collaboration permission:** whether a subject may combine context, memory, reasoning, tools, or outputs with another subject, matter, workroom, or destination.

Conventional access control often handles the first and misses the second. WallGuard exists for the second as much as the first.

A user or agent may be allowed to access Matter A and Matter B separately while still being prohibited from letting Matter A context influence Matter B work. A retrieval system may be allowed to index both matters while still being prohibited from returning both into one ranking context. A model router may be allowed to call a hosted provider for public work while being prohibited from using that provider for restricted work. A memory system may be allowed to store a matter-specific summary while being prohibited from promoting that summary into global memory.

WallGuard therefore governs context flow, not merely object access.

## Definitions

### Wall

A wall is a declared information barrier that constrains subjects, resources, actions, memory, retrieval, tools, connectors, generated artifacts, and destinations under a policy version.

### Professional workroom

A professional workroom is an execution chamber for a client, matter, engagement, project, or restricted context. It binds human participants, agents, tools, data, memory scopes, retrieval scopes, artifact outputs, destinations, and receipts.

A workroom is not merely a chat, folder, dashboard, or board. It is a policy-scoped control chamber.

### Subject

A subject is any entity that can observe, retrieve, transform, decide, collaborate, write memory, invoke tools, receive artifacts, or export information.

Subjects include humans, agents, subagents, service accounts, tools, models, model providers, connectors, workrooms, queues, workers, dashboards, and downstream systems.

### Resource

A resource is any information object or operational object that can be read, written, transformed, summarized, embedded, routed, exported, or used as evidence.

Resources include documents, messages, emails, transcripts, chunks, embeddings, search results, memories, graph edges, tasks, playbooks, run steps, tool outputs, generated artifacts, secrets, logs, receipts, and audit records.

### Context

Context is the active operating frame in which a subject acts. At minimum, WallGuard context should identify workroom, client, matter, policy version, subject session, requested action, resource labels, destination, and enforcement point.

### Destination

A destination is any sink that can receive or preserve information. Destinations include humans, agents, workrooms, memory compartments, search indexes, graph stores, Slack/Teams/email channels, HTTP endpoints, public artifacts, dashboards, ledgers, and external providers.

### Contamination or taint

Contamination is the condition in which restricted context may influence a later operation outside its permitted wall scope.

Contamination is not limited to direct quotation. It may arise through summaries, embeddings, latent session state, model context, cached tool output, graph edges, retrieval rankings, or agent memory.

### Clean-room release

A clean-room release is a governed output path that permits sanitized, policy-approved abstractions to move beyond a restricted wall.

Clean-room release is not a bypass. It requires decision receipt, source-label preservation, destination scope, residual-risk statement, and policy version.

### WallDecisionReceipt

A WallDecisionReceipt is the audit object recording a WallGuard allow, deny, redact, quarantine, escalate, or clean-room release decision.

## Constitutional alignment

WallGuard specializes existing constitutional invariants.

### No hidden authority lane

No subject may use informal collaboration, latent memory, shared vector indexes, cached context, or unstated workroom membership to bypass a declared wall.

Every wall-sensitive decision must identify the authority chain, policy reference, subject, action, resource, context, destination, and enforcement point.

### No action without trace

A wall-sensitive allow, deny, redact, quarantine, escalate, or release decision is a governed action. It requires a trace or receipt.

A blocked cross-wall collaboration is not no event. It is off-history evidence.

### No promotion by prose alone

A clean-room summary, public artifact, global memory write, cross-workroom artifact, or unrestricted answer may not be promoted out of a restricted workroom because a human or model says it is safe. Release requires a policy decision and receipt.

### Evidence must be digital, typed, and digestible

Wall decisions must produce typed evidence that can be audited without leaking the protected payload. Receipts should carry hashes, references, labels, policy versions, and reason codes rather than unrestricted raw content.

### Separation of powers

The actor seeking release must not be the sole authority deciding release. Runtime executors, policy evaluators, monitors, evidence signers, and promotion/release authorities must remain distinct or record explicit exceptions.

### Off-history is retained

Denied access, denied collaboration, denied retrieval, denied memory write, redacted answer, quarantined artifact, and failed release all produce evidence. This evidence supports incident review, monitor calibration, and safety-case audit.

### Privacy and evidence minimization

WallGuard must preserve enough evidence to govern confidentiality while minimizing exposure of restricted content. Audit records should prove what happened without becoming a leakage channel.

## Control principles

### 1. Wall context precedes work

Restricted work must begin with explicit wall context. The system should not infer wall context from filenames, conversation tone, user memory, or model judgment alone.

### 2. Fail closed for missing restricted context

If a resource, subject, or destination appears restricted and the wall context is missing or incomplete, the operation must deny, quarantine, or escalate rather than proceed.

### 3. Access is not collaboration

A subject's permission to read a resource does not automatically authorize collaboration with another subject, export to another destination, memory promotion, or cross-matter synthesis.

### 4. Retrieval is exposure

Retrieval ranking, reranking, summarization, and model context assembly are exposure events. Restricted resources must be filtered before ranking, reranking, summarization, or model exposure.

### 5. Memory writes are high consequence

Durable memory writes, graph edge creation, embeddings, and global summaries can contaminate future work. They require stricter wall checks than transient display.

### 6. Agent state is governed state

An agent that has handled restricted context may carry contaminated session state. WallGuard must govern agent session transfer, subagent delegation, memory cursor reuse, tool grants, and clean-room handoff.

### 7. Tools and connectors are not neutral

A tool call or connector call may export information, mutate state, preserve logs, or create downstream visibility. Tool and connector calls require destination labels and wall decisions.

### 8. Generated artifacts inherit source constraints

A generated artifact inherits restrictions from its sources unless a clean-room release decision changes its classification.

### 9. Metadata can leak

The existence of a matter, client, document, task, run, blocked attempt, or relationship may itself be sensitive. Catalog and search systems must govern metadata visibility.

### 10. Clean-room release is bounded release

Clean-room output must declare what source classes informed it, what was excluded, what destination is allowed, what policy version authorized it, and what residual restrictions remain.

## Minimum WallGuard record fields

A WallGuard decision request should eventually provide at least:

- `subject_id`
- `subject_type`
- `action`
- `resource_refs`
- `resource_labels`
- `workroom_id`
- `client_id`
- `matter_id`
- `wall_policy_id`
- `wall_policy_version`
- `agent_session_id`
- `memory_scope`
- `tool_or_connector_ref`
- `destination_ref`
- `destination_labels`
- `enforcement_point`
- `request_correlation_id`

A WallDecisionReceipt should eventually provide at least:

- `decision_id`
- `decision_time`
- `policy_id`
- `policy_version`
- `subject_ref`
- `action`
- `resource_refs`
- `resource_label_summary`
- `context_ref`
- `destination_ref`
- `outcome`
- `reason_code`
- `enforcement_point`
- `receipt_visibility_class`
- `evidence_refs`
- `redaction_summary`
- `residual_restrictions`

## Decision outcomes

WallGuard policy should support at least these outcomes:

- `allow`
- `deny`
- `redact`
- `quarantine`
- `escalate`
- `clean_room_release_requested`
- `clean_room_release_allowed`
- `clean_room_release_denied`

## Reason-code families

At minimum, WallGuard should distinguish:

- missing wall context
- subject outside wall
- resource outside wall
- incompatible client or matter context
- revoked or expired wall membership
- missing acknowledgment
- recused subject
- contaminated session state
- prohibited memory compartment
- prohibited retrieval source
- prohibited tool or connector
- prohibited destination
- metadata visibility denied
- clean-room release required
- override required
- policy version mismatch

## Downstream implications

### Policy Fabric

Policy Fabric should define WallPolicy, WallDecision, WallDecisionReceipt, WallEvent, CleanRoomRelease, WallOverrideRequest, and WallAcknowledgment semantics.

It is the policy authority for WallGuard decisions. Downstream systems should consume its decisions rather than inventing local wall law.

### API Contracts

API contracts should expose service methods for wall-decision evaluation, dry-run simulation, label registration, receipt emission/fetch, clean-room release request, acknowledgment, override/escalation, and audit export.

### Agent Registry

Agent Registry should record wall memberships, workroom/client/matter scope, recusal state, acknowledgment state, allowed memory compartments, tool grants, session contamination markers, and revocation state.

### AgentPlane

AgentPlane should enforce WallGuard on agent-to-agent collaboration, subagent delegation, run capsules, tool grants, action dispatch, memory access, and clean-room handoff.

### Guardrail Fabric

Guardrail Fabric should bind WallGuard decisions into model calls, tool calls, RAG package use, connector calls, prompt/context assembly, redaction, quarantine, escalation, and artifact release.

### Memory Mesh

Memory Mesh should implement compartment-aware memory reads and writes. Restricted, contaminated, clean-room-derived, client-scoped, matter-scoped, user-private, and global memory must remain distinct.

### Sherlock Search and Query

Search and query systems should enforce policy before source exposure, ranking, reranking, summarization, or answer assembly. Post-filtering is not sufficient.

### Holmes

Holmes should preserve source labels through investigation state, refuse cross-wall synthesis when policy denies it, and request clean-room release when sanitized output may be permitted.

### Prophet Platform

Prophet Platform should surface Professional Workrooms, wall state, acknowledgments, blocked attempts, clean-room release workflows, and receipt references without owning policy authority.

### Prophet Core Ledger

The ledger should treat denied, redacted, quarantined, escalated, and clean-room decisions as first-class events, not as incidental logs.

### SocioSphere and Workspace Inventory

SocioSphere and Workspace Inventory should track the cross-repo WallGuard spine, implementation status, dependency direction, excluded repositories, and compliance posture.

## Minimum conformance posture

A downstream system is minimally WallGuard-aware only if it can answer:

1. What wall context is active?
2. Who or what is the subject?
3. What action is requested?
4. What resource or metadata is involved?
5. What destination or sink is involved?
6. Which policy version was evaluated?
7. Was the decision allow, deny, redact, quarantine, escalate, or clean-room release?
8. What reason code explains the decision?
9. What receipt or event records the decision?
10. What downstream memory, retrieval, artifact, or connector effects are permitted or prohibited?

## Non-claims

This document does not implement WallGuard runtime enforcement.

This document does not define the final JSON Schema or protobuf surface.

This document does not claim production readiness, legal compliance, law-firm compliance certification, consulting-firm compliance certification, or complete conflict-management coverage.

This document does not depend on, import from, or license code from `cascade`, `presidio`, `OrchestraOS`, or any other noncanonical repo.

This document claims only a doctrine boundary: professional-workroom information barriers must govern agentic context flow, not merely document access.
