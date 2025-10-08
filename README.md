# Calculator App

A simple Python calculator supporting addition, subtraction, multiplication, division, power, modulo, and root operations.  
It features a REPL (Read-Eval-Print Loop) interface and keeps a history of calculations.

---

## Features

- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Advanced operations: `^` (power), `%` (modulo), `root`
- History of calculations with clear functionality
- REPL menu for interactive use
- Fully tested with `pytest` and coverage tracking

---

## Setup & Run Locally

```bash
git clone https://github.com/gshab9/Module-5-Assignment
cd Module-5-Assignment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
python -m app.calculator_repl
```
---

## Test Locally

```bash

pytest --cov=app tests/
coverage report
