from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# Chain-of-Thought prompting encourages an LLM to break a complex problem into smaller reasoning steps before providing an answer.
messages = [
    {
        "role": "user",
        "content": """
        A shopkeeper buys a laptop for Rs. 80,000.
        He sells it for Rs. 96,000.

        Calculate his profit percentage.

        Break the solution into clear steps and show the formulas.
        """,
    }
]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)
