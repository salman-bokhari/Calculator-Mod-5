from app.input_validators import validate_numbers
from app.history import History
from app.calculation import Calculation

def process_input(user_input):
    try:
        parts = user_input.split()
        if len(parts) != 3:
            return "Invalid command format"
        a, op, b = parts
        a, b = validate_numbers(a, b)
        calc = Calculation(a, b, op)
        result = calc.perform()
        History.add(a, op, b, result)
        return f"Result: {result}"
    except Exception as e:
        return f"Invalid input: {str(e)}"

def show_history():
    return History.get_history()

def clear_history():
    History.clear_history()
