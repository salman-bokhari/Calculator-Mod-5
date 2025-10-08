import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root, OperationFactory
from app.exceptions import DivisionByZeroError, InvalidOperationError

def test_basic_ops():
    assert Add().execute(1,2) == 3
    assert Subtract().execute(5,3) == 2
    assert Multiply().execute(3,4) == 12
    assert Power().execute(2,3) == 8
    assert Root().execute(27,3) == pytest.approx(3)

def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        Divide().execute(1,0)

def test_operation_factory():
    assert isinstance(OperationFactory.get('+'), Add)
    assert isinstance(OperationFactory.get('root'), Root)
    with pytest.raises(InvalidOperationError):
        OperationFactory.get('unknown')
