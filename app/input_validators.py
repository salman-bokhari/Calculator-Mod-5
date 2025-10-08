from .exceptions import InvalidOperationError

def validate_numbers(*args):
    for a in args:
        try:
            float(a)
        except Exception:
            raise InvalidOperationError(f"Invalid number: {a}")
    return [float(a) for a in args]
