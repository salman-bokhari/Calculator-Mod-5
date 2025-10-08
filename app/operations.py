from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Operation(ABC):
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        pass

class Add(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a - b

class Multiply(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a * b

class Divide(Operation):
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class Power(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a ** b

class Modulo(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a % b

class Root(Operation):
    def calculate(self, a: float, b: float) -> float:
        return a ** (1 / b)

def get_operation(operator: str) -> Optional[Operation]:
    """Return an instance of the correct operation."""
    return {
        "+": Add,
        "-": Subtract,
        "*": Multiply,
        "/": Divide,
        "^": Power,
        "%": Modulo,
        "root": Root
    }.get(operator, None)() if operator in {"+","-","*","/","^","%","root"} else None  # pragma: no cover
