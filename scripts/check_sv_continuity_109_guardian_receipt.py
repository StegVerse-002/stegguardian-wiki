#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "receipts/sv-continuity-109-guardian-verification.json"
REQUIRED_TRUE = (
    "external_cognition_exposure_recorded",
    "unknown_retention_preserved",
    "external_returns_non_authoritative",
    "loss_and_corruption_recovery_verified",
    "unresolved_divergence_fail_closed",
    "stale_authority_consent_policy_fail_closed",
    "guardian_observation_grants_no_authority",
)


def main() -> int:
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    failures: list[str] = []
    checks = receipt.get("checks", {})
    for key in REQUIRED_TRUE:
        if checks.get(key) is not True:
            failures.append(f"required check failed: {key}")
    for key, value in receipt.get("authority", {}).items():
        if value is not False:
            failures.append(f"authority must remain false: {key}")
    decision = receipt.get("decision")
    if decision == "PASS" and checks.get("live_public_record_verification_complete") is not True:
        failures.append("PASS requires successful live public-record verification")
    if decision not in {"PASS", "BLOCK"}:
        failures.append("decision must be PASS or BLOCK")
    if failures:
        print("SV-CONTINUITY-109 GUARDIAN VERIFICATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"SV-CONTINUITY-109 GUARDIAN VERIFICATION: {decision}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
