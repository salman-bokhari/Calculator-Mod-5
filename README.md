# Enhanced Calculator Application

Modular Python calculator demonstrating advanced design patterns (Factory, Strategy, Observer, Memento, Facade),
persistent history management with pandas, configuration via dotenv, and full test coverage with pytest.

## Structure
- app/
  - calculator_repl.py
  - calculation.py
  - calculator_config.py
  - calculator_memento.py
  - exceptions.py
  - history.py
  - input_validators.py
  - operations.py
  - __init__.py
- tests/
  - test_calculations.py
  - test_calculator_repl.py
  - test_calculator_config.py
  - test_calculator_memento.py
  - test_exceptions.py
  - test_history.py
  - test_input_validators.py
  - test_operations.py
- .github/workflows/python-app.yml
- requirements.txt
- .env.example

## Setup (local)
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   pytest --cov=app tests/
   ```
3. Start the REPL:
   ```bash
   python -m app.calculator_repl
   ```

## Notes
- CI is configured to require 100% coverage. Some intentionally unreachable or trivial lines are marked with `# pragma: no cover`.
- The project uses pandas for history management and python-dotenv for configuration.
