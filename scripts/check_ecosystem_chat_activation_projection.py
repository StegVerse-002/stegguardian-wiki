#!/usr/bin/env python3
"""Validate and opportunistically refresh the non-authorizing Ecosystem Chat Guardian projection."""
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/ecosystem-chat-activation-status.json"
STATE_URL = "https://raw.githubusercontent.com/StegVerse-Labs/Site/main/data/ecosystem-chat-activation-state.json"
PACKET_URL = "https://raw.githubusercontent.com/StegVerse-Labs/Site/main/data/ecosystem-chat-activation-propagation.json"
REPOSITORY = "StegVerse-002/stegguardian-wiki"


def digest(value: dict, field: str) -> str:
    material = dict(value)
    material.pop(field, None)
    return hashlib.sha256(json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "StegGuardian-Ecosystem-Chat-Projection/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        value = json.loads(response.read().decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError("source_not_object")
    return value


def validate(value: dict) -> None:
    if value.get("schema") != "stegverse.ecosystem_chat.guardian_projection.v1":
        raise ValueError("projection_schema_mismatch")
    if value.get("repository") != REPOSITORY:
        raise ValueError("projection_repository_mismatch")
    if value.get("manual_user_action_required") is not False:
        raise ValueError("manual_action_must_remain_false")
    boundary = value.get("authority_boundary") or {}
    for key in (
        "projection_grants_guardian_authority",
        "projection_grants_execution_authority",
        "projection_grants_release_authority",
        "projection_is_custody",
    ):
        if boundary.get(key) is not False:
            raise ValueError(f"authority_escalation:{key}")
    if digest(value, "projection_sha256") != value.get("projection_sha256"):
        raise ValueError("projection_hash_mismatch")


def refresh() -> dict:
    state = fetch(STATE_URL)
    packet = fetch(PACKET_URL)
    if digest(state, "state_sha256") != state.get("state_sha256"):
        raise ValueError("source_state_hash_mismatch")
    if digest(packet, "packet_sha256") != packet.get("packet_sha256"):
        raise ValueError("source_packet_hash_mismatch")
    if packet.get("source_state_sha256") != state.get("state_sha256"):
        raise ValueError("source_binding_mismatch")
    destinations = {item.get("repository"): item for item in packet.get("destinations", []) if isinstance(item, dict)}
    destination = destinations.get(REPOSITORY)
    if destination is None:
        raise ValueError("destination_not_declared")
    ready = state.get("state") == "ACTIVATION_COMPLETE" and packet.get("state") == "READY_FOR_DOWNSTREAM_INGESTION" and destination.get("ingestion_ready") is True
    projection = {
        "schema": "stegverse.ecosystem_chat.guardian_projection.v1",
        "repository": REPOSITORY,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "state": "VERIFIED_ACTIVATION_OBSERVED" if ready else "ACTIVATION_EVIDENCE_PENDING",
        "source_repository": "StegVerse-Labs/Site",
        "source_state_sha256": state.get("state_sha256"),
        "source_packet_sha256": packet.get("packet_sha256"),
        "manual_user_action_required": False,
        "authority_boundary": {
            "projection_grants_guardian_authority": False,
            "projection_grants_execution_authority": False,
            "projection_grants_release_authority": False,
            "projection_is_custody": False,
        },
    }
    projection["projection_sha256"] = digest(projection, "projection_sha256")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(projection, indent=2) + "\n", encoding="utf-8")
    return projection


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checked-in-only", action="store_true")
    args = parser.parse_args()
    if args.checked_in_only:
        value = json.loads(OUTPUT.read_text(encoding="utf-8"))
    else:
        try:
            value = refresh()
        except Exception as exc:
            value = json.loads(OUTPUT.read_text(encoding="utf-8"))
            print(f"ECOSYSTEM CHAT GUARDIAN PROJECTION: SOURCE_PENDING ({type(exc).__name__})")
    validate(value)
    print(f"ECOSYSTEM CHAT GUARDIAN PROJECTION: PASS ({value['state']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
