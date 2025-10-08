import pytest
from app.calculation import Calculation

def test_calculation_execute():
    c = Calculation('+', 2, 3)
    assert c.execute() == 5
