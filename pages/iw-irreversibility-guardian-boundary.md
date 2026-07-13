# IW Irreversibility Guardian Boundary

## Canonical source

```text
source_repository: Admissible-Existence/IW
source_commit: 87fd24ea829b413373ea42381dd0b08d45b79239
canonical_markdown: docs/irreversibility.md
publication_pdf: docs/irreversibility.pdf
authority: false
```

This Guardian page describes posture before and near a practical irreversibility boundary. It does not grant Guardian execution authority.

## Latest safe intervention point

```text
t_i^- = expected_irreversibility - confidence_multiplier × uncertainty
L_total = sense + transmit + infer + authorize + actuate + stabilize
t_c = t_i^- - L_total
```

Guardian posture must account for total intervention latency. A physically reversible state may already be practically irreversible when the remaining time is less than the time needed to sense, infer, authorize, actuate, and stabilize.

## Escalation posture

```text
WARN
```

Use when intervention remains possible but recovery volume or safe-decision margin is degrading. Guardian behavior should surface the shrinking margin, preserve evidence, and avoid representing warning as authorization.

```text
STOP
```

Use when practical recovery is no longer available, recovery volume is exhausted, or no usable recovery path remains. Guardian posture should block further commitment within its existing delegated scope and preserve reconstructable evidence.

```text
FAIL_CLOSED
```

Use when a required warrant, evidence item, authority reference, or current recovery path is absent, stale, malformed, or inconsistent. Missing standing must not be converted into inferred permission.

## Recovery-path gates

A recovery path is usable only when it is:

```text
physically available
AND authorized
AND evidentially supported
AND current
AND executable within the remaining recovery time
```

## Required warrants

```text
physical
governance
recoverability
observability
```

Guardian awareness of these warrants does not create them.

## Boundary

```text
Guardian awareness != Guardian authority
WARN != permission
STOP != universal physical impossibility
FAIL_CLOSED != proof of harm
Reference page != live enforcement
```

The IW repository remains the canonical source. This page preserves source attribution and `authority: false`.
