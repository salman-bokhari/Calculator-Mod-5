import sys
from .calculation import CalculatorFacade
from .calculator_config import Config
from .exceptions import CalculatorError
from .history import History
import readline

HELP_TEXT = '''Commands:
  help                show this message
  exit                exit the REPL
  history             show history
  save [path]         save history to csv
  load [path]         load history from csv
  clear               clear history
  undo                undo last calculation
  redo                redo last undone
Operations: add, sub, mul, div, pow, root (usage: add 2 3)
'''

def repl():
    cfg = Config()
    history = History(cfg.history_file)
    history.load()
    calc = CalculatorFacade(history=history)
    print('Enhanced Calculator REPL. type help')
    while True:
        try:
            line = input('> ').strip()
            if not line:
                continue
            parts = line.split()
            cmd = parts[0].lower()
            if cmd in ('exit','quit'):
                print('Goodbye')
                break
            if cmd == 'help':
                print(HELP_TEXT)
                continue
            if cmd == 'history':
                print(history.df.to_string(index=False))
                continue
            if cmd == 'save':
                path = parts[1] if len(parts)>1 else None
                p = history.save(path)
                print(f'Saved to {p}')
                continue
            if cmd == 'load':
                path = parts[1] if len(parts)>1 else None
                history.load(path)
                print('Loaded')
                continue
            if cmd == 'clear':
                history.df = history.df.iloc[0:0]
                print('Cleared')
                continue
            if cmd == 'undo':
                ok = calc.undo()
                print('Undone' if ok else 'Nothing to undo')
                continue
            if cmd == 'redo':
                ok = calc.redo()
                print('Redone' if ok else 'Nothing to redo')
                continue
            # operations
            op_name = cmd
            if len(parts) < 3:
                print('Usage: <op> a b')
                continue
            a, b = parts[1], parts[2]
            try:
                res = calc.perform(op_name, a, b)
                print('=>', res)
            except CalculatorError as e:
                print('Error:', e)
        except EOFError:
            break
        except KeyboardInterrupt:
            print('\nInterrupted')
            break

if __name__ == '__main__':
    repl()
