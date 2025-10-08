# app/exceptions.py

class CalculatorError(Exception):
    """Base class for all calculator-related exceptions."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted in the calculator."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when user input is invalid (e.g., non-numeric input)."""
    pass
