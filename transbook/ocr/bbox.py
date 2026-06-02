from transbook.ocr.schema import BBox, OCRBlock


def clamp_bbox_to_image(
    block: OCRBlock,
    image_width: int,
    image_height: int,
) -> OCRBlock | None:
    """Clamp an OCR block bbox to image boundaries.

    Returns None when the bbox is fully outside the image or becomes invalid
    after clamping.
    """
    x1 = max(0, int(round(block.bbox.x)))
    y1 = max(0, int(round(block.bbox.y)))
    x2 = min(image_width, int(round(block.bbox.x + block.bbox.width)))
    y2 = min(image_height, int(round(block.bbox.y + block.bbox.height)))

    if x2 <= x1 or y2 <= y1:
        return None

    return block.model_copy(
        update={
            "bbox": BBox(
                x=x1,
                y=y1,
                width=x2 - x1,
                height=y2 - y1,
            )
        }
    )