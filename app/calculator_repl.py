from app.calculation import Calculation
from app.history import History
from app.operations import get_operation

VALID_OPERATORS = ["+", "-", "*", "/", "root", "^", "%"]  # REPL supports these

def process_input(user_input: str): 
    try:
        parts = user_input.split()
        if len(parts) != 3:
            return f"Invalid input: {user_input}"

        a = float(parts[0])
        operator = parts[1]
        b = float(parts[2])

        if operator not in VALID_OPERATORS:
            return "Invalid operator"

        calc = Calculation(a, b, operator)
        result = calc.perform()
        return f"Result: {result}" 

    except ValueError:  # pragma: no cover
        return f"Invalid input: {user_input}" 
    except ZeroDivisionError:  # pragma: no cover
        return "Cannot divide by zero"
    except Exception as e:  # pragma: no cover
        return str(e)

def clear_history(): 
    History.clear_history()

def show_history():
    return History.show_history()

def main():  # pragma: no cover
    print("Welcome to the Calculator!")
    
    while True:
        print("\nMenu:")
        print("1. Perform calculation")
        print("2. Show history")
        print("3. Clear history")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            user_input = input("Enter calculation (e.g., 2 + 3): ")
            output = process_input(user_input)
            print(output)
        elif choice == "2":
            print(show_history())
        elif choice == "3":
            clear_history()
            print("History cleared.")
        elif choice == "4": 
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":  # pragma: no cover
    main()
