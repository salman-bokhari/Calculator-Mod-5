from app.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }
        func = ops.get(self.operation)
        if not func:
            raise ValueError(f"Unknown operation: {self.operation}")
        return func(self.a, self.b)

    def to_dict(self):
        return {
            "a": self.a,
            "b": self.b,
            "operation": self.operation,
            "result": self.perform()
        }
