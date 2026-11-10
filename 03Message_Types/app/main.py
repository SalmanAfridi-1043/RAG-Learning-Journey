from openai import OpenAI
from dotenv import load_dotenv
from services.model import chat
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

MODEL = "nvidia/nemotron-3.5-super-vl:free"

# messages = [
#     {"role": "system", "content": "You are a helpful Python tutor."},
#     {"role": "user", "content": "What is a variable?"},
#     {"role": "assistant", "content": "A variable is used to store data."},
#     {"role": "user", "content": "Give me a simple Python example."},
# ]
# for message in messages:
#     print(f"{message['role'].capitalize()}: {message['content']}")


# response = client.chat.completions.create(
#     model=MODEL,
#     messages=messages,
# )

# print(response.choices[0].message.content)


# ----------------------------------------------------------------------------------------

# Store conversation history
messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor.Try to give short and simple answers instead of long explanations. Be to the point and concise.",
    }
]


# # First interaction
# print("User: What is Python?")
# print("Assistant:", chat("What is Python?", messages))

# # Second interaction
# print("\nUser: What are its applications?")
# print("Assistant:", chat("What are its applications?", messages))


# while True:
#     user_input = input("User: ")
#     if user_input.lower() == "exit":
#         break
#     answer = chat(user_input, messages)
#     print(f"Assistant: {answer}")


while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = chat(user_input, messages)
    messages = response["messages"]  # Update messages with the latest conversation
    print(f"Assistant: {response['answer']}")
