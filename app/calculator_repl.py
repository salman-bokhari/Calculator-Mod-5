"""Calculator REPL (Read-Eval-Print Loop) module."""

from app.calculation import Calculation
from app.history import History
from app.operations import add, subtract, multiply, divide
from app.input_validators import validate_numbers


def process_input(user_input: str):
    """Process user input and return the result or message."""
    parts = user_input.strip().split()

    if len(parts) != 3:
        return "Invalid input. Use format: <num1> <operator> <num2>"

    num1, operator, num2 = parts

    try:
        num1, num2 = validate_numbers(num1, num2)
    except ValueError as e:
        return str(e)

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if operator not in operations:
        return "Unsupported operator. Use +, -, *, or /."

    calc = Calculation(num1, num2, operations[operator])
    result = calc.perform()
    History.add_calculation(calc)
    return f"Result: {result}"


def show_history():
    """Display calculation history."""
    if not History.get_history():
        return "No calculations yet."
    lines = []
    for i, calc in enumerate(History.get_history(), start=1):
        lines.append(f"{i}: {calc}")
    return "\n".join(lines)


def clear_history():
    """Clear all history."""
    History.clear_history()
    return "History cleared."


def repl():  # pragma: no cover - interactive mode
    """Interactive calculator REPL loop."""
    print("Calculator REPL. Type 'quit' to exit, 'history' to see history.")  # pragma: no cover
    while True:  # pragma: no cover
        try:  # pragma: no cover
            user_input = input(">> ").strip()  # pragma: no cover
            if user_input.lower() in ("quit", "exit"):  # pragma: no cover
                print("Goodbye!")  # pragma: no cover
                break  # pragma: no cover
            elif user_input.lower() == "history":  # pragma: no cover
                print(show_history())  # pragma: no cover
            elif user_input.lower() == "clear":  # pragma: no cover
                print(clear_history())  # pragma: no cover
            else:  # pragma: no cover
                print(process_input(user_input))  # pragma: no cover
        except Exception as e:  # pragma: no cover
            print(f"Error: {e}")  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    repl()  # pragma: no cover
