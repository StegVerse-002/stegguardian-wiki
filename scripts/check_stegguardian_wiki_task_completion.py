#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "stegguardian-wiki-task-completion-status.json"


def main() -> int:
    if not STATUS.exists():
        raise SystemExit("STEGGUARDIAN TASK COMPLETION: FAIL - status missing")
    data = json.loads(STATUS.read_text(encoding="utf-8"))
    expected = {
        "status_id": "stegguardian-wiki-task-completion-status",
        "repository": "StegVerse-002/stegguardian-wiki",
        "repo_local_build": "AUTOMATED_VALIDATION_READY",
        "active_handoff": "STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md",
        "validation_command": "python scripts/check_stegguardian_wiki_readiness.py",
        "automation_workflow": ".github/workflows/stegguardian-wiki-readiness.yml",
        "next_action": "WAIT_FOR_UPSTREAM_GATE_EVENTS",
        "archive_status": "READY_FOR_HANDOFF",
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise SystemExit(f"STEGGUARDIAN TASK COMPLETION: FAIL - {key}")
    if data.get("continuation_owner") != "repository automation and upstream gate owners":
        raise SystemExit("STEGGUARDIAN TASK COMPLETION: FAIL - continuation owner")
    print("STEGGUARDIAN TASK COMPLETION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
