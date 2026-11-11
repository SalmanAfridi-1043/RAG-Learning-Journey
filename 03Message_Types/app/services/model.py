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
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.5,
        # temperature controls the randomness of the output. A higher temperature (e.g., 0.8) will make the output more random, while a lower temperature (e.g., 0.2) will make it more focused and deterministic.
        max_tokens=150,
        # max_tokens limits the length of the generated response. Limits means how longer or shorter the response can be. For example, if you set max_tokens to 50, the model will generate a response that is at most 50 tokens long.
        top_p=1,  # Top-P controls how many possible next tokens the model considers when generating a response.
        frequency_penalty=0,  # Frequency Penalty discourages the model from repeatedly using the same words or tokens.
        presence_penalty=0,  # Presence Penalty discourages the model from using tokens that have already appeared in the generated text.
        stop=[
            "\nUser:",
            "\nAssistant:",
        ],  # Stop sequences tell the model to stop generating when it encounters a specified sequence.
    )

    # Extract assistant response
    answer = response.choices[0].message.content

    # Save assistant response
    messages.append({"role": "assistant", "content": answer})

    # we need to return both the answer and the updated messages list so that the conversation history is maintained across multiple calls to the chat function.
    return {"answer": answer, "messages": messages}
