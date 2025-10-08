"""REPL module for calculator operations and user interaction."""
from app.calculation import Calculation
from app.input_validators import validate_expression
from app.history import History
from app.exceptions import CalculatorError


def process_input(user_input: str) -> str:
    """Process a single calculator command string."""
    user_input = user_input.strip().lower()
    if user_input in ("exit", "quit"):
        return "Exiting calculator..."

    if user_input == "history":
        hist = History.get_instance()
        if len(hist) == 0:
            return "History is empty."
        return "\n".join(f"{h['a']} {h['op']} {h['b']} = {h['result']}" for h in hist)

    if user_input == "clear history":
        History.clear_history()
        return "History cleared."

    try:
        a, op, b = validate_expression(user_input)
        calc = Calculation(a, b, op)
        result = calc.perform()
        History.add_history(calc.to_dict())
        return f"Result: {result}"
    except CalculatorError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def run_repl():
    """Run interactive REPL loop."""
    print("Welcome to the Calculator! Type 'exit' to quit.")
    while True:
        user_input = input(">>> ")
        response = process_input(user_input)
        print(response)
        if "Exiting" in response:
            break
