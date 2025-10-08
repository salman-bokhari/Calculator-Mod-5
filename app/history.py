import json
import os


class History:
    _history = []

    def __init__(self):
        """Initialize history instance."""
        self._data = []

    def add(self, a, op, b, result, tag=None):
        """Add an entry to this instance and class-level history."""
        entry = {"a": a, "op": op, "b": b, "result": result, "tag": tag}
        self._data.append(entry)
        History._history.append(entry)

    @staticmethod
    def add_history(entry):
        """Add a plain string entry (for REPL)."""
        History._history.append(entry)

    @staticmethod
    def get_history():
        """Return global history list copy."""
        return History._history.copy()

    @staticmethod
    def clear_history():
        """Clears all history entries."""
        History._history = []

    def save(self, path):
        """Save instance history to a JSON file."""
        with open(path, "w") as f:
            json.dump(self._data, f)

    def load(self, path):
        """Load instance history from JSON file."""
        if os.path.exists(path):
            with open(path, "r") as f:
                self._data = json.load(f)
