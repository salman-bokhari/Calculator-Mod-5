import pytest
from app.calculation import CalculatorFacade
from app.history import History
from app.exceptions import InvalidOperationError

def test_perform_and_history(tmp_path):
    h = History()
    calc = CalculatorFacade(history=h)
    r = calc.perform('add', '2', '3')
    assert r == 5
    assert len(h.df) == 1

def test_unknown_op():
    calc = CalculatorFacade()
    with pytest.raises(InvalidOperationError):
        calc.perform('nope', '1','2')
def test_invalid_operation(monkeypatch):
    from app.calculation import Calculation
    calc = Calculation(5, 3, "invalid")
    try:
        calc.perform()
    except ValueError:
        assert True
    else:
        assert False
