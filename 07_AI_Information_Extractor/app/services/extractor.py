from openai import APIError, AuthenticationError, RateLimitError
from pydantic import ValidationError
from app.services.llm_client import client
from app.config.settings import MODEL
from app.models.schemas import PersonInfo


# return Pydantic object of type PersonInfo
def extract_information(text: str) -> PersonInfo:

    # strip() - works like a trim()
    if not text.strip():
        raise ValueError("Input text cannot be empty!")

    messages = [
        {
            "role": "system",
            "content": """
            You are an information extraction assistant.

            Extract:
            - name
            - age
            - country
            - profession
            - skills

            Return valid JSON only.

            For missing information use:
            name: Unknown
            age: 0
            country: Unknown
            profession: Unknown
            skills: []
            """,
        },
        {"role": "user", "content": text},
    ]

    try:
        response = client.chat.completions.create(
            model=MODEL, messages=messages, response_format={"type": "json_object"}
        )

        result = response.choices[0].message.content

        if not result:
            raise ValueError("LLM returned an empty response!")

        infoObject = PersonInfo.model_validate_json(result)

        return infoObject

    except AuthenticationError:
        raise RuntimeError("Invalid Model API key!")

    except RateLimitError:
        raise RuntimeError("Model rate limit exceeded!")

    except ValidationError as e:
        raise RuntimeError(f"Invalid LLM output: {e}")

    except APIError as e:
        raise RuntimeError(f"Model API error: {e}")
