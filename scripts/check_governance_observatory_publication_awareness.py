#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "governance-observatory-publication-awareness-status.json"

def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")

def main():
    data = json.loads(PATH.read_text())
    require(data.get("schema_version") == "1.0.0", "schema_version")
    require(data.get("record_type") == "stegverse.governance_observatory.guardian_publication_awareness", "record_type")
    require(data.get("source_repository") == "StegVerse-Labs/governance-observatory", "source_repository")
    src = data.get("source_publication", {})
    require(src.get("state") == "PUBLISHED", "source state")
    require(src.get("merge_commit") == "52d9a8f596ade145f5b08e44e98395d328476ecc", "source merge")
    release = data.get("source_release", {})
    require(release.get("state") == "RELEASED", "release state")
    require(release.get("version") == "0.1.0", "release version")
    require(release.get("tag_name") == "v0.1.0", "release tag")
    require(release.get("release_id") == 377486341, "release id")
    require(release.get("release_url") == "https://github.com/StegVerse-Labs/governance-observatory/releases/tag/v0.1.0", "release url")
    require(release.get("release_state_head") == "31afc11745507e4764c2c9f44be1e5143e920ef1", "release head")
    require(release.get("release_workflow_run") == 33025454602, "release workflow")
    awareness = data.get("awareness", {})
    for key in (
        "publication_is_not_guardian_authority",
        "visibility_is_not_authority",
        "observation_is_not_standing",
        "documentation_is_not_enforcement",
        "source_capture_is_not_runtime_validation",
        "framework_record_is_not_guardian_interpretation",
    ):
        require(awareness.get(key) is True, key)
    effect = data.get("guardian_effect", {})
    require(effect.get("state") == "VERIFIED_RELEASE_AWARENESS_ONLY", "guardian state")
    for key in (
        "guardian_enforcement_authorized","override_authorized","execution_authorized",
        "publication_authorized","release_authorized","custody_recorded","admissibility_determined",
    ):
        require(effect.get(key) is False, key)
    require(data.get("execution_class") == "PARALLEL_SAFE_NON_HIL_RELEASE_AWARENESS", "execution class")
    require(data.get("hil_dependency_effect") is False, "HIL dependency effect")
    require(data.get("manual_user_action_required") is False, "manual user action")
    print("PASS: Governance Observatory v0.1.0 Guardian release awareness validated")

if __name__ == "__main__":
    main()
