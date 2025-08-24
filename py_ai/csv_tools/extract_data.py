from pathlib import Path
import pandas as pd

def extract_data(file_path: str) -> str:
    """
    Extracts a human-readable summary of CSV/XLSX content.
    Returns a string summarizing columns and first rows.
    """
    p = Path(file_path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if p.suffix.lower() not in [".csv", ".xlsx"]:
        raise ValueError(f"Unsupported file type: {p.suffix}")

    if p.suffix.lower() == ".csv":
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    summary_lines = [f"Columns ({len(df.columns)}): {', '.join(df.columns)}"]
    summary_lines.append(f"Total rows: {len(df)}")
    summary_lines.append("\nSample rows:")
    summary_lines.extend(df.head(5).to_string(index=False).splitlines())

    return "\n".join(summary_lines)
