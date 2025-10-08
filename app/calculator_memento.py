class CalculatorMemento:
    def __init__(self):
        self._state = None

    def save_state(self, state):
        self._state = state

    def restore_state(self):
        return self._state
