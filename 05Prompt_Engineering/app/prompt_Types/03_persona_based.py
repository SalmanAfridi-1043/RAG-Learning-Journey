from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

# Persona-based prompting means assigning the LLM a specific role or identity to influence how it responds.
messages = [
    {
        "role": "system",
        "content": "You are an experienced Python developer. Explain concepts using simple language and practical examples.",
    },
    {"role": "user", "content": "Explain Python decorators."},
]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)
