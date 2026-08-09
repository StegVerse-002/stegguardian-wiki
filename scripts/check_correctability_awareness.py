#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "correctability-awareness-status.json"
EXPECTED_DIGEST = "sha256:030f22b998a6f9c382db5463a4cc55f6d70132d5dd20d880778b5efda9844536"


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main():
    data = json.loads(PATH.read_text())
    require(data.get("record_type") == "stegverse.correctability.guardian_awareness", "record_type")
    require(data.get("source_repository") == "StegVerse-Labs/StegCore", "source_repository")
    require(data.get("source_goal") == "CORRECTABILITY-LAYER-001", "source_goal")
    src = data.get("source_validation", {})
    require(src.get("workflow_run_id") == 30774680694, "workflow_run_id")
    require(src.get("job_id") == 91567818006, "job_id")
    require(src.get("fixture_count") == 10 and src.get("passed_count") == 10, "source validation counts")
    require(src.get("artifact_id") == 8841612361, "artifact_id")
    require(src.get("artifact_digest") == EXPECTED_DIGEST, "artifact_digest")

    awareness = data.get("awareness", {})
    for key in (
        "correctability_is_distinct_from_guardian_enforcement",
        "reconstructability_is_not_authorized_intervention",
        "late_request_is_not_timely_correction",
        "post_irreversibility_compensation_is_not_prevention",
        "visibility_is_not_authority",
        "documentation_is_not_enforcement",
    ):
        require(awareness.get(key) is True, key)

    effect = data.get("guardian_effect", {})
    require(effect.get("state") == "VERIFIED_SOURCE_SEMANTICS_AWARENESS_ONLY", "state")
    for key in (
        "guardian_enforcement_authorized", "override_authorized", "execution_authorized",
        "publication_authorized", "release_authorized", "custody_recorded", "admissibility_determined",
    ):
        require(effect.get(key) is False, key)
    require(data.get("execution_class") == "PARALLEL_SAFE_NON_HIL_AWARENESS", "execution_class")
    require(data.get("manual_user_action_required") is False, "manual_user_action_required")
    print("PASS: bounded correctability Guardian awareness validated")


if __name__ == "__main__":
    main()
