from app.exceptions import CalculatorError, InvalidOperationError
def test_ex_types():
    assert issubclass(InvalidOperationError, CalculatorError)
