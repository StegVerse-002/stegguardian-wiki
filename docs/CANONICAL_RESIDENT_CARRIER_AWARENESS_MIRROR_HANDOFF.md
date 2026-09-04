# Canonical Resident Carrier Awareness Mirror Handoff

Repository: `StegVerse-002/stegguardian-wiki`  
Upstream source: `StegVerse-Labs/.github@b1f2bb3e33a1f93850811f0a751b2055519ab4dd`  
Upstream contract: `control/canonical-resident-carrier-contract.json`  
Authority effect: `NONE_AWARENESS_ONLY`

## Canonical architecture

StegGuardian documentation recognizes StegVerse-001, StegVerse-002, and SV-011 as consumers of the single canonical resident substrate:

```text
HB32 independent oscillator reference
-> HB-derived exact-byte InTr carrier (non-authorizing)
-> one StegVerse-Labs/.github WorkerCoordinator
-> canonical resident request dispatcher
-> task-specific fail-closed consumer/evidence
```

StegGuardian remains evaluation/protection-oriented and does not become heartbeat, WorkerCoordinator, credential, claim/fence, route, transition, execution, or custody authority through this awareness record.

Any future text implying a project-specific second heartbeat, scheduler, WorkerCoordinator, credential lane, claim/fence path, or independent resident runtime for SV001, SV002, or SV-011 is stale unless a later canonical source explicitly supersedes the shared-carrier contract.

## Evidence boundary

Shared architecture is merged upstream. Runtime activation remains task-specific: SV002 requires authentic terminal round-trip evidence; SV-011 requires authentic same-execution Phase-5 ALLOW/DENY evidence; terminal SV001 must not be rerun merely for carrier proof.

Credential authority remains `TV/TVC`; GitHub token runtime authority remains `NONE`.
