from openai import OpenAI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


# Define Pydantic Model
class Student(BaseModel):
    name: str
    age: int
    skills: list[str]


# Ask LLM to extract student information
messages = [
    {
        "role": "system",
        "content": "Extract student information and return valid JSON only.",
    },
    {
        "role": "user",
        "content": """
        My name is Salman. I am 22 years old.
        I know Python, Java, and Machine Learning.

        Extract my information.
        """,
    },
]


response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "json_object"},
    # JSON mode asks the model to return valid JSON.
)


# Get JSON response
json_output = response.choices[0].message.content


# Validate using Pydantic (checks wether JSON matches your expected structure.)
student = Student.model_validate_json(json_output)


# Display structured response
print("PYDANTIC OBJECT : ")
print(student)

print("\nNAME:", student.name)
print("AGE:", student.age)
print("SKILLS:", student.skills)

print("\nDICTIONARY:")
print(student.model_dump())
