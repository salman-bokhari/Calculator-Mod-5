class Memento:
    """
    Simple memento storing a snapshot of state (expects a dict with copy-able values).
    """
    def __init__(self, state):
        # store shallow copy to avoid external mutation
        self._state = state.copy() if hasattr(state, 'copy') else dict(state)

    def get_state(self):
        return self._state.copy()

class Caretaker:
    """
    Caretaker managing undo/redo stacks of mementos.
    """
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def undo(self, current_state):
        """
        Pop last memento for undo, push current_state onto redo stack.
        Returns the popped memento or None if no undo available.
        """
        if not self._undo_stack:
            return None
        m = self._undo_stack.pop()
        self._redo_stack.append(Memento(current_state))
        return m

    def redo(self):
        """
        Pop from redo stack and push that state onto undo stack.
        Returns the memento restored or None if redo not available.
        """
        if not self._redo_stack:
            return None
        m = self._redo_stack.pop()
        # push a copy back to undo stack so multiple redo/undo sequence works
        self._undo_stack.append(Memento(m.get_state()))
        return m
