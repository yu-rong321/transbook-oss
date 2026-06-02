import json
from pathlib import Path

from PIL import Image

from transbook.ocr.mock_ocr import run_mock_ocr
from transbook.render.pillow_overlay import render_translated_block
from transbook.translation.mock_translator import translate_text
from transbook.vision.background_sampler import analyze_block_background


def _write_json(path: Path, data: object) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def process_image(image_path: Path, target_lang: str, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    image = Image.open(image_path).convert("RGB")

    ocr_result = run_mock_ocr(
        image_width=image.width,
        image_height=image.height,
    )

    visual_metadata = []
    translation_blocks = []

    rendered = image.copy()

    for block in ocr_result.blocks:
        visual = analyze_block_background(image, block)
        translated_text = translate_text(block.text, target_lang)

        visual_metadata.append(visual.model_dump())
        translation_blocks.append(
            {
                "block_id": block.id,
                "source_text": block.text,
                "translated_text": translated_text,
                "target_lang": target_lang,
            }
        )

        if visual.recommended_render_mode == "replace":
            rendered = render_translated_block(
                image=rendered,
                block=block,
                visual=visual,
                translated_text=translated_text,
            )

    _write_json(out_dir / "ocr_blocks.json", ocr_result.model_dump())
    _write_json(out_dir / "visual_metadata.json", visual_metadata)
    _write_json(out_dir / "translation_blocks.json", translation_blocks)

    rendered.save(out_dir / "rendered.png")