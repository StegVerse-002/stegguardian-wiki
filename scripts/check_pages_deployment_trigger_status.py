import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "pages-deployment-trigger-status.json"
DOC = ROOT / "docs" / "PAGES_DEPLOYMENT_TRIGGER_DIAGNOSIS.md"
EXPECTED_PUBLIC_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
REQUIRED_NON_CLAIMS = {
    "public_url_verified": False,
    "workflow_run_confirmed": False,
    "github_pages_settings_confirmed": False,
    "deployment_success_confirmed": False,
    "guardian_enforcement_authority": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_pages_deployment_trigger_status")
        payload = {}
    else:
        payload = json.loads(STATUS.read_text(encoding="utf-8"))

    if not DOC.exists():
        errors.append("missing_pages_deployment_trigger_diagnosis_doc")

    if payload.get("record_type") != "stegguardian_pages_deployment_trigger_status":
        errors.append("record_type_mismatch")
    if payload.get("repo") != "StegVerse-002/stegguardian-wiki":
        errors.append("repo_mismatch")
    if payload.get("public_url") != EXPECTED_PUBLIC_URL:
        errors.append("public_url_mismatch")
    if payload.get("status") != "deployment_trigger_unconfirmed":
        errors.append("status_must_remain_unconfirmed_until_live_verification")

    evidence = payload.get("evidence", {})
    if evidence.get("workflow_runs_returned") != 0:
        errors.append("workflow_runs_evidence_must_match_observed_zero")
    if evidence.get("combined_status_entries_returned") != 0:
        errors.append("combined_status_evidence_must_match_observed_zero")

    repo_side = payload.get("repo_side_state", {})
    for key in [
        "pages_workflow_present",
        "workflow_dispatch_present",
        "push_main_trigger_present",
    ]:
        if repo_side.get(key) is not True:
            errors.append("repo_side_state_missing:" + key)
    if repo_side.get("static_site_output_path") != "_site":
        errors.append("static_site_output_path_mismatch")
    if repo_side.get("deploy_action") != "actions/deploy-pages@v4":
        errors.append("deploy_action_mismatch")

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("PAGES DEPLOYMENT TRIGGER STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("PAGES DEPLOYMENT TRIGGER STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
