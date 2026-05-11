# Human Protection Layer (HPL) — reconciliation draft v0.1

Status: reconciliation draft, not final runtime schema.

Owner: ProCybernetica reconciliation track.

Adopters: SocioProphet/human-digital-twin, SocioProphet/gaia-world-model, SocioProphet/superconscious, and future Digital Control Atlas profiles.

## 0. Principle

People are protected before models are useful.

A chart may be mathematically coherent and still blocked. A solver may converge and still be unsafe. A claim may be interesting and still be non-exportable. A control program may be valid in simulation and forbidden in the world. A human twin may generate evidence but must never replace the human.

This layer exists to make that principle executable, reviewable, and difficult to bypass.

## 1. Scope

The Human Protection Layer applies to any system, repository, agent, profile, control program, model, solver, or export that can affect a person by measuring, modeling, inferring, ranking, predicting, targeting, excluding, including, persuading, experimenting upon, representing, or acting upon them.

It covers direct human-contact systems and indirect systems whose outputs shape decisions about people. It also covers Gaia-scale actions when affected populations can be harmed by a world-model action, intervention, omission, policy recommendation, infrastructure action, or environmental control plan.

## 2. Protected person

A protected person is anyone who is:

- measured;
- modeled;
- inferred about;
- represented by a digital twin;
- ranked, scored, classified, or predicted;
- included in or excluded from a system output;
- targeted by a message, action, policy, or experiment;
- exposed to physical, cognitive, economic, social, environmental, or reputational risk;
- affected by an Atlas, GAIA, HDT, Superconscious, ProCybernetica, AgentPlane, or SourceOS action.

Protection is not limited to direct users. Non-users and bystanders are protected if a system output can materially affect them.

## 3. Human-impacting action

A human-impacting action is any action that can change a person's environment, opportunities, reputation, body, cognitive state, privacy state, resource access, legal standing, social exposure, or future treatment.

Examples include:

- exporting a human digital twin claim;
- generating or acting on a physiological, cognitive, behavioral, capability, trust, risk, or health-related inference;
- running a bioelectronic, biometric, sensor, or field-coupling protocol;
- recommending an intervention affecting a population;
- triggering workflow, access, employment, finance, care, enforcement, or governance decisions;
- persuading, nudging, emotionally targeting, or otherwise shaping behavior using personalized inference;
- delegating action to an agent over tools, infrastructure, repositories, devices, browsers, terminals, services, or models.

## 4. Validity is not permission

Atlas validity is not operational permission.

A program can be:

- mathematically valid;
- scientifically speculative;
- valid only in simulation;
- valid for phantom or synthetic benchmarks;
- valid for ex vivo research;
- blocked for in vivo or human-contact use;
- blocked by consent policy;
- blocked by privacy policy;
- blocked by missing authority;
- blocked by underidentification;
- blocked by unsupported mechanism claims;
- blocked by affected-population risk;
- blocked by public/private publication boundary.

Every profile MUST expose both a technical status and a policy status.

## 5. Seven protection gates

Every human-impacting profile or program must pass the applicable gates before export or action.

### Gate 0 — Claim boundary

Purpose: protect people from false, overstated, mystical, unsupported, or non-falsifiable claims.

Required checks:

- claim has evidence tier;
- claim has mechanism status;
- claim has scope and limitation statement;
- claim has falsification or revision condition when research-facing;
- speculative claims cannot be exported as validated;
- metaphor-only language cannot become a mechanism label.

Default blocked mechanism labels:

- phantom_dna_field;
- semantic_wave_text;
- dna_inductor;
- dna_speaker_microphone;
- holographic_gene_laser;
- native_dna_biological_magnet;
- unreplicated_field_genetics_mechanism.

These may appear only as excluded claims, historical references, or metaphor-only labels.

### Gate 1 — Consent and autonomy

Purpose: protect human agency.

Required checks:

- consent scope is explicit;
- consent receipt or policy basis is recorded;
- consent is revocable where applicable;
- use purpose is bounded;
- model use, data use, research use, export use, and contact/intervention use are separately scoped;
- vulnerable population and bystander checks are performed where relevant;
- no consent means no export of human-derived private claims unless a valid legal/ethics basis exists and is recorded.

### Gate 2 — Privacy and minimization

Purpose: prevent digital twins from becoming shadow dossiers.

Required checks:

