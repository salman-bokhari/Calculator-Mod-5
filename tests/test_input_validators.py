import pytest
from app.input_validators import validate_numbers
from app.exceptions import InvalidOperationError

def test_validate_numbers_ok():
    nums = validate_numbers('1','2.5')
    assert nums == [1.0,2.5]

def test_validate_numbers_bad():
    with pytest.raises(InvalidOperationError):
        validate_numbers('a', '2')
