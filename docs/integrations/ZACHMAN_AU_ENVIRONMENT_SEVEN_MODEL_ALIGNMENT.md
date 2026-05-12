# Zachman Agent-Unit Environment and Seven-Model Alignment

**Status:** Draft v0.1
**Track:** Enterprise ontology, agent-unit assembly, environment aperture, organization/economy alignment, and legacy-SOA modernization
**Applies to:** Cybernetic Governance Fabric, AgentPlane, PolicyFabric, SocioSphere, Prophet Platform, SourceOS, proof packs, and future civic/enterprise ontology work
**Purpose:** Align the Zachman-derived Agent-Unit ontology, Environment primitive, ORG/FOAF/vCard/FIBO organization stack, legacy SOA modernization pattern, evidence-and-time spine, and Seven-Model Stack with ProCybernetica's cybernetic governance doctrine.

---

## 1. Thesis

The Cybernetic Governance Fabric needs an enterprise-ontology layer that can answer not only whether an agent action is lawful, traceable, and evidence-bearing, but also where that action sits in an enterprise, organization, economy, environment, and review context.

The Zachman-derived Agent-Unit model supplies that upper ontology.

The six interrogatives become orthogonal primitives:

- `What` -> Artifact;
- `How` -> Capability;
- `Where` -> Locale;
- `Who` -> Principal;
- `When` -> Event;
- `Why` -> Motive.

The environment extension adds:

- `Environment` -> exogenous regime, hazard, quota, norm, and signal field;
- `Aperture` -> explicit boundary contract between an AgentUnit and its Environment;
- `RegimeModel` -> mapping from signals to environment state with uncertainty.

The suprarow `Omega` captures the enterprise as one AgentUnit inside a larger ecosystem of markets, regulators, infrastructure, communities, standards bodies, vendors, adversaries, and physical constraints.

This turns governance from a hermetic internal-control system into a field-aware cybernetic system.

---

## 2. Alignment to the Cybernetic Governance Fabric

| Zachman / AU concept | Cybernetic Governance concept | Role in ProCybernetica |
|---|---|---|
| Artifact | Evidence object / state delta | What changed or is being governed |
| Capability | Governed action / tool grant / runtime operation | How change is performed |
| Locale | Runtime boundary / trust zone / transport channel | Where action occurs or propagates |
| Principal | Authority chain / role / signer / accountability subject | Who can act or is accountable |
| Event | Action trace / monitor alert / receipt / transition | When action and evidence occur |
| Motive | Policy, objective, constraint, proof-pack disposition | Why action is permitted or required |
| Environment | Regime, hazard, norm, quota, external shock | Exogenous field conditioning the action |
| Aperture | Environment boundary contract | How environment affects AU behavior |
| RegimeModel | Environment inference artifact | How regime changes are detected |
| Omega row | Ecosystem view | How the enterprise is situated in supra-enterprise governance |

The atomic proof tuple becomes:

`<Principal, Capability, ArtifactDelta, Locale, Event, Motive, Environment>`

This is compatible with the Cybernetic Governance Fabric's action trace, evidence receipt, authority chain, release-delta report, off-history evidence, safety case, proof pack, and AgentPlane run capsule.

---

## 3. AgentUnit as the assembly unit

An `AgentUnit` is the canonical enterprise/agent assembly object.

It must bind:

- `hasPrincipal` — Who is authorized/accountable;
- `pursues` — Why it exists and what constraints bind it;
- `offersCapability` — How it acts;
- `maintains` — What state or artifacts it owns;
- `operatesAt` — Where it runs or connects;
- `schedules` — When it acts or is reviewed;
- `aperture` — which Environment it observes, commits to, and is constrained by;
- `governedBy` — policy and safety-case bundle;
- `observes` — telemetry and evidence channels.

This maps directly to AgentPlane:

