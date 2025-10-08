from datetime import datetime
from app.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, lhs, rhs, operation):
        self.lhs = lhs
        self.rhs = rhs
        self.operation = operation
        self.result = None
        self.timestamp = datetime.now().isoformat()

    def perform(self):
        """Perform the calculation based on the operation."""
        ops = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }
        func = ops.get(self.operation)
        if not func:
            raise ValueError(f"Unknown operation: {self.operation}")
        self.result = func(self.lhs, self.rhs)
        return self.result

    def to_dict(self):
        """Return calculation details as a dictionary."""
        return {
            "lhs": self.lhs,
            "op": self.operation,
            "rhs": self.rhs,
            "result": self.result,
            "timestamp": self.timestamp
        }

    def __repr__(self):  # pragma: no cover
        return f"Calculation({self.lhs}, {self.rhs}, '{self.operation}') = {self.result}"
