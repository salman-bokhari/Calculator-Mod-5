from app.operations import get_operation
from app.history import History

class Calculation:
    def __init__(self, a: float, b: float, operator: str):
        self.a = a
        self.b = b
        self.operator = operator

    def perform(self) -> float:
        """
        Perform the calculation using the operator and operands.
        Raises ValueError if operator is invalid.
        Saves the result to history.
        """
        operation = get_operation(self.operator)  # already an instance
        if operation is None:  # pragma: no cover
            raise ValueError(f"Invalid operator: {self.operator}")

        result = operation.calculate(self.a, self.b)

        # Save to history with a placeholder timestamp/tag
        History.add(self.a, self.operator, self.b, result, "t")  # pragma: no cover

        return result

    def to_dict(self):
        return {
            "a": self.a,
            "b": self.b,
            "operator": self.operator,
        }  # pragma: no cover
