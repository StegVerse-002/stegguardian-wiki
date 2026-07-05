from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs" / "GUARDIAN_AGGREGATE_WORKFLOW_DELTA.md"
CHECKER = ROOT / "scripts" / "check_guardian_local_state.py"

REQUIRED_TEXT = [
    "Guardian Aggregate Workflow Delta",
    "python scripts/check_guardian_local_state.py",
    "python scripts/check_llm_free_tier_trust_chain_page.py",
    "python scripts/check_page_index.py",
    "python scripts/check_pages_workflow_validation.py",
    "python scripts/check_workflow_verification_status.py",
    "Replace the two direct validation steps with the aggregate check",
    "This document does not modify workflow permissions",
    "claim workflow success",
    "claim public deployment success",
]


def main() -> int:
    errors = []
    if not DELTA.exists():
        errors.append("missing_aggregate_workflow_delta")
        text = ""
    else:
        text = DELTA.read_text(encoding="utf-8")

    if not CHECKER.exists():
        errors.append("missing_aggregate_local_state_checker")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("delta_missing:" + item)

    if errors:
        print("GUARDIAN AGGREGATE WORKFLOW DELTA: FAIL - " + ", ".join(errors))
        return 1
    print("GUARDIAN AGGREGATE WORKFLOW DELTA: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
