import pytest
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError

def test_validate_numbers_good():
    result = validate_numbers("5", "2")
    assert result == [5.0, 2.0]

def test_validate_numbers_bad():
    with pytest.raises(InvalidInputError):
        validate_numbers("a", "2")