- raw private evidence remains local by default;
- exports contain minimal derived claims, not raw evidence, unless explicitly authorized;
- provenance is content-addressed and reviewable;
- raw biometrics, raw physiology, raw cognition traces, raw private telemetry, and raw personal sensor data are non-exportable by default;
- derived claims carry minimization basis;
- retention, revocation, and deletion/quarantine paths exist.

### Gate 3 — Physical safety

Purpose: prevent bodily harm.

Default policy:

- human actuation is blocked by default;
- simulation is allowed when safe and labeled;
- synthetic and phantom testing may be allowed when scoped;
- ex vivo research requires protocol labeling and safety model;
- in vivo or human-contact work requires independent review, applicable ethics/regulatory path, runtime monitoring, emergency stop, and dose/safety model.

Required checks for any physical protocol:

- dose model present;
- thermal model present where energy deposition is possible;
- rate and amplitude limits present;
- runtime monitor present for any real-world actuation path;
- emergency stop or rollback path present when applicable;
- independent safety review required for human-contact paths;
- human-contact device/software functions cannot be authorized by planning code alone.

### Gate 4 — Psychological and cognitive safety

Purpose: protect mental agency, dignity, and non-manipulation.

Required checks:

- no hidden persuasion;
- no emotional exploitation;
- no covert personality inference export;
- no mental-health, capability, or identity classification without a declared boundary and appropriate authority;
- no autonomous high-stakes decision;
- human appeal path exists for human-impacting outputs;
- operational traces are safe summaries, not private chain-of-thought exposure.

### Gate 5 — Cyber, adversarial, and misuse safety

Purpose: prevent harmful reuse, surveillance, coercive profiling, policy bypass, and unsafe automation.

Required checks:

- misuse review completed for human-boundary, world-action, actuation, inference, surveillance-adjacent, and autonomous-agent profiles;
- tool authority declared;
- no invisible authority;
- no credential, host, shell, browser, socket, deployment, or model-routing authority unless declared in trust surface metadata;
- policy admission required before side effects;
- autonomous execution denied by default;
- red-team or adversarial review required for high-impact profiles.

### Gate 6 — Redress, revocation, appeal, and auditability

Purpose: guarantee recourse.

Required capabilities:

- inspect claims about the person;
- inspect provenance and evidence tier;
- challenge a claim;
- revoke consent where applicable;
- delete or quarantine private evidence where applicable;
- inspect export history;
- appeal high-impact decisions;
- obtain human contact or human review path;
- replay the operational trace at a safe evidence level.

## 6. Safety status vocabulary

Profiles MUST use specific status labels rather than a single pass/fail boolean.

Allowed status labels:

- SAFE_TO_SIMULATE;
- SAFE_TO_PUBLISH_AS_SPEC;
- SAFE_TO_USE_AS_INTERNAL_PLANNING;
- SAFE_TO_EXPORT_AS_CLAIM;
- SAFE_FOR_SYNTHETIC_TEST;
- SAFE_FOR_PHANTOM_TEST;
- SAFE_FOR_EX_VIVO_RESEARCH;
- REQUIRES_ETHICS_REVIEW;
- REQUIRES_REGULATORY_REVIEW;
- BLOCKED_HUMAN_ACTUATION;
- BLOCKED_UNSUPPORTED_CLAIM;
- BLOCKED_PRIVACY_RISK;
- BLOCKED_CONSENT_MISSING;
- BLOCKED_AUTHORITY_MISSING;
- BLOCKED_UNDERIDENTIFIED;
- BLOCKED_AFFECTED_POPULATION_RISK;
- BLOCKED_POLICY;
- SPECULATIVE_ONLY.

## 7. Evidence tiers

Evidence tier MUST be explicit for exported claims and Atlas profile outputs.

- E0 — metaphor, analogy, or conceptual note;
- E1 — mathematical formalism or typed specification;
- E2 — simulation fixture or toy model;
- E3 — calibrated synthetic or phantom benchmark;
- E4 — ex vivo or lab-controlled evidence;
- E5 — observational real-world evidence;
- E6 — controlled intervention evidence under approved protocol;
- E7 — operationally validated with replay, monitoring, and postmortem evidence.

No profile may export E0/E1/E2 as operationally validated. Human-contact or world-impacting action requires a separate policy decision even when evidence tier is high.

## 8. Repository adoption matrix

### ProCybernetica

Role: doctrine, reconciliation, conformance law, public-first publication boundary, promotion discipline, and control-node governance.

Initial responsibility:

