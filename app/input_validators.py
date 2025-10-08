from app.exceptions import InvalidOperationError


def validate_number(value):
    """Ensure the provided input can be converted to a float."""
    try:
        return float(value)
    except ValueError:
        raise InvalidOperationError(f"Invalid number: {value}")


def validate_numbers(a, b):
    """Validate two inputs and return them as floats in a list."""
    return [validate_number(a), validate_number(b)]
