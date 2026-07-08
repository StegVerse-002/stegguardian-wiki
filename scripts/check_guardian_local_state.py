import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    [sys.executable, "scripts/check_llm_free_tier_trust_chain_page.py"],
    [sys.executable, "scripts/check_page_index.py"],
    [sys.executable, "scripts/check_page_relationship_graph.py"],
    [sys.executable, "scripts/check_cross_wiki_metadata_graph.py"],
    [sys.executable, "scripts/check_machine_record_publication_status.py"],
    [sys.executable, "scripts/check_public_records_manifest.py"],
    [sys.executable, "scripts/check_pages_deployment_trigger_status.py"],
    [sys.executable, "scripts/check_observed_machine_record_publication_evidence.py"],
    [sys.executable, "scripts/check_handoff_delta_observed_publication_success.py"],
    [sys.executable, "scripts/check_public_url_machine_records_delta.py"],
    [sys.executable, "scripts/check_public_url_confirmation_plan.py"],
    [sys.executable, "scripts/check_handoff_delta_public_url_confirmation_plan.py"],
    [sys.executable, "scripts/check_pages_workflow_validation.py"],
    [sys.executable, "scripts/check_workflow_verification_status.py"],
    [sys.executable, "scripts/check_aggregate_workflow_delta.py"],
    [sys.executable, "scripts/check_user_observed_workflow_evidence.py"],
    [sys.executable, "scripts/check_public_url_verification_status.py"],
    [sys.executable, "scripts/check_stegguardian_verification_status.py"],
]


def main() -> int:
    failures = []
    for command in COMMANDS:
        result = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        print("$ " + " ".join(command))
        print(result.stdout.rstrip())
        if result.returncode != 0:
            failures.append(" ".join(command))

    if failures:
        print("STEGGUARDIAN LOCAL STATE: FAIL - " + "; ".join(failures))
        return 1

    print("STEGGUARDIAN LOCAL STATE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
