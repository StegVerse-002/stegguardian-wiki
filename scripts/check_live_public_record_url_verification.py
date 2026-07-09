import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "live-public-record-url-verification.json"
EXPECTED_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
EXPECTED_RECORDS = {
    "data/public-records-manifest.json",
    "data/cross-wiki-metadata-graph.json",
    "data/cross-wiki-health-status.json",
    "data/deployment-receipt.json",
    "data/session-coordination-status.json",
    "data/pages-deployment-trigger-status.json",
}
REQUIRED_NON_CLAIMS = {
    "all_machine_record_urls_confirmed": False,
    "peer_machine_records_verified": False,
    "cross_repo_authority_granted": False,
    "standing_conferred": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_live_public_record_url_verification")
        payload = {}
    else:
        payload = json.loads(STATUS.read_text(encoding="utf-8"))

    if payload.get("record_type") != "stegguardian_live_public_record_url_verification":
        errors.append("record_type_mismatch")
    if payload.get("repo") != "StegVerse-002/stegguardian-wiki":
        errors.append("repo_mismatch")
    if payload.get("public_url") != EXPECTED_URL:
        errors.append("public_url_mismatch")
    if payload.get("homepage_user_observed_live") is not True:
        errors.append("homepage_user_observed_live_must_be_true")

    records = set(payload.get("machine_public_records_expected", []))
    for record in sorted(EXPECTED_RECORDS - records):
        errors.append("missing_expected_record:" + record)
    for record in sorted(records - EXPECTED_RECORDS):
        errors.append("unexpected_expected_record:" + record)
    for record in sorted(EXPECTED_RECORDS):
        if not (ROOT / record).exists():
            errors.append("missing_local_record_source:" + record)

    state = payload.get("verification_state", {})
    if state.get("homepage_rendered") is not True:
        errors.append("homepage_rendered_must_be_true")
    if state.get("machine_records_listed_on_homepage") is not True:
        errors.append("machine_records_listed_on_homepage_must_be_true")
    if state.get("external_fetch_confirmed_by_current_session") is not False:
        errors.append("external_fetch_confirmed_must_remain_false_until_fetched")
    if state.get("all_machine_record_urls_confirmed") is not False:
        errors.append("all_machine_record_urls_confirmed_must_remain_false_until_fetched")

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("LIVE PUBLIC RECORD URL VERIFICATION: FAIL - " + ", ".join(errors))
        return 1
    print("LIVE PUBLIC RECORD URL VERIFICATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
