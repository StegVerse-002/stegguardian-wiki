import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "data" / "cross-wiki-metadata-graph.json"
REQUIRED_NODES = {
    "stegguardian-wiki",
    "admissibility-wiki",
    "stegverse-site",
    "stegtalk-wiki",
}
REQUIRED_EDGES = {
    ("stegguardian-wiki", "admissibility-wiki", "derives_boundary_terms_from"),
    ("stegguardian-wiki", "stegverse-site", "publishing_mesh_peer"),
    ("stegguardian-wiki", "stegtalk-wiki", "documents_guardian_controls_for"),
}
REQUIRED_NON_CLAIMS = {
    "cross_wiki_authority_granted": False,
    "public_url_confirmed_by_connector": False,
    "standing_conferred": False,
    "execution_authority": False,
}


def main() -> int:
    errors = []
    if not GRAPH.exists():
        errors.append("missing_cross_wiki_metadata_graph")
        payload = {}
    else:
        payload = json.loads(GRAPH.read_text(encoding="utf-8"))

    if payload.get("graph_type") != "stegverse_cross_wiki_metadata_graph_seed":
        errors.append("graph_type_mismatch")
    if payload.get("scope") != "guardian_seed":
        errors.append("scope_mismatch")

    nodes = {node.get("id"): node for node in payload.get("nodes", [])}
    for node_id in REQUIRED_NODES:
        if node_id not in nodes:
            errors.append("missing_node:" + node_id)

    guardian = nodes.get("stegguardian-wiki", {})
    for record in [
        "data/page-index.json",
        "data/page-metadata.schema.json",
        "data/page-relationship-graph.json",
        "data/public-records-manifest.json",
    ]:
        if record not in guardian.get("machine_records", []):
            errors.append("guardian_missing_machine_record:" + record)
        if not (ROOT / record).exists():
            errors.append("missing_local_machine_record:" + record)

    edges = {
        (edge.get("from"), edge.get("to"), edge.get("relationship"))
        for edge in payload.get("edges", [])
    }
    for edge in REQUIRED_EDGES:
        if edge not in edges:
            errors.append("missing_edge:" + "->".join(edge))

    verification = payload.get("verification_state", {})
    if verification.get("guardian_local_records") != "installed":
        errors.append("guardian_local_records_state_mismatch")
    if verification.get("cross_wiki_public_url_confirmation") != "pending":
        errors.append("public_url_confirmation_must_remain_pending")
    if verification.get("cross_wiki_machine_record_confirmation") != "pending":
        errors.append("machine_record_confirmation_must_remain_pending")

    non_claims = payload.get("non_claims", {})
    for key, value in REQUIRED_NON_CLAIMS.items():
        if non_claims.get(key) is not value:
            errors.append("non_claim_mismatch:" + key)

    if errors:
        print("CROSS WIKI METADATA GRAPH: FAIL - " + ", ".join(errors))
        return 1
    print("CROSS WIKI METADATA GRAPH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
