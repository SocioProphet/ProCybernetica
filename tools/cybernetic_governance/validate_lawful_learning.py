#!/usr/bin/env python3
"""Validate calibrated lawful-learning schemas and examples.

This is a lightweight repository-native conformance smoke for #24. It validates
that JSON Schemas parse as draft 2020-12, YAML examples parse and contain their
expected semantic sections, and the deterministic toy test module is available.
It does not use live data or claim empirical results.
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]

# Make the repo root importable so `procyber.lawful_learning.toy` resolves regardless of
# how the validator is invoked. When run as a subprocess (see the conformance tests),
# sys.path[0] is this script's directory, not the repo root, so the `procyber` package is
# otherwise unimportable without an installed distribution or an external PYTHONPATH.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SCHEMA_DIR = ROOT / "schemas" / "lawful-learning"
EXAMPLE_DIR = ROOT / "examples" / "lawful-learning"

SCHEMA_FILES = [
    "model.schema.json",
    "constraint.schema.json",
    "ledger.schema.json",
]

EXAMPLE_FILES = [
    "model.yaml",
    "tuning.yaml",
    "ledger.yaml",
]

EXPECTED_EXAMPLE_SECTIONS = {
    "model.yaml": {"model", "constraints", "gates", "truth"},
    "tuning.yaml": {"tuning", "search_ranges"},
    "ledger.yaml": {"ledger"},
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing JSON schema: {path}") from None
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in {path}: {exc}") from None


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"missing YAML example: {path}") from None
    if not isinstance(loaded, dict):
        raise SystemExit(f"YAML example must parse to mapping: {path}")
    return loaded


def validate_schema(name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / name
    diagnostics: list[str] = []
    schema = load_json(path)

    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # pragma: no cover - diagnostic only
        diagnostics.append(f"invalid JSON Schema: {exc}")

    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        diagnostics.append("schema must declare JSON Schema draft 2020-12")
    if not schema.get("$id"):
        diagnostics.append("schema must declare $id")
    if schema.get("type") != "object":
        diagnostics.append("schema root type must be object")
    if not schema.get("required"):
        diagnostics.append("schema must declare required fields")
    if not schema.get("properties"):
        diagnostics.append("schema must declare properties")

    return {
        "kind": "schema",
        "file": f"schemas/lawful-learning/{name}",
        "passed": not diagnostics,
        "diagnostics": diagnostics,
    }


def validate_example(name: str) -> dict[str, Any]:
    path = EXAMPLE_DIR / name
    diagnostics: list[str] = []
    payload = load_yaml(path)

    expected = EXPECTED_EXAMPLE_SECTIONS[name]
    missing = expected - set(payload)
    if missing:
        diagnostics.append(f"missing expected sections: {sorted(missing)}")

    if name == "model.yaml":
        if payload.get("model", {}).get("spectral_modes") != 22:
            diagnostics.append("model.yaml must pin spectral_modes to 22")
        if payload.get("constraints", {}).get("enforcement") not in {"slack_penalty", "hard_activation", "augmented_lagrangian"}:
            diagnostics.append("model.yaml must use a lawful constraint enforcement mode")
        if payload.get("gates", {}).get("thresholds") != "learned_quantile":
            diagnostics.append("model.yaml must use learned_quantile thresholds")
    elif name == "tuning.yaml":
        reject_if = payload.get("tuning", {}).get("reject_if", {})
        required_rejections = {"max_violation_exceeds", "support_below_minimum", "gate_instability_exceeds", "pair_count_exceeds"}
        missing_rejections = required_rejections - set(reject_if)
        if missing_rejections:
            diagnostics.append(f"tuning.yaml missing reject_if controls: {sorted(missing_rejections)}")
    elif name == "ledger.yaml":
        ledger = payload.get("ledger", {})
        if ledger.get("hash") != "sha256":
            diagnostics.append("ledger.yaml must use sha256 hash discipline")
        if ledger.get("serialization", {}).get("canonical") is not True:
            diagnostics.append("ledger.yaml must require canonical serialization")
        if ledger.get("replay", {}).get("deterministic") is not True:
            diagnostics.append("ledger.yaml must require deterministic replay")

    return {
        "kind": "example",
        "file": f"examples/lawful-learning/{name}",
        "passed": not diagnostics,
        "diagnostics": diagnostics,
    }


def validate_toy_module() -> dict[str, Any]:
    diagnostics: list[str] = []
    try:
        toy = importlib.import_module("procyber.lawful_learning.toy")
    except Exception as exc:  # pragma: no cover - diagnostic only
        diagnostics.append(f"could not import toy module: {exc}")
        return {"kind": "toy", "file": "procyber/lawful_learning/toy.py", "passed": False, "diagnostics": diagnostics}

    for fn_name in [
        "spectral_construction_example",
        "monotone_projection_pava",
        "dominance_slack",
        "edgeworth_project_f11",
        "learned_gate",
        "end_to_end_example",
    ]:
        if not hasattr(toy, fn_name):
            diagnostics.append(f"toy module missing {fn_name}")

    return {
        "kind": "toy",
        "file": "procyber/lawful_learning/toy.py",
        "passed": not diagnostics,
        "diagnostics": diagnostics,
    }


def validate() -> dict[str, Any]:
    results = [validate_schema(name) for name in SCHEMA_FILES]
    results.extend(validate_example(name) for name in EXAMPLE_FILES)
    results.append(validate_toy_module())
    return {
        "validator": "lawful_learning_conformance.validator.v1",
        "passed": all(result["passed"] for result in results),
        "schema_count": len(SCHEMA_FILES),
        "example_count": len(EXAMPLE_FILES),
        "results": results,
        "non_claims": [
            "No live data are used.",
            "YAML examples are deterministic formal configuration examples only.",
            "Toy examples are deterministic calculations, not empirical results."
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    result = validate()
    print(json.dumps(result, indent=2, sort_keys=True))
    if not args.json:
        if result["passed"]:
            print("PASS: lawful-learning conformance smoke")
        else:
            print("FAIL: lawful-learning conformance smoke", file=sys.stderr)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
