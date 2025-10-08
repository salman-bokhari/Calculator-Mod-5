import pytest
from app import operations

def test_addition():
    assert operations.add(2, 3) == 5

def test_subtraction():
    assert operations.subtract(5, 3) == 2

def test_multiplication():
    assert operations.multiply(4, 2) == 8

def test_division():
    assert operations.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        operations.divide(5, 0)

def test_power():
    assert operations.power(2, 3) == 8

def test_modulo():
    assert operations.modulo(10, 3) == 1
