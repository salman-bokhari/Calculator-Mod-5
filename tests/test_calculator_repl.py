from app.calculator_repl import HELP_TEXT
from app import calculator_repl

def test_help_contains_commands():
    assert 'help' in HELP_TEXT

def test_run_with_exit(monkeypatch):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator_repl.run_repl()

def test_invalid_command(monkeypatch):
    inputs = iter(["invalid", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calculator_repl.run_repl()
