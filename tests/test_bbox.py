from transbook.ocr.bbox import clamp_bbox_to_image
from transbook.ocr.schema import BBox, OCRBlock


def test_valid_bbox_is_preserved():
    block = OCRBlock(
        id="block_001",
        text="Hello",
        bbox=BBox(x=10, y=20, width=100, height=40),
        score=0.99,
    )

    safe = clamp_bbox_to_image(block, image_width=300, image_height=200)

    assert safe is not None
    assert safe.bbox.x == 10
    assert safe.bbox.y == 20
    assert safe.bbox.width == 100
    assert safe.bbox.height == 40


def test_partially_out_of_bounds_bbox_is_clamped():
    block = OCRBlock(
        id="block_001",
        text="Hello",
        bbox=BBox(x=-10, y=20, width=50, height=40),
        score=0.99,
    )

    safe = clamp_bbox_to_image(block, image_width=300, image_height=200)

    assert safe is not None
    assert safe.bbox.x == 0
    assert safe.bbox.y == 20
    assert safe.bbox.width == 40
    assert safe.bbox.height == 40


def test_fully_out_of_bounds_bbox_returns_none():
    block = OCRBlock(
        id="block_001",
        text="Hello",
        bbox=BBox(x=400, y=20, width=50, height=40),
        score=0.99,
    )

    safe = clamp_bbox_to_image(block, image_width=300, image_height=200)

    assert safe is None