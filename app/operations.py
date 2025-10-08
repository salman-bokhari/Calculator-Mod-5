from abc import ABC, abstractmethod
from .exceptions import DivideByZeroError, InvalidOperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, *operands):
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
        if b == 0:
            raise DivideByZeroError('Division by zero')
        return a / b

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Root(Operation):
    def execute(self, a, b):
        # b-th root of a -> a ** (1/b)
        if b == 0:
            raise InvalidOperationError('Root by zero')
        return a ** (1.0 / b)

# Factory
def operation_factory(name):
    name = name.lower()
    return {
        'add': Add(),
        '+': Add(),
        'sub': Subtract(),
        '-': Subtract(),
        'mul': Multiply(),
        '*': Multiply(),
        'div': Divide(),
        '/': Divide(),
        'pow': Power(),
        '^': Power(),
        'root': Root(),
    }.get(name)
