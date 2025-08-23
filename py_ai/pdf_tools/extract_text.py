from typing import Optional
import fitz
from pathlib import Path

def extract_text(pdf_path: str) -> str:
    """
    Extract text from a PDF file (all pages).
    Raises FileNotFoundError for missing files and ValueError for non-PDFs.
    """
    p = Path(pdf_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")
    if p.suffix.lower() != ".pdf":
        raise ValueError(f"Not a PDF file: {pdf_path}")

    text_chunks = []
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text_chunks.append(page.get_text())
    return "\n".join(text_chunks).strip()
