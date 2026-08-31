#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
idx=json.loads((ROOT/"data/cosv/task-vector-index.json").read_text())
state=json.loads((ROOT/"data/stegguardian-wiki-orchestration-state.json").read_text())
blocked={x["task_id"]:x for x in state["blocked_tasks"]}
assert idx["profile"]=="task.v1" and idx["width"]==14 and idx["authority_effect"]=="NONE"
row=idx["tasks"][0]
assert row["task_id"]=="GUARDIAN-HIL-0001"
assert row["binding_mode"]=="EXTERNAL_PROJECTION_READ_ONLY"
rec=json.loads((ROOT/row["vector_ref"]).read_text())
m=rec["exact_metrics"]
assert rec["vector"]==row["vector"]=="60000000109000"
assert m["lifecycle"]=="BLOCKED"
assert m["blocker_count"]==len(blocked["GUARDIAN-HIL-0001"]["dependencies"])==9
assert m["canonical_owner_installed"] is True
assert m["evidence_complete"] is False
assert m["activated"] is False and m["propagated"] is False
assert rec["authority_effect"]=="NONE"
assert state["policy"]["guardian_interpretation_requires_complete_upstream_chain"] is True
assert state["authority"]["guardian_enforcement"] is False
assert idx["coverage"]["repository_vector_present_claimed"] is False
print("GUARDIAN_COSV_PROJECTION_PASS blockers=9 repository_vector_present=false")
