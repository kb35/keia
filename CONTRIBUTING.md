# Contributing

Contributions are welcome. This framework improves when people apply it to new domains and share what they learn.

## What to Contribute

| Contribution | Where It Goes | Review |
|-------------|--------------|--------|
| New domain example | `references/domains/` | Light review (does it follow the schema?) |
| New object profile | `references/object-profiles/` | Light review |
| Bug fix in schemas | `schemas/` | Standard review |
| New schema | `schemas/` | Careful review (schemas are contracts) |
| Rule improvement | `.cursor/rules/` | Careful review (rules define behavior) |
| Documentation | `docs/` | Light review |
| Tooling (validator, scaffolding) | `setup/` | Standard review |

## How to Contribute

1. Fork the repository
2. Create a branch (`feature/your-description`)
3. Make your changes
4. Run `setup/validate.py` to check schema conformance
5. Submit a merge request with a clear description of what changed and why

## Guidelines

- **Follow the schemas.** Every content file must conform to its schema. Run the validator before submitting.
- **One concern per MR.** A new domain index is one MR. A schema change is a separate MR.
- **Explain the "why."** Especially for schema or rule changes: why is this needed? What gap does it close?
- **Keep examples generic.** Domain examples should be understandable without industry-specific knowledge.
- **No proprietary content.** Examples must not include real company data, credentials, or internal URLs.

## Schema Changes

Schemas are contracts. Changing a schema may break existing content files. Schema changes require:

1. A clear rationale (what gap does this close?)
2. Migration notes (how do existing files update?)
3. A version bump in the schema file
4. Updated examples that conform to the new schema

## Code of Conduct

Be respectful, constructive, and specific. Focus on improving the framework, not critiquing the people using it.
