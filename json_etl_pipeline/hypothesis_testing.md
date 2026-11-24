# Hypothesis Testing

This project includes simple business hypothesis checks to demonstrate how raw JSON logs can be converted into QA insights.

## Hypothesis 1

Rejected cases are more common when system-generated descriptions are too short.

### Test

Flag records where `system_description` has fewer than 30 characters.

### Output Field

`description_too_short`

---

## Hypothesis 2

Missing subject category increases rejected-case risk.

### Test

Flag records where `subject_category` is blank or missing.

### Output Field

`missing_subject_category`

---

## Hypothesis 3

Low confidence records require closer review.

### Test

Flag records where `confidence_score` is below 0.70.

### Output Field

`low_confidence`

## Note

These checks are business validation examples, not formal statistical significance tests. They are designed to show how operational assumptions can be converted into testable data-quality rules.
