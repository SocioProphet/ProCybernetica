#!/usr/bin/env python3
"""Validate reciprocal channel governance schema fixtures.

This validator is repository-local. It validates public-synthetic schema
records and checks cross-record semantic constraints for reciprocal channel
governance. It does not implement runtime sensing, memory, graph, action, or
agent services.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "cybernetic-governance"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "reciprocal-channel-governance" / "rcg-schema-records.synthetic.json"

SCHEMA_FILES = [
    "channel_authority_envelope.v1.json",
    "channel_observation.v1.json",
    "interpretant_candidate.v1.json",
    "repair_event.v1.json",
    "collapse_decision.v1.json",
]

HIGH_RISK_SINKS = {"confirmed_memory", "graph_edge", "claim_promotion", "policy_binding", "high_risk_action", "publish", "delete", "authorize_agent"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_schemas() -> dict[str, dict[str, Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    for name in SCHEMA_FILES:
        schema = load_json(SCHEMA_DIR / name)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
    return schemas


def validate_payload(schema: dict[str, Any], payload: dict[str, Any]) -> list[str]:
    errors = sorted(Draft202012Validator(schema).iter_errors(payload), key=lambda error: list(error.absolute_path))
    return [f"/{'/'.join(str(part) for part in error.absolute_path)}: {error.message}" for error in errors]


def schema_record_results(schemas: dict[str, dict[str, Any]], fixture: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for record in fixture["records"]:
        schema = schemas[record["target_schema"]]
        diagnostics = validate_payload(schema, record["payload"])
        actual_result = "fail" if diagnostics else "pass"
        results.append(
            {
                "fixture_id": record["fixture_id"],
                "target_schema": record["target_schema"],
                "expected_result": record["expected_result"],
                "actual_result": actual_result,
                "passed": actual_result == record["expected_result"],
                "diagnostics": diagnostics,
            }
        )
    return results


def passing_payloads_by_schema(fixture: dict[str, Any], schema_name: str) -> list[dict[str, Any]]:
    return [
        record["payload"]
        for record in fixture["records"]
        if record["target_schema"] == schema_name and record["expected_result"] == "pass"
    ]


def semantic_results(fixture: dict[str, Any]) -> list[dict[str, Any]]:
    envelopes = {payload["envelope_id"]: payload for payload in passing_payloads_by_schema(fixture, "channel_authority_envelope.v1.json")}
    observations = {payload["observation_id"]: payload for payload in passing_payloads_by_schema(fixture, "channel_observation.v1.json")}
    interpretants = {payload["interpretant_id"]: payload for payload in passing_payloads_by_schema(fixture, "interpretant_candidate.v1.json")}
    repairs = {payload["repair_id"]: payload for payload in passing_payloads_by_schema(fixture, "repair_event.v1.json")}
    collapses = passing_payloads_by_schema(fixture, "collapse_decision.v1.json")

    checks: list[dict[str, Any]] = []

    for observation_id, observation in observations.items():
        envelope_ref = observation["authority_envelope_ref"]
        checks.append(
            {
                "check_id": f"observation-authority-resolves:{observation_id}",
                "passed": envelope_ref in envelopes,
                "diagnostics": [] if envelope_ref in envelopes else [f"missing authority envelope {envelope_ref}"],
            }
        )

    for interpretant_id, interpretant in interpretants.items():
        observation_ref = interpretant["observation_ref"]
        checks.append(
            {
                "check_id": f"interpretant-observation-resolves:{interpretant_id}",
                "passed": observation_ref in observations,
                "diagnostics": [] if observation_ref in observations else [f"missing observation {observation_ref}"],
            }
        )

    for repair_id, repair in repairs.items():
        observation_ref = repair["observation_ref"]
        checks.append(
            {
                "check_id": f"repair-observation-resolves:{repair_id}",
                "passed": observation_ref in observations,
                "diagnostics": [] if observation_ref in observations else [f"missing observation {observation_ref}"],
            }
        )

    for collapse in collapses:
        collapse_id = collapse["collapse_id"]
        source_ok = collapse["source_observation_ref"] in observations
        candidate_missing = [ref for ref in collapse["candidate_interpretants"] if ref not in interpretants]
        selected_ok = collapse["selected_interpretant_ref"] in collapse["candidate_interpretants"]
        envelope = envelopes.get(collapse["authority_envelope_ref"])
        envelope_ok = envelope is not None
        sink = collapse["downstream_sink"]
        allowed_ok = envelope_ok and sink in envelope["allowed_sinks"]
        repair_missing = [ref for ref in collapse.get("repair_event_refs", []) if ref not in repairs]
        high_risk_without_repair = sink in HIGH_RISK_SINKS and not collapse.get("repair_event_refs")
        passed = source_ok and not candidate_missing and selected_ok and envelope_ok and allowed_ok and not repair_missing and not high_risk_without_repair
        diagnostics = []
        if not source_ok:
            diagnostics.append(f"missing source observation {collapse['source_observation_ref']}")
        diagnostics.extend(f"missing candidate interpretant {ref}" for ref in candidate_missing)
        if not selected_ok:
            diagnostics.append("selected interpretant is not present in candidate_interpretants")
        if not envelope_ok:
            diagnostics.append(f"missing authority envelope {collapse['authority_envelope_ref']}")
        elif not allowed_ok:
            diagnostics.append(f"sink {sink} is not allowed by authority envelope {collapse['authority_envelope_ref']}")
        diagnostics.extend(f"missing repair event {ref}" for ref in repair_missing)
        if high_risk_without_repair:
            diagnostics.append(f"high-risk sink {sink} requires at least one repair event")
        checks.append(
            {
                "check_id": f"collapse-semantics:{collapse_id}",
                "passed": passed,
                "diagnostics": diagnostics,
            }
        )

    return checks


def validate() -> dict[str, Any]:
    schemas = load_schemas()
    fixture = load_json(FIXTURE_PATH)
    schema_results = schema_record_results(schemas, fixture)
    semantic = semantic_results(fixture)
    expected_schema_coverage = {record["target_schema"] for record in fixture["records"]}
    all_results = schema_results + semantic
    passed = expected_schema_coverage == set(SCHEMA_FILES) and all(result.get("passed") for result in all_results)
    return {
        "validator": "reciprocal_channel_governance.validator.v1",
        "passed": passed,
        "schema_record_count": len(schema_results),
        "semantic_check_count": len(semantic),
        "schema_coverage": sorted(expected_schema_coverage),
        "results": all_results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: reciprocal channel governance schema fixtures")
        else:
            print("FAIL: reciprocal channel governance schema fixtures", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
