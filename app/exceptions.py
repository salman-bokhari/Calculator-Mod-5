class CalculatorError(Exception):
    """Base class for all calculator-related exceptions."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted in the calculator."""
    pass
