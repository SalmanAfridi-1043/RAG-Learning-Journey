from pydantic import BaseModel, Field, ValidationError


# Define a Pydantic Model
class Student(BaseModel):
    name: str
    age: int = Field(gt=0)
    skills: list[str]


# Valid Data
student = Student(name="Salman", age=22, skills=["Python", "Java", "AI"])

print("STUDENT OBJECT : ")
print(student)

# Accessing Values
print("\nNAME:", student.name)
print("AGE:", student.age)

# Convert into Dictionary
print("\nDICTIONARY:")
print(student.model_dump())

# Convert into JSON
print("\nJSON:")
print(student.model_dump_json(indent=4))


# Invalid Data
try:
    invalid_student = Student(name="Ali", age=-5, skills=["Python"])
except ValidationError as e:
    print("\nVALIDATION ERROR:")
    print(e)
