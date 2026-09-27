# Changelog

All notable changes to the Keia framework.

## [0.5.0] - 2026-09-27

### Added
- Operations Framework concept page (site/concepts/operations-framework.md)
  - Defines the operational model upstream of the framework primitives
  - Six concepts: technology standards, space types, device profiles, projects, project stages, lifecycle stages
  - Three work patterns: projects, incidents, service management
  - Five ITIL-aligned lifecycle stages with defined tasks
  - Role mapping, capacity planning, logical/physical device identity
  - Adaptation guide for other teams
- Operations Framework added to mkdocs nav (first item under Concepts)
- Operations Framework referenced from site homepage "Under the Hood" section

## [0.4.0] - 2026-09-24

### Added
- Session summary runtime schema (schemas/runtime/session-summary.schema.yaml)
- AGENTS.md for universal editor compatibility
- CLAUDE.md updated for consistency
- .gitlab-ci.yml for automated validation on push/MR
- Composite profile example (conference-room-medium)
- Target state example (valid-incident-report)
- Playbook example (device-commissioning)
- Schema count: 20 -> 21 (added session-summary)

### Changed
- README.md: updated directory structure, schema count, all sections reflect final state

## [0.3.0] - 2026-09-24

### Added
- Schema validator script (setup/validate.py) with coverage reporting
- Migration guide (docs/migration.md) for bringing existing content into the framework
- Second worked example: Project Management domain with portfolio-health topic and project-record profile
- Multi-user conflict resolution rules in learning.mdc
- Scaffolding CLI: create-domain.sh, create-topic.sh, create-profile.sh

### Changed
- learning.mdc: added multi-user conflict resolution section

## [0.2.0] - 2026-09-24

### Added
- Write verification (read-after-write) in governance.mdc
- Safety boundaries: loop detection, scope boundary, resource budget, wall-clock check-in, rollback guidance
- Write verification runtime schema (schemas/runtime/write-verification.schema.yaml)
- Decision trace runtime schema (schemas/runtime/decision-trace.schema.yaml)
- Eval framework: eval-scenario config schema + example golden-set tests
- Quickstart guide (docs/quickstart.md)
- Scaffolding CLI: create-domain.sh, create-topic.sh, create-profile.sh
- CLAUDE.md for Claude Code compatibility
- CONTRIBUTING.md, LICENSE (Apache 2.0), .gitignore
- Incident report template example
- CHANGELOG.md

### Changed
- governance.mdc: expanded from basic tiers to full write lifecycle + safety
- workflow.mdc: Phase 3 (Act) now references verification and safety boundaries
- README.md: added write lifecycle diagram, safety boundaries, quickstart link
- Schema count: 17 -> 20 (added write-verification, decision-trace, eval-scenario)

## [0.1.0] - 2026-09-23

### Added
- Initial skeleton framework: 9 primitives, 5 rules, 17 schemas
- Core rules: workflow.mdc, governance.mdc, output.mdc, learning.mdc, principles.mdc
- Content schemas: domain-index, topic-index, object-profile, composite-profile, target-state, platform-reference, source-entry
- Config schemas: routing-entry, applicability-rule, tool-classification, role-definition
- Runtime schemas: prompt-classification, resolution-plan, action-preview, verification-summary, learning-record
- Starter config: routing registry, applicability rules, tool classification, engineer role
- Worked examples: domain index, topic index, object profile, platform reference, source registry
- README.md with full architecture documentation
