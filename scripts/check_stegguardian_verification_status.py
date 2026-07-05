from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "STEGGUARDIAN_VERIFICATION_STATUS.md"

REQUIRED_TEXT = [
    "StegGuardian Wiki Verification Status",
    "local_status: PASS",
    "aggregate_checker: INSTALLED",
    "workflow_evidence_user_observed: SUCCESS",
    "connector_confirmed_workflow_metadata: UNCONFIRMED",
    "public_url_connector_verified: PENDING",
    "python scripts/check_guardian_local_state.py",
    "USER_OBSERVED_WORKFLOW_EVIDENCE.md",
    "WORKFLOW_VERIFICATION_STATUS.md",
    "PUBLIC_URL_VERIFICATION_STATUS.md",
    "https://stegverse-002.github.io/stegguardian-wiki/",
    "docs/GUARDIAN_AGGREGATE_WORKFLOW_DELTA.md",
    "does not claim connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not PAGE.exists():
        errors.append("missing_stegguardian_verification_status")
        text = ""
    else:
        text = PAGE.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("page_missing:" + item)

    if errors:
        print("STEGGUARDIAN VERIFICATION STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("STEGGUARDIAN VERIFICATION STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
