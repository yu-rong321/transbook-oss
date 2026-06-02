from PIL import Image

from transbook.ocr.schema import BBox, OCRBlock
from transbook.vision.background_sampler import analyze_block_background


def test_solid_background_is_classified_as_replace():
    image = Image.new("RGB", (200, 100), "white")
    block = OCRBlock(
        id="block_001",
        text="Hello",
        bbox=BBox(x=20, y=20, width=80, height=30),
        score=0.99,
    )

    visual = analyze_block_background(image, block)

    assert visual.block_id == "block_001"
    assert visual.background_color == "#ffffff"
    assert visual.background_mode == "solid"
    assert visual.recommended_render_mode == "replace"