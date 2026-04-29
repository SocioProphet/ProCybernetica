from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema

from .paths import SCHEMAS

SCHEMA_MAP: dict[str, str] = {
    "artifact_envelope": "artifact_envelope.schema.json",
    "capability_descriptor": "capability_descriptor.schema.json",
    "claim": "claim.schema.json",
    "command_envelope": "command_envelope.schema.json",
    "delegation_envelope": "delegation_envelope.schema.json",
    "evaluation_result": "evaluation_result.schema.json",
    "incident_report": "incident_report.schema.json",
    "node_descriptor": "node_descriptor.schema.json",
    "observation_envelope": "observation_envelope.schema.json",
    "policy_envelope": "policy_envelope.schema.json",
    "promotion_decision": "promotion_decision.schema.json",
    "provenance_record": "provenance_record.schema.json",
    "replay_envelope": "replay_envelope.schema.json",
    "status_envelope": "status_envelope.schema.json",
    "trace_event": "trace_event.schema.json",
    "transition_record": "transition_record.schema.json",
}


class SchemaBundle:
    """Load and validate ProCybernetica JSON Schema contracts."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or SCHEMAS
        self._cache: dict[str, dict[str, Any]] = {}

    def load(self, name: str) -> dict[str, Any]:
        if name not in SCHEMA_MAP:
            known = ", ".join(sorted(SCHEMA_MAP))
            raise KeyError(f"unknown schema {name!r}; known schemas: {known}")
        if name not in self._cache:
            path = self.root / SCHEMA_MAP[name]
            self._cache[name] = json.loads(path.read_text(encoding="utf-8"))
        return self._cache[name]

    def validate(self, name: str, payload: dict[str, Any]) -> None:
        jsonschema.validate(payload, self.load(name))
