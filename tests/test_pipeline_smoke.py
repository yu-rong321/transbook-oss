import json

from PIL import Image, ImageDraw

from transbook.pipeline.process_image import process_image


def test_process_image_writes_expected_outputs(tmp_path):
    image_path = tmp_path / "page.png"
    out_dir = tmp_path / "out"

    image = Image.new("RGB", (800, 500), "white")
    draw = ImageDraw.Draw(image)
    draw.text((120, 100), "Hello world", fill="black")
    image.save(image_path)

    process_image(
        image_path=image_path,
        target_lang="zh-TW",
        out_dir=out_dir,
    )

    assert (out_dir / "ocr_blocks.json").exists()
    assert (out_dir / "visual_metadata.json").exists()
    assert (out_dir / "translation_blocks.json").exists()
    assert (out_dir / "rendered.png").exists()

    translation_blocks = json.loads((out_dir / "translation_blocks.json").read_text(encoding="utf-8"))

    assert translation_blocks[0]["source_text"] == "Hello world"
    assert translation_blocks[0]["translated_text"] == "[zh-TW] Hello world"