| AgentUnit element | AgentPlane binding |
|---|---|
| AgentUnit identity | run capsule `agent_id` |
| Capability | tool grant / action dispatch |
| Principal | authority chain / signer / operator |
| Artifact state | action trace / environment delta |
| Event | run event / evidence receipt |
| Motive | policy / objective / safe-completion decision |
| Environment | aperture event / regime condition |

---

## 4. Environment primitive and Aperture contracts

Every AgentUnit must declare at least one Aperture, or it falsely represents itself as sealed from the world.

An Aperture records observables, commitments, exposures, controls, quotas, jurisdictions, regime model, environment signals, and signed aperture events.

Environment-conditioned governance requires every material capability to define:

- `preconditions_E`;
- `effects_E`;
- `fallbacks_E`;
- `regimeApplicability`.

A regime switch is not mere telemetry. It is a governance event that can affect permission scope, autonomy tier, release gates, and proof-pack disposition.

---

## 5. ORG / FOAF / vCard / FIBO alignment

ORG/FOAF/vCard provide the institutional grammar for Who and Where.

FIBO-style legal/business semantics provide formal legal identity, organization, identifier, role, jurisdiction, contract, and economic classification rigor.

Core mapping:

| External ontology term | AU primitive | ProCybernetica use |
|---|---|---|
| `org:Organization` | Principal | accountable organization |
| `org:FormalOrganization` | Principal | legal entity with formal identifier |
| `org:OrganizationalUnit` | Principal | internal authority/control boundary |
| `foaf:Agent` | Principal | person, organization, or software actor |
| `org:Membership` | Who-to-Who relation | role-bearing association |
| `org:Role` | Principal/Capability binding | authority and duty scope |
| `org:Post` | Capability carrier | position that binds role to unit |
| `org:Site` + `vcard:Address` | Locale | jurisdiction, placement, hazard exposure |
| `org:ChangeEvent` | Event / PROV Activity | time-stamped organizational transition |
| `org:identifier` | Artifact identifier | LEI, DUNS, EIN, VAT, CAGE, ABN, etc. |
| `org:classification` | Motive/Artifact code | NAICS, ISIC, NACE, sector obligations |

Required namespace family:

- ORG;
- FOAF;
- vCard;
- PROV-O;
- TIME;
- GeoSPARQL;
- DCAT;
- SKOS;
- LCC;
- ODRL;
- GoodRelations;
- schema.org;
- FIBO modules where applicable;
- EnRM, CGRM, PRM, SRM, DRM, TRM.

---

## 6. Seven-Model Stack alignment

The Seven-Model Stack names the planes that the AU ontology must cover.

| Seven-Model plane | AU primitive focus | Governance role |
|---|---|---|
| EnRM | Environment + Aperture | regime, hazard, quota, norm, exogenous shock |
| CGRM | Motive + Principal | rights, obligations, sanctions, communities |
| PRM+ | Event + Artifact | performance targets and observations |
| BRM+ | Principal + Motive | value network and business outcomes |
| SRM+ | Capability + Locale | services, interfaces, SLAs, responsibilities |
| DRM+ | Artifact | data, lineage, consent, provenance |
| TRM+ | Event + Artifact | technical attestation, supply chain, runtime proof |

This should drive the canonical event envelope and proof-pack evidence lanes.

---

## 7. Canonical event spine alignment

Every action, lifecycle transition, runtime decision, and customer outcome should share a time-normalized evidence envelope.

Required event-spine fields should include event identity, dual time, calendar keys, party/account/device/session placement, channel/system/line-of-business, release/requirement/test/defect/model/dataset/certificate identifiers, network and agent markers, service ID, policy IDs, attestation ID, lineage ID, performance ID, environment regime ID, community ID, and attributes.

This event spine aligns with:

- `agent_action_trace.v1.json`;
- `evidence_receipt.v1.json`;
- `release_delta_report.v1.json`;
- `artifact_provenance.v1.json`;
- `proof_pack_manifest.v1.json`;
- AgentPlane run capsules;
- SourceOS local-first state evidence.

---

## 8. Legacy SOA modernization alignment

