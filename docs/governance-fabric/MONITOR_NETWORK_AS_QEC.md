# Monitor Network as Error-Correcting Code

## Purpose

This document defines the monitor-network doctrine for Cybernetic Governance Fabric.

The claim is structural: distributed monitor networks should be designed like error-correcting systems over behavioral observations.

## Structural mapping

| Error-correction concept | Governance analogue |
|---|---|
| Logical state | Canonical agent/system state |
| Physical qubits | Individual monitors / evidence sources |
| Stabilizer measurement | Monitor query |
| Syndrome | Pattern of monitor alerts |
| Decoder | Meta-monitor interpreting alerts |
| Code distance | Minimum monitor compromises needed for silent failure |
| Fault tolerance | Ability to preserve correct governance state under monitor failures |

## Monitor types

### Authority monitor

Observes authority-chain violations, hidden authority lanes, and delegation anomalies.

### Runtime monitor

Observes tool execution, sandbox boundary, irreversible actions, and trace completeness.

### Policy monitor

Observes policy conformance and policy conflict.

### Privacy monitor

Observes overcollection, data exposure, redaction failure, and evidence minimization violations.

### Evidence monitor

Observes receipt integrity, missing hashes, source-lock drift, and ledger anomalies.

### Release monitor

Observes release-delta risk and rollback state.

### Publication monitor

Observes public-claim non-claim boundaries and evidence readiness.

### Meta-monitor

Observes monitors themselves.

## Stabilizer monitor

A stabilizer monitor checks a property that should remain invariant across governed execution.

Examples:

- every governed action has a trace;
- every promotion references evidence;
- every emergency action has a bounded scope;
- every irreversible action references approval;
- every public claim references a certificate or evidence bundle.

## Syndrome decoder

The syndrome decoder maps alert patterns into likely governance faults.

Example:

```text
missing trace + emergency label + no after-action review
  -> emergency authority normalization risk
```

The decoder must be separately governed. A captured decoder can neutralize the monitor network.

## Code distance

Monitor-network code distance is the minimum number of monitor failures or compromises required to silently corrupt the inferred governance state.

A code-distance-1 governance system is one monitor failure away from silent compromise.

The Tier 1 target is to measure code distance qualitatively. The Tier 2/3 target is to compute it from monitor coverage graphs.

## Collusion attacks

Correlated monitor failure is the main hard case.

The fabric must model:

- shared dependencies;
- shared authority owners;
- shared logging infrastructure;
- shared model judgments;
- shared blind spots.

QEC-style thinking helps because correlated errors require different codes than independent errors.

## Runtime boundary

This doctrine does not implement a decoder. It defines the monitor-network model that later schemas and metrics will implement.
