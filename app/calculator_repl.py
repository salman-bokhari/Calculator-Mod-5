from app.calculation import Calculation
from app.history import History
from app.input_validators import validate_number
from app.exceptions import InvalidInputError

class CalculatorREPL:
    def __init__(self):
        self.history = History()

    def run(self):  # pragma: no cover
        print("Simple Calculator. Type 'exit' to quit.")
        while True:
            try:
                lhs = input("Enter first number: ")
                if lhs.lower() == "exit":
                    break
                rhs = input("Enter second number: ")
                if rhs.lower() == "exit":
                    break
                op = input("Enter operation (add, subtract, multiply, divide): ").lower()
                if op == "exit":
                    break
                result = self.perform_and_store(lhs, rhs, op)
                print(f"Result: {result}")
            except InvalidInputError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"Error: {e}")

    def perform_and_store(self, lhs, rhs, op):
        """Perform a calculation and save it in history."""
        lhs = validate_number(lhs)
        rhs = validate_number(rhs)
        calc = Calculation(lhs, rhs, op)
        result = calc.perform()
        self.history.add(calc.to_dict())
        return result

    def get_history(self):
        """Return calculation history."""
        return self.history.get_history()
