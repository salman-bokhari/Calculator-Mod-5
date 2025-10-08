import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root, operation_factory
from app.exceptions import DivideByZeroError, InvalidOperationError

@pytest.mark.parametrize('cls,a,b,expected', [
    (Add, 1,2,3),
    (Subtract,5,3,2),
    (Multiply,3,4,12),
    (Power,2,3,8),
    (Root,27,3,3),
])
def test_basic_ops(cls,a,b,expected):
    op = cls()
    assert op.execute(a,b) == expected

def test_divide_by_zero():
    op = Divide()
    with pytest.raises(DivideByZeroError):
        op.execute(1,0)

def test_factory():
    assert operation_factory('add').execute(1,2) == 3
    assert operation_factory('+').execute(2,3) == 5
    assert operation_factory('root').execute(16,4) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
