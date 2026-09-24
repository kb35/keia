# Example: Project Management Domain

This example proves the framework works beyond hardware and infrastructure. A project record is a managed object, just like a network switch, with its own "healthy state" definition across multiple platforms.

## Domain Index

**File:** `references/domains/project-management.md`

The project management domain covers portfolio tracking, vendor coordination, and meeting preparation. It does NOT cover technical execution (that belongs in domain-specific domains).

## Topic Index

**File:** `references/topics/project-management/portfolio-health.md`

Comparison questions:
- Has the project stage progressed in the last 2 weeks?
- Are notes fresh (updated within 14 days)?
- Are all required fields populated?
- Is the project past any deadline without a status update?

## Object Profile: Project Record

**File:** `references/object-profiles/project-record-profile.yaml`

The project record profile shows that ANY managed object can have a profile, not just hardware:

| Platform | Required Fields | Healthy Indicators |
|---------|----------------|-------------------|
| Project tracker | name, stage, engineer, PM, dates, notes | Stage current, notes fresh, fields populated |
| Email | (none required) | Recent communication if project is active |
| Calendar | (none required) | Milestones have calendar entries |
| Document storage | scope_document | Scope doc exists and is linked |

**Consistency checks:**
- Stage in tracker matches phase in scope document
- Assigned engineer appears in recent communications
- Key dates have corresponding calendar entries

**Discrimination logic:**

| Symptom | Likely Causes | First Check |
|---------|-------------|-------------|
| Project stale | Waiting on vendor, blocked, deprioritized, forgotten | Project tracker notes |
| Project past due | Scope change, vendor delay, resource conflict | Project tracker dates |

**Not-applicable:** inventory, DNS, monitoring, fleet management (projects aren't devices)

## What This Proves

The same 9 primitives, the same schemas, the same workflow, applied to a completely different domain. Replace "switch" with "project," replace "Netbox" with "Smartsheet," and the architecture holds.
