from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOKUP = ROOT / "FINAL_CONNECTOR_WORKFLOW_LOOKUP.md"

REQUIRED_TEXT = [
    "Final Connector Workflow Lookup",
    "a1a156c098a34808f8b687e0feca1cff6c78bd66",
    "workflow_runs: none returned",
    "pr2_merged: true",
    "pages_workflow_conflict_resolved: true",
    "public_site_user_observed: true",
    "connector_visible_workflow_runs: pending",
    "does not claim connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not LOOKUP.exists():
        errors.append("missing_final_connector_workflow_lookup")
        text = ""
    else:
        text = LOOKUP.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("lookup_missing:" + item)

    if errors:
        print("FINAL CONNECTOR WORKFLOW LOOKUP: FAIL - " + ", ".join(errors))
        return 1
    print("FINAL CONNECTOR WORKFLOW LOOKUP: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
