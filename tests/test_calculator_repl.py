import pytest
from app.calculator_repl import process_input, show_history, clear_history
from app.history import History

def test_addition():
    clear_history()
    result = process_input("2 + 3")
    assert "Result: 5" in result

def test_subtraction():
    clear_history()
    result = process_input("7 - 2")
    assert "Result: 5" in result

def test_invalid_operator():
    result = process_input("4 ^ 2")
    assert "Result:" in result
    result = process_input("4 & 2")
    assert "Invalid operation" in result or "Invalid input" in result

def test_invalid_input_format():
    result = process_input("5 +")
    assert "Invalid command format" in result

def test_non_numeric():
    result = process_input("a + 3")
    assert "Invalid number input" in result

def test_history_addition_and_show_clear():
    clear_history()
    assert show_history().empty
    process_input("1 + 2")
    assert not show_history().empty
