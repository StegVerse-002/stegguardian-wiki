#!/usr/bin/env python3
"""Fail closed if Guardian activation loses terminal-custody or serialized workflow binding."""
from pathlib import Path
import sys

IMPORTER = Path("scripts/import_publisher_ecosystem_chat_activation.py")
LOCAL_CHAIN = Path("scripts/check_guardian_local_state.py")
WORKFLOW = Path(".github/workflows/pages.yml")


def fail(message: str) -> None:
    print(f"GUARDIAN_ACTIVATION_ORCHESTRATION_CONTRACT: FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for path in (IMPORTER, LOCAL_CHAIN, WORKFLOW):
        if not path.is_file():
            fail(f"missing {path}")
    importer = IMPORTER.read_text(encoding="utf-8")
    chain = LOCAL_CHAIN.read_text(encoding="utf-8")
    workflow = WORKFLOW.read_text(encoding="utf-8")
    for marker in (
        "terminal_custody_verified",
        "terminal_custody_sha256",
        "master-records/orchestration",
        "custody_repository_mismatch",
        "ecosystem_chat_activation_projection.v2",
        '"projection_is_guardian_enforcement_authority": False',
    ):
        if marker not in importer:
            fail(f"importer marker absent: {marker}")
    if "scripts/check_guardian_activation_orchestration_contract.py" not in chain:
        fail("contract is not bound into Guardian local-state validation")
    on_block = workflow.split("permissions:", 1)[0]
    if "schedule:" in on_block:
        fail("Pages workflow must not own an hourly timer")
    for marker in (
        "cancel-in-progress: true",
        "github.event_name == 'push'",
        "Validate Guardian activation orchestration contract",
        "python scripts/check_guardian_activation_orchestration_contract.py",
    ):
        if marker not in workflow:
            fail(f"workflow marker absent: {marker}")
    if "cancel-in-progress: false" in workflow:
        fail("superseded Pages runs must be cancelled")
    print("GUARDIAN_ACTIVATION_ORCHESTRATION_CONTRACT: PASS")
    print("terminal_custody_required=true")
    print("guardian_authority_granted=false")
    print("schedule_authority=false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
