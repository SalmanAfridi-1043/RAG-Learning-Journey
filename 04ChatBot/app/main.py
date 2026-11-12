from app.services.chat_service import chat


print("================================")
print("       LLM CHATBOT")
print("================================")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("\nUser : ")

    if user_input.lower() == "exit":
        print("\n------ Chat End -----\n")
        break

    print("Assistant: ", end="", flush=True)

    chat(user_input)

    print("\n---------- Response Completed ----------\n")
