import pandas as pd


def calculate_shrinkage_rate(
    expected_workdays: float,
    actual_workdays: float
) -> float:
    """
    Calculate shrinkage rate.

    Formula:
    shrinkage = (expected_workdays - actual_workdays) / expected_workdays
    """
    if expected_workdays == 0:
        return 0

    return round(
        (expected_workdays - actual_workdays) / expected_workdays,
        4
    )


def add_shrinkage_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add shrinkage rate column to leave summary data.
    """
    df = df.copy()

    df["shrinkage_rate"] = df.apply(
        lambda row: calculate_shrinkage_rate(
            row["expected_workdays"],
            row["actual_workdays"]
        ),
        axis=1
    )

    return df


def format_weekly_summary(row: pd.Series) -> str:
    """
    Create a notification-ready weekly leave summary.
    """
    shrinkage_percent = round(row["shrinkage_rate"] * 100, 2)

    return (
        f"Week: {row['week']} | "
        f"Project: {row['project']} | "
        f"Planned Leaves: {row['planned_leaves']} | "
        f"Expected Workdays: {row['expected_workdays']} | "
        f"Actual Workdays: {row['actual_workdays']} | "
        f"Shrinkage: {shrinkage_percent}%"
    )


if __name__ == "__main__":
    data = pd.read_csv("sample_leave_data.csv")

    summary = add_shrinkage_rate(data)

    summary["weekly_message"] = summary.apply(
        format_weekly_summary,
        axis=1
    )

    print(summary)
