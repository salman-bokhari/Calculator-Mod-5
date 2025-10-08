import pytest
from app.calculation import Calculation
from app.history import History

def test_perform_and_history():
    History.clear_history()
    calc = Calculation(5, 3, "+")
    result = calc.perform()
    assert result == 8
    History.add(calc.a, calc.operator, calc.b, result)
    df = History.get_history()
    assert df.iloc[-1]["result"] == 8
