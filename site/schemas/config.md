# Config Schemas

5 schemas that define the structure of control files.

## routing-entry

**Governs:** `config/routing/registry.yaml`

| Section | Required | Purpose |
|---------|----------|---------|
| `prompt_archetypes` | Yes | Named request types, each with an evidence pattern |
| `object_types` | Yes | The things your team manages |
| `scopes` | Yes | Size categories (single, group, site, fleet, portfolio) |
| `routes` | Yes | The routing matrix: match + frontier + domain + triggers |

Each route has a `match` (archetype + object + scope), a `first_frontier` (systems to check first), a `primary_domain`, and up to 6 `expansion_triggers`.

## applicability-rule

**Governs:** `config/routing/applicability.yaml`

| Field | Required | Purpose |
|-------|----------|---------|
| `id` | Yes | Unique rule identifier |
| `applies_to` | Yes | Conditions: domain, object_type, archetypes, topic |
| `decision` | Yes | required_systems, optional_systems, not_applicable_systems |

!!! warning "Conflict prevention"
    A system cannot appear in both `required` and `not_applicable` for the same rule.

## tool-classification

**Governs:** `config/tool-classification.yaml`

| Section | Required | Purpose |
|---------|----------|---------|
| `tiers` | Yes | Tier definitions (read, write, prohibited, guidance) |
| `tools` | Yes | Per-tool: name, tier, description, actions, rate_limit |

## role-definition

**Governs:** `config/roles/*.yaml`

| Field | Required | Purpose |
|-------|----------|---------|
| `role.name` | Yes | Human-readable name |
| `narration_depth` | Yes | standard or expert |
| `delivery_preferences` | Yes | Language style + default format |
| `write_access` | Yes | Which write tools this role can use (empty = read-only) |

## eval-scenario

**Governs:** `evals/*.yaml`

| Section | Required | Purpose |
|---------|----------|---------|
| `scenario` | Yes | ID, name, description, category |
| `input` | Yes | The user's prompt + optional context |
| `expected` | Yes | Classification assertions + must_check/must_not_check/must_contain |

Categories: routing, resolution, applicability, verification, safety.
