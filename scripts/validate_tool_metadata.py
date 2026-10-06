#!/usr/bin/env python3
"""Validate structured OSINT tool metadata in Markdown frontmatter.

This intentionally uses only Python's standard library. It checks for the
presence of the normalized metadata fields without requiring a YAML package.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "osint-tools"

REQUIRED_MARKERS = (
    "tool:",
    "  name:",
    "  url:",
    "  status:",
    "  categories:",
    "  inputs:",
    "  capabilities:",
    "  pricing:",
    "    model:",
    "    free_tier:",
    "    paid_unlocks:",
    "  account_required:",
    "  platform:",
    "  open_source:",
    "  geographic_scope:",
    "  last_verified:",
)

DATE_RE = re.compile(r"^  last_verified:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    fm = frontmatter(path.read_text(encoding="utf-8"))

    if fm is None:
        return ["missing YAML frontmatter"]

    # Legacy entries are allowed during migration. Once an entry opts into the
    # structured 'tool:' block, all normalized fields become mandatory.
    if "\ntool:" not in "\n" + fm:
        return []

    for marker in REQUIRED_MARKERS:
        if marker not in fm:
            errors.append(f"missing field: {marker.strip()}")

    match = DATE_RE.search(fm)
    if not match:
        errors.append("last_verified must use YYYY-MM-DD")

    return errors


def main() -> int:
    failures = 0
    structured = 0
    legacy = 0

    for path in sorted(TOOLS_DIR.glob("*.md")):
        fm = frontmatter(path.read_text(encoding="utf-8"))
        if fm and "\ntool:" in "\n" + fm:
            structured += 1
        else:
            legacy += 1

        errors = validate(path)
        if errors:
            failures += 1
            print(f"{path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")

    print(f"Structured entries: {structured}")
    print(f"Legacy entries awaiting migration: {legacy}")

    if failures:
        print(f"Metadata validation failed for {failures} file(s).", file=sys.stderr)
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
