# Roadmap

The Keia is designed to evolve from files in a repo to a standalone platform. This roadmap describes the planned progression. Contributions at any stage are welcome.

## Current State

The framework ships as YAML files, behavioral rules, and schemas that can be consumed by any AI editor (Cursor, Claude Code) or used to generate a static website. This is useful today for teams that want structured operational knowledge.

## Planned Stages

### Stage 1: Knowledge Base (current)

**What exists now.** YAML profiles and schemas in a Git repo. A build script generates a static website. Content is edited through Git (merge requests, review, version history). The website is read-only; Git is the editor.

- Browsable website generated from YAML
- Device profiles, configuration guides, troubleshooting
- Schema validation on every commit
- Deployed to GitLab/GitHub Pages

### Stage 2: Collaborative Knowledge Base

**A web application with role-based access.** Users log in and interact with the knowledge base through a browser. Different roles have different capabilities.

Planned capabilities:

- **Viewers** browse profiles, configuration guides, and troubleshooting
- **Contributors** suggest edits, add notes, flag outdated content
- **Editors** (service managers, senior engineers) review and approve changes
- **Admins** manage roles, configure the system

Changes flow through an approval process (contributor suggests, editor reviews, system rebuilds). The underlying data is still YAML in Git, but the web interface hides that complexity. No one needs to know Git or YAML to use the system.

Technology direction: web application deployable on OpenShift/Kubernetes.

### Stage 3: Live Platform Integration

**The knowledge base connects to live operational platforms via APIs.** Profiles define what "correct" looks like. The system queries live platforms and compares reality against the profiles.

Planned capabilities:

- Platform connectors (REST APIs, MCP servers) for inventory, DNS, monitoring, fleet management
- Periodic automated checks: query devices, compare against profiles, report drift
- Health dashboard: per-device, per-domain status (green/amber/red)
- Drift detection before users report problems
- All reads, no writes. The system observes but doesn't change anything.

### Stage 4: AI-Assisted Operations

**An AI layer answers questions from the knowledge base and assists with verification.** Users interact through a chat interface on the web application.

Planned capabilities:

- Natural language queries: "Is the codec in Cedar Room healthy?"
- AI reads the structured profiles and checks live platforms
- Guided troubleshooting: AI walks through the discrimination logic from the profile
- Context-aware responses shaped by the user's role
- Learning loop: corrections from users improve the profiles

### Stage 5: Autonomous Agents

**The system proactively detects and resolves issues within governed boundaries.**

Planned capabilities:

- Proactive drift detection and proposed remediation
- Automated routine maintenance (firmware verification, certificate renewal)
- Governance enforced at every step: reads are autonomous, writes require confirmation, prohibited actions are never attempted
- The same read/write/prohibited tiers apply whether a human or an agent initiates the action
- Audit trail for every action

## Architecture Direction

The platform is designed to run on OpenShift/Kubernetes as a self-contained application:

```
┌─────────────────────────────────────────────────┐
│  Web Interface                                   │
│  Browse, search, contribute, review, dashboard   │
├─────────────────────────────────────────────────┤
│  API Layer                                       │
│  REST/GraphQL API for all operations             │
├─────────────────────────────────────────────────┤
│  Workflow Engine                                 │
│  URAD-L: Understand, Resolve, Act, Deliver, Learn│
├─────────────────────────────────────────────────┤
│  Knowledge Layer                                 │
│  Profiles, schemas, routing, governance          │
│  (the YAML files that exist today)               │
├─────────────────────────────────────────────────┤
│  Platform Connectors                             │
│  REST APIs, MCP servers, browser automation      │
├─────────────────────────────────────────────────┤
│  AI Layer                                        │
│  Model-agnostic: works with any LLM backend      │
├─────────────────────────────────────────────────┤
│  OpenShift / Kubernetes                          │
└─────────────────────────────────────────────────┘
```

The Knowledge Layer (YAML files, schemas, rules) is the foundation that exists today. Each layer above it is an increment of the roadmap. The framework is useful at every stage: you don't need the full platform to benefit from structured operational knowledge.

## Contributing

Contributions are welcome at any stage. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- **Stage 1 contributions**: new schemas, better examples, documentation, validation tooling
- **Stage 2 contributions**: web application architecture, role-based access design, UI components
- **Stage 3 contributions**: platform connector implementations, API design
- **Stage 4 contributions**: AI integration patterns, learning loop implementation
- **Stage 5 contributions**: agent governance patterns, autonomous workflow design
