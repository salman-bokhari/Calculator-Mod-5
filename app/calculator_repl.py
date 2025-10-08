from app.operations import add, subtract, multiply, divide
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError
from app.history import History

calc_history = History()

def calculate(a, op, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return divide(a, b)
    else:
        raise InvalidOperationError(f"Invalid operation: {op}")

def process_input(command):
    """Processes a single command string like '2 + 3'."""
    parts = command.split()
    if len(parts) != 3:
        return "Invalid command format"

    num1, op, num2 = parts
    try:
        a, b = validate_numbers(num1, num2)
        result = calculate(a, op, b)
        calc_history.add(a, op, b, result)
        return f"Result: {result}"
    except (InvalidInputError, InvalidOperationError, ZeroDivisionError) as e:
        return str(e)
    except Exception as e:
        return f"Unexpected error: {e}"

def show_history():
    return calc_history.get_history()

def clear_history():
    calc_history.df = calc_history.df.iloc[0:0]
