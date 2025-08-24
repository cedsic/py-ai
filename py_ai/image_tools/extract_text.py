from typing import Optional
import cv2
import pytesseract
from pathlib import Path
from PIL import Image

def extract_text(image_path: str) -> str:
    """
    Extract text from an image using OpenCV + pytesseract.
    """
    p = Path(image_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {image_path}")
    if p.suffix.lower() not in [".png", ".jpg", ".jpeg"]:
        raise ValueError(f"Unsupported image format: {p.suffix}")

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(thresh)

    return text.strip()
