from .exceptions import InvalidOperationError

def validate_numbers(*args):
    for a in args:
        try:
            float(a)
        except Exception:
            raise InvalidOperationError(f"Invalid number: {a}")
    return [float(a) for a in args]

def validate_number(value):
    """Validate and convert input into a float. Raise ValueError if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number: {value}")
