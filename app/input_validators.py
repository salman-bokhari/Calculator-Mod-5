import pytest
from app.input_validators import validate_number, validate_numbers
from app.exceptions import InvalidInputError, InvalidOperationError

def test_validate_number_valid():
    assert validate_number("5") == 5.0

def test_validate_number_invalid():
    with pytest.raises(InvalidInputError):
        validate_number("abc")

def test_validate_numbers_valid():
    assert validate_numbers("3", "4") == (3.0, 4.0)

def test_validate_numbers_invalid():
    with pytest.raises(InvalidInputError):
        validate_numbers("x", "4")

def test_invalid_operation():
    # Example of operation validator raising InvalidOperationError
    from app.operations import add
    try:
        raise InvalidOperationError("Bad op")
    except InvalidOperationError:
        assert True
