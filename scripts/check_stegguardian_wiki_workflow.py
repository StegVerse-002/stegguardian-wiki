#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "stegguardian-wiki-readiness.yml"


def main() -> int:
    if not WORKFLOW.exists():
        raise SystemExit("STEGGUARDIAN WIKI WORKFLOW: FAIL - workflow missing")
    text = WORKFLOW.read_text(encoding="utf-8")
    required = [
        "name: StegGuardian Wiki Readiness",
        "pull_request:",
        "push:",
        "workflow_dispatch:",
        "python scripts/check_stegguardian_wiki_readiness.py",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit("STEGGUARDIAN WIKI WORKFLOW: FAIL - required workflow text missing")
    print("STEGGUARDIAN WIKI WORKFLOW: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
