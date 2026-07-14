#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    "scripts/check_repo_standards_guardian_summary.py",
    "scripts/check_stegguardian_wiki_workflow.py",
)


def main() -> int:
    for check in CHECKS:
        result = subprocess.run([sys.executable, check], cwd=ROOT)
        if result.returncode:
            print(f"STEGGUARDIAN WIKI READINESS: FAIL - {check}")
            return result.returncode
    print("STEGGUARDIAN WIKI READINESS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
