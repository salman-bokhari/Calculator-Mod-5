import pytest
from app.input_validators import parse_number, parse_tokens
from app.exceptions import CalculatorError

@pytest.mark.parametrize('s,expected', [
    ('1', 1), ('2.5', 2.5), ('-3', -3), ('0', 0)
])
def test_parse_number_success(s, expected):
    assert parse_number(s) == expected

def test_parse_number_fail():
    with pytest.raises(CalculatorError):
        parse_number('notanumber')

def test_parse_tokens():
    assert parse_tokens(' + 1 2 ') == ['+','1','2']
