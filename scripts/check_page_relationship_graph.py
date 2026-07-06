import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "page-index.json"
GRAPH = ROOT / "data" / "page-relationship-graph.json"
SCHEMA = ROOT / "data" / "page-metadata.schema.json"

REQUIRED_NODES = {
    "stegtalk-guardian-account-boundary",
    "guardian-account-boundary-vocabulary",
    "recovery-authority",
    "account-federation",
    "device-bound-guardian-enforcement",
    "entity-sandbox-runner-repair-reentry-flow",
    "llm-free-tier-trust-chain",
    "stegguardian-verification-status",
}

REQUIRED_EDGES = {
    ("stegtalk-guardian-account-boundary", "guardian-account-boundary-vocabulary", "uses_vocabulary"),
    ("stegtalk-guardian-account-boundary", "recovery-authority", "depends_on_boundary"),
    ("stegtalk-guardian-account-boundary", "account-federation", "depends_on_boundary"),
    ("stegtalk-guardian-account-boundary", "device-bound-guardian-enforcement", "depends_on_boundary"),
    ("entity-sandbox-runner-repair-reentry-flow", "stegtalk-guardian-account-boundary", "must_reenter_ingestion_before_authority"),
    ("llm-free-tier-trust-chain", "stegguardian-verification-status", "verified_by"),
    ("stegguardian-verification-status", "llm-free-tier-trust-chain", "summarizes_verification_for"),
}

REQUIRED_NON_CLAIMS = {
    "graph_grants_authority": False,
    "graph_confers_standing": False,
    "graph_verifies_public_url": False,
    "graph_replaces_commit_time_evaluation": False,
}


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.exists():
        errors.append("missing:" + str(path.relative_to(ROOT)))
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid_json:{path.relative_to(ROOT)}:{exc}")
        return {}


def main() -> int:
    errors: list[str] = []
    index = load_json(INDEX, errors)
    graph = load_json(GRAPH, errors)
    schema = load_json(SCHEMA, errors)

    if schema.get("title") != "StegGuardian Page Metadata":
        errors.append("schema_title_mismatch")
    if "related_pages" not in schema.get("required", []):
        errors.append("schema_missing_related_pages_requirement")

    index_paths = {page.get("path") for page in index.get("pages", [])}
    nodes = graph.get("nodes", [])
    node_ids = {node.get("id") for node in nodes}
    node_paths = {node.get("path") for node in nodes}

    for node_id in REQUIRED_NODES:
        if node_id not in node_ids:
            errors.append("missing_node:" + node_id)

    for path in node_paths:
        if path not in index_paths:
            errors.append("graph_node_path_missing_from_index:" + str(path))

    edge_tuples = {
        (edge.get("from"), edge.get("to"), edge.get("relationship"))
        for edge in graph.get("edges", [])
    }
    for edge in REQUIRED_EDGES:
        if edge not in edge_tuples:
            errors.append("missing_edge:" + "->".join(edge))

    for edge in graph.get("edges", []):
        if edge.get("from") not in node_ids:
            errors.append("edge_from_missing_node:" + str(edge.get("from")))
        if edge.get("to") not in node_ids:
            errors.append("edge_to_missing_node:" + str(edge.get("to")))

    non_claims = graph.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("graph_non_claim_mismatch:" + key)

    if errors:
        print("STEGGUARDIAN PAGE RELATIONSHIP GRAPH: FAIL - " + ", ".join(errors))
        return 1
    print("STEGGUARDIAN PAGE RELATIONSHIP GRAPH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
