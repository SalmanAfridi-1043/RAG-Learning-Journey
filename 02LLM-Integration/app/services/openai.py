from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


# MODEL = "gtp-4o-mini"


# def generate_answer(prompt: str) -> str:
#     response = client.responses.create(model=MODEL, input=prompt)
#     # return response.choices[0].text
#     return response.output_text


# ---------------------------------------------------------------------------------

MODEL = "nvidia/nemotron-3.5-super-vl:free"


def generate_answer(prompt: str, system_instruction: str) -> str:
    response = client.responses.create(
        model=MODEL, instructions=system_instruction, input=prompt
    )
    return response.output_text
