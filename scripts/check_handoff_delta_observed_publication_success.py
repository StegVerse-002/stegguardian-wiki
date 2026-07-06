from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "docs" / "HANDOFF_DELTA_OBSERVED_PUBLICATION_SUCCESS.md"
EVIDENCE = ROOT / "OBSERVED_MACHINE_RECORD_PUBLICATION_EVIDENCE.md"

REQUIRED_TEXT = [
    "Handoff Delta: Observed Publication Success",
    "OBSERVED_MACHINE_RECORD_PUBLICATION_EVIDENCE.md",
    "scripts/check_observed_machine_record_publication_evidence.py",
    "python scripts/check_guardian_local_state.py",
    "deploy: success",
    "readiness: success",
    "page relationship graph: pass",
    "public records manifest: pass",
    "repo standards guardian summary: pass",
    "pages deployment: reported success",
    "connector_confirmed_run_ids: pending",
    "independent_public_url_confirmation: pending",
    "does not grant guardian enforcement authority",
]


def main() -> int:
    errors = []
    if not DELTA.exists():
        errors.append("missing_handoff_delta_observed_publication_success")
        text = ""
    else:
        text = DELTA.read_text(encoding="utf-8")

    if not EVIDENCE.exists():
        errors.append("missing_observed_machine_record_publication_evidence")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("delta_missing:" + item)

    if errors:
        print("HANDOFF DELTA OBSERVED PUBLICATION SUCCESS: FAIL - " + ", ".join(errors))
        return 1
    print("HANDOFF DELTA OBSERVED PUBLICATION SUCCESS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
