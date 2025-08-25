import argparse
from pathlib import Path
from .core import extract_file, summarize_file

def main():
    parser = argparse.ArgumentParser(
        prog="py-ai",
        description="Py.ai: Extract or Summarize any file (PDF, CSV/XLSX, Images)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Choose a command")

    # === Extract command ===
    extract_parser = subparsers.add_parser("extract", help="Extract content from a file")
    extract_parser.add_argument("file", help="Path to file (PDF, CSV/XLSX, PNG/JPG)")

    # === Summarize command ===
    summarize_parser = subparsers.add_parser("summarize", help="Summarize content using AI")
    summarize_parser.add_argument("file", help="Path to file (PDF, CSV/XLSX, PNG/JPG)")
    summarize_parser.add_argument("--max-chars", type=int, default=800, help="Maximum characters in summary")

    args = parser.parse_args()
    file_path = Path(args.file)

    try:
        if args.command == "extract":
            text = extract_file(file_path)
            print(text)
        elif args.command == "summarize":
            summary = summarize_file(file_path, max_chars=args.max_chars)
            print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
