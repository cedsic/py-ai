from pathlib import Path
import fitz
from ..utils import summarize_text

def extract_text(file_path: str) -> str:
    p = Path(file_path)
    if not p.exists() or p.suffix.lower() != ".pdf":
        raise ValueError("File not found or not a PDF")
    text = []
    with fitz.open(file_path) as doc:
        for page in doc:
            text.append(page.get_text())
    return "\n".join(text).strip()

def summarize_pdf(file_path: str, max_chars: int = 800) -> str:
    text = extract_text(file_path)
    return summarize_text(text, max_chars=max_chars)
