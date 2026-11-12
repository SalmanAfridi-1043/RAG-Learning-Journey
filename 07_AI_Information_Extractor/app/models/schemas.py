from pydantic import BaseModel, Field


# Responsible for Data with structured output
class PersonInfo(BaseModel):
    name: str = Field(description="Full name of the person")
    age: int = Field(description="Age of the person")
    country: str = Field(description="Country of the person")
    profession: str = Field(description="Profession or job title")
    skills: list[str] = Field(description="List of skills")


# ExtractionResponse: Defines the overall application response.
class ExtractionResponse(BaseModel):
    success: bool
    data: PersonInfo


# Why separate schemas:
# Because our LLM extraction logic shouldn't be responsible for defining the data structure. We keep data models independent and reusable.
