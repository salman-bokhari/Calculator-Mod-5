from app.operations import add, subtract, multiply, divide, power, modulo

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        if self.operation == "add":
            return add(self.a, self.b)
        elif self.operation == "subtract":
            return subtract(self.a, self.b)
        elif self.operation == "multiply":
            return multiply(self.a, self.b)
        elif self.operation == "divide":
            return divide(self.a, self.b)
        elif self.operation == "power":
            return power(self.a, self.b)
        elif self.operation == "modulo":
            return modulo(self.a, self.b)
        else:
            raise ValueError(f"Invalid operation: {self.operation}")

    def to_dict(self):
        return {
            "a": self.a,
            "b": self.b,
            "operation": self.operation,
            "result": self.perform()
        }
