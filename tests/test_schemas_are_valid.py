from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_ROOT = ROOT / "schemas"


def test_all_json_schemas_are_valid_draft_2020_12() -> None:
    schema_paths = sorted(SCHEMA_ROOT.glob("*.schema.json"))
    assert schema_paths, "no schema files found"

    for path in schema_paths:
        schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
