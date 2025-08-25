from pathlib import Path
from .extractors import pdf, image, csv

def extract_file(file_path: Path) -> str:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = file_path.suffix.lower()
    if suffix == ".pdf":
        return pdf.extract_text(file_path)
    elif suffix in [".png", ".jpg", ".jpeg"]:
        return image.extract_text(file_path)
    elif suffix in [".csv", ".xlsx"]:
        return csv.extract_data(file_path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

def summarize_file(file_path: Path, max_chars: int = 800) -> str:
    suffix = file_path.suffix.lower()
    if suffix == ".pdf":
        return pdf.summarize_pdf(file_path, max_chars=max_chars)
    elif suffix in [".png", ".jpg", ".jpeg"]:
        return image.summarize_image(file_path, max_chars=max_chars)
    elif suffix in [".csv", ".xlsx"]:
        return csv.summarize_csv(file_path, max_chars=max_chars)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
