import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from app.tools.calculator import calculator_tool, calculate_sum


load_dotenv()

MODEL = "nvidia/nemotron-3.5-super-vl:free"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"), base_url="https://openrouter.ai/api/v1"
)

# Available Python functions
available_tools = {"calculate_sum": calculate_sum}


user_input = "Calculate 25 + 35 using the calculator tool."


# Step 1: Send request to LLM
response = client.responses.create(
    model=MODEL, input=user_input, tools=[calculator_tool], tool_choice="required"
)


# Step 2: Prepare conversation history
conversation_history = [{"role": "user", "content": user_input}, *response.output]


# Step 3: Execute tool calls
for item in response.output:
    if item.type == "function_call":
        print("\nTool Requested:", item.name)

        arguments = json.loads(item.arguments)  # from JSON to dictionary

        function = available_tools[item.name]

        result = function(**arguments)

        print("Execution Result:", result)

        # Step 4: Send tool result back to LLM
        conversation_history.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": str(result),
            }
        )


# Step 5: Get final response from LLM
final_response = client.responses.create(
    model=MODEL, input=conversation_history, tools=[calculator_tool]
)

print("\nFinal Assistant Response : ")
print(final_response.output_text)
