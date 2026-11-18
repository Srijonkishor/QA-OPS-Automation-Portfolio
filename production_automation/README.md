# Production Automation

This project demonstrates a simplified QA production automation workflow.

## Purpose

The goal is to automate daily production tracking for QA operations.

Instead of manually checking production numbers every day, this workflow:

1. Calculates the previous working day.
2. Reads production records.
3. Validates required fields.
4. Updates existing records or appends new records.
5. Prevents duplicate rows using operator and date as the unique key.

## Key Concepts

- Previous working-day logic
- Production count tracking
- Schema validation
- Duplicate-safe updates
- Backfill-friendly design

## Example Fields



| Field | Description |
|---|---|
| operator_id | Sanitized QA/operator identifier |
| work_date | Production date |
| production_count | Number of completed items |

## How To Run

```bash
python business_day.py
python table_updater.py
