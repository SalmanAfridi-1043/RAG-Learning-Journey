from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# System Prompt: Defines the model's behavior, instructions, personality, and rules.
# User Prompt: Contains the actual request or question from the user.
messages = [
    {
        "role": "system",
        "content": """
        You are a Python programming tutor.

        Rules:
        - Use simple English.
        - Explain concepts in bullet points.
        - Always provide a practical Python example.
        - Avoid unnecessary theory.
        """,
    },
    {"role": "user", "content": "Explain Python list comprehensions."},
]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)


# Remember:
# - System = How the model should behave.
# - User = What the model should do.
# - Assistant = Previous model responses.
