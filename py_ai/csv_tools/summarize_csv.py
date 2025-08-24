from __future__ import annotations
import os
from openai import OpenAI
from dotenv import load_dotenv
from .extract_data import extract_data

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_csv(file_path: str, max_chars: int = 800) -> str:
    """
    Pipeline: Extract CSV/XLSX data with Python, then summarize using AI.
    """
    text = extract_data(file_path)
    if not text.strip():
        return ""

    prompt = f"Summarize the following data and provide insights in less than {max_chars} characters:\n\n{text}"

    response = client.responses.create(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": "You are a helpful data analyst."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.output_text.strip()
