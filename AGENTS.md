# AGENTS.md

## Project Goal

This repository implements an OCR-to-translation overlay pipeline for image-based ebooks and documents.

## Engineering Rules

- OCR bounding boxes are the source of truth for text regions.
- OpenCV/Pillow should analyze OCR bounding boxes, not create a competing text detection system in the MVP.
- Never commit user-uploaded books, copyrighted samples, API keys, or `.env` files.
- All OCR and translation providers must be mockable.
- Tests must not call real OCR or translation APIs by default.
- Rendering must never modify blocks that are not selected.
- BBox coordinates must be validated against image dimensions.
- Logs must not contain full OCR text from private user inputs.

## Preferred Commands

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
python -m transbook.cli process samples/input/page_001.png --target-lang zh-TW --out outputs/page_001