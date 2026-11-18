import pandas as pd


def remove_duplicate_materials(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate material IDs before sampling.
    """
    return df.drop_duplicates(subset=["material_id"]).reset_index(drop=True)


def sample_fixed_count(
    df: pd.DataFrame,
    count: int,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Randomly sample a fixed number of records.
    """
    if df.empty:
        return df

    sample_size = min(count, len(df))

    return df.sample(
        n=sample_size,
        random_state=random_state
    ).reset_index(drop=True)


def sample_by_reviewer_percentage(
    df: pd.DataFrame,
    percentage: float,
    random_state: int = 42
) -> pd.DataFrame:
    """
    Sample a percentage of records per reviewer.
    """
    sampled_groups = []

    for reviewer_id, group_df in df.groupby("reviewer_id"):
        sample_size = max(1, round(len(group_df) * percentage))

        sampled = group_df.sample(
            n=min(sample_size, len(group_df)),
            random_state=random_state
        )

        sampled_groups.append(sampled)

    if not sampled_groups:
        return pd.DataFrame(columns=df.columns)

    return pd.concat(sampled_groups, ignore_index=True)


if __name__ == "__main__":
    data = pd.read_csv("sample_qa_data.csv")

    data = remove_duplicate_materials(data)

    fixed_sample = sample_fixed_count(
        data,
        count=5
    )

    percentage_sample = sample_by_reviewer_percentage(
        data,
        percentage=0.10
    )

    print("Fixed sample")
    print(fixed_sample)

    print("\nPercentage sample")
    print(percentage_sample)
