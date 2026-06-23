# Device-Bound Guardian Enforcement

## Purpose

Device-bound guardian enforcement describes when a guardian capability may bind protection, recovery, or enforcement behavior to a specific device or device state.

## Boundary

Device-bound enforcement must be explicitly authorized. It must not be inferred from local account readiness, guardian documentation, or prototype candidate status.

## Required Inputs

A device-bound enforcement claim should identify:

- device or device class
- account or entity protected
- guardian role
- enforcement scope
- evidence references
- device state or attestation reference
- policy reference
- delegation reference when applicable
- validity window
- recovery or fail-closed behavior
- receipt output

## Non-Claims

Device-bound enforcement does not follow automatically from:

- account profile readiness
- account session readiness
- local shell readiness
- public discovery readiness
- boundary documentation

## Standing Rule

A device-bound guardian action is admissible only when current authority, policy, evidence, device state, and context support the action at the time of enforcement.
