# Pipeline Flow

```text
1. Load raw nested JSON review logs
2. Extract fields from nested system, reviewer, and metadata objects
3. Convert raw status codes into readable review status labels
4. Validate required output columns
5. Add hypothesis and data-quality flags
6. Export cleaned structured CSV
7. Export hypothesis test results
8. Generate readable Markdown case summaries
```

## Design Principles

- Keep raw mock data separate from transformed outputs.
- Use small functions with clear responsibilities.
- Make transformation logic easy to test.
- Avoid hardcoding confidential or internal data.
- Generate outputs that are useful for both technical and non-technical stakeholders.
