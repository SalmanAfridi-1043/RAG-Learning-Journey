from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# A prompt template is a reusable prompt containing variables that we can dynamically replace with different values.

# Prompt Template
prompt_template = """
You are a programming tutor.

Explain the following programming concept:
{topic}

Use simple English and provide one Python example.
"""

# Dynamic Variables (used to assign the main topic to the template)
topic = "Python Loop"

# Generate Prompt (-> .format() replaces the template variable with the actual value.)
prompt = prompt_template.format(topic=topic)

messages = [{"role": "user", "content": prompt}]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)
