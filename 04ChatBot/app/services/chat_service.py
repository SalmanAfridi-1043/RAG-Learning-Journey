from app.services.llm_service import client
from app.config.setting import MODEL, TEMPERATURE, MAX_TOKENS


messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer clearly and accurately.",
    }
]


def chat(user_input: str) -> str:

    messages.append({"role": "user", "content": user_input})

    answer = ""

    try:
        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            stream=True,
        )

        for chunk in stream:
            content = chunk.choices[0].delta.content

            if content:
                # print the chunkds in stream flow and make the whole response step-wise and in runtime
                print(content, end="", flush=True)
                answer += content  # collecting answer to store it in history

        print()

        messages.append({"role": "assistant", "content": answer})

    except Exception as e:
        print("\nError:", e)
        messages.pop()
        return ""
