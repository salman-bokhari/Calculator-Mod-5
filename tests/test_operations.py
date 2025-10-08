# tests/test_operations.py
import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Modulo, Root, get_operation

def test_addition():
    assert Add().calculate(2, 3) == 5

def test_subtraction():
    assert Subtract().calculate(5, 3) == 2

def test_multiplication():
    assert Multiply().calculate(4, 2) == 8

def test_division():
    assert Divide().calculate(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().calculate(5, 0)

def test_power():
    assert Power().calculate(2, 3) == 8

def test_modulo():
    assert Modulo().calculate(10, 3) == 1

def test_root():
    assert Root().calculate(8, 3) == pytest.approx(2)

def test_get_operation_valid():
    # Use get_operation and call calculate directly
    for op in ["+", "-", "*", "/", "^", "%", "root"]:
        instance = get_operation(op)
        assert instance is not None
        assert instance.calculate(1, 1) is not None

def test_get_operation_none_usage():
    # Hit the "None" branch for coverage
    instance = get_operation("invalid")  # <-- triggers cls is None
    assert instance is None

def test_get_operation_invalid_operator():
    op = get_operation("unknown_operator")
    assert op is None
