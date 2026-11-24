import pandas as pd


def get_nested_value(data: dict, path: list[str], default=None):
    """
    Safely extract a nested value from a dictionary.

    Example:
        get_nested_value(record, ["review_payload", "system_result", "description"])
    """
    current = data

    for key in path:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
        if current is None:
            return default

    return current


def classify_review_status(status_code) -> str:
    """
    Convert raw status code into readable status.

    Example mapping:
    - 2 = published
    - 3 = rejected
    """
    mapping = {
        2: "published",
        3: "rejected",
        "2": "published",
        "3": "rejected"
    }
    return mapping.get(status_code, "unknown")


def flatten_review_record(record: dict) -> dict:
    """
    Convert one nested JSON review record into a flat dictionary.
    """
    status_code = get_nested_value(
        record,
        ["review_payload", "reviewer_result", "status_code"],
        default=""
    )

    return {
        "material_id": record.get("material_id", ""),
        "operator_id": record.get("operator_id", ""),
        "review_date": record.get("review_date", ""),
        "system_description": get_nested_value(record, ["review_payload", "system_result", "description"], ""),
        "reviewer_description": get_nested_value(record, ["review_payload", "reviewer_result", "description"], ""),
        "review_status": classify_review_status(status_code),
        "status_code": status_code,
        "entity_type": get_nested_value(record, ["review_payload", "system_result", "entity_type"], ""),
        "subject_category": get_nested_value(record, ["review_payload", "reviewer_result", "subject_category"], ""),
        "confidence_score": get_nested_value(record, ["review_payload", "system_result", "confidence_score"], None),
        "language": get_nested_value(record, ["review_payload", "metadata", "language"], ""),
        "region": get_nested_value(record, ["review_payload", "metadata", "region"], ""),
        "source": get_nested_value(record, ["review_payload", "metadata", "source"], "")
    }


def transform_records(records: list[dict]) -> pd.DataFrame:
    """
    Transform raw JSON records into a structured dataframe.
    """
    flattened_records = [flatten_review_record(record) for record in records]
    df = pd.DataFrame(flattened_records)

    if not df.empty:
        df["confidence_score"] = pd.to_numeric(df["confidence_score"], errors="coerce")

    return df
