#!/usr/bin/env python3
"""
Context Engine Schema Validator

Validates all content and config files against their schemas.
Uses only Python standard library (no pip dependencies).

Usage:
    python setup/validate.py              # Validate everything
    python setup/validate.py --layer content   # Validate knowledge files only
    python setup/validate.py --layer config    # Validate config files only
    python setup/validate.py --file references/domains/infrastructure.md
"""

import os
import sys
import re
import glob
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Resolve project root (parent of setup/)
ROOT = Path(__file__).resolve().parent.parent

# --- ANSI colors for terminal output ---
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

class ValidationError:
    def __init__(self, file_path, message, severity="error"):
        self.file_path = str(file_path)
        self.message = message
        self.severity = severity  # error, warning

    def __str__(self):
        color = RED if self.severity == "error" else YELLOW
        label = "ERROR" if self.severity == "error" else "WARN"
        return f"{color}[{label}]{RESET} {self.file_path}: {self.message}"


def find_files(root, pattern):
    """Find files matching a glob pattern relative to root."""
    return sorted(root.glob(pattern))


def read_yaml_frontmatter(filepath):
    """Extract key-value pairs from YAML files (simple parser, no pyyaml needed)."""
    fields = {}
    content = filepath.read_text(encoding="utf-8")
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#") or stripped == "" or stripped == "---":
            continue
        if ":" in stripped:
            key = stripped.split(":")[0].strip()
            value = ":".join(stripped.split(":")[1:]).strip().strip('"').strip("'")
            if value:
                fields[key] = value
    return fields, content


def check_markdown_sections(filepath, required_sections):
    """Check that a markdown file contains required H2 sections."""
    errors = []
    content = filepath.read_text(encoding="utf-8")
    headings = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    heading_lower = [h.lower().strip() for h in headings]

    for section in required_sections:
        if section.lower() not in heading_lower:
            errors.append(ValidationError(
                filepath.relative_to(ROOT),
                f"Missing required section: '## {section}'"
            ))
    return errors


def check_yaml_required_fields(filepath, required_fields):
    """Check that a YAML file contains required top-level fields."""
    errors = []
    fields, content = read_yaml_frontmatter(filepath)

    for field in required_fields:
        if field not in fields and field not in content:
            errors.append(ValidationError(
                filepath.relative_to(ROOT),
                f"Missing required field: '{field}'"
            ))
    return errors


def check_freshness(filepath, field_name="last_verified", threshold_days=90, error_days=180):
    """Check if a date field is within freshness thresholds."""
    errors = []
    fields, _ = read_yaml_frontmatter(filepath)

    date_str = fields.get(field_name) or fields.get("last_updated")
    if not date_str:
        return errors

    try:
        date_val = datetime.strptime(date_str, "%Y-%m-%d")
        age_days = (datetime.now() - date_val).days

        if age_days > error_days:
            errors.append(ValidationError(
                filepath.relative_to(ROOT),
                f"Stale: {field_name} is {age_days} days old (threshold: {error_days})",
                severity="error"
            ))
        elif age_days > threshold_days:
            errors.append(ValidationError(
                filepath.relative_to(ROOT),
                f"Aging: {field_name} is {age_days} days old (warning threshold: {threshold_days})",
                severity="warning"
            ))
    except ValueError:
        pass  # Can't parse date, skip freshness check

    return errors


def validate_domain_indexes(root):
    """Validate all domain index files."""
    errors = []
    files = find_files(root / "references" / "domains", "*.md")

    for f in files:
        if f.name.startswith("_"):
            continue  # Skip examples
        errors.extend(check_markdown_sections(f, [
            "Scope", "Topics", "Cross-Domain Connections"
        ]))
    return files, errors


def validate_topic_indexes(root):
    """Validate all topic index files."""
    errors = []
    files = find_files(root / "references" / "topics", "**/*.md")

    for f in files:
        if f.name.startswith("_"):
            continue
        errors.extend(check_markdown_sections(f, [
            "Scope", "Relevant Objects", "Evidence Surfaces",
            "Comparison Questions", "Expansion Triggers"
        ]))

        # Check expansion trigger count (max 6)
        content = f.read_text(encoding="utf-8")
        triggers_section = re.search(
            r"## Expansion Triggers\n(.*?)(?=\n## |\Z)",
            content, re.DOTALL
        )
        if triggers_section:
            triggers = re.findall(r"^- ", triggers_section.group(1), re.MULTILINE)
            if len(triggers) > 6:
                errors.append(ValidationError(
                    f.relative_to(root),
                    f"Too many expansion triggers: {len(triggers)} (max 6)"
                ))
    return files, errors


def validate_object_profiles(root):
    """Validate all object profile files."""
    errors = []
    files = find_files(root / "references" / "object-profiles", "*.yaml")

    required = ["schema", "profile", "platforms", "consistency", "discrimination", "not_applicable"]
    for f in files:
        if f.name.startswith("_"):
            continue
        errors.extend(check_yaml_required_fields(f, required))
        errors.extend(check_freshness(f, "last_updated"))
    return files, errors


def validate_source_registry(root):
    """Validate all source registry files."""
    errors = []
    files = find_files(root / "registry" / "sources", "*.yaml")

    for f in files:
        if f.name.startswith("_"):
            continue
        errors.extend(check_yaml_required_fields(f, ["name", "entries"]))
        errors.extend(check_freshness(f, "last_verified"))
    return files, errors


