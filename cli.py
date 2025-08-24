import argparse
from py_ai.pdf_tools import extract_text as extract_pdf_text, summarize_pdf
from py_ai.image_tools import extract_text as extract_image_text, summarize_image

def main():
    parser = argparse.ArgumentParser(prog="py-ai", description="Python AI tools (Py.ai).")
    subparsers = parser.add_subparsers(dest="tool", required=True, help="Select a tool")

    # === PDF tool ===
    pdf_parser = subparsers.add_parser("pdf", help="PDF-related commands")
    pdf_sub = pdf_parser.add_subparsers(dest="command", required=True)
    extract_parser = pdf_sub.add_parser("extract", help="Extract text from PDF")
    extract_parser.add_argument("pdf", help="Path to PDF file")
    summarize_parser = pdf_sub.add_parser("summarize", help="Summarize PDF")
    summarize_parser.add_argument("pdf", help="Path to PDF file")
    summarize_parser.add_argument("--max-chars", type=int, default=800, help="Max chars in summary")

    # === Image tool ===
    img_parser = subparsers.add_parser("image", help="Image-related commands")
    img_sub = img_parser.add_subparsers(dest="command", required=True)
    extract_img_parser = img_sub.add_parser("extract", help="Extract text from image")
    extract_img_parser.add_argument("image", help="Path to image file")
    summarize_img_parser = img_sub.add_parser("summarize", help="Summarize image text")
    summarize_img_parser.add_argument("image", help="Path to image file")
    summarize_img_parser.add_argument("--max-chars", type=int, default=800, help="Max chars in summary")

    args = parser.parse_args()

    if args.tool == "pdf":
        if args.command == "extract":
            print(extract_pdf_text(args.pdf))
        elif args.command == "summarize":
            print(summarize_pdf(args.pdf, max_chars=args.max_chars))

    elif args.tool == "image":
        if args.command == "extract":
            print(extract_image_text(args.image))
        elif args.command == "summarize":
            print(summarize_image(args.image, max_chars=args.max_chars))

if __name__ == "__main__":
    main()
