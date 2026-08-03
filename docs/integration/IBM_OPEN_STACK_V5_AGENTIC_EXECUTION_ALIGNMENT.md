# IBM open-stack v5 "agentic execution" — Agent Ontology alignment

Integrates the IBM open-stack **v5** "agentic execution" model into the estate Agent
Ontology, per **prophet-workspace#108 (item 4)**. Consume-not-fork: the contract does
not restate the ontology — it **binds** the v5 vocabulary to already-owned estate types.

## Source (reference only; not vendored)

- Workbook: `ibm_open_stack_inventory_v5_agentic_execution_remounted.xlsx`
- SHA-256 (FIPS-180-4): `d538d74099e4953eb2c41086aae80d59813e3fa9bc41ada08d42585b8385c056`
- Sheets consumed: **Execution_Class_Legend** (the 7 execution classes),
  **Semantic_SubLayer_Map** (the 4 semantic sub-layers), **Agentic_Execution_Model**
  (per-plane primary/secondary class, autonomy, risk tier — provenance for the fixture).
- The **v4** workbook (`..._v4_protocol_trust_alignment_...`) is the protocol/trust-primitive
  predecessor and is **out of scope here** (kept as the trust-primitive reference per #108).

## What the contract binds

`schemas/agentic_execution_class.schema.json` (registry `AgenticExecutionClassRegistry`).
Each binding maps one v5 execution class to estate types already owned elsewhere:

| v5 concept | estate type it binds to | source of truth |
|---|---|---|
| Execution class (7) | `execution_class` closed enum | v5 Execution_Class_Legend |
| Ontology node | `control_node_type` — 11 ProCybernetica ControlNode types | `schemas/control_node.schema.json` (ADR-0002 L2, **ProCybernetica#124**) |
| Host agent | `agent_class` — 5 AgentPassport classes | sourceos-spec `schemas/AgentPassport.json` (T0-1); OWL/SHACL in **ontogenesis#140** |
| Semantic sub-layer (4) | `semantic_sublayer` closed enum | v5 Semantic_SubLayer_Map |
| Semantic coordinate | `coordinate_axis` — 11 AgentCoordinateVector sefirotic axes | `contracts/AgentCoordinateVector.v0.1.json` |

`semantic_sublayer` + `coordinate_axis` are a **both-or-neither** block: a binding that
represents one of the four semantic sub-layers pins it to an estate coordinate axis.

The estate mapping shipped in the valid fixture
(`tests/fixtures/agentic-execution-class/estate-agentic-execution-classes.valid.json`)
covers all seven execution classes and all four semantic sub-layers, e.g.:

- `grounding_safe_read` → `Memory` / `Observability` / `WorldModel` (retrieval/metrics/graph),
  bound to the `retrieval_semantics→yesod`, `metrics_semantics→hod`, `graph_krr→daat` coordinates;
- `policy_audit_oversight` → `ValueJudgment` (system_core), `glossary_ontology→binah`;
- `tool_with_approval` → `Execution`; `inter_agent_coordination` → `Coordination`;
- `human_workflow_system` → `Lifecycle`; `acp_client_ide` → `Interfaces` (third_party).

## Teeth (both ways) — `tools/cybernetic_governance/validate_agentic_execution_class.py`

A binding onto a valid ontology node + a valid agent_class **VERIFIES**. Rejected:
unknown execution class (AEC-T1), an **undeclared ontology node** (AEC-T2), an **unknown
agent_class** e.g. `anySource` (AEC-T3), a **semantic sub-layer not in the map** (AEC-T4),
an unknown coordinate axis (AEC-T5), duplicate identity (AEC-T6), the same
(execution_class, agent_class, control_node_type) triple twice (AEC-T7), a dangling
semantic binding (AEC-T8).

**Consume-not-fork reconciliation.** The validator asserts the enums it vendors equal the
estate source-of-truth contracts, so this binding and the ontology cannot silently drift:
- `coordinate_axis` is reconciled against `contracts/AgentCoordinateVector.v0.1.json` (on main; always enforced);
- `control_node_type` is reconciled against `schemas/control_node.schema.json` **whenever it is
  present** — i.e. the guard tightens automatically once **ProCybernetica#124** lands on main, and
  falls back to the vendored canonical 11 (with provenance) before then, never crashing.

Run: `make agentic-execution-class-ci` (validator + `tests/test_agentic_execution_class.py`,
per-tooth mutation coverage). CI: `.github/workflows/agentic-execution-class.yml`.

## Out of scope / follow-up (@mdheller)

**Runtime execution routing per class** — dispatching a request to the right surface, selecting
the membrane gate to cross, and enforcing the autonomy posture per execution class — is not part
of this contract. It is filed as a follow-up. This PR delivers only the typed, reconciled binding.
