from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parent
SCHEMAS = REPO_ROOT / "schemas"
PROFILES = REPO_ROOT / "profiles"
EXAMPLES = REPO_ROOT / "examples"
