#!/usr/bin/env python3
"""Fetch and verify StegGuardian Wiki public machine-record URLs.

This script is intentionally not part of the default local aggregate gate because it
requires external network access to GitHub Pages. Run it from an environment that can
reach https://stegverse-002.github.io/stegguardian-wiki/.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://stegverse-002.github.io/stegguardian-wiki/"
EXPECTED_RECORDS = [
    "data/public-records-manifest.json",
    "data/cross-wiki-metadata-graph.json",
    "data/cross-wiki-health-status.json",
    "data/cross-wiki-health-status.schema.json",
    "data/deployment-receipt.json",
    "data/session-coordination-status.json",
    "data/pages-deployment-trigger-status.json",
    "data/live-public-record-url-verification.json",
]
EXPECTED_RECORD_TYPES = {
    "data/public-records-manifest.json": "stegguardian_public_records_manifest",
    "data/cross-wiki-metadata-graph.json": "stegguardian_cross_wiki_metadata_graph",
    "data/cross-wiki-health-status.json": "stegguardian_cross_wiki_health_status",
    "data/cross-wiki-health-status.schema.json": "StegVerse Cross-Wiki Health Status",
    "data/deployment-receipt.json": "stegguardian_pages_deployment_receipt",
    "data/session-coordination-status.json": "stegguardian_session_coordination_status",
    "data/pages-deployment-trigger-status.json": "stegguardian_pages_deployment_trigger_status",
    "data/live-public-record-url-verification.json": "stegguardian_live_public_record_url_verification",
}


def fetch_json(url: str, timeout: float) -> tuple[bool, dict[str, Any], str | None]:
    request = urllib.request.Request(url, headers={"User-Agent": "stegguardian-live-record-verifier/0.2"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", None)
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return False, {"http_status": exc.code}, f"http_error:{exc.code}"
    except Exception as exc:
        return False, {}, f"fetch_error:{type(exc).__name__}:{exc}"

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        return False, {"http_status": status, "bytes": len(body)}, f"json_decode_error:{exc}"

    observed_type = payload.get("record_type") or payload.get("manifest_type") or payload.get("title")
    payload_meta = {
        "http_status": status,
        "bytes": len(body.encode("utf-8")),
        "record_type": observed_type,
    }
    return status == 200, payload_meta, None


def build_report(base_url: str, timeout: float) -> dict[str, Any]:
    base = base_url if base_url.endswith("/") else base_url + "/"
    results = []
    all_ok = True
    for path in EXPECTED_RECORDS:
        url = base + path
        ok, meta, error = fetch_json(url, timeout)
        observed_type = meta.get("record_type")
        expected_type = EXPECTED_RECORD_TYPES[path]
        type_ok = observed_type == expected_type
        record_ok = ok and type_ok
        all_ok = all_ok and record_ok
        results.append(
            {
                "path": path,
                "url": url,
                "http_ok": ok,
                "type_ok": type_ok,
                "expected_type": expected_type,
                "observed_type": observed_type,
                "meta": meta,
                "error": error,
            }
        )

    return {
        "schema_version": "0.2.0",
        "record_type": "stegguardian_live_public_record_url_fetch_report",
        "repo": "StegVerse-002/stegguardian-wiki",
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "base_url": base,
        "all_machine_record_urls_confirmed": all_ok,
        "results": results,
        "non_claims": {
            "peer_machine_records_verified": False,
            "cross_repo_authority_granted": False,
            "standing_conferred": False,
            "execution_authority": False,
        },
    }


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--write-report", type=Path, default=None)
    args = parser.parse_args(argv)

    report = build_report(args.base_url, args.timeout)
    text = json.dumps(report, indent=2, sort_keys=True)
    if args.write_report:
        destination = args.write_report
        if not destination.is_absolute():
            destination = ROOT / destination
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if report["all_machine_record_urls_confirmed"] else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
