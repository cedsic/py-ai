from pathlib import Path
import pandas as pd
from ..utils import summarize_text

def extract_data(file_path: str) -> str:
    p = Path(file_path)
    if not p.exists() or p.suffix.lower() not in [".csv", ".xlsx"]:
        raise ValueError("Unsupported file type")
    df = pd.read_csv(file_path) if p.suffix.lower() == ".csv" else pd.read_excel(file_path)
    lines = [f"Columns ({len(df.columns)}): {', '.join(df.columns)}", f"Total rows: {len(df)}"]
    lines.append("\nSample rows:")
    lines.extend(df.head(5).to_string(index=False).splitlines())
    return "\n".join(lines)

def summarize_csv(file_path: str, max_chars: int = 800) -> str:
    text = extract_data(file_path)
    return summarize_text(text, max_chars=max_chars)
