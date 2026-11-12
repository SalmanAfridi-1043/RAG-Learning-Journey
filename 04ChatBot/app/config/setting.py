import os
from dotenv import load_dotenv


load_dotenv()


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


MODEL = "nvidia/nemotron-3.5-super-vl:free"


TEMPERATURE = 0.7
MAX_TOKENS = 600
