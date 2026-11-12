from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


MODEL = "nvidia/nemotron-3.5-super-vl:free"


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

# Zero-shot prompting means asking an LLM to perform a task without providing any examples.
messages = [
    {
        "role": "user",
        "content": "Explain Python decorators in simple words with one example.",
    }
]


response = client.chat.completions.create(model=MODEL, messages=messages)


print(response.choices[0].message.content)
