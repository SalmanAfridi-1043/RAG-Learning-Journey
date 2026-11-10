from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)


MODEL = "nvidia/nemotron-3.5-super-vl:free"


def chat(user_input: str, messages: list):
    # Add user input to message list
    messages.append({"role": "user", "content": user_input})

    # Send complete conversation
    response = client.chat.completions.create(model=MODEL, messages=messages)

    # Extract assistant response
    answer = response.choices[0].message.content

    # Save assistant response
    messages.append({"role": "assistant", "content": answer})

    # we need to return both the answer and the updated messages list so that the conversation history is maintained across multiple calls to the chat function.
    return {"answer": answer, "messages": messages}
