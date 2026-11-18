from datetime import date, timedelta


def get_previous_working_day(run_date: date | None = None) -> date:
    """
    Return the most recent working day before the given run date.

    If today is Monday, the target date should be the previous Friday.
    If today is Tuesday-Friday, the target date should be yesterday.
    If today is Saturday or Sunday, the target date should be Friday.
    """
    if run_date is None:
        run_date = date.today()

    target_date = run_date - timedelta(days=1)

    while target_date.weekday() >= 5:
        target_date -= timedelta(days=1)

    return target_date


def format_date_for_sql(target_date: date) -> str:
    """
    Format date as YYYY-MM-DD for SQL filters.
    """
    return target_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    target = get_previous_working_day()
    print("Previous working day:", target)
    print("SQL date:", format_date_for_sql(target))
