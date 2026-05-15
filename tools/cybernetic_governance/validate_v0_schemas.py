#!/usr/bin/env python3
"""Validate ProCybernetica v0 schema normalization.

This validator checks the canonical v0 JSON Schema family from ADR-0002 and
SCHEMA_PROFILE_RECONCILIATION. It validates structure, metadata, draft version,
additionalProperties posture, and expected fixture/test references. It does not
expand runtime implementation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"

CANONICAL_V0_SCHEMAS = [
    "node_descriptor.schema.json",
    "artifact_envelope.schema.json",
    "policy_envelope.schema.json",
    "command_envelope.schema.json",
    "delegation_envelope.schema.json",
    "observation_envelope.schema.json",
    "status_envelope.schema.json",
    "event_envelope.schema.json",
    "trace_event.schema.json",
    "transition_record.schema.json",
    "replay_envelope.schema.json",
    "evaluation_result.schema.json",
    "promotion_decision.schema.json",
    "incident_report.schema.json",
    "claim.schema.json",
    "provenance_record.schema.json",
    "capability_descriptor.schema.json",
]

# These schemas already have dedicated public-synthetic test coverage in the
# repository-local test suite. Some v0 schemas are documented as public contract
# surfaces without full fixture-specific tests yet; those are tracked by the
# status report rather than silently treated as absent.
EXPECTED_FIXTURE_BACKED_SCHEMAS = {
    "node_descriptor.schema.json",
    "artifact_envelope.schema.json",
    "policy_envelope.schema.json",
    "command_envelope.schema.json",
    "delegation_envelope.schema.json",
    "observation_envelope.schema.json",
    "status_envelope.schema.json",
    "event_envelope.schema.json",
    "trace_event.schema.json",
    "transition_record.schema.json",
    "replay_envelope.schema.json",
    "evaluation_result.schema.json",
    "promotion_decision.schema.json",
    "claim.schema.json",
    "provenance_record.schema.json",
    "capability_descriptor.schema.json",
}

DEFERRED_FIXTURE_SCHEMAS = {
    "incident_report.schema.json": "incident fixture coverage remains public-contract tracked; runtime incident semantics are not expanded in #6",
}

REQUIRED_METADATA_FIELDS = {"$schema", "$id", "title", "description", "type", "properties", "required", "additionalProperties"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing schema file: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from None


def validate_schema_file(schema_name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / schema_name
    diagnostics: list[str] = []
    if not path.exists():
        return {
            "schema": schema_name,
            "exists": False,
            "passed": False,
            "diagnostics": ["missing canonical v0 schema file"],
        }

    payload = load_json(path)
    try:
        Draft202012Validator.check_schema(payload)
    except Exception as exc:  # pragma: no cover - diagnostic path
        diagnostics.append(f"invalid JSON Schema: {exc}")

    missing_metadata = REQUIRED_METADATA_FIELDS - set(payload)
    if missing_metadata:
        diagnostics.append(f"missing metadata fields: {sorted(missing_metadata)}")

    if payload.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        diagnostics.append("$schema must be JSON Schema draft 2020-12")

    schema_id = payload.get("$id")
    if not isinstance(schema_id, str) or not schema_id:
        diagnostics.append("$id must be a non-empty string")
    elif not schema_id.startswith("https://schemas.socioprophet.org/procybernetica/"):
        diagnostics.append("$id must use canonical v0 prefix https://schemas.socioprophet.org/procybernetica/")

    if payload.get("type") != "object":
        diagnostics.append("v0 schema root type must be object")

    if not isinstance(payload.get("required"), list) or not payload.get("required"):
        diagnostics.append("required must be a non-empty list")

    if not isinstance(payload.get("properties"), dict) or not payload.get("properties"):
        diagnostics.append("properties must be a non-empty object")

    if "schema_version" not in payload.get("properties", {}):
        diagnostics.append("schema_version property is required for v0 schemas")

    additional_properties = payload.get("additionalProperties")
    if additional_properties not in {True, False}:
        diagnostics.append("additionalProperties must be explicit boolean true or false")

    return {
        "schema": schema_name,
        "exists": True,
        "passed": not diagnostics,
        "id": schema_id,
        "title": payload.get("title"),
        "fixture_status": "fixture-backed" if schema_name in EXPECTED_FIXTURE_BACKED_SCHEMAS else "deferred-fixture",
        "diagnostics": diagnostics,
    }


def validate() -> dict[str, Any]:
    results = [validate_schema_file(schema_name) for schema_name in CANONICAL_V0_SCHEMAS]
    canonical_set = set(CANONICAL_V0_SCHEMAS)
    fixture_backed = EXPECTED_FIXTURE_BACKED_SCHEMAS
    missing_fixture_tracking = fixture_backed - canonical_set
    deferred_unknown = set(DEFERRED_FIXTURE_SCHEMAS) - canonical_set

    diagnostics = []
    if missing_fixture_tracking:
        diagnostics.append(f"fixture-backed schemas not canonical: {sorted(missing_fixture_tracking)}")
    if deferred_unknown:
        diagnostics.append(f"deferred fixture schemas not canonical: {sorted(deferred_unknown)}")

    passed = all(result["passed"] for result in results) and not diagnostics
    return {
        "validator": "procybernetica_v0_schema.validator.v1",
        "passed": passed,
        "schema_count": len(CANONICAL_V0_SCHEMAS),
        "fixture_backed_count": len(EXPECTED_FIXTURE_BACKED_SCHEMAS),
        "deferred_fixture_schemas": DEFERRED_FIXTURE_SCHEMAS,
        "diagnostics": diagnostics,
        "results": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: v0 schemas validate")
        else:
            print("FAIL: v0 schemas validate", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
