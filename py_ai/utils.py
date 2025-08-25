import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text: str, max_chars: int = 800, role: str = "assistant") -> str:
    """
    Summarize text using OpenAI API.
    """
    if not text.strip():
        return ""
    prompt = f"Summarize the following text in less than {max_chars} characters:\n\n{text}"
    response = client.responses.create(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": f"You are a helpful {role} that summarizes text clearly and concisely."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.output_text.strip()
