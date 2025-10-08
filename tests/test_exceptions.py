import pytest
from app.exceptions import CalculatorError, DivisionByZeroError, InvalidOperationError

def test_exceptions_inheritance():
    assert issubclass(DivisionByZeroError, CalculatorError)
    assert issubclass(InvalidOperationError, CalculatorError)
