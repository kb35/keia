# Quickstart: Your First Domain in 30 Minutes

Fork, create one domain, one profile, one platform connection, ask your first question.

## Prerequisites

- An AI editor (Cursor, Claude Code, or similar)
- At least one platform you manage with an API or MCP server
- 30 minutes

## Steps

### 1. Fork and Open (2 minutes)

Fork or clone the repository. Open it in your editor. The rules activate automatically.

### 2. Create Your First Domain (10 minutes)

```bash
./setup/create-domain.sh infrastructure
```

Edit `references/domains/infrastructure.md`: set the owner, write the scope, list 2-3 topics with their tools, add cross-domain connections.

### 3. Create Your First Object Profile (10 minutes)

```bash
./setup/create-profile.sh network-switch
```

Edit `references/object-profiles/network-switch-profile.yaml`: define 2-3 platforms with required fields and healthy indicators, add consistency checks and discrimination logic.

!!! tip "This is the most important file"
    The object profile encodes expert knowledge of what "correct" looks like. Even a minimal profile dramatically improves troubleshooting and verification.

### 4. Register a Platform Connection (5 minutes)

Edit `config/tool-classification.yaml`:

```yaml
tools:
  inventory_read:
    tier: read
    description: "Query device inventory"
    actions:
      get_device: read
      search: read
```

Connect the MCP server in your editor's configuration.

### 5. Add a Route (3 minutes)

Edit `config/routing/registry.yaml`, add a route in the `routes:` section.

Edit `config/routing/applicability.yaml`, add a rule for your object type.

### 6. Ask Your First Question

> "Check the status of [device] in [location]"

Watch the agent classify, route, load your profile, query the platform, and compare against the healthy state.

## What to Build Next

| Next Step | What It Adds | Effort |
|-----------|-------------|--------|
| Add a second platform | Cross-platform consistency checks | 5 min |
| Create a topic index | Comparison questions + expansion triggers | 10 min |
| Add source registry entries | Documentation references | 10 min |
| Create an output template | Structured outputs | 15 min |
| Add a second domain | Cross-domain connections | 20 min |

## Troubleshooting

**Agent doesn't use my domain:** Check that `primary_domain` in the route matches your domain index filename (without `.md`).

**Agent checks too many systems:** Add an applicability rule that sets `not_applicable_systems` for your object type.

**Agent asks confirmation for reads:** Your tool is missing from `tool-classification.yaml` (defaults to write tier).
