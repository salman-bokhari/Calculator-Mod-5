from app.calculator_repl import main

def test_run_with_exit(monkeypatch):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()  # should exit cleanly without exception

def test_invalid_command(monkeypatch):
    inputs = iter(["nonsense", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()  # should handle invalid gracefully
