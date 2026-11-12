from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# Context-based prompting -  means providing relevant background information to an LLM so it can generate more accurate and relevant responses.

context = """
I am a beginner Python developer.
I am currently learning Object-Oriented Programming.
I already understand variables, functions, and loops.
"""

question = "Explain Python classes and objects."

messages = [
    {
        "role": "system",
        "content": f"""
        Use the following user context when answering:

        {context}

        Adjust your explanation according to the user's knowledge.
        """,
    },
    {"role": "user", "content": question},
]

response = client.chat.completions.create(model=MODEL, messages=messages)

print(response.choices[0].message.content)


# What's important:
# context: Background information about the user or task.
# question: The actual request.
# The LLM uses both to generate a relevant response.

# Real-world applications:
# - Chatbots that understand previous conversations.
# - RAG applications that provide documents as context.
