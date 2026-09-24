# Schemas

18 schemas that define every content type in the framework. Everything else is an instance of one of these.

## How Schemas Work

Each content file in the framework has a `schema:` field in its YAML frontmatter (or follows a defined markdown structure). The validator (`setup/validate.py`) checks every file against its schema.

- **Required fields** must be present. Missing = validation failure.
- **Optional fields** may be omitted without error.
- **Enum fields** must match one of the allowed values.
- **Reference fields** must point to files that actually exist.

## Three Layers

### Content Schemas (`content/`)
Define the structure of knowledge files: domain indexes, topic indexes, profiles, references, and source registry entries.

### Config Schemas (`config/`)
Define the structure of control files: routing registry, applicability rules, tool tiers, and role definitions.

### Runtime Schemas (`runtime/`)
Define what each workflow phase produces. These are not files on disk; they are the contracts for what the AI generates at runtime. They make the workflow predictable and composable.

## Validation

Run `python setup/validate.py` to check all files against their schemas. The validator:
1. Discovers all YAML and Markdown files
2. Identifies the schema type from the `schema:` field or file location
3. Checks required fields, enum values, and cross-references
4. Reports errors with file path, line, and what's missing

Integrate into CI to prevent non-conforming files from merging.
