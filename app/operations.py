from abc import ABC, abstractmethod
from .exceptions import DivisionByZeroError, InvalidOperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Add(Operation):
    def execute(self, a, b):
        return a + b

class Subtract(Operation):
    def execute(self, a, b):
        return a - b

class Multiply(Operation):
    def execute(self, a, b):
        return a * b

class Divide(Operation):
    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise DivisionByZeroError("division by zero")

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Root(Operation):
    def execute(self, a, b):
        # b-th root of a
        if b == 0:
            raise InvalidOperationError("root degree cannot be zero")
        return a ** (1.0 / b)

class OperationFactory:
    _map = {
        '+': Add,
        'add': Add,
        '-': Subtract,
        'sub': Subtract,
        '*': Multiply,
        'mul': Multiply,
        '/': Divide,
        'div': Divide,
        '^': Power,
        'pow': Power,
        'root': Root
    }

    @classmethod
    def get(cls, op_key):
        try:
            op_cls = cls._map[op_key]
        except KeyError:
            raise InvalidOperationError(f"Unknown operation: {op_key}")
        return op_cls()
