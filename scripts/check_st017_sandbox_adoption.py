#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "templates/sandbox-first/stegguardian-wiki.sandbox-profile.json"
RUNNER = ROOT / "scripts/run_sandbox_validation.py"
WORKFLOW = ROOT / ".github/workflows/pages.yml"
HANDOFF = ROOT / "STEGGUARDIAN_WIKI_MIRROR_HANDOFF.md"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--structural-only", action="store_true")
    parser.parse_args()
    errors=[]
    for p in (PROFILE,RUNNER,WORKFLOW,HANDOFF):
        if not p.exists(): errors.append("missing:"+str(p.relative_to(ROOT)))
    if PROFILE.exists():
        try: profile=json.loads(PROFILE.read_text())
        except Exception as exc: errors.append("invalid_profile:"+str(exc)); profile={}
        if profile.get("repository")!="StegVerse-002/stegguardian-wiki": errors.append("profile_repository_mismatch")
        ids=[c.get("id") for c in profile.get("commands",[])]
        for required in ("compile-python","validate-guardian-local-state","validate-pages-workflow","validate-st017-adoption"):
            if required not in ids: errors.append("missing_command:"+required)
    if WORKFLOW.exists():
        text=WORKFLOW.read_text()
        for marker in ("pull_request:","validate:","python scripts/run_sandbox_validation.py","stegguardian-st017-sandbox-report","github.event_name != 'pull_request'","needs: validate","verify-live-public-records:"):
            if marker not in text: errors.append("workflow_missing:"+marker)
    if HANDOFF.exists() and "ST-017 Sandbox-First Adoption" not in HANDOFF.read_text(): errors.append("handoff_missing_st017")
    if errors:
        print("STEGGUARDIAN ST-017 ADOPTION: FAIL - "+", ".join(errors)); return 1
    print("STEGGUARDIAN ST-017 ADOPTION: PASS"); return 0
if __name__=="__main__": raise SystemExit(main())
