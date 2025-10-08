from app.operations import add, subtract, multiply, divide
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError


def calculate(a, op, b):
    """Performs the calculation and returns the result."""
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    else:
        raise InvalidOperationError(f"Invalid operation: {op}")


def main(interactive=True, commands=None):
    """
    Run the calculator REPL.
    If interactive=True → asks user input.
    If interactive=False → runs through provided `commands` (for testing).
    """
    print("Simple Calculator REPL. Type 'quit' to exit.")

    if not interactive:
        # Non-interactive mode for pytest
        results = []
        for num1, op, num2 in commands:
            try:
                a, b = validate_numbers(num1, num2)
                result = calculate(a, op, b)
                results.append(result)
            except Exception as e:
                results.append(str(e))
        return results

    # Interactive mode for manual use
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

        except (InvalidInputError, InvalidOperationError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
