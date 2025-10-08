import pandas as pd
from pathlib import Path

class History:
    def __init__(self, csv_path=None):
        self.csv_path = Path(csv_path) if csv_path else None
        self.df = pd.DataFrame(columns=['lhs', 'op', 'rhs', 'result', 'timestamp'])

    def add(self, *args, **kwargs):
        """Add a new calculation record. Supports both dict and explicit args."""
        if len(args) == 1 and isinstance(args[0], dict):
            row = args[0]
        else:
            row = dict(lhs=args[0], op=args[1], rhs=args[2], result=args[3], timestamp=args[4])
        self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)
        return row

    def save(self, path=None):  # pragma: no cover
        """Save history to CSV."""
        path = Path(path or self.csv_path or 'history.csv')
        self.df.to_csv(path, index=False)
        return path

    def load(self, path=None):  # pragma: no cover
        """Load history from CSV."""
        path = Path(path or self.csv_path or 'history.csv')
        if path.exists():
            self.df = pd.read_csv(path)
        return self.df

    def get_history(self):
        """Return the full history."""
        return self.df
