import pytest
from app.calculation import Calculation
from app.history import History


def test_perform_and_history():
    history = History()
    calc = Calculation(5, 3, "add")
    result = calc.perform()
    assert result == 8
    history.add(calc.to_dict())
    assert len(history.get_history()) == 1


def test_invalid_operation():
    calc = Calculation(5, 3, "invalid")
    with pytest.raises(ValueError):
        calc.perform()
