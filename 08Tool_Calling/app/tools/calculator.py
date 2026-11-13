def calculate_sum(a: float, b: float) -> float:
    """Calculate the sum of two numbers."""
    return a + b


calculator_tool = {
    "type": "function",
    "name": "calculate_sum",
    "description": "Calculate the sum of two numbers.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number"},
            "b": {"type": "number", "description": "Second number"},
        },
        "required": ["a", "b"],
        "additionalProperties": False,
    },
    "strict": True,
}
