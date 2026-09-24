# Schema Reference

21 schemas define every content type in the framework. They are the contracts that make the architecture enforceable.

## Three Layers

| Layer | Count | Purpose |
|-------|-------|---------|
| [Content schemas](content.md) | 7 | Structure of knowledge files |
| [Config schemas](config.md) | 5 | Structure of control files |
| [Runtime schemas](runtime.md) | 8 | What each workflow phase produces |

## How Schemas Work

Each content file has a `schema:` field identifying its type. The validator (`setup/validate.py`) checks every file against its schema.

- **Required fields** must be present
- **Enum fields** must match allowed values
- **Reference fields** must point to files that exist
- **Freshness fields** are checked against thresholds

## Validation

```bash
# Check all files
python setup/validate.py

# Check only knowledge files
python setup/validate.py --layer content

# Show coverage report
python setup/validate.py --coverage
```

Integrate into CI with `.gitlab-ci.yml` to block non-conforming merges.
