from transbook.ocr.schema import BBox, OCRBlock, OCRPageResult


def run_mock_ocr(image_width: int, image_height: int) -> OCRPageResult:
    return OCRPageResult(
        image_width=image_width,
        image_height=image_height,
        blocks=[
            OCRBlock(
                id="block_001",
                text="Hello world",
                bbox=BBox(
                    x=image_width * 0.15,
                    y=image_height * 0.20,
                    width=image_width * 0.40,
                    height=image_height * 0.08,
                ),
                score=0.99,
                source="mock",
            )
        ],
    )