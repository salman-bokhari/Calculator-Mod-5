from .operations import operation_factory
from .input_validators import validate_numbers
from .exceptions import InvalidOperationError
from .history import History
from .calculator_memento import Memento, Caretaker
from datetime import datetime

class CalculatorFacade:
    def __init__(self, history: History=None):
        self.history = history or History()
        self.caretaker = Caretaker()
        # save initial state
        self._save_state()

    def _save_state(self):
        state = {'history': self.history.df.copy()}
        self.caretaker.save(Memento(state))

    def perform(self, op_name, a, b):
        op = operation_factory(op_name)
        if not op:
            raise InvalidOperationError(f'Unknown op: {op_name}')
        a, b = validate_numbers(a, b)
        result = op.execute(a, b)
        ts = datetime.utcnow().isoformat()
        self.history.add(a, op_name, b, result, ts)
        # auto-save state after successful calculation
        self._save_state()
        return result

    def undo(self):
        m = self.caretaker.undo({'history': self.history.df})
        if not m:
            return False
        state = m.get_state()
        self.history.df = state['history'].copy()
        return True

    def redo(self):
        m = self.caretaker.redo()
        if not m:
            return False
        state = m.get_state()
        self.history.df = state['history'].copy()
        return True