- reconcile HPL vocabulary;
- decide canonical envelope names;
- define control-node mapping;
- define policy/conformance requirements;
- publish public-safe specs, tests, and synthetic fixtures.

### Human Digital Twin

Role: human-boundary claims, consented exports, Ω readiness, privacy minimization, and human-safe profile gates.

Initial responsibility:

- block human actuation by default;
- keep raw private evidence local by default;
- export only minimal claims with Ω, provenance, consent, and evidence tier;
- host FCBCP/HSP-Map as research-only Atlas profiles unless separately approved.

### GAIA World Model

Role: Earth/world charts, provenance-backed world-state, action templates, affected-population review, and public reports.

Initial responsibility:

- put Atlas profiles through CV → ontology → validation → actions → reports;
- attach affected-population review to world actions;
- prevent speculative world-control claims from becoming action templates.

### Superconscious

Role: thin cognition/control loop for planning, policy-admission requests, model/tool routing requests, safe operational traces, replay plans, and benchmark assertions.

Initial responsibility:

- propose Atlas programs but never authorize them;
- emit safe traces, not hidden authority;
- require policy admission before side effects;
- remain deterministic/no-side-effect in M1 posture.

## 9. Trust-surface requirement

No Atlas solver, planner, actuator, memory handler, model route, browser/terminal controller, deployment action, or egress path may become operational unless its authority is declared in the applicable trust-surface metadata and admitted by policy.

Minimum trust-surface fields for Atlas/HPL use:

```yaml
authority:
  can_plan: true
  can_simulate: false
  can_read_world_data: false
  can_read_human_data: false
  can_export_claim: false
  can_actuate_world: false
  can_actuate_human: false
  can_emit_policy_request: true
  can_write_memory: false
  can_call_network: false
  can_mutate_host: false
```

## 10. Minimum envelope shape

Every human-impacting Atlas or HDT/HPL output should be reducible to this envelope:

```yaml
program_id: string
profile_id: string
subject_scope: none | individual | group | population | bystander_possible
protected_person_risk: low | medium | high | unknown
evidence_tier: E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7
status: string
claim_boundary:
  mechanism_status: validated | hypothesis | metaphor_only | excluded | unknown
  unsupported_claim_blocked: boolean
consent:
  required: boolean
  present: boolean
  scope: [string]
privacy:
  raw_private_evidence_attached: boolean
  minimization_basis: string
physical_safety:
  human_actuation: blocked | simulation_only | protocol_required | approved_external_process
cognitive_safety:
  hidden_persuasion: blocked
  high_impact_decision: blocked | review_required | approved_external_process
misuse_review:
  required: boolean
  completed: boolean
redress:
  inspect: boolean
  challenge: boolean
  revoke: boolean
  appeal: boolean
policy:
  decision: allow | deny | block | needs_review
  reasons: [string]
provenance:
  evidence_hash: string
  policy_version: string
  reviewer_or_process: string
```

## 11. Minimum tests required before promotion

- unsupported mechanism labels are blocked;
- speculative claims cannot export as validated;
- human actuation is blocked by default;
- raw private evidence cannot export by default;
- missing consent blocks human-derived export where consent is required;
- missing trust-surface authority blocks tool or runtime side effects;
- high-impact outputs require appeal/redress path;
- world-action profiles require affected-population risk review;
- Superconscious planning trace cannot authorize execution;
- GAIA action report must include provenance and policy decision;
- HDT Ω export must include evidence tier and minimization basis.

## 12. Publication boundary

Public by default:

- HPL doctrine;
- schemas after reconciliation;
- synthetic fixtures;
- simulated Atlas runs;
- conformance tests;
- public-safe reports;
- excluded-claim registry.

Private, redacted, or locally retained by default:

- human raw observations;
- live private telemetry;
- credentials or secrets;
- sensitive deployment configuration;
- legally restricted third-party material;
- human-identifying or sensitive evidence not explicitly consented for publication;
- security details that materially increase exploitation risk.

## 13. Immediate reconciliation tasks

1. Reconcile HPL terms with ProCybernetica lifecycle, promotion, replay, and control-node vocabulary.
2. Map HPL envelopes to Human Digital Twin Ω exports.
3. Map HPL status labels to GAIA action reports.
4. Map HPL policy-admission requests to Superconscious safe traces.
5. Produce provisional schemas only after term reconciliation.
6. Build public-safe fixtures and negative tests before any runtime expansion.
