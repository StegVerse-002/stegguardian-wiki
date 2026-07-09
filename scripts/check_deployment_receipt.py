import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "data" / "deployment-receipt.json"
EXPECTED_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
EXPECTED_RECORDS = {
    "data/page-index.json",
    "data/page-metadata.schema.json",
    "data/page-relationship-graph.json",
    "data/cross-wiki-metadata-graph.json",
    "data/pages-deployment-trigger-status.json",
    "data/public-records-manifest.json",
    "docs/PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md",
    "docs/STEGGUARDIAN_VERIFICATION_STATUS.md",
}
REQUIRED_NON_CLAIMS = {
    "public_url_verified": False,
    "workflow_run_confirmed": False,
    "artifact_hash_confirmed": False,
    "deployment_success_confirmed": False,
    "guardian_enforcement_authority": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not RECEIPT.exists():
        errors.append("missing_deployment_receipt")
        payload = {}
    else:
        payload = json.loads(RECEIPT.read_text(encoding="utf-8"))

    if payload.get("record_type") != "stegguardian_pages_deployment_receipt":
        errors.append("record_type_mismatch")
    if payload.get("repo") != "StegVerse-002/stegguardian-wiki":
        errors.append("repo_mismatch")
    if payload.get("public_url") != EXPECTED_URL:
        errors.append("public_url_mismatch")
    if payload.get("publication_mode") != "github_pages_actions":
        errors.append("publication_mode_mismatch")
    if payload.get("static_site_output_path") != "_site":
        errors.append("static_site_output_path_mismatch")
    if payload.get("deployment_state") != "pending_external_confirmation":
        errors.append("deployment_state_must_remain_pending_until_verified")
    if payload.get("expected_source_branch") != "main":
        errors.append("expected_source_branch_mismatch")
    if payload.get("expected_workflow") != ".github/workflows/pages.yml":
        errors.append("expected_workflow_mismatch")
    if payload.get("expected_deploy_action") != "actions/deploy-pages@v4":
        errors.append("expected_deploy_action_mismatch")

    records = set(payload.get("expected_public_records", []))
    missing = EXPECTED_RECORDS - records
    extra = records - EXPECTED_RECORDS
    for path in sorted(missing):
        errors.append("missing_expected_public_record:" + path)
    for path in sorted(extra):
        errors.append("unexpected_expected_public_record:" + path)
    for path in sorted(EXPECTED_RECORDS):
        if not (ROOT / path).exists():
            errors.append("missing_local_public_record_source:" + path)

    inputs = payload.get("confirmation_inputs", {})
    if inputs.get("deployment_url_confirmed") is not False:
        errors.append("deployment_url_confirmed_must_remain_false_until_verified")
    if inputs.get("public_record_urls_confirmed") is not False:
        errors.append("public_record_urls_confirmed_must_remain_false_until_verified")
    if inputs.get("workflow_run_id") is not None:
        errors.append("workflow_run_id_must_remain_null_until_confirmed")
    if inputs.get("artifact_hash") is not None:
        errors.append("artifact_hash_must_remain_null_until_confirmed")
    if inputs.get("confirmed_at") is not None:
        errors.append("confirmed_at_must_remain_null_until_confirmed")

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("PAGES DEPLOYMENT RECEIPT: FAIL - " + ", ".join(errors))
        return 1
    print("PAGES DEPLOYMENT RECEIPT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
