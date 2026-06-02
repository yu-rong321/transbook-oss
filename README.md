\# TransBook OSS



TransBook OSS is an open-source OCR-to-translation overlay pipeline for image-based ebooks and documents.



It detects text regions, extracts visual metadata, translates selected text blocks, and renders translated text back into the original image layout.



\## MVP Pipeline



```text

Image

→ OCR blocks

→ Visual metadata

→ Translation

→ Overlay rendering

→ Translated image

Current Status



This repository is currently an MVP prototype.



The first version uses:



Mock OCR

Mock translation

Pillow-based overlay rendering

Synthetic sample images only



The goal is to establish a clean, testable, open-source core before integrating real OCR and translation providers.



Quickstart



Install in editable mode:



python -m pip install -e ".\[dev]"



Create a synthetic sample image:



python -c "from PIL import Image, ImageDraw; img=Image.new('RGB',(800,500),'white'); d=ImageDraw.Draw(img); d.text((120,100),'Hello world',fill='black'); img.save('samples/input/page\_001.png')"



Run the pipeline:



python -m transbook.cli process samples/input/page\_001.png --target-lang zh-TW --out outputs/page\_001



Expected output:



outputs/page\_001/

├─ ocr\_blocks.json

├─ visual\_metadata.json

├─ translation\_blocks.json

└─ rendered.png

Project Scope



This project focuses on the core document-image translation engine.



Included:



OCR block schema

Visual metadata extraction

Background color sampling

Mock translation

Pillow overlay rendering

CLI workflow

Tests for the MVP pipeline



Not included:



DRM circumvention

Copyrighted book datasets

Payment systems

User account systems

Commercial publisher workflows

Private user-uploaded documents

Engineering Principle



OCR bounding boxes are the source of truth for text regions.



OpenCV or Pillow may analyze OCR bounding boxes, but the MVP should not create a competing text-detection pipeline.



License



Apache-2.0

