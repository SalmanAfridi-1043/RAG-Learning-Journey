from openai import OpenAI
from app.config.settings import OPENROUTER_API_KEY, BASE_URL

# client: Reusable connection for our application.
client = OpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)
