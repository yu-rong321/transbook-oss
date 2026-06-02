import argparse
from pathlib import Path

from transbook.pipeline.process_image import process_image


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TransBook OSS image OCR translation overlay pipeline"
    )
    subparsers = parser.add_subparsers(dest="command")

    process_parser = subparsers.add_parser("process")
    process_parser.add_argument("image")
    process_parser.add_argument("--target-lang", default="zh-TW")
    process_parser.add_argument("--out", default="outputs/page_001")

    args = parser.parse_args()

    if args.command == "process":
        process_image(
            image_path=Path(args.image),
            target_lang=args.target_lang,
            out_dir=Path(args.out),
        )
        print(f"Output written to: {args.out}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()