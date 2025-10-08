class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    pass

class InvalidOperationError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass
