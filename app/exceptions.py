class CalculatorError(Exception):
    """Base calculator exception."""
    pass

class InvalidOperationError(CalculatorError):
    pass

class DivideByZeroError(CalculatorError):
    pass
