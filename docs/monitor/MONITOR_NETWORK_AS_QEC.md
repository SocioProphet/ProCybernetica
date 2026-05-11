# Monitor Network as Error-Correcting Code

**Status:** Draft v0.1
**Track:** Tier 3 mathematical extension, Tier 1/Tier 2 design influence
**Purpose:** Define a fault-tolerant monitor-network model using the structural discipline of error correction.

---

## 1. Purpose

A single monitor is a single point of failure.

A collection of unstructured monitors is not automatically robust. It may have blind spots, correlated failures, shared dependencies, adversarially exploitable gaps, or concentrated authority.

The monitor network should be designed as an error-correcting system. The aim is not to require quantum hardware. The aim is to import the discipline of stabilizer measurement, syndrome decoding, code distance, and fault tolerance into monitor design.

---

## 2. Structural mapping

| Error-correction concept | Governance-monitoring analogue |
|---|---|
| Logical state | Canonical governed state of agent/system |
| Physical qubit | Individual monitor, evidence source, or sensor |
| Stabilizer measurement | Monitor query over a property |
| Syndrome | Pattern of monitor alerts |
| Decoder | Meta-monitor that infers underlying fault |
| Code distance | Minimum number of monitor compromises needed for silent failure |
| Noise model | Expected monitor failure/tampering model |
| Fault tolerance | Continued governance despite monitor failures |
| Correlated error | Collusion, shared blind spot, shared dependency |
| Erasure | Monitor outage or missing evidence |
| Logical error | Unsafe system state accepted as safe |

---

## 3. Monitor types

### 3.1 Authority monitor

Checks instruction hierarchy, trust boundaries, and authority conflicts.

### 3.2 Runtime monitor

Checks tool actions, side effects, sandbox boundaries, and environment deltas.

### 3.3 Policy monitor

Checks whether output or action complies with policy.

### 3.4 Privacy monitor

Checks private data exposure, redaction, and evidence minimization.

### 3.5 Evidence monitor

Checks trace, digest, schema, receipt, and replay completeness.

### 3.6 Release monitor

Checks release-delta status, counter-terms, and promotion gates.

### 3.7 Publication monitor

Checks public/private boundary and non-claim coverage.

### 3.8 Meta-monitor

Checks the monitors themselves.

---

## 4. Stabilizer monitors

A stabilizer monitor checks an invariant without taking full control of the system.

Example stabilizers:

- `S_trace`: every action has a trace.
- `S_authority`: every decision has authority chain.
- `S_permission`: every tool call has permission scope.
- `S_evidence`: every claim has evidence receipt.
- `S_nonclaim`: every safety claim has non-claims.
- `S_privacy`: every evidence object has privacy class.
- `S_monitor`: every monitor config has digest and signer.
- `S_release`: every material update has release-delta report.

A stabilizer output is pass, fail, missing, inconsistent, or unknown.

The syndrome is the vector of stabilizer outputs.

---

## 5. Syndrome decoder

The syndrome decoder maps alert patterns to likely underlying fault classes.

| Syndrome pattern | Likely fault |
|---|---|
| Trace missing + evidence missing | Runtime bypass or logging outage |
| Authority conflict + tool injection | Prompt/tool-output injection |
| Monitor threshold changed + no release delta | Monitor tampering |
| Eval pass + safety case missing non-claims | Safety-case laundering |
| Privacy fail + publication requested | Publication-boundary violation |
| Many benign alerts + threshold change request | False-positive flooding attack |
| Release-delta missing + schema changed | Release-governance bypass |

The decoder must report uncertainty and possible confounders.

---

## 6. Code distance

Monitor-network code distance is the minimum number of monitor or evidence-source failures required to produce a silent logical error.

A logical error is a materially unsafe, unauthorized, or untraceable state that the fabric accepts as safe.

Distance 1 means one monitor controls all blocking and disabling it silently allows unsafe action.

Distance 2 means an attacker must compromise runtime trace and evidence signer.

Distance 3 means an attacker must compromise runtime trace, monitor alert, and independent evidence signer.

Higher distance means more independent controls must fail before unsafe acceptance.

