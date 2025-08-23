import argparse
from py_ai.pdf_tools import extract_text, summarize_pdf
# from py_ai.image_tools import resize_image  # future example

def main():
    parser = argparse.ArgumentParser(prog="py-ai", description="Python AI tools (Py.ai).")
    subparsers = parser.add_subparsers(dest="tool", required=True, help="Select a tool")

    # === PDF tool ===
    pdf_parser = subparsers.add_parser("pdf", help="PDF-related commands")
    pdf_sub = pdf_parser.add_subparsers(dest="command", required=True)

    # pdf extract
    extract_parser = pdf_sub.add_parser("extract", help="Extract text from PDF")
    extract_parser.add_argument("pdf", help="Path to PDF file")

    # pdf summarize
    summarize_parser = pdf_sub.add_parser("summarize", help="Summarize PDF")
    summarize_parser.add_argument("pdf", help="Path to PDF file")
    summarize_parser.add_argument("--max-chars", type=int, default=800, help="Max chars in summary")

    # === IMAGE tool example (future) ===
    # image_parser = subparsers.add_parser("image", help="Image-related commands")
    # image_sub = image_parser.add_subparsers(dest="command", required=True)
    # resize_parser = image_sub.add_parser("resize", help="Resize an image")
    # resize_parser.add_argument("image", help="Image path")
    # resize_parser.add_argument("--width", type=int)
    # resize_parser.add_argument("--height", type=int)

    args = parser.parse_args()

    # PDF tool commands
    if args.tool == "pdf":
        if args.command == "extract":
            print(extract_text(args.pdf))
        elif args.command == "summarize":
            print(summarize_pdf(args.pdf, max_chars=args.max_chars))

if __name__ == "__main__":
    main()
