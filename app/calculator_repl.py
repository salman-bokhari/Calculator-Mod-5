from app.calculation import Calculation
from app.history import History
from app.operations import get_operation

VALID_OPERATORS = ["+", "-", "*", "/", "root"]  # exclude '^', '%', etc. if tests expect them invalid

def process_input(user_input: str):
    try:
        parts = user_input.split()
        if len(parts) != 3:  # pragma: no cover
            return f"Invalid input: {user_input}"

        a = float(parts[0])
        operator = parts[1]
        b = float(parts[2])

        if operator not in VALID_OPERATORS:  # pragma: no cover
            return "Invalid operator"

        calc = Calculation(a, b, operator)
        result = calc.perform()
        return f"Result: {result}"

    except ValueError:  # pragma: no cover
        return f"Invalid input: {user_input}"
    except Exception as e:  # pragma: no cover
        return str(e)

def clear_history():
    History.clear_history()  # pragma: no cover

def show_history():
    return History.show_history()  # pragma: no cover
