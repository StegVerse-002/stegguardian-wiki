# Entity Sandbox Runner Repair Reentry Flow

## Status

```text
source_repo: StegGhost/entity-sandbox-runner
release_goal: admissibility_plane_activation_candidate
wiki_status: documentation_surface_installed
activation_state: pending_external_evidence
```

## Guardian relevance

The entity sandbox runner now describes a repair flow where sandbox work is non-authoritative and must re-enter ingestion before the next state can be evaluated.

This is relevant to StegGuardian because guardian, recovery, account, and boundary enforcement flows must not treat repair outputs as direct authority.

## Documented flow

```text
failed or partial startup signal
→ manifest-bearing repair request
→ ingestion routing
→ transition table resolution
→ CGE route fingerprint
→ transition receipt
→ sandbox repair
→ repair result
→ ingestion re-entry
→ startup repair result application
→ admissibility verification
```

## Boundary

Sandbox repair is not enforcement authority.

A repaired artifact must return through ingestion before it can affect guardian-facing or boundary-facing state.

## Non-claims

```text
This page does not certify runtime admissibility.
This page does not issue commit-time permission.
This page does not replace entity-sandbox-runner transition receipts.
This page does not make StegGuardian the source of truth for sandbox repair outcomes.
```

## Required source evidence

```text
StegGhost/entity-sandbox-runner release/entity_sandbox_runner_admissibility_plane_release_packet.json
StegGhost/entity-sandbox-runner brain_reports/admissibility_plane_verification.json
StegGhost/entity-sandbox-runner brain_reports/release_integration_verification.json
StegGhost/entity-sandbox-runner transition_receipts/
```
