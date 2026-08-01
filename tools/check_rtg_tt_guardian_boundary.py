#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data/rtg-tt/guardian-boundary.v0.1.json'
d=json.loads(p.read_text())
assert d['contract_version']=='rtg-tt-v0.1'
assert d['site_source']=='StegVerse-Labs/Site@50d417b2dbf29d3812bdae8c3d1942b1ce5a5162'
assert d['stegcore_source']=='StegVerse-Labs/StegCore@47cb26c513c9404017e650e025b8cc14eb02c41c'
assert d['guardian_rules']['authority_escalation']=='DENY'
assert d['guardian_rules']['unresolved_evidence']=='DEFER'
assert all(v is False for v in d['authority'].values())
print('RTG_TT_GUARDIAN_BOUNDARY_PASS')
