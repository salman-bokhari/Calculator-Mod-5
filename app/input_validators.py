from app.exceptions import InvalidInputError, InvalidOperationError

def validate_number(value):
    """Ensure the provided input can be converted to a float."""
    try:
        return float(value)
    except ValueError:
        raise InvalidInputError(f"Invalid number: {value}")

def validate_numbers(a, b):
    """Validate two numbers and return floats."""
    return validate_number(a), validate_number(b)

def validate_expression(expr: str):
    """Parse a simple 'a op b' string into numbers and operator."""
    parts = expr.split()
    if len(parts) != 3:
        raise InvalidOperationError(f"Invalid expression format: {expr}")
    num1, op, num2 = parts
    a, b = validate_numbers(num1, num2)
    if op not in ("+", "-", "*", "/"):
        raise InvalidOperationError(f"Invalid operator: {op}")
    return a, op, b
