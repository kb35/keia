# Project Management

> **Owner:** {your project management lead}

## Scope

Project tracking, status reporting, vendor coordination, timeline management, and milestone delivery. Covers the lifecycle from project creation through closeout. Does NOT cover the technical execution of project work (that belongs in domain-specific domains like Infrastructure or AV).

## Topics

### Portfolio Health

Active project tracking, stage progression, risk identification, overdue detection.

- **Topic index:** `references/topics/project-management/portfolio-health.md`
- **Object profile:** `references/object-profiles/project-record-profile.yaml`
- **Reference data:** `references/project-tracker-reference.yaml`
- **Tools:** project_tracker_read, email_read, calendar_read
- **Source Registry:** `registry/sources/_example-source.yaml` -> Project management guides

**Why stage progression matters:** A project stuck in the same stage for more than 2 weeks without updated notes is a signal. It may be blocked, deprioritized, or forgotten. The agent should flag stale projects proactively.

### Vendor Coordination

Vendor communication, quote tracking, scheduling, scope alignment.

- **Topic index:** (create when needed)
- **Tools:** email_read, document_read, project_tracker_read
- **Source Registry:** Vendor SOWs, quotes, and contracts in document storage

### Meeting Preparation

Assembling context for project review meetings, stakeholder updates, and sync calls.

- **Topic index:** (create when needed)
- **Tools:** calendar_read, email_read, project_tracker_read, document_read

## Cross-Domain Connections

- When a project involves device installation -> check the relevant technical domain (Infrastructure, AV, Print)
- When a project has open tickets -> check Support domain
- When a project status is reported to leadership -> check Organization domain for stakeholder context
- When a vendor deliverable is due -> check Delivery domain for change management requirements

## Knowledge Layer Checklist

- [ ] Project phase definitions and stage numbers
- [ ] Status reporting template
- [ ] Vendor onboarding standards
- [ ] Meeting preparation checklist
