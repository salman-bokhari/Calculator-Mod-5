from app.calculation import Calculation
from app.history import History

def main():
    history = History()
    print("Simple Calculator. Type 'exit' to quit.")
    while True:
        user_input = input("Enter operation (add/subtract/multiply/divide/power/modulo) or 'exit': ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        if user_input not in {"add", "subtract", "multiply", "divide", "power", "modulo"}:
            print("Invalid command. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            calc = Calculation(a, b, user_input)
            result = calc.perform()
            history.add(calc.to_dict())
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
