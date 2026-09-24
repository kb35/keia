# Project Management Topic: Portfolio Health

## Scope

Monitoring the health of active projects across the portfolio: stage progression, note freshness, deadline compliance, risk identification, and assignment completeness.

## Relevant Objects

- project
- portfolio

## Evidence Surfaces

- `references/object-profiles/project-record-profile.yaml`
- `registry/sources/_example-source.yaml`
- Project tracker (stage, dates, assignments, notes)
- Email (recent vendor/stakeholder communications)
- Calendar (upcoming milestones, meetings)
- Document storage (scope documents, vendor quotes)

## Comparison Questions

- Is the project stage current (has it progressed in the last 2 weeks)?
- Are the notes fresh (updated within 14 days)?
- Are all required fields populated (stage, assigned engineer, assigned PM, dates)?
- Is the project past any deadline without a status update?
- Does the project have a scope document linked?

## Expansion Triggers

- Project involves devices -> expand into relevant technical domain for device-level verification
- Project has open incidents -> expand into Support domain
- Project deadline passed with no update -> flag as risk, expand into email for recent communications
- Multiple projects at same site are stale -> possible site-level coordination issue, expand scope to site
