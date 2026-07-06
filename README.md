# Moderation Map Lint

<p align="center">
  <img src="assets/readme-cover.svg" alt="Moderation Map Lint cover" width="100%" />
</p>

![stack](https://img.shields.io/badge/stack-Python-4b5563?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-2563eb?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-16a34a?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-dc2626?style=flat-square)

Check moderation policy maps for missing categories and escalation gaps.

## The short version

`moderation-map-lint` is intentionally small: feed it a file, get deterministic findings, and decide whether the result should block a merge or just guide cleanup.

## Rule surface

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-action` | high | policy category has no action |
| `missing-human-review` | medium | human review path is missing |
| `unknown-appeal` | low | appeal path is unclear |

## Usage

```bash
python -m pip install -e ".[dev]"
moderation-map-lint examples/sample.txt
moderation-map-lint examples/sample.txt --json --fail-on medium
```

## Useful defaults

| Option | Reason |
| --- | --- |
| `--json` | machine-readable output for scripts |
| `--fail-on medium` | stricter CI gate when warnings matter |
| `--format auto` | let the reader detect text, CSV, JSON, or JSONL |

## Local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m moderation_map_lint --help
```
