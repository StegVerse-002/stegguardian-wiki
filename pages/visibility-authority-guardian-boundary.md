# Visibility and Authority Guardian Boundary

StegGuardian must not infer authority from visibility, acknowledgement, mirroring, indexing, rendering, or reconstruction.

A publicly visible record may still be review-only and non-authoritative. Guardian logic must evaluate the declared process state and each authority dimension independently before allowing any consequential action.

## Guardian invariants

```text
public visibility != Guardian authority
acknowledgement != endorsement
acknowledgement != attribution
reference != public association
reconstruction != authorization
publication != execution authority
```

When `process_state` is `REVIEW_ONLY`, every authority flag must remain false and endorsement, compatibility, and interoperability must remain `NONE`. Any conflict fails closed.

Guardian enforcement may consume a valid authority decision as evidence, but it does not create the decision, expand its scope, or convert visibility into authority. A missing, malformed, stale, conflicting, or visibility-derived authority source must produce a blocked or quarantined posture before consequence.

The implemented ecosystem chain is:

- SDK: declares state and produces acknowledgement or transition receipts;
- Publisher: enforces consequential publication actions;
- Site: renders human and machine projections without authority inference;
- Master-Records: custodies and reconstructs records without creating authorization;
- StegGuardian: preserves the boundary at enforcement and recovery surfaces.

This page is documentation and propagation awareness only. It grants no Guardian enforcement, publication, execution, custody, release, deployment, standing, or admissibility authority.
