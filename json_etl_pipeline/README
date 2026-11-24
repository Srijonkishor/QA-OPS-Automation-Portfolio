# JSON ETL Review Log Parser

This module demonstrates a GitHub-friendly ETL pipeline for processing nested JSON review logs commonly found in QA operations, Trust & Safety workflows, moderation quality checks, and operational analytics.

The pipeline extracts raw JSON records, validates business assumptions, transforms nested fields into structured tabular data, and generates readable case summaries for non-technical stakeholders.

## Problem Statement

Operational review logs are often stored as nested JSON payloads. These payloads contain valuable information, but they are difficult to analyze directly because important values are hidden inside nested objects.

This project converts raw JSON review logs into:

- Clean CSV outputs
- Hypothesis validation results
- Data-quality checks
- Readable case summaries
- Dashboard-ready structured data

## Pipeline Flow

```text
Raw JSON review logs
→ Extract records
→ Flatten nested fields
→ Validate business hypotheses
→ Apply data-quality checks
→ Export cleaned CSV
→ Generate readable Markdown summaries
```

## Folder Structure

```text
json_etl_pipeline/
├── README.md
├── data/
│   ├── raw_review_logs.json
│   └── policy_mapping.csv
├── output/
│   └── .gitkeep
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── generate_summary.py
│   └── run_pipeline.py
├── docs/
│   ├── data_dictionary.md
│   ├── hypothesis_testing.md
│   └── pipeline_flow.md
└── tests/
    └── test_transform.py
```

## Skills Demonstrated

- JSON parsing
- ETL pipeline design
- Python scripting
- pandas data transformation
- Data validation
- Hypothesis testing
- QA review log analysis
- Readable summary generation
- Trust & Safety analytics
- Operational data cleaning

## Example Use Case

A QA or Trust & Safety team receives raw review logs in JSON format. Each record includes system predictions, reviewer decisions, metadata, and status codes.

The pipeline converts those logs into structured records that can be used for:

- QA reporting
- Rejected-case analysis
- Dashboard inputs
- Reviewer feedback
- Data-quality validation
- Business-readable summaries

## How To Run

From the main repository root:

```bash
cd json_etl_pipeline
python src/run_pipeline.py
```

Expected outputs:

```text
output/cleaned_review_logs.csv
output/hypothesis_test_results.csv
output/readable_case_summaries.md
```

## Data Privacy Note

This project uses mock data only. It does not include confidential company data, internal review IDs, real material IDs, employee information, internal table names, internal links, or proprietary business logic.
