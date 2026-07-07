import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    [sys.executable, "scripts/check_guardian_local_state.py"],
    [sys.executable, "scripts/check_guardian_build_readiness.py"],
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
        print("STEGGUARDIAN LOCAL STATE WITH READINESS: FAIL - " + "; ".join(failures))
        return 1

    print("STEGGUARDIAN LOCAL STATE WITH READINESS: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
