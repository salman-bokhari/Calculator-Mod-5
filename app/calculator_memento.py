class Memento:
    def __init__(self, state):
        self._state = state.copy(deep=True) if hasattr(state, 'copy') else state

    def get_state(self):
        return self._state

class Caretaker:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            return None
        m = self._undo_stack.pop()
        self._redo_stack.append(m)
        return m

    def redo(self):
        if not self._redo_stack:
            return None
        m = self._redo_stack.pop()
        self._undo_stack.append(m)
        return m
