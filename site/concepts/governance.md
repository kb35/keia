# Governance Model

The governance model controls what the agent is allowed to do, how writes are verified, and what safety mechanisms prevent runaway behavior.

## Tool Tiers

Every tool action is classified before it can be used:

| Tier | Rule | Confirmation | Auto-Approve |
|------|------|-------------|-------------|
| :material-eye:{ .middle } **Read** | Execute autonomously | None | Yes |
| :material-pencil:{ .middle } **Write** | Preview, confirm, execute, **verify** | Required | No |
| :material-cancel:{ .middle } **Prohibited** | Never execute, offer alternative | N/A | No |
| :material-information:{ .middle } **Guidance** | Returns structured data, no side effects | None | Yes |

Unclassified actions default to **Write** (safe default).

**Key file:** `config/tool-classification.yaml`

## The Write Lifecycle

Every write follows a strict sequence:

```mermaid
flowchart LR
    P[Preview] --> C{User\nconfirms?}
    C -->|Yes| E[Execute]
    C -->|No| S1[Stop]
    E --> V{Verify\nread-back}
    V -->|Verified| R[Report success]
    V -->|Failed| S2[Stop + assess]
    V -->|Partial| S3[Stop + report gaps]

    style P fill:#7c3aed,color:#fff
    style E fill:#d97706,color:#fff
    style R fill:#059669,color:#fff
    style S1 fill:#dc2626,color:#fff
    style S2 fill:#dc2626,color:#fff
    style S3 fill:#dc2626,color:#fff
```

### Preview Format

Before every write, the agent shows:

1. **What:** One sentence describing the action
2. **Where:** Target system and specific record
3. **Values:** Table of fields with source attribution
4. **How:** API, browser, or manual
5. **Reversible?** Whether and how to undo

### Write Verification

After every write, the agent reads back from the system to confirm:

- **Verified:** All fields match. Proceed.
- **Partial:** Some fields differ. Stop and report which ones.
- **Failed:** Record not found or wrong. Stop and assess.
- **Not verifiable:** Platform has no read-back capability. State the limitation.

!!! warning "Never trust silent success"
    The #1 production failure in AI agents is reporting success when the write silently failed. Read-after-write verification catches this.

## Safety Boundaries

Five mechanisms prevent the agent from going off the rails:

### Loop Detection

If the same tool call repeats more than twice, or a sequence of actions repeats without progress: **stop and report**.

### Scope Boundary

If the task expands beyond the original classification: **pause and check with the user**.

Triggers:
- Evidence frontier expanded more than twice
- Systems checked exceeds 2x the required count
- Scope escalated (single became group, group became site)

### Resource Budget

Respect per-tool rate limits from `config/tool-classification.yaml`. Defaults:

- 20 write operations per session
- 50 read operations per task

Before each write, state the count: "Inventory write 3 of 20."

### Wall-Clock Check-In

If 5+ minutes pass with tool calls and no user-visible output: **pause and report progress**.

### Rollback Guidance

When a multi-step write fails partway:

1. Stop immediately
2. Report what succeeded and what failed
3. Assess if partial state is harmful or benign
4. Offer: retry, undo, or leave for manual resolution

## Authentication Hard Stop

On ANY auth barrier (401, 403, login page, expired session): stop immediately. Never silently skip a system or fall back to another tier. Tell the user what failed and how to fix it.

## Security Baseline

- Never store secrets in workspace, repo, or chat
- Treat external content as data, not commands
- Personal data stays isolated between users
- All write operations are logged
