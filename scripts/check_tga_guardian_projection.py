#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'pages' / 'temporal-governed-analysis-guardian-boundary.md'
STATUS = ROOT / 'data' / 'tga-guardian-projection-status.json'
HANDOFF = ROOT / 'docs' / 'TGA_GUARDIAN_PROJECTION_MIRROR_HANDOFF.md'


def main() -> int:
    for path in (PAGE, STATUS, HANDOFF):
        if not path.is_file():
            print(f'TGA_GUARDIAN_PROJECTION=FAIL missing={path.relative_to(ROOT)}')
            return 1
    page = PAGE.read_text(encoding='utf-8')
    status = json.loads(STATUS.read_text(encoding='utf-8'))
    handoff = HANDOFF.read_text(encoding='utf-8')
    markers = [
        'Canonical representation is not canonical reality',
        'UNRESOLVED', 'CONTRADICTORY',
        'Counterfactual analysis cannot rewrite historical applicability',
        'Narration is not canonical evidence',
        'does not satisfy `GUARDIAN-HIL-0001`',
    ]
    missing = [m for m in markers if m not in page]
    if missing:
        print('TGA_GUARDIAN_PROJECTION=FAIL missing_markers=' + repr(missing))
        return 1
    if any(status.get('authority', {}).values()):
        print('TGA_GUARDIAN_PROJECTION=FAIL authority_escalation')
        return 1
    if status.get('hil_dependency_effect') is not False:
        print('TGA_GUARDIAN_PROJECTION=FAIL hil_dependency_effect')
        return 1
    if not all(status.get('preserved', {}).values()):
        print('TGA_GUARDIAN_PROJECTION=FAIL preserved_semantics')
        return 1
    if 'authority_effect: NONE_GOVERNANCE_PROJECTION_ONLY' not in handoff:
        print('TGA_GUARDIAN_PROJECTION=FAIL handoff_boundary')
        return 1
    print('TGA_GUARDIAN_PROJECTION=PASS')
    print('authority_effect=NONE_GOVERNANCE_PROJECTION_ONLY')
    print('hil_dependency_effect=false')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
