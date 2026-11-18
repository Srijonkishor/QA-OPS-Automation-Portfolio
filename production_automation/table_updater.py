import pandas as pd


REQUIRED_COLUMNS = [
    "operator_id",
    "work_date",
    "production_count"
]


def validate_schema(df: pd.DataFrame) -> None:
    """
    Validate that the required columns exist in the dataframe.
    """
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def upsert_production_records(
    existing_df: pd.DataFrame,
    new_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Update existing production records or append new records.

    Unique key:
    - operator_id
    - work_date
    """
    validate_schema(existing_df)
    validate_schema(new_df)

    existing_df = existing_df.copy()
    new_df = new_df.copy()

    existing_df["record_key"] = (
        existing_df["operator_id"].astype(str)
        + "|"
        + existing_df["work_date"].astype(str)
    )

    new_df["record_key"] = (
        new_df["operator_id"].astype(str)
        + "|"
        + new_df["work_date"].astype(str)
    )

    existing_df = existing_df[
        ~existing_df["record_key"].isin(new_df["record_key"])
    ]

    final_df = pd.concat(
        [existing_df, new_df],
        ignore_index=True
    )

    final_df = final_df.drop(columns=["record_key"])

    return final_df


if __name__ == "__main__":
    existing = pd.read_csv("sample_production_data.csv")

    new_records = pd.DataFrame(
        [
            {
                "operator_id": "operator_001",
                "work_date": "2026-11-17",
                "production_count": 42
            },
            {
                "operator_id": "operator_002",
                "work_date": "2026-11-17",
                "production_count": 38
            }
        ]
    )

    updated = upsert_production_records(existing, new_records)

    print(updated)
