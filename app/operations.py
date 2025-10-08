class Add:
    def calculate(self, a, b):
        return a + b

class Subtract:
    def calculate(self, a, b):
        return a - b

class Multiply:
    def calculate(self, a, b):
        return a * b

class Divide:
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

class Power:
    def calculate(self, a, b):
        return a ** b

class Root:
    def calculate(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Root degree cannot be zero")
        return a ** (1 / b)

def get_operation(op):
    ops = {
        "+": Add,
        "-": Subtract,
        "*": Multiply,
        "/": Divide,
        "^": Power,
        "root": Root
    }
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    return ops[op]
