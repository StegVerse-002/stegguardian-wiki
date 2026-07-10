from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "fetch_live_public_record_urls.py"
RUNBOOK = ROOT / "docs" / "LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md"

REQUIRED_SCRIPT_TEXT = [
    "EXPECTED_RECORDS",
    "data/public-records-manifest.json",
    "data/cross-wiki-metadata-graph.json",
    "data/cross-wiki-health-status.json",
    "data/deployment-receipt.json",
    "data/session-coordination-status.json",
    "data/pages-deployment-trigger-status.json",
    "data/live-public-record-url-verification.json",
    "--write-report",
    "all_machine_record_urls_confirmed",
]

REQUIRED_RUNBOOK_TEXT = [
    "Live Public Record URL Fetch Runbook",
    "python scripts/fetch_live_public_record_urls.py --write-report data/live-public-record-url-fetch-report.json",
    "does not grant cross-repo authority",
]


def main() -> int:
    errors = []
    if not SCRIPT.exists():
        errors.append("missing_fetch_script")
        script_text = ""
    else:
        script_text = SCRIPT.read_text(encoding="utf-8")

    if not RUNBOOK.exists():
        errors.append("missing_fetch_runbook")
        runbook_text = ""
    else:
        runbook_text = RUNBOOK.read_text(encoding="utf-8")

    for text in REQUIRED_SCRIPT_TEXT:
        if text not in script_text:
            errors.append("fetch_script_missing:" + text)
    for text in REQUIRED_RUNBOOK_TEXT:
        if text not in runbook_text:
            errors.append("fetch_runbook_missing:" + text)

    if errors:
        print("LIVE PUBLIC RECORD FETCH TOOLING: FAIL - " + ", ".join(errors))
        return 1
    print("LIVE PUBLIC RECORD FETCH TOOLING: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
