from pydantic import BaseModel, Field, ValidationError


# Define Expected Structure
class Student(BaseModel):
    name: str
    age: int = Field(gt=0, lt=100)
    skills: list[str]


# Example LLM Output (Valid JSON)
llm_output = """
{
    "name": "Salman",
    "age": 22,
    "skills": ["Python", "Java", "AI"]
}
"""


try:
    # Convert JSON into validated Pydantic object
    student = Student.model_validate_json(llm_output)

    print("VALID OUTPUT!")
    print(student.model_dump())

except ValidationError as e:
    print("VALIDATION FAILED!")
    print(e)


# Test Invalid Output
invalid_output = """
{
    "name": "Ali",
    "age": -5,
    "skills": "Python"
}
"""


try:
    student = Student.model_validate_json(invalid_output)

    print("VALID OUTPUT!")
    print(student.model_dump())

except ValidationError as e:
    print("\nVALIDATION FAILED!")
    print(e)
