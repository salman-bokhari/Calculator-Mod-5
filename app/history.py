import csv

class History:
    def __init__(self):
        self._history = []

    def add(self, operand_a=None, operation=None, operand_b=None, result=None, timestamp=None):
        """Add a calculation record to history."""
        record = {
            "operand_a": operand_a,
            "operation": operation,
            "operand_b": operand_b,
            "result": result,
            "timestamp": timestamp
        }
        self._history.append(record)

    def all(self):
        """Return all history records."""
        return self._history

    def clear(self):
        """Clear the entire history."""
        self._history.clear()

    def get_history(self):
        """Return the calculation history (alias for all)."""
        return self._history

    def save(self, filepath):  # pragma: no cover
        """Save history to a CSV file."""
        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["operand_a", "operation", "operand_b", "result", "timestamp"])
            writer.writeheader()
            writer.writerows(self._history)

    def load(self, filepath):  # pragma: no cover
        """Load history from a CSV file."""
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            self._history = [row for row in reader]
