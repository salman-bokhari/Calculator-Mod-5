from app.operations import add, subtract, multiply, divide
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError


def main():
    print("Simple Calculator REPL. Type 'quit' to exit.")

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

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                raise InvalidOperationError(f"Invalid operation: {op}")

            print(f"Result: {result}")

        except (InvalidInputError, InvalidOperationError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
