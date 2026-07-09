import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "session-coordination-status.json"
EXPECTED_REPO = "StegVerse-002/stegguardian-wiki"
EXPECTED_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
REQUIRED_CHECKED_SOURCES = {
    "open_issues",
    "open_pull_requests",
    "repository_coordination_records",
    "current_mirror_handoff",
}
REQUIRED_UNASSIGNED_TASKS = {
    "verify live deployment receipt URL responds",
    "verify public records manifest URL responds",
    "create reusable cross-wiki health checker",
    "create cross-wiki discovery status record",
    "mirror discovery status into handoff",
}
REQUIRED_NON_CLAIMS = {
    "all_external_sessions_observed": False,
    "github_pages_settings_read_by_connector": False,
    "manual_human_session_locks_detected": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_session_coordination_status")
        payload = {}
    else:
        payload = json.loads(STATUS.read_text(encoding="utf-8"))

    if payload.get("record_type") != "stegguardian_session_coordination_status":
        errors.append("record_type_mismatch")
    if payload.get("repo") != EXPECTED_REPO:
        errors.append("repo_mismatch")
    if payload.get("duplicate_work_detected") is not False:
        errors.append("duplicate_work_must_be_false")

    checked_sources = set(payload.get("checked_sources", []))
    for source in sorted(REQUIRED_CHECKED_SOURCES - checked_sources):
        errors.append("missing_checked_source:" + source)

    resolved = payload.get("resolved_issue", {})
    if resolved.get("name") != "stegguardian_pages_publication_repair":
        errors.append("resolved_issue_name_mismatch")
    if resolved.get("state") != "resolved_by_live_site_confirmation":
        errors.append("resolved_issue_state_mismatch")
    if resolved.get("public_url") != EXPECTED_URL:
        errors.append("resolved_issue_public_url_mismatch")
    if resolved.get("do_not_restart") is not True:
        errors.append("resolved_issue_do_not_restart_missing")

    current_goal = payload.get("current_goal", {})
    if current_goal.get("name") != "cross_wiki_discovery_and_health":
        errors.append("current_goal_name_mismatch")
    if current_goal.get("state") != "active":
        errors.append("current_goal_state_mismatch")

    routing = payload.get("parallel_session_routing", [])
    if len(routing) < 3:
        errors.append("parallel_session_routing_incomplete")

    tasks = set(payload.get("unassigned_tasks", []))
    for task in sorted(REQUIRED_UNASSIGNED_TASKS - tasks):
        errors.append("missing_unassigned_task:" + task)

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("SESSION COORDINATION STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("SESSION COORDINATION STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
