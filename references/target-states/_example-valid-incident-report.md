# Target State: Valid Incident Report

> Category: valid-artifact

## Scope

Defines what a correct, complete incident report looks like. Used when the agent generates or reviews an incident report artifact.

## Correct State

A valid incident report:
- Has all summary fields populated (date, reporter, site, affected object, severity, status)
- Includes the reported symptom in the user's words, not paraphrased
- Lists every system checked with its finding (not just the ones that had problems)
- Identifies a root cause (or explicitly states "root cause not yet determined")
- Describes the resolution with specific actions taken
- Includes verification that the fix worked (read-back, monitoring check, user confirmation)
- Has a timeline with at least: symptom reported, investigation started, resolution applied
- Lists any follow-up actions with owners

## Evidence Surfaces

- Platform APIs (for systems-checked data)
- User report (for symptom description)
- Resolution log (for what was done)
- Monitoring (for verification)

## Mandatory Comparisons

- Reported symptom vs actual finding (are they consistent?)
- Resolution vs verification (does the fix actually address the root cause?)
- Systems checked vs applicability rules (were all required systems checked?)
- Timeline vs tool call log (are the timestamps consistent?)

## Notes

This target state is used in two ways:
1. When the agent generates an incident report: check it against this target state before delivering
2. When the agent reviews an existing incident report: identify which conditions are not met
