from .operations import OperationFactory
from .exceptions import CalculatorError

class Calculation:
    def __init__(self, op_key, a, b):
        self.op_key = op_key
        self.a = a
        self.b = b
        self._op = OperationFactory.get(op_key)

    def execute(self):
        return self._op.execute(self.a, self.b)
