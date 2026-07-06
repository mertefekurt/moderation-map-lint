# Moderation Map Lint

![Moderation Map Lint cover](assets/readme-cover.svg)

Check moderation policy maps for missing categories and escalation gaps.

## The rule file is the product

- `missing-action` (high): policy category has no action. Fix: Declare block, allow, escalate, or transform behavior..
- `missing-human-review` (medium): human review path is missing. Fix: Define escalation criteria and owner..
- `unknown-appeal` (low): appeal path is unclear. Fix: Document user appeal or review process..

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/moderation-map-lint.git
cd moderation-map-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
moderation-map-lint examples/sample.txt
moderation-map-lint examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
