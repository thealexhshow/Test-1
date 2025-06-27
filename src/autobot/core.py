import os
from dotenv import load_dotenv
import openai

load_dotenv()                       # reads .env in project root
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Return a single response string from the model."""
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
    )
    return resp.choices[0].message.content.strip()
