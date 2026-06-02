import pytest
from pydantic import ValidationError

from transbook.ocr.schema import BBox, OCRBlock


def test_bbox_requires_positive_width_and_height():
    with pytest.raises(ValidationError):
        BBox(x=0, y=0, width=0, height=10)

    with pytest.raises(ValidationError):
        BBox(x=0, y=0, width=10, height=-1)


def test_ocr_block_score_must_be_between_zero_and_one():
    with pytest.raises(ValidationError):
        OCRBlock(
            id="block_001",
            text="Hello",
            bbox=BBox(x=0, y=0, width=100, height=20),
            score=1.5,
        )