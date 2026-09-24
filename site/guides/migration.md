# Migration Guide

You already have documentation, standards, and tools. Here's where they map in the framework.

## The Mapping

| What You Have | Where It Goes |
|--------------|--------------|
| Team documentation (wiki, Drive, Confluence) | `registry/sources/*.yaml` - point to docs, don't copy them |
| Standards ("all switches must have...") | `references/object-profiles/*.yaml` - healthy state definitions |
| Naming conventions, field rules | `references/*-reference.yaml` - platform-specific facts |
| Processes with ordered steps | `playbooks/*.yaml` - multi-phase process guides |
| Knowledge about what to check | `references/topics/**/*.md` - comparison questions |
| Domain expertise | `references/domains/*.md` - entry points |

!!! info "Don't copy content"
    The source registry points to documents. It doesn't copy them. If the document changes, the pointer still works.

## Migration Order

| Step | What | Time |
|------|------|------|
| 1 | Create 3-5 domain indexes | 30 min |
| 2 | Create 1 object profile per domain | 1 hour |
| 3 | Register platforms in tool-classification | 15 min |
| 4 | Add routing rules | 15 min |
| 5 | Add applicability rules | 15 min |
| 6 | Add 10-20 source registry entries | 30 min |
| 7 | Create 2-3 templates | 30 min |
| 8 | Write eval scenarios | 30 min |

**Total:** approximately 4 hours for a basic but functional setup.

## What You Can Skip

- **Composite profiles:** Only if you manage rooms or spaces
- **Target states for artifacts:** Only if you produce structured outputs
- **Playbooks:** The framework works without them
- **Skills:** Optional shortcuts, add later

## Validation

```bash
python setup/validate.py           # Check all files
python setup/validate.py --coverage # Show gaps
```
