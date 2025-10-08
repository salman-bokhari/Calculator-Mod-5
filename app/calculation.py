from app.operations import get_operation

class Calculation:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator

    def perform(self):
        op_class = get_operation(self.operator)
        operation = op_class()
        return operation.calculate(self.a, self.b)

    def to_dict(self):
        return {
            "a": self.a,
            "b": self.b,
            "operator": self.operator,
        }
