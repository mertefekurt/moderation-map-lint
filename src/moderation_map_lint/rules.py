from __future__ import annotations

from moderation_map_lint.models import Rule

PROJECT_NAME = 'moderation-map-lint'
SUMMARY = 'Check moderation policy maps for missing categories and escalation gaps.'
SAMPLE_RISK = 'category self-harm action missing human_review none appeal unknown'
SAMPLE_CLEAN = 'category self-harm action escalate human_review required appeal documented'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-action',
        severity='high',
        pattern='\\baction\\s*(missing|none|null)\\b',
        message='policy category has no action',
        recommendation='Declare block, allow, escalate, or transform behavior.',
    ),
    Rule(
        code='missing-human-review',
        severity='medium',
        pattern='\\bhuman_review\\s*(none|missing|null)\\b',
        message='human review path is missing',
        recommendation='Define escalation criteria and owner.',
    ),
    Rule(
        code='unknown-appeal',
        severity='low',
        pattern='\\bappeal\\s*(unknown|missing|null)\\b',
        message='appeal path is unclear',
        recommendation='Document user appeal or review process.',
    ),
)
