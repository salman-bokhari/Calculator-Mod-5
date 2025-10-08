from app.calculator_repl import main
from unittest.mock import patch

def test_main_quit(monkeypatch):
    # Simulate user typing 'quit'
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    main()  # should exit gracefully without error

def test_main_valid_addition(monkeypatch):
    inputs = iter(['5', '+', '2', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()  # simulate REPL session performing 5 + 2

def test_main_invalid_input(monkeypatch):
    # Input invalid data first, then quit
    inputs = iter(['abc', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()

def test_main_invalid_operation(monkeypatch):
    # Input valid number but invalid operator
    inputs = iter(['3', '%', '2', 'quit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