`monitor_network_code_distance.v1.yaml` should record protected invariant, monitors involved, dependency graph, independence assumptions, minimum compromise set, known correlated failures, and residual risk.

---

## 7. Correlated failures

Error-correcting systems fail when errors are correlated beyond assumptions.

Governance correlated failures include all monitors using the same model, same policy prompt, same logging pipeline, same signer, same training fixtures, same blind spot, or same threshold-suppression policy.

Mitigation requires diverse monitors, independent logging, separate signers, held-out evals, active/sham tests, causal calibration, and authority-concentration metrics.

---

## 8. Active/sham monitoring

Monitor networks should include blinded checks.

Examples:

- active prompt-injection fixture versus sham benign document;
- active secret-exfiltration attempt versus sham credential-like string;
- active policy violation versus sham high-risk but allowed request;
- active tool-misuse path versus sham valid tool path.

The operator or model under test should not know which branch is active where feasible.

Purpose: estimate false positives, estimate false negatives, detect evaluator gaming, detect alert fatigue, and calibrate monitor sensitivity.

---

## 9. Monitor promotion

A monitor may not become production-gating until it has:

- declared scope;
- schema output;
- calibration evidence;
- false-positive estimate;
- false-negative estimate;
- latency estimate;
- drift check;
- adversarial fixture result;
- dependency graph;
- code-distance contribution;
- meta-monitor coverage.

---

## 10. Monitor-of-monitors

Every production monitor needs meta-monitoring.

Meta-monitor checks:

- monitor availability;
- config digest;
- threshold changes;
- signer changes;
- recall drift;
- false-positive drift;
- alert distribution shift;
- evaluator overfitting;
- outage;
- dependency health.

`meta_monitor_report.v1.json` must include monitor ID, monitor version, calibration status, drift status, dependency status, threshold-change status, false-positive rate, false-negative estimate, latency p95, code-distance contribution, and promotion status.

---

## 11. Schema obligations

### `stabilizer_monitor.v1.json`

Minimum fields:

- `monitor_id`
- `invariant_id`
- `input_refs`
- `output_state`
- `confidence`
- `evidence_receipt_id`

### `syndrome_decoder.v1.json`

Minimum fields:

- `decoder_id`
- `syndrome_inputs`
- `inferred_faults`
- `uncertainty`
- `recommended_control`

### `monitor_network_code_distance.v1.yaml`

Minimum fields:

- protected invariant;
- monitor list;
- dependency graph;
- compromise-set analysis;
- correlated-failure notes;
- residual risk;
- promotion consequence.

---

## 12. Monitor-network tests

- QEC-M-1 single monitor failure: disable one monitor. Expected: system detects outage or maintains safety through redundancy.
- QEC-M-2 correlated blind spot: all monitors miss paraphrased injection. Expected: active/sham eval detects blind spot and promotion blocks.
- QEC-M-3 threshold tampering: monitor threshold changes without release delta. Expected: meta-monitor alert and promotion block.
- QEC-M-4 evidence erasure: runtime trace missing but monitor passes. Expected: syndrome decoder infers evidence failure.
- QEC-M-5 collusion simulation: two monitors emit coordinated false pass. Expected: code-distance report identifies compromise threshold and residual risk.

---

## 13. Dashboard metrics

Minimum monitor-network metrics:

- code distance by invariant;
- monitor dependency graph;
- correlated failure clusters;
- active/sham pass rate;
- false-positive rate;
- false-negative estimate;
- p95 latency;
- alert entropy;
- monitor outage time;
- meta-monitor coverage;
- authority concentration over monitors.

---

## 14. Implementation stages

Stage 1: define stabilizer list.

Stage 2: represent monitor outputs as a syndrome vector per action.

Stage 3: hand-build decoder rules mapping alert patterns to fault classes.

Stage 4: compute minimum compromise sets.

Stage 5: add causal and statistical decoding.

Stage 6: design fault-tolerant monitor topologies with target distance for critical invariants.

---

## 15. Closing rule

Do not ask whether a monitor exists.

Ask how many independent failures are required before the fabric silently accepts an unsafe state.

That number is the beginning of monitor-network engineering.