The legacy SOA stack should not be discarded. It should be agentized.

Preserve SPARQL access, OPC UA semantics, KPI authoring/runtime, event correlation, model access, and industrial adapters.

Modernize by replacing the ESB chokepoint with event fabric and attestation bus; wrapping adapters as AgentUnits; converting services into Capabilities with preconditions, effects, policies, evidence, and environment fallbacks; promoting ModelStore into a knowledge graph with PROV/ORG/FIBO/DRM/PRM semantics; binding Sites and Locales to Environment via Aperture; and making KPI results attested, replayable, and proof-pack-ready.

Canonical agentized exemplars:

- OPC Ingest AU;
- ModelServices AU;
- KPI/Objective AU;
- Release Control AU;
- Governance Evidence AU.

---

## 9. Relationship to proof packs

The SocioProphet Proof Pack should become the reviewer-facing surface over this ontology.

Proof packs should cite product efficacy evidence from PRM observations; governance/control evidence from ProCybernetica receipts and safety cases; delivery/adoption evidence from event-spine and lifecycle records; market proof from ORG/FIBO/GoodRelations/schema.org records; environment/regime evidence from Aperture events; and AgentPlane run capsules and operator readouts.

This prevents proof packs from becoming slideware. Every proof-pack claim should point to typed event, artifact, organization, service, environment, or attestation evidence.

---

## 10. Schema targets

Add after the core Tier 1 governance schemas stabilize:

- `agent_unit.v1.json`
- `agent_unit_bundle_manifest.v1.json`
- `environment.v1.json`
- `aperture.v1.json`
- `regime_model.v1.json`
- `aperture_event.v1.json`
- `enterprise_event_envelope.v1.json`
- `organization_identity_profile.v1.json`
- `site_locale_profile.v1.json`
- `service_capability_profile.v1.json`
- `dataset_lineage_profile.v1.json`
- `performance_observation_profile.v1.json`
- `technical_attestation_profile.v1.json`
- `seven_model_alignment_profile.v1.json`

These should reference, not replace:

- `authority_chain.v1.json`;
- `agent_action_trace.v1.json`;
- `tool_permission_scope.v1.json`;
- `evidence_receipt.v1.json`;
- `artifact_provenance.v1.json`;
- `cybernetic_safety_case.v1.json`;
- `proof_pack_manifest.v1.json`;
- `agentplane_run_capsule.v1.json`.

---

## 11. Validation targets

Validation should include:

- every AgentUnit has all six bundles plus at least one Aperture;
- every Capability declares environment preconditions/effects/fallbacks;
- every Site/Locale has jurisdiction and environment exposure;
- every runtime action emits the seven-field proof tuple;
- every Service references interface, SLA target, legal basis, and attestation;
- every Dataset/Model resolves to lineage and provenance;
- every performance observation records sample size and method;
- every proof-pack claim references lower-level evidence;
- every environment regime switch emits an Aperture Event.

---

## 12. Repo placement

ProCybernetica owns ontology alignment doctrine, schemas, validation rules, proof-pack connection, governance contracts, and assurance posture.

Prophet Platform consumes event-spine and service/capability profiles for runtime, eval fabric, dashboards, evidence APIs, and proof-pack production.

SocioSphere indexes AgentUnit, organization, service, dependency, safety-case, and workspace registry metadata.

AgentPlane consumes AgentUnit capability, tool grants, run capsules, action dispatch, environment-conditioned fallbacks, and operator readout contracts.

SourceOS provides local-first persistence, sync, provenance, replay, and state-integrity substrate for event spine and Aperture events.

---

## 13. Non-claims

This document does not implement the full AU, ORG/FIBO, Environment, Seven-Model, or SOA-modernization schema set.

It does not claim that Zachman, ORG, FIBO, Seven-Model, and SOA concepts are identical.

It does not require every proof pack to contain every possible evidence exhibit.

It establishes the alignment path and schema roadmap so later implementation can be typed, evidence-backed, and reviewable.
