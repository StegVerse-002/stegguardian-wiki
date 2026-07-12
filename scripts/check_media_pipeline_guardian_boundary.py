#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "pages" / "media-pipeline-guardian-boundary.md"
INDEX = ROOT / "data" / "page-index.json"
HANDOFF = ROOT / "STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md"

PAGE_MARKERS = [
    "Status: downstream awareness-only summary",
    "StegVerse-Labs/collective-environment-engine",
    "GCAT-BCAT-Engine/Publisher",
    "StegVerse-Labs/Site/docs/media/media-pipeline-overview.md",
    "live camera use",
    "live microphone use",
    "public broadcast capability",
    "guardian_authority: false",
    "execution_authority: false",
    "broadcast_authority: false",
]

INDEX_MARKERS = [
    '"title": "Media Pipeline Guardian Boundary"',
    '"path": "pages/media-pipeline-guardian-boundary.md"',
    '"activation_state": "downstream_awareness_only"',
]

HANDOFF_MARKERS = [
    "pages/media-pipeline-guardian-boundary.md",
    "scripts/check_media_pipeline_guardian_boundary.py",
    "media pipeline downstream awareness",
]


def require(path: Path, markers: list[str]) -> list[str]:
    if not path.exists():
        return [f"missing file: {path.relative_to(ROOT)}"]
    text = path.read_text(encoding="utf-8")
    return [f"{path.relative_to(ROOT)} missing {marker!r}" for marker in markers if marker not in text]


def main() -> int:
    errors = []
    errors.extend(require(PAGE, PAGE_MARKERS))
    errors.extend(require(INDEX, INDEX_MARKERS))
    errors.extend(require(HANDOFF, HANDOFF_MARKERS))
    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("PASS media pipeline Guardian boundary")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
