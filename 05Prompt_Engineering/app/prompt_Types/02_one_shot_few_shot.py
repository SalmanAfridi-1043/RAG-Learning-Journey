from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# One-shot: Give the LLM one example before asking it to perform a task.
messages = [
    {
        "role": "user",
        "content": """
        Convert English sentences into professional business language.

        Example:

        Input: Hey, send me the report.
        Output: Could you please share the report?

        Now convert:

        Input: Give me the project details.
        Output:
        """,
    }
]

# Few-shot: Give the LLM multiple examples so it can understand the expected pattern.
messages = [
    {
        "role": "user",
        "content": """
        Convert English sentences into professional business language.

        Examples:

        Input: Hey, send me the report.
        Output: Could you please share the report?

        Input: I need this done quickly.
        Output: I would appreciate it if this could be completed promptly.

        Now convert:

        Input: Give me the project details.
        Output:
        """,
    }
]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)
