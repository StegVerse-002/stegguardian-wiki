from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "USER_OBSERVED_WORKFLOW_EVIDENCE.md"

REQUIRED_TEXT = [
    "User-Observed Workflow Evidence",
    "StegGuardian Wiki Readiness #31: success",
    "Publish StegGuardian Wiki #46: success",
    "Publish StegGuardian Wiki #45: success",
    "commit b8d9d97",
    "status: user_observed_success_connector_unconfirmed",
    "does not claim connector-confirmed workflow metadata",
    "public deployment verification",
]


def main() -> int:
    errors = []
    if not EVIDENCE.exists():
        errors.append("missing_user_observed_workflow_evidence")
        text = ""
    else:
        text = EVIDENCE.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("evidence_missing:" + item)

    if errors:
        print("USER OBSERVED WORKFLOW EVIDENCE: FAIL - " + ", ".join(errors))
        return 1
    print("USER OBSERVED WORKFLOW EVIDENCE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
