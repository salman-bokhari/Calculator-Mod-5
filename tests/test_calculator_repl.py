import pytest
from app.calculator_repl import process_input, show_history, clear_history
from app.history import History

def test_addition():
    result = process_input("2 + 3")
    assert "Result: 5" in result

def test_subtraction():
    result = process_input("7 - 2")
    assert "Result: 5" in result

def test_invalid_operator():
    result = process_input("4 ^ 2")
    assert "Unsupported operator" in result

def test_invalid_input_format():
    result = process_input("5 +")
    assert "Invalid input" in result

def test_non_numeric():
    result = process_input("a + 3")
    assert "Invalid number input" in result

def test_history_addition_and_show_clear():
    History.clear_history()
    process_input("1 + 1")
    output = show_history()
    assert "Result" not in output  # show_history returns string of past calcs
    assert "1:" in output

    msg = clear_history()
    assert msg == "History cleared."
    assert show_history() == "No calculations yet."
