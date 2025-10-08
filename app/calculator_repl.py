from app.operations import add, subtract, multiply, divide, power, modulo
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError
from app.history import History

calc_history = History()

def calculate(a, op, b):
    ops = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        '%': modulo
    }
    func = ops.get(op)
    if not func:
        raise InvalidOperationError("Unsupported operator")
    return func(a, b)

def process_input(command):
    parts = command.split()
    if len(parts) != 3:
        return "Invalid input"
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
