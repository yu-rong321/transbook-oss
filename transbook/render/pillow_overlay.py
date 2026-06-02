from PIL import Image, ImageDraw, ImageFont

from transbook.ocr.bbox import clamp_bbox_to_image
from transbook.ocr.schema import OCRBlock
from transbook.vision.visual_metadata import VisualMetadata


def render_translated_block(
    image: Image.Image,
    block: OCRBlock,
    visual: VisualMetadata,
    translated_text: str,
) -> Image.Image:
    output = image.convert("RGB").copy()

    safe_block = clamp_bbox_to_image(
        block=block,
        image_width=output.width,
        image_height=output.height,
    )

    if safe_block is None:
        return output

    draw = ImageDraw.Draw(output)

    x1 = int(safe_block.bbox.x)
    y1 = int(safe_block.bbox.y)
    x2 = int(safe_block.bbox.x + safe_block.bbox.width)
    y2 = int(safe_block.bbox.y + safe_block.bbox.height)

    draw.rectangle(
        [x1, y1, x2, y2],
        fill=visual.background_color,
    )

    try:
        font = ImageFont.truetype(
            "arial.ttf",
            size=max(12, int(safe_block.bbox.height * 0.45)),
        )
    except OSError:
        font = ImageFont.load_default()

    draw.text(
        (x1, y1),
        translated_text,
        fill="#111111",
        font=font,
    )

    return output