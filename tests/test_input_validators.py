import pytest
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError

def test_validate_numbers_ok():
    result = validate_numbers('1', '2.5')
    assert result == [1.0, 2.5]

def test_validate_numbers_bad():
    with pytest.raises(InvalidInputError):
        validate_numbers('a', '2')
