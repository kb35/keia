# Quickstart: Your First Domain in 30 Minutes

This guide takes you from a fresh fork to a working system with one domain, one profile, and one platform connection. You'll ask a question and see the full routing-resolution-verification path in action.

## Prerequisites

- An AI editor that supports rules (Cursor, Claude Code, or similar)
- At least one platform you manage that has an API or MCP server (inventory system, ticketing system, monitoring tool, etc.)
- 30 minutes

## Step 1: Fork and Open (2 minutes)

Fork or clone this repository. Open it in your AI editor.

The rules in `.cursor/rules/` activate automatically. The AI now understands the 5-phase workflow, the governance model, and the output standards. It just has no domain knowledge yet.

## Step 2: Define Your First Domain (10 minutes)

Copy the example domain index:

```
cp references/domains/_example.md references/domains/your-domain.md
```

Open `references/domains/your-domain.md` and replace the placeholders:

1. **Change the title** to your domain name (e.g., "Infrastructure", "Customer Accounts", "Patient Records")
2. **Set the owner** to whoever is responsible for this area
3. **Write the scope** in one paragraph: what falls in this domain, what doesn't
4. **List 2-3 topics** within the domain. For each topic:
   - Name and brief description
   - What tools/platforms are relevant
   - What object types are involved
5. **Write 3-4 cross-domain connections**: "When X happens in this domain, check Y domain"

Don't worry about topic index files or source registry links yet. Those come later. A domain index with just scope, topics (as descriptions), and cross-domain connections is enough to start.

## Step 3: Create Your First Object Profile (10 minutes)

Copy the example object profile:

```
cp references/object-profiles/_example-profile.yaml references/object-profiles/your-object.yaml
```

Open `references/object-profiles/your-object.yaml` and replace the placeholders:

1. **Set the profile name** (e.g., "Network Switch", "Customer Account", "Server Instance")
2. **Define 2-3 platforms** this object should be tracked in. For each platform:
   - What fields are required (hostname, IP, status, owner, etc.)
   - What "healthy" looks like (status: active, all fields populated, etc.)
3. **Define 1-2 consistency checks**: what should match across platforms (e.g., "hostname in inventory should match hostname in DNS")
4. **Define 1-2 discrimination entries**: when something is wrong, what are the likely causes and where to look first
5. **List not-applicable platforms**: what systems DON'T apply to this object type

This is the most important file in the framework. It encodes the expert knowledge of what "correct" looks like. Even a minimal profile dramatically improves the agent's ability to verify and troubleshoot.

## Step 4: Register One Platform Connection (5 minutes)

Open `config/tool-classification.yaml` and add your first platform:

```yaml
tools:
  your_platform_read:
    tier: read
    description: "Query your platform for records"
    actions:
      get_record: read
      search: read
      list: read
```

If you also have write access:

```yaml
  your_platform_write:
    tier: write
    description: "Create or update records in your platform"
    actions:
      create: write
      update: write
    rate_limit: 20
```

Then connect the actual MCP server in your editor's MCP configuration (this is editor-specific; see your editor's docs for adding MCP servers).

## Step 5: Add One Route (3 minutes)

Open `config/routing/registry.yaml` and add your first route in the `routes:` section:

```yaml
routes:
  - match:
      archetype: troubleshoot
      object_type: device           # or whatever your object type is
      scope: single
    first_frontier: [your_platform_read]
    primary_domain: your-domain     # matches your domain index filename
    expansion_triggers:
      - "data mismatch -> check secondary platform"
```

And one applicability rule in `config/routing/applicability.yaml`:

```yaml
rules:
  - id: your-first-rule
    applies_to:
      object_type: device           # or your object type
      archetypes: [troubleshoot, verify]
    decision:
      required_systems: [your_platform_read]
      optional_systems: []
      not_applicable_systems: []
```

## Step 6: Ask Your First Question (done!)

Open a new conversation in your editor and ask:

> "Check the status of [specific object] in [specific location]"

Watch what happens:

1. **Understand**: The agent classifies your request as `troubleshoot + device + single`
2. **Resolve**: It loads your domain index, finds your object profile, checks which systems are required
3. **Act**: It queries your platform using the MCP connection
4. **Deliver**: It compares what it found against your profile's healthy indicators
5. **Learn**: If you correct anything, it captures the correction

You now have a working domain-specific AI assistant. It knows what "correct" looks like for your object type, it knows which platform to check, and it can explain the gap between expected and actual state.

## What to Build Next

| Next Step | What It Adds | Effort |
|-----------|-------------|--------|
| **Add a second platform** | Cross-platform consistency checks become possible | 5 minutes |
| **Create a topic index** | The agent gets comparison questions and expansion triggers | 10 minutes |
| **Add source registry entries** | The agent can point to your team's documentation | 10 minutes |
| **Create an output template** | Structured outputs (tickets, reports) follow a consistent format | 15 minutes |
| **Add a second domain** | Cross-domain connections light up | 20 minutes |
| **Add a second role** | Different users get role-appropriate output | 5 minutes |

The knowledge layer grows through use. Every correction the agent captures is a piece of domain knowledge being formalized. You don't need to populate everything upfront.

## Troubleshooting

**The agent doesn't use my domain index:**
Check that your route in `config/routing/registry.yaml` has `primary_domain` matching the filename (without `.md`) of your domain index.

**The agent checks systems I didn't configure:**
Check `config/routing/applicability.yaml`. If no rule matches, the agent falls back to checking everything it can access. Add a rule that explicitly sets required and not-applicable systems.

**The agent asks for confirmation on reads:**
Check `config/tool-classification.yaml`. Your read tools must have `tier: read`. If a tool is missing from the classification, it defaults to `write` (which requires confirmation).

**The agent doesn't compare against the profile:**
Make sure your object profile is in `references/object-profiles/` and your domain index or topic index links to it. The Resolve phase follows links from the domain index to find profiles.
