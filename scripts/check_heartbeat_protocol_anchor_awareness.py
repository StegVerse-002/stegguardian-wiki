#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "data" / "heartbeat-protocol-anchor-awareness.json"


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    require(data.get("record_type") == "stegverse.heartbeat_protocol.guardian_awareness", "record_type")
    require(data.get("source_repository") == "StegVerse-Labs/.github", "source_repository")
    require(data.get("source_goal") == "HEARTBEAT-PROTOCOL-ANCHOR-013", "source_goal")

    refs = data.get("source_refs", {})
    for key in ("semantics_handoff", "identifier_encoding_handoff", "live_status", "live_proof_handoff", "validation_receipt"):
        require(bool(refs.get(key)), f"source ref {key}")

    protocol = data.get("protocol", {})
    require(protocol.get("anchor_epoch") == 32, "anchor_epoch")
    require(protocol.get("anchor_heartbeat_id") == "HB-0000000W", "anchor_heartbeat_id")
    encoding = protocol.get("heartbeat_identifier_encoding", {})
    require(encoding.get("encoding") == "FIXED_WIDTH_BASE36", "identifier encoding")
    require(encoding.get("prefix") == "HB-", "identifier prefix")
    require(encoding.get("width") == 8, "identifier width")
    require(encoding.get("alphabet") == "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", "identifier alphabet")
    require(encoding.get("integer_epoch_remains_canonical") is True, "integer epoch canonical")
    require(encoding.get("reversible") is True, "identifier reversible")
    require(protocol.get("anchor_time_utc") == "2026-08-23T19:00:00.000Z", "anchor_time_utc")
    require(protocol.get("period_ms") == 10, "period_ms")
    require(protocol.get("reference_rate_hz") == 100, "reference_rate_hz")
    require(protocol.get("progression_dependency") == "OSCILLATOR_ONLY", "progression_dependency")
    for key in ("continuous_process_required", "resident_sampler_required_for_progression", "observation_is_causal"):
        require(protocol.get(key) is False, key)
    require(protocol.get("missed_references_continue_to_exist") is True, "missed_references_continue_to_exist")
    require(protocol.get("live_proof_state") == "COMPLETED", "live_proof_state")
    require(protocol.get("live_proof_transition_id") == "INDEPENDENT_HEARTBEAT_LIVE_PROOF_VERIFIED", "live_proof_transition_id")

    guardian = data.get("guardian_interpretation", {})
    for key in (
        "heartbeat_reference_is_guardian_authority",
        "heartbeat_reference_is_enforcement_trigger",
        "heartbeat_reference_is_admissibility",
        "heartbeat_reference_is_custody",
        "heartbeat_reference_is_publication_authority",
        "heartbeat_reference_is_execution_authority",
        "guardian_observation_causes_heartbeat_progression",
        "repository_orchestration_heartbeat_is_protocol_epoch",
    ):
        require(guardian.get(key) is False, key)
    require(guardian.get("repository_orchestration_heartbeat_role") == "WORKLOAD_HEALTH_PROJECTION_ONLY", "repository_orchestration_heartbeat_role")
    require(guardian.get("time_role") == "WATCHDOG_ONLY", "time_role")

    hil = data.get("hil_boundary", {})
    require(hil.get("hil_guardian_task") == "GUARDIAN-HIL-0001", "hil_guardian_task")
    require(hil.get("hil_dependency_state") == "BLOCKED_BUT_OBSERVED", "hil_dependency_state")
    require(hil.get("heartbeat_awareness_satisfies_hil_dependencies") is False, "heartbeat_awareness_satisfies_hil_dependencies")
    require(hil.get("heartbeat_awareness_grants_guardian_hil_interpretation") is False, "heartbeat_awareness_grants_guardian_hil_interpretation")

    authority = data.get("authority", {})
    for key in ("guardian_enforcement", "override", "execution", "publication", "deployment", "release", "custody", "admissibility", "heartbeat_timing"):
        require(authority.get(key) is False, f"authority {key}")

    require(data.get("credential_authority") == "TV/TVC", "credential_authority")
    require(data.get("github_runtime_authority") == "NONE", "github_runtime_authority")
    require(data.get("third_party_runtime_required") is False, "third_party_runtime_required")
    require(data.get("manual_user_action_required") is False, "manual_user_action_required")
    print("PASS: bounded HB32 Guardian awareness validated")


if __name__ == "__main__":
    main()
