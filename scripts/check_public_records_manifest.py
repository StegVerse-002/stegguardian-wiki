import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "public-records-manifest.json"
REQUIRED_RECORDS = {
    "data/page-index.json": "published_by_current_workflow",
    "data/page-metadata.schema.json": "published_by_current_workflow",
    "data/page-relationship-graph.json": "published_by_current_workflow",
    "data/cross-wiki-metadata-graph.json": "published_by_current_workflow",
    "data/cross-wiki-health-status.json": "published_by_current_workflow",
    "data/ecosystem-documentation-endpoints.json": "published_by_current_workflow",
    "data/live-public-record-url-verification.json": "published_by_current_workflow",
    "docs/LIVE_PUBLIC_RECORD_URL_FETCH_RUNBOOK.md": "published_by_current_workflow",
    "data/deployment-receipt.json": "published_by_current_workflow",
    "data/session-coordination-status.json": "published_by_current_workflow",
    "data/pages-deployment-trigger-status.json": "published_by_current_workflow",
    "docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md": "published_by_current_workflow",
    "data/public-records-manifest.json": "published_by_current_workflow",
}
REQUIRED_NON_CLAIMS = {
    "public_url_verified": False,
    "connector_confirmed_workflow_metadata": False,
    "guardian_enforcement_authority": False,
    "execution_authority": False,
    "commit_time_standing": False,
}


def main() -> int:
    errors = []
    if not MANIFEST.exists():
        errors.append("missing_public_records_manifest")
        payload = {}
    else:
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))

    if payload.get("manifest_type") != "stegguardian_public_records_manifest":
        errors.append("manifest_type_mismatch")
    if payload.get("base_url") != "https://stegverse-002.github.io/stegguardian-wiki/":
        errors.append("base_url_mismatch")

    records = {record.get("path"): record for record in payload.get("records", [])}
    for path, state in REQUIRED_RECORDS.items():
        if not (ROOT / path).exists():
            errors.append("missing_local_record:" + path)
        record = records.get(path)
        if record is None:
            errors.append("manifest_missing_record:" + path)
            continue
        if record.get("installed") is not True:
            errors.append("manifest_record_not_installed:" + path)
        if record.get("public_exposure_state") != state:
            errors.append("manifest_record_state_mismatch:" + path)
        expected_url = "https://stegverse-002.github.io/stegguardian-wiki/" + path
        if record.get("url") != expected_url:
            errors.append("manifest_record_url_mismatch:" + path)

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("manifest_non_claim_mismatch:" + key)

    if errors:
        print("PUBLIC RECORDS MANIFEST: FAIL - " + ", ".join(errors))
        return 1
    print("PUBLIC RECORDS MANIFEST: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
