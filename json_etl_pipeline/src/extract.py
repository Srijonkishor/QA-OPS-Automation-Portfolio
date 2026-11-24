import json
from pathlib import Path
from typing import Any


def load_json_records(path: str | Path) -> list[dict[str, Any]]:
    """
    Load raw JSON review logs from a file.

    Args:
        path: Path to JSON file.

    Returns:
        A list of review log dictionaries.
    """
    path = Path(path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Expected JSON root to be a list of records.")

    return data
