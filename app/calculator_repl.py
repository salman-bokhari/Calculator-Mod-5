from app.operations import add, subtract, multiply, divide
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError
from app.history import History

def calculate(a, op, b):
    """Performs the calculation and returns the result."""
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

def process_input(expression):
    """
    Process a single expression like "2 + 3" in non-interactive mode.
    Returns the result or error message.
    """
    try:
        tokens = expression.strip().split()
        if len(tokens) != 3:
            return "Invalid expression format"
        num1, op, num2 = tokens
        a, b = validate_numbers(num1, num2)
        result = calculate(a, op, b)

        # Add to history
        History.add(a, op, b, result, "t")  # 't' is placeholder type
        return f"Result: {result}"
    except (InvalidInputError, InvalidOperationError, ZeroDivisionError) as e:
        return str(e)
    except Exception as e:
        return f"Unexpected error: {e}"

def show_history():
    hist = History.get_history()
    if not hist:
        return "History is empty."
    return "\n".join(f"{h['a']} {h['op']} {h['b']} = {h['result']}" for h in hist)

def clear_history():
    History.clear_history()
    return "History cleared."

def run_repl():
    """Interactive REPL mode."""
    print("Simple Calculator REPL. Type 'quit' to exit.")
    # pragma: no cover
    while True:
        try:
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':
                break

            op = input("Enter operation (+, -, *, /): ")
            if op.lower() == 'quit':
                break

            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                break

            a, b = validate_numbers(num1, num2)
            result = calculate(a, op, b)
            print(f"Result: {result}")

            History.add(a, op, b, result, "manual")
        except (InvalidInputError, InvalidOperationError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
