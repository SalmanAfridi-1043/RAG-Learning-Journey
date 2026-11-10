# from app.services.gemini import generate_answer
from app.services.openai import generate_answer

# response = client.models.generate_content(
#     model="gemini-3.8-flash", contents="Explain what an API is in simple words."
# )

# print(response.text)

# now created and used in  a function to generate answer using the gemini model
# print(generate_answer("Explain what an API is in simple words."))


# -------------------------------------------------------------------------------------
# using system instruction to guide the model's response
# prompt = "Explain what a REST API is in simple words."
# system_instruction = (
#     "You are a helpful assistant that explains technical concepts in simple terms."
# )
# answer = generate_answer(prompt, system_instruction)
# print(answer)


# -------------------------------------------------------------------------------------

prompt = "Explain what a REST API is in simple words."
system_instruction = (
    "You are a helpful assistant that explains technical concepts in simple terms."
)

answer = generate_answer(prompt, system_instruction)
print(answer)
