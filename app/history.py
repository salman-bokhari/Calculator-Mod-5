"""History module for tracking calculator operations."""
import pandas as pd


class History:
    """Keeps track of calculation history and allows saving/loading."""

    _history_instance = None  # Singleton-style shared instance

    def __init__(self):
        self.df = pd.DataFrame(columns=["a", "op", "b", "result", "tag"])

    def add(self, *args, **kwargs):
        """Add a calculation entry to history.
        Supports both dict input and individual args."""
        if len(args) == 1 and isinstance(args[0], dict):
            entry = args[0]
        else:
            a, op, b, result, tag = args if len(args) == 5 else (None, None, None, None, None)
            entry = {"a": a, "op": op, "b": b, "result": result, "tag": tag}
        self.df = pd.concat([self.df, pd.DataFrame([entry])], ignore_index=True)

    def save(self, path):
        """Save history to a CSV file."""
        self.df.to_csv(path, index=False)

    def load(self, path):
        """Load history from a CSV file."""
        self.df = pd.read_csv(path)

    def clear(self):
        """Clear the history."""
        self.df = pd.DataFrame(columns=["a", "op", "b", "result", "tag"])

    @classmethod
    def get_instance(cls):
        """Return shared history instance."""
        if cls._history_instance is None:
            cls._history_instance = History()
        return cls._history_instance

    @classmethod
    def add_history(cls, *args, **kwargs):
        """Add entry using shared instance."""
        cls.get_instance().add(*args, **kwargs)

    @classmethod
    def clear_history(cls):
        """Clear shared instance history."""
        cls.get_instance().clear()

    def __len__(self):
        return len(self.df)

    def __iter__(self):
        for _, row in self.df.iterrows():
            yield row.to_dict()
