import sys
from .input_validators import parse_tokens, parse_number
from .calculation import Calculation
from .history import HistoryManager
from .calculator_memento import Memento, Caretaker
from .calculator_config import CalculatorConfig
from .exceptions import CalculatorError

class Observer:
    def update(self, event, payload):
        raise NotImplementedError

class LoggerObserver(Observer):
    def update(self, event, payload):
        print(f"[LOG] Event={event} Payload={payload}")

class AutoSaveObserver(Observer):
    def __init__(self, history_manager):
        self.history = history_manager

    def update(self, event, payload):
        if event == 'calculation_done' and self.history.auto_save:
            self.history.save()

class CalculatorFacade:
    def __init__(self, config=None):
        self.config = config or CalculatorConfig()
        self.history = HistoryManager(csv_path=self.config.history_csv, auto_save=self.config.auto_save)
        self.caretaker = Caretaker()
        self.observers = []
        # initial memento
        self.caretaker.save(Memento(self.history.df))

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, event, payload):
        for o in self.observers:
            try:
                o.update(event,payload)
            except Exception:
                pass

    def calculate(self, op_key, a, b):
        calc = Calculation(op_key, a, b)
        result = calc.execute()
        self.history.add(op_key, a, b, result)
        self.caretaker.save(Memento(self.history.df))
        self.notify('calculation_done', {'op': op_key, 'a': a, 'b': b, 'result': result})
        return result

    def undo(self):
        m = self.caretaker.undo()
        if m is None:
            raise CalculatorError('Nothing to undo')
        self.history.df = m.get_state()
        return True

    def redo(self):
        m = self.caretaker.redo()
        if m is None:
            raise CalculatorError('Nothing to redo')
        self.history.df = m.get_state()
        return True

    def save(self, path=None):
        self.history.save(path)

    def load(self, path=None):
        self.history.load(path)

    def clear_history(self):
        self.history.clear()

def repl_loop():
    calc = CalculatorFacade()
    calc.attach(LoggerObserver())
    calc.attach(AutoSaveObserver(calc.history))
    print("Enhanced Calculator REPL. Type 'help' for commands.")
    while True:
        try:
            line = input('> ').strip()
            if not line:
                continue
            tokens = parse_tokens(line)
            cmd = tokens[0].lower()
            if cmd in ('exit','quit'):
                print('bye')
                break
            if cmd == 'help':
                print("Commands: help, history, exit, clear, undo, redo, save [path], load [path]\nOperations: + - * / ^ root\nUsage: <op> <a> <b>")
                continue
            if cmd == 'history':
                print(calc.history.all())
                continue
            if cmd == 'clear':
                calc.clear_history()
                print('history cleared')
                continue
            if cmd == 'save':
                path = tokens[1] if len(tokens) > 1 else None
                calc.save(path)
                print('saved')
                continue
            if cmd == 'load':
                path = tokens[1] if len(tokens) > 1 else None
                calc.load(path)
                print('loaded')
                continue
            if cmd == 'undo':
                calc.undo()
                print('undone')
                continue
            if cmd == 'redo':
                calc.redo()
                print('redone')
                continue

            # else treat as operation line
            if len(tokens) < 3:
                print('invalid input: need op and two numbers')
                continue
            op_key = tokens[0]
            a = parse_number(tokens[1])
            b = parse_number(tokens[2])
            res = calc.calculate(op_key, a, b)
            print(res)
        except CalculatorError as ce:
            print('Error:', ce)
        except Exception as e:
            print('Unexpected error:', e)

if __name__ == '__main__':
    repl_loop()
