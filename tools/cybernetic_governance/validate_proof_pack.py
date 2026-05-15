#!/usr/bin/env python3
"""Validate SocioProphet proof-pack fixtures.

This validator is repository-local and public-synthetic. It validates proof-pack
schema shape plus the cross-field review rules that JSON Schema alone cannot
express. It does not turn proof packs into raw evidence stores and does not
adjudicate live production or regulated-readiness claims.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "assurance"
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "proof-pack" / "proof-pack-fixtures.synthetic.json"

SCHEMA_FILES = [
    "proof_pack_manifest.v1.json",
    "proof_pack_artifact_entry.v1.json",
    "proof_pack_evidence_lane.v1.json",
    "proof_pack_disposition.v1.json",
    "proof_pack_scorecard.v1.json",
    "proof_pack_redaction_status.v1.json",
    "proof_pack_claim_discipline.v1.json",
]

EXPECTED_FAILURE_REASONS = {
    "schema_validation_error",
    "claim_level_requires_evidence_backing",
    "artifact_entry_requires_governed_evidence_ref",
}

GOVERNED_EVIDENCE_KINDS = {
    "evidence_receipt",
    "release_delta_report",
    "cybernetic_safety_case",
    "artifact_provenance",
    "agentplane_proof_pack_exhibit",
    "agentplane_run_capsule",
    "operator_readout",
    "bridge_record",
    "certificate",
    "evaluation_result",
}

PRODUCTION_OR_REGULATED_CLAIMS = {"production_parity", "regulated_readiness"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def schema_errors(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(payload), key=str)]


def artifact_entry_failures(payload: dict[str, Any]) -> list[str]:
    evidence_kinds = {entry.get("evidence_kind") for entry in payload.get("evidence_refs", [])}
    if evidence_kinds.isdisjoint(GOVERNED_EVIDENCE_KINDS):
        return ["artifact_entry_requires_governed_evidence_ref"]
    return []


def claim_discipline_failures(payload: dict[str, Any]) -> list[str]:
    claimed_level = payload.get("claimed_level")
    evidence_level = payload.get("evidence_level_proven")
    verdict = payload.get("verdict")

    if claimed_level == "regulated_readiness":
        if evidence_level != "regulated" or verdict == "supported":
            return ["claim_level_requires_evidence_backing"]

    if claimed_level == "production_parity":
        if evidence_level not in {"production", "regulated"} or verdict == "supported":
            return ["claim_level_requires_evidence_backing"]

    if claimed_level in PRODUCTION_OR_REGULATED_CLAIMS and evidence_level in {"none", "synthetic", "pilot"}:
        return ["claim_level_requires_evidence_backing"]

    return []


def custom_failures(target_schema: str, payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if target_schema == "proof_pack_artifact_entry.v1.json":
        failures.extend(artifact_entry_failures(payload))
    if target_schema == "proof_pack_claim_discipline.v1.json":
        failures.extend(claim_discipline_failures(payload))
    return failures


def validate_fixture_set(path: Path) -> dict[str, Any]:
    schemas = load_schemas()
    fixture_set = load_json(path)
    results: list[dict[str, Any]] = []
    overall_pass = True

    for fixture in fixture_set.get("fixtures", []):
        fixture_id = fixture.get("fixture_id", "<missing>")
        target_schema = fixture.get("target_schema")
        expected_result = fixture.get("expected_result")
        expected_failure_reason = fixture.get("expected_failure_reason")
        payload = fixture.get("payload", {})
        diagnostics: list[str] = []
        observed_failures: list[str] = []

        if target_schema not in schemas:
            diagnostics.append(f"unknown target schema: {target_schema}")
            observed_failures.append("schema_validation_error")
        else:
            messages = schema_errors(schemas[target_schema], payload)
            if messages:
                diagnostics.extend(messages)
                observed_failures.append("schema_validation_error")
            observed_failures.extend(custom_failures(str(target_schema), payload))

        observed_failures = sorted(set(observed_failures))
        actual_result = "fail" if observed_failures else "pass"
        passed = actual_result == expected_result

        if expected_result == "fail":
            if expected_failure_reason not in EXPECTED_FAILURE_REASONS:
                passed = False
                diagnostics.append(f"unknown or missing expected_failure_reason: {expected_failure_reason}")
            elif expected_failure_reason not in observed_failures:
                passed = False
                diagnostics.append(
                    f"expected failure reason {expected_failure_reason!r} not observed; observed {observed_failures}"
                )

        if expected_result == "pass" and observed_failures:
            diagnostics.append(f"unexpected failures: {observed_failures}")

        overall_pass = overall_pass and passed
        results.append(
            {
                "fixture_id": fixture_id,
                "target_schema": target_schema,
                "expected_result": expected_result,
                "actual_result": actual_result,
                "expected_failure_reason": expected_failure_reason,
                "observed_failures": observed_failures,
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    return {
        "validator": "proof_pack.validator.v1",
        "fixture_file": str(path.relative_to(ROOT)),
        "passed": overall_pass,
        "fixture_count": len(fixture_set.get("fixtures", [])),
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", nargs="?", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    result = validate_fixture_set(args.fixture)
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: proof-pack fixtures")
        else:
            print("FAIL: proof-pack fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
