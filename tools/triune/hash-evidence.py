#!/usr/bin/env python3
"""Produce a deterministic SHA-256 digest for an evidence artifact.

Usage:
    python tools/triune/hash-evidence.py /path/to/evidence.json

Output (JSON):
    {"path": "...", "sha256": "<64 hex chars>", "bytes": 1234}
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def hash_evidence(path: str | Path) -> dict:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"evidence file not found: {p}")
    data = p.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    size = len(data)
    return {
        "path": str(p.resolve()),
        "sha256": digest,
        "bytes": size,
        "empty": size == 0,
    }


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: hash-evidence.py <path>", file=sys.stderr)
        sys.exit(1)
    try:
        result = hash_evidence(sys.argv[1])
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
