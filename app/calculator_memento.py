class CalculatorMemento:
    """
    Implements the Memento pattern to save and restore calculator state.
    """
    def __init__(self):
        self._state = None

    def save_state(self, state):
        """
        Save the provided state.
        """
        self._state = state

    def restore_state(self):
        """
        Restore the previously saved state.
        Returns None if no state was saved.
        """
        return self._state
