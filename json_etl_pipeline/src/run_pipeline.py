from pathlib import Path
import sys

# Allow running this file directly from the json_etl_pipeline folder.
sys.path.append(str(Path(__file__).resolve().parent))

from extract import load_json_records
from transform import transform_records
from validate import validate_required_columns, add_quality_flags, run_hypothesis_tests
from generate_summary import generate_markdown_report


ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "output"


def run_pipeline() -> None:
    """
    Run the full JSON ETL pipeline.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    raw_records = load_json_records(DATA_DIR / "raw_review_logs.json")

    cleaned_df = transform_records(raw_records)
    validate_required_columns(cleaned_df)

    cleaned_df = add_quality_flags(cleaned_df)
    hypothesis_results_df = run_hypothesis_tests(cleaned_df)
    readable_report = generate_markdown_report(cleaned_df)

    cleaned_output_path = OUTPUT_DIR / "cleaned_review_logs.csv"
    hypothesis_output_path = OUTPUT_DIR / "hypothesis_test_results.csv"
    summary_output_path = OUTPUT_DIR / "readable_case_summaries.md"

    cleaned_df.to_csv(cleaned_output_path, index=False)
    hypothesis_results_df.to_csv(hypothesis_output_path, index=False)
    summary_output_path.write_text(readable_report, encoding="utf-8")

    print("JSON ETL pipeline completed successfully.")
    print(f"Cleaned data: {cleaned_output_path}")
    print(f"Hypothesis results: {hypothesis_output_path}")
    print(f"Readable summaries: {summary_output_path}")


if __name__ == "__main__":
    run_pipeline()
