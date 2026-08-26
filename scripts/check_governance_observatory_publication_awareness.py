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
    require(effect.get("state") == "VERIFIED_PUBLICATION_AWARENESS_ONLY", "guardian state")
    for key in (
        "guardian_enforcement_authorized","override_authorized","execution_authorized",
        "publication_authorized","release_authorized","custody_recorded","admissibility_determined",
    ):
        require(effect.get(key) is False, key)
    require(data.get("execution_class") == "PARALLEL_SAFE_NON_HIL_AWARENESS", "execution class")
    require(data.get("hil_dependency_effect") is False, "HIL dependency effect")
    require(data.get("manual_user_action_required") is False, "manual user action")
    print("PASS: Governance Observatory Guardian publication awareness validated")

if __name__ == "__main__":
    main()
