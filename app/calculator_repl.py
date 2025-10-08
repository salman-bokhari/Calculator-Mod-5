from app.calculation import Calculation
from app.operations import add, subtract, multiply, divide
from app.history import History
from app.exceptions import InvalidInputError, InvalidOperationError


def process_input(user_input):
    """Parse and process a single calculation command string."""
    try:
        parts = user_input.strip().split()
        if len(parts) != 3:
            return "Invalid input format. Use: <num1> <op> <num2>"

        a_str, op, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            raise InvalidOperationError(f"Invalid number: {a_str if not a_str.replace('.', '', 1).isdigit() else b_str}")

        op_map = {
            '+': "add",
            '-': "subtract",
            '*': "multiply",
            '/': "divide"
        }

        if op not in op_map:
            return f"Unsupported operator: {op}"

        operation_name = op_map[op]
        calc = Calculation(a, b, operation_name)
        result = calc.perform()
        History.add_history(f"{a} {op} {b} = {result}")
        return f"Result: {result}"

    except (InvalidInputError, InvalidOperationError) as e:
        return str(e)
    except ZeroDivisionError:
        return "Error: Division by zero."
    except Exception as e:
        return f"Unexpected error: {e}"


def show_history():
    """Return calculation history as string."""
    hist = History.get_history()
    if not hist:
        return "No calculations yet."
    return "\n".join(f"{i + 1}: {h}" for i, h in enumerate(hist))


def clear_history():
    """Clear the calculator history."""
    History.clear_history()
    return "History cleared."


def repl():  # pragma: no cover
    """Run interactive REPL."""
    print("Simple Calculator REPL. Type 'quit' to exit.")
    while True:
        user_input = input(">>> ")
        if user_input.lower() in {"quit", "exit"}:
            break
        print(process_input(user_input))
