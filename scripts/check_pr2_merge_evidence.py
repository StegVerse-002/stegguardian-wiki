from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "PR2_MERGE_EVIDENCE.md"

REQUIRED_TEXT = [
    "PR2 Merge Evidence",
    "number: 2",
    "title: Align Pages workflow with local state checks",
    "state: closed",
    "merged: true",
    "merge_commit: 1d0c3be4a9905394abb73aa1ad710d74abcbf434",
    "workflow_conflict_resolved: true",
    "pages_workflow_preserved: true",
    "main_integrated: true",
    "merge_commit_workflow_runs: none returned by connector",
    "does not claim connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not EVIDENCE.exists():
        errors.append("missing_pr2_merge_evidence")
        text = ""
    else:
        text = EVIDENCE.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("merge_evidence_missing:" + item)

    if errors:
        print("PR2 MERGE EVIDENCE: FAIL - " + ", ".join(errors))
        return 1
    print("PR2 MERGE EVIDENCE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
