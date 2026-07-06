from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "docs" / "MACHINE_RECORD_PUBLICATION_STATUS.md"
RECORDS = [
    ROOT / "data" / "page-index.json",
    ROOT / "data" / "page-metadata.schema.json",
    ROOT / "data" / "page-relationship-graph.json",
]

REQUIRED_TEXT = [
    "Machine Record Publication Status",
    "data/page-index.json",
    "data/page-metadata.schema.json",
    "data/page-relationship-graph.json",
    "data/page-index.json: published by current static site path",
    "data/page-metadata.schema.json: installed locally, public exposure pending",
    "data/page-relationship-graph.json: installed locally, public exposure pending",
    "does not claim public URL verification",
    "connector-confirmed workflow metadata",
]


def main() -> int:
    errors = []
    if not STATUS.exists():
        errors.append("missing_machine_record_publication_status")
        text = ""
    else:
        text = STATUS.read_text(encoding="utf-8")

    for record in RECORDS:
        if not record.exists():
            errors.append("missing_record:" + str(record.relative_to(ROOT)))

    for item in REQUIRED_TEXT:
        if item not in text:
            errors.append("status_missing:" + item)

    if errors:
        print("MACHINE RECORD PUBLICATION STATUS: FAIL - " + ", ".join(errors))
        return 1
    print("MACHINE RECORD PUBLICATION STATUS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
