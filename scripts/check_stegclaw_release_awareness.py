#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "stegclaw-release-awareness.json"

def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")

def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    require(data.get("schema_version") == "1.0.0", "schema_version")
    require(data.get("record_type") == "stegverse.stegclaw.guardian_release_awareness", "record_type")
    require(data.get("source_repository") == "Data-Continuation/StegClaw", "source_repository")
    src = data.get("source_release", {})
    require(src.get("state") == "RELEASED", "release state")
    require(src.get("version") == "1.0.0", "release version")
    require(src.get("tag_name") == "v1.0.0", "release tag")
    require(src.get("release_id") == 381434394, "release id")
    require(src.get("release_target") == "6b89a4bfb3d4c2fcc61e6cccaa4f292fb4d58cdb", "release target")
    require(src.get("validation_run") == 33650991623, "validation run")
    require(src.get("validation_artifact_id") == 9854745757, "validation artifact")
    awareness = data.get("awareness", {})
    for key in ("release_is_not_guardian_authority","visibility_is_not_authority","documentation_is_not_enforcement","source_release_is_not_runtime_activation","repository_state_is_not_guardian_interpretation","cosv_state_is_not_execution_authority"):
        require(awareness.get(key) is True, key)
    effect = data.get("guardian_effect", {})
    require(effect.get("state") == "VERIFIED_RELEASE_AWARENESS_ONLY", "guardian state")
    for key in ("guardian_enforcement_authorized","override_authorized","execution_authorized","publication_authorized","release_authorized","custody_recorded","admissibility_determined","runtime_activation_claimed"):
        require(effect.get(key) is False, key)
    require(data.get("execution_class") == "PARALLEL_SAFE_NON_HIL_RELEASE_AWARENESS", "execution class")
    require(data.get("hil_dependency_effect") is False, "HIL dependency effect")
    require(data.get("authority_effect") == "NONE", "authority effect")
    require(data.get("manual_user_action_required") is False, "manual action")
    print("PASS: StegClaw v1.0.0 Guardian release awareness validated")

if __name__ == "__main__":
    main()
