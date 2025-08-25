from pathlib import Path
import cv2
import pytesseract
from ..utils import summarize_text

def extract_text(file_path: str) -> str:
    p = Path(file_path)
    if not p.exists() or p.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
        raise ValueError("Unsupported image format")
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(thresh)
    return text.strip()

def summarize_image(file_path: str, max_chars: int = 800) -> str:
    text = extract_text(file_path)
    return summarize_text(text, max_chars=max_chars)
