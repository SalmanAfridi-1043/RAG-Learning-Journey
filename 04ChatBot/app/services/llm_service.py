from openai import OpenAI
from app.config.setting import OPENROUTER_API_KEY


client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")
