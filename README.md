# Case Repository Workflow

This project demonstrates a simplified case repository workflow for QA and Trust & Safety operations.

## Purpose

The goal is to convert raw review records into a structured case repository.

In real QA operations, review data can come from different sources and may include nested JSON fields, review status codes, material IDs, operator IDs, and metadata that need to be cleaned and enriched.

This public version uses mock data only.

## What This Project Demonstrates

- Parsing raw review records
- Extracting values from JSON-like fields
- Classifying review status
- Filtering rejected cases
- Enriching cases with import task IDs
- Creating a clean case repository output

## Workflow

```text
Raw review records
→ Parse JSON fields
→ Classify review status
→ Filter rejected cases
→ Enrich with import task ID
→ Export structured case repository
