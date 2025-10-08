from .exceptions import CalculatorError

def parse_tokens(line: str):
    """Parse input line into tokens. Expected: <op> <a> <b> or commands."""
    tokens = line.strip().split()
    return tokens

def parse_number(s: str):
    # LBYL example
    try:
        if '.' in s:
            return float(s)
        return int(s)
    except ValueError:
        # EAFP example: try converting with float
        try:
            return float(s)
        except Exception as e:
            raise CalculatorError(f"Invalid number: {s}") from e
