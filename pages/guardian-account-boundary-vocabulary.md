# Guardian Account Boundary Vocabulary

## Purpose

This page defines baseline StegGuardian wiki terms for account, guardian, recovery, and boundary documentation.

## Terms

### Account Profile

A local record describing an account holder, display identity, and linked entities. An account profile is not, by itself, external identity federation or production login authority.

### Account Session

A local runtime record describing an account profile operating through a shell, view, or event sequence. An account session is not, by itself, cross-device persistence or recovery authority.

### Guardian Boundary

The declared limit of what a guardian component may observe, protect, recover, or enforce. A guardian boundary must distinguish prototype documentation from production enforcement.

### Recovery Authority

The authority to restore or rebind access after loss, compromise, or device transition. Recovery authority requires explicit standing and must not be inferred from local account readiness.

### Local Candidate

A non-production state showing that a local prototype path is built and documented. A local candidate is not production approval.

### Production Ready

A state that may only be claimed when the governing source artifact explicitly records `production_ready: true`.

## Required Boundary Rule

Guardian/account pages must not imply external account federation, production identity, recovery authority, or guardian enforcement unless a source artifact explicitly grants that standing.
