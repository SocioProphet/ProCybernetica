#!/usr/bin/env python3
"""Validate the Governed Closed-Loop Control Contract (control-loop.schema.json).

This validator is repository-local, deterministic, and side-effect free. It certifies
whether a proposed ControlLoop record is CONSTITUTIONALLY ADMISSIBLE. It does NOT run
any remediation, dispatch any actuator, or emit production telemetry — a ControlLoop
record is a measurement/design artifact.

Teeth (both directions), seated under ControlNodes #124 / RCS ADR-0003 / Crown K1:
  * a loop with NO ValueJudgment gate is REJECTED           (no ungoverned autonomy)
  * a fired remediation with NO audit_receipt is REJECTED   (invariant_0_2 no action without trace)
  * a control-max / domination objective is REJECTED        (Crown/Telos K1, hellgraph#52)
  * a remediation that FIRED while the judge DENIED is REJECTED (separation of powers, 0_5)
  * a remediation that FIRED without its sensor signal crossing
    threshold is REJECTED                                   (no spurious action)
  * a loop that closes sense->model->judge->act->receipt with a
    coherent, bounded objective and a crossed threshold VERIFIES.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "contracts" / "control-loop.schema.json"
ENUMS_PATH = ROOT / "schemas" / "cybernetic-governance" / "enums.v1.json"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "control-loop"
EXPECTATIONS_PATH = FIXTURE_DIR / "expectations.json"

# Objectives that assert control-maximisation / domination are inadmissible (Crown K1).
UNCONSTITUTIONAL_OBJECTIVES = {"control-max", "domination", "unbounded-optimization"}

# Reason codes are stable identifiers so tests (and reviewers) can assert on WHY, not prose.
R_SCHEMA_INVALID = "SCHEMA_INVALID"
R_NO_VALUE_JUDGMENT_GATE = "NO_VALUE_JUDGMENT_GATE"
R_NO_AUDIT_RECEIPT_ON_FIRED = "NO_AUDIT_RECEIPT_ON_FIRED"
R_UNCONSTITUTIONAL_OBJECTIVE = "UNCONSTITUTIONAL_OBJECTIVE_CROWN_K1"
R_JUDGE_DENIED_BUT_FIRED = "JUDGE_DENIED_BUT_FIRED"
R_SPURIOUS_ACTION = "SPURIOUS_ACTION_NO_THRESHOLD_CROSS"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_validator() -> Draft202012Validator:
    """Build an offline validator with enums.v1.json served from disk (no network).

    The contract references the constitutional-invariant enum by enums.v1.json's own
    absolute $id; we register that resource so the $ref resolves locally.
    """
    schema = load_json(SCHEMA_PATH)
    enums = load_json(ENUMS_PATH)
    registry = Registry().with_resources(
        [
            (enums["$id"], Resource.from_contents(enums)),
            (schema["$id"], Resource.from_contents(schema)),
        ]
    )
    return Draft202012Validator(schema, registry=registry)


def _crosses_threshold(observed: float, comparator: str, value: float) -> bool:
    return {
        "gt": observed > value,
        "gte": observed >= value,
        "lt": observed < value,
        "lte": observed <= value,
        "ne": observed != value,
    }[comparator]


def evaluate_control_loop(record: Any, validator: Draft202012Validator | None = None) -> dict:
    """Return {'admissible': bool, 'reasons': [reason_code, ...]}.

    Deterministic and pure. Structural failures (schema) short-circuit to a single
    reason so the verdict is stable regardless of jsonschema's error ordering.
    """
    validator = validator or _schema_validator()
    reasons: list[str] = []

    if not isinstance(record, dict):
        return {"admissible": False, "reasons": [R_SCHEMA_INVALID]}

    # Structural tooth first: no ValueJudgment gate at all -> no ungoverned autonomy.
    if "value_judgment" not in record:
        return {"admissible": False, "reasons": [R_NO_VALUE_JUDGMENT_GATE]}

    if list(validator.iter_errors(record)):
        return {"admissible": False, "reasons": [R_SCHEMA_INVALID]}

    # Crown K1: a control-max / domination objective is inadmissible, fired or not.
    if record["objective"]["objective_kind"] in UNCONSTITUTIONAL_OBJECTIVES:
        reasons.append(R_UNCONSTITUTIONAL_OBJECTIVE)

    actuator = record["actuator"]
    fired = bool(actuator["fired"])
    if fired:
        # No action without trace.
        if record.get("audit_receipt") in (None, {}):
            reasons.append(R_NO_AUDIT_RECEIPT_ON_FIRED)
        # Separation of powers: the judge must have allowed the act.
        if record["value_judgment"]["gate_result"] != "allow":
            reasons.append(R_JUDGE_DENIED_BUT_FIRED)
        # No spurious action: the sensor signal must have crossed threshold.
        sensor = record["sensor"]
        observed = sensor.get("observed_value")
        thr = sensor["threshold"]
        if observed is not None and not _crosses_threshold(
            float(observed), thr["comparator"], float(thr["value"])
        ):
            reasons.append(R_SPURIOUS_ACTION)

    return {"admissible": len(reasons) == 0, "reasons": reasons}


def run() -> dict:
    """Evaluate every fixture against its declared expectation. Returns a JSON report."""
    validator = _schema_validator()
    expectations = load_json(EXPECTATIONS_PATH)
    checks: list[dict] = []
    for name, expect in sorted(expectations.items()):
        record = load_json(FIXTURE_DIR / name)
        verdict = evaluate_control_loop(record, validator)
        want_admissible = expect["verdict"] == "accept"
        want_reason = expect.get("reason")
        passed = verdict["admissible"] == want_admissible
        if want_reason is not None:
            passed = passed and (want_reason in verdict["reasons"])
        checks.append(
            {
                "fixture": name,
                "check_id": expect.get("check_id", name),
                "expected": expect["verdict"],
                "expected_reason": want_reason,
                "got_admissible": verdict["admissible"],
                "got_reasons": verdict["reasons"],
                "passed": passed,
            }
        )
    return {
        "validator": "validate_control_loop",
        "schema": str(SCHEMA_PATH.relative_to(ROOT)),
        "total": len(checks),
        "failed": [c for c in checks if not c["passed"]],
        "checks": checks,
        "ok": all(c["passed"] for c in checks),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the full JSON report")
    args = parser.parse_args(argv)
    report = run()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for c in report["checks"]:
            mark = "ok " if c["passed"] else "FAIL"
            print(f"{mark} {c['check_id']}: expected={c['expected']} reasons={c['got_reasons']}")
        print(f"{report['total'] - len(report['failed'])}/{report['total']} teeth held")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
