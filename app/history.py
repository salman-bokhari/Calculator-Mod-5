class History:
    _history = []

    @staticmethod
    def add_history(entry):
        History._history.append(entry)

    @staticmethod
    def get_history():
        return History._history.copy()

    @staticmethod
    def clear_history():
        """Clears all history entries."""
        History._history = []
