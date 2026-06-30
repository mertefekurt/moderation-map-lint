# moderation-map-lint

**CI Gate.** Check moderation policy maps for missing categories and escalation gaps.

## Goal

Moderation coverage is easy to describe but hard to operationalize. This CLI reviews policy maps for missing actions and human review paths.

## GitHub Actions

`moderation-map-lint` accepts moderation policy map or safety config in text, JSON, JSONL, or CSV form.

## Local Debugging

```bash
python -m pip install -e ".[dev]"
moderation-map-lint examples/sample.txt
moderation-map-lint examples/sample.txt --json --fail-on medium
```

## JSON Output

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-action` | high | policy category has no action |
| `missing-human-review` | medium | human review path is missing |
| `unknown-appeal` | low | appeal path is unclear |

## Roadmap

```bash
ruff check .
pytest
python -m moderation_map_lint --help
```

License: MIT

### Example Input

```text
category self-harm action missing human_review none appeal unknown
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the moderation-map-lint policy surface explicit.
