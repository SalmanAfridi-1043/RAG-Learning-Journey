import os
from dotenv import load_dotenv

load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing!")

BASE_URL = "https://openrouter.ai/api/v1"
