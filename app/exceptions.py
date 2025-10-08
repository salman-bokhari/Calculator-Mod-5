class CalculatorError(Exception):
    pass

class InvalidInputError(CalculatorError):
    pass

class InvalidOperationError(CalculatorError):
    pass
