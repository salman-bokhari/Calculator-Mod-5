class CalculatorError(Exception):
    """Base class for all calculator exceptions."""
    pass

class InvalidInputError(CalculatorError):
    """Raised when input is not a valid number."""
    pass

class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is provided."""
    pass
