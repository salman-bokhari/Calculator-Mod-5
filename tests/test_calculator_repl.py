import pytest
from app.calculator_repl import process_input, clear_history, show_history
from app.history import History

@pytest.fixture(autouse=True)
def clear_hist():
    History.clear_history()

def test_process_input_addition():
    assert process_input("2 + 3") == "Result: 5.0"

def test_process_input_subtraction():
    assert process_input("7 - 2") == "Result: 5.0"

def test_process_input_multiplication():
    assert process_input("4 * 3") == "Result: 12.0"

def test_process_input_division():
    assert process_input("10 / 2") == "Result: 5.0"

def test_process_input_root():
    assert process_input("16 root 2") == "Result: 4.0"

def test_process_input_power():
    assert process_input("4 ^ 2") == "Result: 16.0"

def test_process_input_modulo():
    assert process_input("10 % 3") == "Result: 1.0"

def test_process_input_invalid_operator():
    # Using an operator not in VALID_OPERATORS
    assert process_input("4 & 2") == "Invalid operator"

def test_process_input_invalid_format():
    assert process_input("invalid input") == "Invalid input: invalid input"

def test_clear_and_show_history():
    process_input("1 + 2")
    hist = show_history()
    assert not hist.empty
    clear_history()
    assert show_history().empty
