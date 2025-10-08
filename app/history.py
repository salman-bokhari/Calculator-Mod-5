"""History module for tracking calculator operations."""
import pandas as pd

class History:
    """Keeps track of calculation history and allows saving/loading."""

    def __init__(self):
        # Create a DataFrame to store operations
        self.df = pd.DataFrame(columns=["a", "op", "b", "result", "tag"])

    def add(self, a, op, b, result, tag=None):
        """Add a calculation entry to history."""
        new_entry = {"a": a, "op": op, "b": b, "result": result, "tag": tag}
        self.df = pd.concat([self.df, pd.DataFrame([new_entry])], ignore_index=True)

    def save(self, path):
        """Save history to a CSV file."""
        self.df.to_csv(path, index=False)

    def load(self, path):
        """Load history from a CSV file."""
        self.df = pd.read_csv(path)

    def clear(self):
        """Clear the history."""
        self.df = pd.DataFrame(columns=["a", "op", "b", "result", "tag"])

    def __len__(self):
        """Return number of entries."""
        return len(self.df)

    def __iter__(self):
        """Iterate over history rows as dictionaries."""
        for _, row in self.df.iterrows():
            yield row.to_dict()
