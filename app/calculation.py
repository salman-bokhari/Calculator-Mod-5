from .operations import operation_factory
from .input_validators import validate_numbers
from .exceptions import InvalidOperationError
from .history import History
from .calculator_memento import Memento, Caretaker
from datetime import datetime

class CalculatorFacade:
    """Facade for performing operations, maintaining history and memento state."""
    def __init__(self, history: History=None):
        self.history = history or History()
        self.caretaker = Caretaker()
        # save initial state
        self._save_state()

    def _save_state(self):
        state = {'history': self.history.df.copy()}
        self.caretaker.save(Memento(state))

    def perform(self, op_name, a, b):
        """
        Perform an operation (op_name) on operands a and b.
        Raises InvalidOperationError for unknown ops or validation errors.
        """
        op = operation_factory(op_name)
        if not op:
            raise InvalidOperationError(f'Unknown op: {op_name}')
        # validate numbers (may raise InvalidOperationError)
        a, b = validate_numbers(a, b)
        # execute using operation instance (some operations expect (a,b))
        result = op.execute(a, b)
        ts = datetime.utcnow().isoformat()
        self.history.add(a, op_name, b, result, ts)
        # auto-save state after successful calculation
        self._save_state()
        return result

    def undo(self):
        """
        Undo last saved state. Returns True if undone, False if no state.
        """
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
