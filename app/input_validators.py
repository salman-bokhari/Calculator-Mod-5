from app.exceptions import InvalidInputError

def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise InvalidInputError("Invalid number input")

def validate_numbers(a, b):
    return [validate_number(a), validate_number(b)]
