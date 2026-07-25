#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "pages" / "visibility-authority-guardian-boundary.md"
STATUS = ROOT / "data" / "visibility-authority-guardian-status.json"


def main() -> int:
    failures: list[str] = []
    if not PAGE.exists():
        failures.append("missing Guardian boundary page")
    else:
        text = PAGE.read_text(encoding="utf-8")
        for marker in (
            "public visibility != Guardian authority",
            "acknowledgement != endorsement",
            "reconstruction != authorization",
            "Any conflict fails closed.",
            "grants no Guardian enforcement",
        ):
            if marker not in text:
                failures.append(f"missing page marker: {marker}")

    if not STATUS.exists():
        failures.append("missing Guardian status")
    else:
        data = json.loads(STATUS.read_text(encoding="utf-8"))
        invariants = data.get("invariants") or {}
        for key in (
            "public_visibility_is_guardian_authority",
            "acknowledgement_is_endorsement",
            "acknowledgement_is_attribution",
            "reconstruction_is_authorization",
            "publication_is_execution_authority",
        ):
            if invariants.get(key) is not False:
                failures.append(f"{key} must be false")
        if data.get("manual_user_action_required") is not False:
            failures.append("manual_user_action_required must be false")
        if data.get("production_ready") is not False:
            failures.append("production_ready must remain false")

    print("VISIBILITY AUTHORITY GUARDIAN BOUNDARY:", "FAIL" if failures else "PASS")
    for failure in failures:
        print(f"- {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
