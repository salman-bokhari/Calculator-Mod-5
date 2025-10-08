# Enhanced Calculator

A modular calculator demonstrating Factory, Strategy (operations as classes), Observer (history can be observed externally), Memento (undo/redo), Facade and pandas-backed history.

Run REPL: `python -m app.calculator_repl`

Tests: `pytest --maxfail=1 -q`

Config: create a `.env` with `CALC_HISTORY=history.csv`
