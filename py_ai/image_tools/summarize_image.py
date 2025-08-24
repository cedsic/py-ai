import os
from openai import OpenAI
from dotenv import load_dotenv
from .extract_text import extract_text

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, max_chars: int = 800) -> str:
    if not text.strip():
        return ""

    prompt = f"Summarize the following text in less than {max_chars} characters:\n\n{text}"

    response = client.responses.create(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text clearly and concisely."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.output_text.strip()

def summarize_image(image_path: str, max_chars: int = 800) -> str:
    text = extract_text(image_path)
    return summarize_text(text, max_chars=max_chars)
