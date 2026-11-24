import pandas as pd


REQUIRED_COLUMNS = [
    "material_id",
    "operator_id",
    "review_date",
    "system_description",
    "reviewer_description",
    "review_status",
    "entity_type",
    "subject_category",
    "confidence_score"
]


def validate_required_columns(df: pd.DataFrame) -> None:
    """
    Validate that all required columns exist after transformation.
    """
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def add_quality_flags(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add data-quality and hypothesis-testing flags.
    """
    df = df.copy()

    df["description_too_short"] = df["system_description"].fillna("").str.len() < 30
    df["missing_subject_category"] = df["subject_category"].fillna("").str.strip() == ""
    df["low_confidence"] = df["confidence_score"].fillna(0) < 0.70
    df["is_rejected"] = df["review_status"] == "rejected"

    return df


def run_hypothesis_tests(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run simple hypothesis checks and return summarized test results.

    These are business-readable validations, not statistical significance tests.
    """
    df = add_quality_flags(df)

    tests = []

    tests.append({
        "hypothesis": "Rejected cases are more common when system descriptions are too short.",
        "test_field": "description_too_short",
        "total_flagged_records": int(df["description_too_short"].sum()),
        "rejected_flagged_records": int(df[df["description_too_short"]]["is_rejected"].sum()),
        "rejection_rate_when_flagged": round(float(df[df["description_too_short"]]["is_rejected"].mean() or 0), 4)
    })

    tests.append({
        "hypothesis": "Missing subject category increases rejected-case risk.",
        "test_field": "missing_subject_category",
        "total_flagged_records": int(df["missing_subject_category"].sum()),
        "rejected_flagged_records": int(df[df["missing_subject_category"]]["is_rejected"].sum()),
        "rejection_rate_when_flagged": round(float(df[df["missing_subject_category"]]["is_rejected"].mean() or 0), 4)
    })

    tests.append({
        "hypothesis": "Low confidence records require closer review.",
        "test_field": "low_confidence",
        "total_flagged_records": int(df["low_confidence"].sum()),
        "rejected_flagged_records": int(df[df["low_confidence"]]["is_rejected"].sum()),
        "rejection_rate_when_flagged": round(float(df[df["low_confidence"]]["is_rejected"].mean() or 0), 4)
    })

    return pd.DataFrame(tests)
