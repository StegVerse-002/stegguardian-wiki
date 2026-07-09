import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "cross-wiki-health-status.json"
EXPECTED_REPO = "StegVerse-002/stegguardian-wiki"
EXPECTED_ORIGIN_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
REQUIRED_PEERS = {
    "stegguardian-wiki": "https://stegverse-002.github.io/stegguardian-wiki/",
    "stegtalk-wiki": "https://stegverse-labs.github.io/stegtalk-wiki/",
    "admissibility-wiki": "https://stegverse-labs.github.io/admissibility-wiki/",
    "stegverse-site": "https://stegverse-labs.github.io/Site/",
}
REQUIRED_NEXT_ACTIONS = {
    "confirm peer public URLs respond",
    "confirm each peer exposes a public records manifest or declare missing",
    "standardize cross-wiki health records across StegTalk Wiki, Admissibility Wiki, and Site",
    "promote reusable checker to repo-standards after local proof",
}
REQUIRED_NON_CLAIMS = {
    "all_peer_urls_verified": False,
    "peer_machine_records_verified": False,
    "cross_repo_authority_granted": False,
    "standing_conferred": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_cross_wiki_health_status")
        payload = {}
    else:
        payload = json.loads(STATUS.read_text(encoding="utf-8"))

    if payload.get("record_type") != "stegguardian_cross_wiki_health_status":
        errors.append("record_type_mismatch")
    if payload.get("repo") != EXPECTED_REPO:
        errors.append("repo_mismatch")
    if payload.get("status") != "pending_live_peer_checks":
        errors.append("status_must_remain_pending_until_peer_checks")
    if payload.get("origin_public_url") != EXPECTED_ORIGIN_URL:
        errors.append("origin_public_url_mismatch")

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
    for key in [
        "live_peer_http_confirmed",
        "peer_machine_records_confirmed",
        "cross_wiki_schema_consistency_confirmed",
    ]:
        if checks.get(key) is not False:
            errors.append("check_must_remain_false_until_verified:" + key)

    next_actions = set(payload.get("next_actions", []))
    for action in sorted(REQUIRED_NEXT_ACTIONS - next_actions):
        errors.append("missing_next_action:" + action)

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
