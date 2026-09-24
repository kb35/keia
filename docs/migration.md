# Migration Guide

How to bring your existing documentation, standards, and processes into the Context Engine framework.

## Who This Is For

You already have:
- Team documentation (wikis, Google Docs, Confluence, SharePoint)
- Standards and conventions (written or unwritten)
- Platforms you manage objects in (inventory systems, ticketing, monitoring)
- Processes for common tasks (runbooks, checklists, playbooks)

This guide maps each of these to the right place in the framework.

## The Mapping

### Your Documentation -> Source Registry

Your team's existing documents don't move. They stay where they are (wiki, Drive, Confluence). The framework points to them.

For each important document:
1. Create an entry in `registry/sources/{category}.yaml`
2. Set the `id`, `title`, `description`, `domains`, and `topics`
3. Set the `access` tiers: how to get to this document (API, browser URL, manual instructions)
4. Set `last_verified` to today

The framework now knows the document exists, what domain it belongs to, and how to access it. The agent will reference it during resolution instead of guessing.

**What NOT to migrate:** Don't copy document content into the framework. The source registry is pointers, not copies. If the document changes, the pointer still works.

### Your Standards -> Object Profiles + Platform References

Standards define "how things should be." In the framework, that becomes two things:

| Your Standard | Framework Equivalent |
|--------------|---------------------|
| "All switches must have hostname, IP, serial in the inventory" | Object profile (`references/object-profiles/`) - the `platforms.inventory.required_fields` section |
| "Hostnames follow the pattern SITE-ROOM-ROLE-NN" | Platform reference (`references/*-reference.yaml`) - a "Naming Conventions" section |
| "Every device must be in inventory AND DNS" | Object profile - the `consistency` section (cross-platform checks) |
| "When a device is unreachable, check monitoring first" | Object profile - the `discrimination` section |

To migrate:
1. List the object types your team manages
2. For each, run `./setup/create-profile.sh {object-name}`
3. Fill in the platforms, healthy indicators, consistency checks, and troubleshooting logic from your existing standards

### Your Processes -> Playbooks (or just domain knowledge)

Not every process needs to become a playbook. Ask: is this a sequence that matters, or is it knowledge the agent should know?

| Your Process | Framework Equivalent | Why |
|-------------|---------------------|-----|
| "Switch replacement checklist: steps 1-12 in order" | Playbook (`playbooks/*.yaml`) | Order matters, steps are dependent |
| "Always check DNS after updating inventory" | Object profile consistency check | It's a comparison rule, not a procedure |
| "For printer issues, check uniFLOW first" | Object profile discrimination logic | It's a routing decision, not a procedure |
| "Onboarding a new site: phases and milestones" | Playbook | Multi-phase, multi-stakeholder |
| "Our VLAN layout uses 100 for data, 200 for voice" | Platform reference section | It's a fact, not a procedure |

### Your Platforms -> Tool Classification + Config

For each platform your team uses:
1. Add it to `config/tool-classification.yaml` with the right tier (read/write/prohibited)
2. If it has an MCP server, register it in your editor's MCP config
3. Create a platform reference at `references/{platform}-reference.yaml` with the facts the agent needs (naming conventions, field mappings, lifecycle states)
4. Add applicability rules in `config/routing/applicability.yaml` (which object types need this platform?)

### Your Team Structure -> Roles + Domain Ownership

| Your Structure | Framework Equivalent |
|---------------|---------------------|
| "Engineers do technical work" | `config/roles/engineer.yaml` |
| "PMs track timelines and vendors" | `config/roles/pm.yaml` |
| "Alice owns the AV domain" | `owner` field in `references/domains/av.md` |
| "Bob handles EMEA network devices" | Doesn't map to framework (assignment, not architecture) |

## Migration Order

Do this in order. Each step builds on the previous.

| Step | What | Time | Unlocks |
|------|------|------|---------|
| 1 | Create 3-5 domain indexes | 30 min | The agent knows your areas of responsibility |
| 2 | Create 1 object profile per domain | 1 hour | The agent knows what "correct" looks like |
| 3 | Register your platforms in tool-classification | 15 min | The agent can query your systems |
| 4 | Add routing rules | 15 min | The agent routes requests to the right domain |
| 5 | Add applicability rules | 15 min | The agent checks the right systems per object type |
| 6 | Add 10-20 source registry entries | 30 min | The agent can reference your documentation |
| 7 | Create 2-3 templates | 30 min | Structured outputs follow your conventions |
| 8 | Write eval scenarios | 30 min | You can verify the system works after changes |

Total: approximately 4 hours for a basic but functional setup.

## What You Can Skip

- **Composite profiles**: Only needed if you manage rooms/spaces with multiple components. Skip for teams that manage individual objects.
- **Target states for artifacts**: Only needed if you produce structured outputs (tickets, reports) that need validation. Skip initially.
- **Playbooks**: The framework works without playbooks. Add them later for complex multi-phase processes.
- **Skills**: Optional shortcuts. The framework reasons from primitives without skills.

## Validation

After migrating, run:

```bash
python setup/validate.py
python setup/validate.py --coverage
```

The validator checks that files follow their schemas. The coverage report shows gaps: domains without topics, object types without profiles, etc.
