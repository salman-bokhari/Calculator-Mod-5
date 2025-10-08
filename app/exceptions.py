class CalculatorError(Exception):
    """Base class for calculator exceptions."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when the user enters invalid input."""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid operation is requested."""
    pass
