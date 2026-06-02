from PIL import Image, ImageStat

from transbook.ocr.bbox import clamp_bbox_to_image
from transbook.ocr.schema import OCRBlock
from transbook.vision.visual_metadata import VisualMetadata


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def analyze_block_background(image: Image.Image, block: OCRBlock) -> VisualMetadata:
    rgb_image = image.convert("RGB")
    safe_block = clamp_bbox_to_image(
        block=block,
        image_width=rgb_image.width,
        image_height=rgb_image.height,
    )

    if safe_block is None:
        return VisualMetadata(
            block_id=block.id,
            background_color="#ffffff",
            estimated_text_color=None,
            background_variance=0.0,
            background_mode="complex",
            recommended_render_mode="manual_review",
        )

    x1 = int(safe_block.bbox.x)
    y1 = int(safe_block.bbox.y)
    x2 = int(safe_block.bbox.x + safe_block.bbox.width)
    y2 = int(safe_block.bbox.y + safe_block.bbox.height)

    crop = rgb_image.crop((x1, y1, x2, y2))
    stat = ImageStat.Stat(crop)

    mean_rgb = tuple(int(v) for v in stat.mean)
    variance = sum(stat.var) / len(stat.var)

    if variance < 50:
        background_mode = "solid"
        render_mode = "replace"
    elif variance < 500:
        background_mode = "simple"
        render_mode = "replace"
    else:
        background_mode = "complex"
        render_mode = "manual_review"

    return VisualMetadata(
        block_id=block.id,
        background_color=_rgb_to_hex(mean_rgb),
        estimated_text_color=None,
        background_variance=variance,
        background_mode=background_mode,
        recommended_render_mode=render_mode,
    )