def validate_routing(root):
    """Validate routing registry and applicability rules."""
    errors = []
    files = []

    registry = root / "config" / "routing" / "registry.yaml"
    if registry.exists():
        files.append(registry)
        errors.extend(check_yaml_required_fields(registry, [
            "prompt_archetypes", "object_types", "scopes"
        ]))

    applicability = root / "config" / "routing" / "applicability.yaml"
    if applicability.exists():
        files.append(applicability)

    return files, errors


def validate_tool_classification(root):
    """Validate tool classification file."""
    errors = []
    tc = root / "config" / "tool-classification.yaml"
    if tc.exists():
        errors.extend(check_yaml_required_fields(tc, ["tiers"]))
        return [tc], errors
    return [], errors


def generate_coverage_report(root):
    """Generate a coverage report showing what's populated vs empty."""
    report = []

    domains = list(find_files(root / "references" / "domains", "*.md"))
    domains = [d for d in domains if not d.name.startswith("_")]

    topics = list(find_files(root / "references" / "topics", "**/*.md"))
    topics = [t for t in topics if not t.name.startswith("_")]

    profiles = list(find_files(root / "references" / "object-profiles", "*.yaml"))
    profiles = [p for p in profiles if not p.name.startswith("_")]

    composites = list(find_files(root / "references" / "composite-profiles", "*.yaml"))
    composites = [c for c in composites if not c.name.startswith("_")]

    target_states = list(find_files(root / "references" / "target-states", "*.md"))
    target_states = [t for t in target_states if not t.name.startswith("_")]

    sources = list(find_files(root / "registry" / "sources", "*.yaml"))
    sources = [s for s in sources if not s.name.startswith("_")]

    templates = list(find_files(root / "templates", "*.md"))
    templates = [t for t in templates if not t.name.startswith("_")]

    evals = list(find_files(root / "evals", "*.yaml"))
    evals = [e for e in evals if not e.name.startswith("_")]

    report.append(f"\n{BOLD}=== Coverage Report ==={RESET}\n")
    report.append(f"  Domains:            {len(domains)}")
    report.append(f"  Topic indexes:      {len(topics)}")
    report.append(f"  Object profiles:    {len(profiles)}")
    report.append(f"  Composite profiles: {len(composites)}")
    report.append(f"  Target states:      {len(target_states)}")
    report.append(f"  Source registry:    {len(sources)}")
    report.append(f"  Templates:          {len(templates)}")
    report.append(f"  Eval scenarios:     {len(evals)}")

    # Check for domains without topics
    for domain in domains:
        domain_name = domain.stem
        domain_topics = list(find_files(root / "references" / "topics" / domain_name, "*.md"))
        domain_topics = [t for t in domain_topics if not t.name.startswith("_")]
        if not domain_topics:
            report.append(f"  {YELLOW}[GAP]{RESET} Domain '{domain_name}' has no topic indexes")

    if not profiles:
        report.append(f"  {YELLOW}[GAP]{RESET} No object profiles defined")
    if not evals:
        report.append(f"  {YELLOW}[GAP]{RESET} No eval scenarios defined")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Context Engine Schema Validator")
    parser.add_argument("--layer", choices=["content", "config", "all"], default="all")
    parser.add_argument("--file", type=str, help="Validate a single file")
    parser.add_argument("--coverage", action="store_true", help="Show coverage report")
    args = parser.parse_args()

    all_errors = []
    all_warnings = []
    total_files = 0

    print(f"\n{BOLD}Context Engine Validator{RESET}")
    print(f"Root: {ROOT}\n")

    if args.coverage:
        print(generate_coverage_report(ROOT))
        return

    # Run validators
    validators = []
    if args.layer in ("content", "all"):
        validators.extend([
            ("Domain indexes", validate_domain_indexes),
            ("Topic indexes", validate_topic_indexes),
            ("Object profiles", validate_object_profiles),
            ("Source registry", validate_source_registry),
        ])
    if args.layer in ("config", "all"):
        validators.extend([
            ("Routing", validate_routing),
            ("Tool classification", validate_tool_classification),
        ])

    for name, validator in validators:
        files, errors = validator(ROOT)
        total_files += len(files)

        file_errors = [e for e in errors if e.severity == "error"]
        file_warnings = [e for e in errors if e.severity == "warning"]
        all_errors.extend(file_errors)
        all_warnings.extend(file_warnings)

        status = f"{GREEN}OK{RESET}" if not file_errors else f"{RED}{len(file_errors)} errors{RESET}"
        warnings_str = f" ({YELLOW}{len(file_warnings)} warnings{RESET})" if file_warnings else ""
        print(f"  {name}: {len(files)} files - {status}{warnings_str}")

    # Print all errors and warnings
    if all_errors or all_warnings:
        print(f"\n{BOLD}--- Issues ---{RESET}")
        for e in all_errors:
            print(f"  {e}")
        for w in all_warnings:
            print(f"  {w}")

    # Summary
    print(f"\n{BOLD}--- Summary ---{RESET}")
    print(f"  Files checked: {total_files}")
    print(f"  Errors: {len(all_errors)}")
    print(f"  Warnings: {len(all_warnings)}")

    # Coverage report
    print(generate_coverage_report(ROOT))

    if all_errors:
        print(f"\n{RED}Validation failed.{RESET}")
        sys.exit(1)
    else:
        print(f"\n{GREEN}Validation passed.{RESET}")
        sys.exit(0)


if __name__ == "__main__":
    main()
