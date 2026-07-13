#!/usr/bin/env python3
from __future__ import annotations
import json, shutil, subprocess, sys, tempfile, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    profile_path = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "templates/sandbox-first/stegguardian-wiki.sandbox-profile.json")
    output_path = ROOT / (sys.argv[2] if len(sys.argv) > 2 else "reports/sandbox-first-validation.report.json")
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    exclude = set(profile.get("exclude", []))
    results = []
    with tempfile.TemporaryDirectory(prefix="stegguardian-st017-") as tmp:
        sandbox = Path(tmp) / "repo"
        shutil.copytree(ROOT, sandbox, ignore=shutil.ignore_patterns(*exclude))
        (sandbox / "reports").mkdir(exist_ok=True)
        for command in profile["commands"]:
            started = time.monotonic()
            try:
                completed = subprocess.run(command["argv"], cwd=sandbox, text=True, capture_output=True, timeout=profile.get("timeout_seconds", 300), check=False)
                passed = completed.returncode == command.get("expected_exit", 0)
                result = {"id": command["id"], "status": "PASS" if passed else "FAIL", "exit_code": completed.returncode, "duration_seconds": round(time.monotonic()-started, 3), "stdout_tail": completed.stdout[-4000:], "stderr_tail": completed.stderr[-4000:]}
            except subprocess.TimeoutExpired as exc:
                passed = False
                result = {"id": command["id"], "status": "FAIL", "timed_out": True, "duration_seconds": round(time.monotonic()-started, 3), "stdout_tail": str(exc.stdout or "")[-4000:], "stderr_tail": str(exc.stderr or "")[-4000:]}
            results.append(result)
            if not passed:
                break
    status = "PASS" if len(results) == len(profile["commands"]) and all(r["status"] == "PASS" for r in results) else "FAIL"
    report = {"schema_version": "1.0.0", "record_type": "sandbox_validation_report", "repository": profile["repository"], "profile_id": profile["profile_id"], "observed_at": datetime.now(timezone.utc).isoformat(), "sandbox_status": status, "github_actions_status": "NOT_OBSERVED", "public_output_status": "NOT_VERIFIED", "results": results, "non_claims": {"remote_ci_success": False, "public_output_verified": False, "deployment_authority": False, "execution_authority": False, "standing": False, "admissibility": False}}
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(f"ST-017 SANDBOX: {status}")
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
