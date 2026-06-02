from PIL import Image, ImageDraw, ImageFont

from transbook.ocr.schema import OCRBlock
from transbook.vision.visual_metadata import VisualMetadata


def render_translated_block(
    image: Image.Image,
    block: OCRBlock,
    visual: VisualMetadata,
    translated_text: str,
) -> Image.Image:
    output = image.convert("RGB").copy()
    draw = ImageDraw.Draw(output)

    x1 = int(block.bbox.x)
    y1 = int(block.bbox.y)
    x2 = int(block.bbox.x + block.bbox.width)
    y2 = int(block.bbox.y + block.bbox.height)

    draw.rectangle(
        [x1, y1, x2, y2],
        fill=visual.background_color,
    )

    try:
        font = ImageFont.truetype("arial.ttf", size=max(12, int(block.bbox.height * 0.45)))
    except OSError:
        font = ImageFont.load_default()

    draw.text(
        (x1, y1),
        translated_text,
        fill="#111111",
        font=font,
    )

    return output