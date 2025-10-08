# tests/test_calculation.py
import pytest
from app.calculation import Calculation
from app.history import History

def test_perform_addition():
    History.clear_history()
    calc = Calculation(5, 3, "+")
    result = calc.perform()
    assert result == 8
    assert not History.show_history().empty

def test_perform_subtraction():
    History.clear_history()
    calc = Calculation(10, 4, "-")
    result = calc.perform()
    assert result == 6
    assert not History.show_history().empty

def test_perform_multiplication():
    History.clear_history()
    calc = Calculation(4, 2, "*")
    result = calc.perform()
    assert result == 8
    assert not History.show_history().empty

def test_perform_division():
    History.clear_history()
    calc = Calculation(10, 2, "/")
    result = calc.perform()
    assert result == 5
    assert not History.show_history().empty

def test_divide_by_zero():
    calc = Calculation(5, 0, "/")
    with pytest.raises(ZeroDivisionError):
        calc.perform()

def test_invalid_operator():
    calc = Calculation(2, 3, "invalid")
    with pytest.raises(ValueError):
        calc.perform()
