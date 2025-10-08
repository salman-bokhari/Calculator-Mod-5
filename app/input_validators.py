from app.exceptions import InvalidInputError, InvalidOperationError

def validate_number(value):
    """Ensure the provided input can be converted to a float."""
    try:
        return float(value)
    except ValueError:
        raise InvalidInputError(f"Invalid number: {value}")

def validate_numbers(a, b):
    return validate_number(a), validate_number(b)
