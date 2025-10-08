import pytest
from app.calculation import Calculation
from app.history import History
from app.operations import get_operation

def test_perform_and_history():
    History.clear_history()
    calc = Calculation(5, 3, "+")
    result = calc.perform()
    assert result == 8

def test_perform_multiplication():
    calc = Calculation(4, 2, "*")
    result = calc.perform()
    assert result == 8

def test_perform_division():
    calc = Calculation(10, 2, "/")
    result = calc.perform()
    assert result == 5
