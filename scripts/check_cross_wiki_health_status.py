import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "cross-wiki-health-status.json"
SCHEMA = ROOT / "data" / "cross-wiki-health-status.schema.json"
EXPECTED_REPO = "StegVerse-002/stegguardian-wiki"
EXPECTED_ORIGIN_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
EXPECTED_REGISTRY = "data/ecosystem-documentation-endpoints.json"
REQUIRED_PEERS = {
    "stegguardian-wiki": "https://stegverse-002.github.io/stegguardian-wiki/",
    "stegtalk-wiki": "https://stegverse-labs.github.io/stegtalk-wiki/",
    "admissibility-wiki": "https://stegverse-labs.github.io/admissibility-wiki/",
    "stegverse-site": "https://stegverse-labs.github.io/Site/",
}
REQUIRED_NON_CLAIMS = {
    "all_peer_urls_verified": False,
    "peer_machine_records_verified": False,
    "cross_repo_authority_granted": False,
    "standing_conferred": False,
    "execution_authority": False,
}


def load_json(path: Path, errors: list[str], label: str) -> dict:
    if not path.exists():
        errors.append("missing:" + label)
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid_json:{label}:{exc}")
        return {}


def main() -> int:
    errors: list[str] = []
    payload = load_json(STATUS, errors, "cross_wiki_health_status")
    schema = load_json(SCHEMA, errors, "cross_wiki_health_schema")

    if schema.get("title") != "StegVerse Cross-Wiki Health Status":
        errors.append("schema_title_mismatch")
    if schema.get("properties", {}).get("schema_version", {}).get("const") != "1.0.0":
        errors.append("schema_version_mismatch")
    required = set(schema.get("required", []))
    for field in ("schema_ref", "peer_registry", "checks", "next_actions", "non_claims"):
        if field not in required:
            errors.append("schema_missing_required:" + field)

    if payload.get("schema_version") != "1.0.0":
        errors.append("record_schema_version_mismatch")
    if payload.get("schema_ref") != "data/cross-wiki-health-status.schema.json":
        errors.append("record_schema_ref_mismatch")
    if payload.get("record_type") != "stegguardian_cross_wiki_health_status":
        errors.append("record_type_mismatch")
    if payload.get("repo") != EXPECTED_REPO:
        errors.append("repo_mismatch")
    if payload.get("status") != "pending_live_peer_checks":
        errors.append("status_must_remain_pending_until_peer_checks")
    if payload.get("origin_public_url") != EXPECTED_ORIGIN_URL:
        errors.append("origin_public_url_mismatch")
    if payload.get("peer_registry") != EXPECTED_REGISTRY:
        errors.append("peer_registry_mismatch")

    peers = {peer.get("id"): peer for peer in payload.get("peers", [])}
    for peer_id, public_url in REQUIRED_PEERS.items():
        peer = peers.get(peer_id)
        if not peer:
            errors.append("missing_peer:" + peer_id)
            continue
        if peer.get("public_url") != public_url:
            errors.append("peer_public_url_mismatch:" + peer_id)
        if not peer.get("repo"):
            errors.append("peer_repo_missing:" + peer_id)
        if not peer.get("relationship"):
            errors.append("peer_relationship_missing:" + peer_id)

    checks = payload.get("checks", {})
    if checks.get("peer_urls_declared") is not True:
        errors.append("peer_urls_declared_must_be_true")
    if checks.get("origin_records_declared") is not True:
        errors.append("origin_records_declared_must_be_true")
    for key in (
        "live_peer_http_confirmed",
        "peer_machine_records_confirmed",
        "cross_wiki_schema_consistency_confirmed",
    ):
        if checks.get(key) is not False:
            errors.append("check_must_remain_false_until_verified:" + key)

    if not payload.get("next_actions"):
        errors.append("next_actions_must_be_non_empty")

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("CROSS WIKI HEALTH STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("CROSS WIKI HEALTH STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
