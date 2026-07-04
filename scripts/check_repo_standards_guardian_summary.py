#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "pages" / "repo-standards-guardian-summary.md"
STATUS = ROOT / "data" / "repo-standards-guardian-summary.json"
HANDOFF = ROOT / "STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md"


def read(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"REPO STANDARDS GUARDIAN SUMMARY: FAIL - missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    page = read(PAGE)
    handoff = read(HANDOFF)
    data = json.loads(read(STATUS))

    if "READY_FOR_UPSTREAM_GATE_EVENTS" not in page:
        raise SystemExit("REPO STANDARDS GUARDIAN SUMMARY: FAIL - page status missing")
    if "Standing-Proof-Engine v0.5.0" not in handoff:
        raise SystemExit("REPO STANDARDS GUARDIAN SUMMARY: FAIL - active handoff not preserved")
    expected = {
        "status_id": "repo-standards-guardian-summary",
        "repository": "StegVerse-002/stegguardian-wiki",
        "status": "READY_FOR_UPSTREAM_GATE_EVENTS",
        "next_action": "WAIT_FOR_UPSTREAM_GATE_EVENTS",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise SystemExit(f"REPO STANDARDS GUARDIAN SUMMARY: FAIL - {key} expected {value!r}, got {data.get(key)!r}")
    print("REPO STANDARDS GUARDIAN SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
