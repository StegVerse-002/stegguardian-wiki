import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "ecosystem-documentation-endpoints.json"
EXPECTED = {
    "stegverse-site": ("StegVerse-Labs/Site", "https://stegverse-labs.github.io/Site/"),
    "admissibility-wiki": ("StegVerse-Labs/admissibility-wiki", "https://stegverse-labs.github.io/admissibility-wiki/"),
    "stegguardian-wiki": ("StegVerse-002/stegguardian-wiki", "https://stegverse-002.github.io/stegguardian-wiki/"),
    "stegtalk-wiki": ("StegVerse-Labs/stegtalk-wiki", "https://stegverse-labs.github.io/stegtalk-wiki/"),
}


def main() -> int:
    errors = []
    if not REGISTRY.exists():
        errors.append("missing_endpoint_registry")
        payload = {}
    else:
        payload = json.loads(REGISTRY.read_text(encoding="utf-8"))

    if payload.get("record_type") != "stegverse_ecosystem_documentation_endpoints":
        errors.append("record_type_mismatch")

    endpoints = {item.get("id"): item for item in payload.get("endpoints", [])}
    for endpoint_id, (repo, url) in EXPECTED.items():
        item = endpoints.get(endpoint_id)
        if not item:
            errors.append("missing_endpoint:" + endpoint_id)
            continue
        if item.get("repo") != repo:
            errors.append("repo_mismatch:" + endpoint_id)
        if item.get("url") != url:
            errors.append("url_mismatch:" + endpoint_id)
        if not item.get("role"):
            errors.append("role_missing:" + endpoint_id)

    verification = payload.get("verification", {})
    if verification.get("site_web_fetch_confirmed") is not True:
        errors.append("site_fetch_confirmation_missing")
    if verification.get("guardian_user_observed_live") is not True:
        errors.append("guardian_user_observation_missing")
    if verification.get("all_endpoints_confirmed") is not False:
        errors.append("all_endpoints_must_remain_false_until_verified")

    if errors:
        print("ECOSYSTEM DOCUMENTATION ENDPOINTS: FAIL - " + ", ".join(errors))
        return 1
    print("ECOSYSTEM DOCUMENTATION ENDPOINTS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
