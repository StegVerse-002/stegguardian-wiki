from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "GUARDIAN_BUILD_READINESS.md"

REQUIRED_TEXT = [
    "Guardian Build Readiness",
    "page index installed",
    "metadata schema installed",
    "relationship graph installed",
    "public records manifest installed",
    "verification status page installed",
    "workflow publication path wired",
    "observed publication success recorded",
    "aggregate local checker installed",
    "handoff deltas installed",
    "python scripts/check_guardian_local_state.py",
    "connector run ids pending",
    "independent public URL confirmation pending",
    "cross wiki metadata graph",
    "does not claim workflow metadata confirmation",
]


def main() -> int:
    errors = []
    if not SUMMARY.exists():
        errors.append("missing_guardian_build_readiness")
        text = ""
    else:
        text = SUMMARY.read_text(encoding="utf-8")

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("readiness_missing:" + item)

    if errors:
        print("GUARDIAN BUILD READINESS: FAIL - " + ", ".join(errors))
        return 1
    print("GUARDIAN BUILD READINESS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
