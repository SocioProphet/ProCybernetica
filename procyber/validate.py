from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schema_bundle import SchemaBundle


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_file(path: str | Path, schema: str) -> str:
    payload = load_json(path)
    SchemaBundle().validate(schema, payload)
    return f"valid: {path} as {schema}"
