from app.calculation import Calculation
from app.history import History
from app.input_validators import validate_number

class CalculatorREPL:
    def __init__(self):
        self.history = History()

    def perform_and_store(self, lhs, rhs, op):
        lhs = validate_number(lhs)
        rhs = validate_number(rhs)
        calc = Calculation(lhs, rhs, op)
        result = calc.perform()
        self.history.add(**calc.to_dict())
        return result

    def get_history(self):
        return self.history.df.to_dict(orient="records")

    def run(self):  # pragma: no cover
        print("Simple Calculator. Type 'exit' to quit.")
        while True:
            lhs = input("Enter first number: ")
            if lhs.lower() == "exit":
                break
            rhs = input("Enter second number: ")
            if rhs.lower() == "exit":
                break
            op = input("Enter operation (add, subtract, multiply, divide): ").lower()
            if op == "exit":
                break
            try:
                result = self.perform_and_store(lhs, rhs, op)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

def main():  # pragma: no cover
    """Entry point for running the calculator REPL."""
    CalculatorREPL().run()

if __name__ == "__main__":  # pragma: no cover
    main()
