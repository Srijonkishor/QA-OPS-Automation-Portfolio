import pandas as pd


def generate_case_summary(row: pd.Series) -> str:
    """
    Generate a readable Markdown summary for one review case.
    """
    material_id = row.get("material_id", "N/A")
    review_status = row.get("review_status", "N/A")
    entity_type = row.get("entity_type", "N/A")
    subject_category = row.get("subject_category", "N/A") or "Missing subject category"
    confidence_score = row.get("confidence_score", "N/A")
    system_description = row.get("system_description", "N/A")
    reviewer_description = row.get("reviewer_description", "N/A")

    if review_status == "rejected":
        plain_summary = (
            "The system output was rejected after manual review. "
            "The reviewer feedback should be included in QA analysis and used to identify recurring quality gaps."
        )
    elif review_status == "published":
        plain_summary = (
            "The system output was accepted after review. "
            "This case can be used as a positive reference example for quality monitoring."
        )
    else:
        plain_summary = (
            "The review status is unknown. "
            "This case should be checked before being used in reporting."
        )

    return f"""## {material_id}

**Review Status:** {review_status}  
**Entity Type:** {entity_type}  
**Subject Category:** {subject_category}  
**Confidence Score:** {confidence_score}  

**System Description:** {system_description}  

**Reviewer Finding:** {reviewer_description}  

### Readable Summary
{plain_summary}
"""


def generate_markdown_report(df: pd.DataFrame) -> str:
    """
    Generate readable Markdown summaries for all cases.
    """
    sections = ["# Readable Case Summaries", ""]

    for _, row in df.iterrows():
        sections.append(generate_case_summary(row))
        sections.append("---")

    return "\n".join(sections)
