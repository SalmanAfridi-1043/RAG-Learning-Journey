from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

messages = [
    {
        "role": "system",
        "content": "Return only valid JSON. Do not include Markdown code blocks.",
    },
    {
        "role": "user",
        "content": """
        Create student information with these details:

        Name: Salman
        Age: 22
        Skills: Python, Java, AI

        Return JSON with name, age, and skills.
        """,
    },
]

response = client.chat.completions.create(model=MODEL, messages=messages)

# Get JSON string
json_output = response.choices[0].message.content

print("RAW JSON : ")
print(json_output)

# Convert JSON string into Python dictionary
student = json.loads(json_output)

print("\nPYTHON DICTIONARY : ")
print(student)

print("\nACCESSING DATA : ")
print(student["name"])
print(student["skills"])

# Convert dictionary back into JSON
converted_json = json.dumps(student, indent=4)

print("\nFORMATTED JSON:")
print(converted_json)


# Two important methods:
# - json.loads() → JSON string to Python dictionary.
# - json.dumps() → Python dictionary to JSON string.
