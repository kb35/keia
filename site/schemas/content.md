# Content Schemas

7 schemas that define the structure of knowledge files.

## domain-index

**Governs:** `references/domains/*.md`

| Section | Required | Purpose |
|---------|----------|---------|
| `scope` | Yes | What falls in this domain |
| `topics` | Yes | List of topic entries with profile, reference, and tool links |
| `cross_domain` | Yes | Connections to other domains |
| `knowledge_layer_checklist` | No | Standards and guides that apply |

Each topic entry must include: name, topic_index path, profiles, references, tools, and source_registry links.

## topic-index

**Governs:** `references/topics/{domain}/*.md`

| Section | Required | Purpose |
|---------|----------|---------|
| `scope` | Yes | What this topic covers |
| `relevant_objects` | Yes | Object types (must match registry) |
| `evidence_surfaces` | Yes | Files and systems to consult |
| `comparison_questions` | Yes | Key questions to answer |
| `expansion_triggers` | Yes (max 6) | When to broaden into other domains |

## object-profile

**Governs:** `references/object-profiles/*.yaml`

The most important schema in the framework. Defines what "correct" looks like for a single managed object.

| Section | Required | Purpose |
|---------|----------|---------|
| `profile` | Yes | Name, role, version, owner |
| `sources` | Yes | Knowledge files this profile draws from |
| `platforms` | Yes | Per-platform healthy state (fields + indicators) |
| `consistency` | Yes | Cross-platform comparison rules |
| `discrimination` | Yes | Troubleshooting classification logic |
| `not_applicable` | Yes | Platforms that don't apply |

## composite-profile

**Governs:** `references/composite-profiles/*.yaml`

| Section | Required | Purpose |
|---------|----------|---------|
| `profile` | Yes | Name, type, purpose, capacity |
| `equipment_categories` | Yes | What belongs in this space (with object profile links) |
| `verification_model` | Yes | How to verify completeness |
| `discrimination` | No | Room-level troubleshooting logic |

## target-state

**Governs:** `references/target-states/*.md`

| Section | Required | Purpose |
|---------|----------|---------|
| `category` | Yes | valid-artifact, evidence-expectations, or state |
| `scope` | Yes | What this applies to |
| `correct_state` | Yes | Verifiable conditions (min 3) |
| `evidence_surfaces` | Yes | Where to find verification data |
| `mandatory_comparisons` | Yes | Cross-checks that must be performed |

## platform-reference

**Governs:** `references/*-reference.yaml`

| Section | Required | Purpose |
|---------|----------|---------|
| `name` | Yes | Platform name |
| `access` | Yes | Method (mcp/browser/api/manual) + tool/URL |
| `sections` | Yes (min 1) | Organized knowledge about the platform |

## source-entry

**Governs:** `registry/sources/*.yaml`

| Field | Required | Purpose |
|-------|----------|---------|
| `id` | Yes | Unique identifier |
| `title` | Yes | Document title |
| `domains` | Yes | Relevant domains |
| `last_verified` | Yes | Freshness tracking (warn at 90 days, error at 180) |
| `access` | Yes (min 1 tier) | How to get to the document (API > browser > manual) |
