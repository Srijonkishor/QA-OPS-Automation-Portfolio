import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from transform import classify_review_status, flatten_review_record


def test_classify_review_status():
    assert classify_review_status(2) == "published"
    assert classify_review_status(3) == "rejected"
    assert classify_review_status("2") == "published"
    assert classify_review_status("3") == "rejected"
    assert classify_review_status(999) == "unknown"


def test_flatten_review_record():
    record = {
        "material_id": "MAT-TEST",
        "operator_id": "operator_test",
        "review_date": "2026-11-20",
        "review_payload": {
            "system_result": {
                "description": "Sample system description",
                "confidence_score": 0.75,
                "entity_type": "product"
            },
            "reviewer_result": {
                "description": "Sample reviewer finding",
                "status_code": 3,
                "subject_category": "label_mismatch"
            },
            "metadata": {
                "language": "en",
                "region": "sample_region",
                "source": "mock_source"
            }
        }
    }

    flattened = flatten_review_record(record)

    assert flattened["material_id"] == "MAT-TEST"
    assert flattened["review_status"] == "rejected"
    assert flattened["entity_type"] == "product"
    assert flattened["subject_category"] == "label_mismatch"
