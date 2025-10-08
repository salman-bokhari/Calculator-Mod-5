import pandas as pd
from pathlib import Path
from datetime import datetime

class History:
    """Manages calculator operation history using a pandas DataFrame."""

    def __init__(self, csv_path=None):
        self.csv_path = Path(csv_path) if csv_path else None
        # Keep consistent columns expected by tests
        self.df = pd.DataFrame(columns=["lhs", "op", "rhs", "result", "timestamp"])

    def add(self, *args, **kwargs):
        """
        Add a calculation record.

        Supported call styles:
          - add(lhs, op, rhs, result, timestamp=None)
          - add(record_dict) where dict has keys lhs, op, rhs, result, timestamp
          - add(lhs=..., op=..., rhs=..., result=..., timestamp=...)
        """
        # Case: single dictionary passed
        if args and isinstance(args[0], dict):
            row = args[0].copy()
        # Case: positional args (lhs, op, rhs, result, [timestamp])
        elif args and len(args) >= 4:
            lhs, op, rhs, result = args[:4]
            timestamp = args[4] if len(args) > 4 else kwargs.get("timestamp") or datetime.utcnow().isoformat()
            row = {"lhs": lhs, "op": op, "rhs": rhs, "result": result, "timestamp": timestamp}
        else:
            # Keyword-style
            lhs = kwargs.get("lhs")
            op = kwargs.get("op")
            rhs = kwargs.get("rhs")
            result = kwargs.get("result")
            timestamp = kwargs.get("timestamp") or datetime.utcnow().isoformat()
            if lhs is None and op is None and rhs is None and result is None:
                raise ValueError("Invalid arguments for History.add()")
            row = {"lhs": lhs, "op": op, "rhs": rhs, "result": result, "timestamp": timestamp}

        # Ensure all expected keys exist (tests expect these column names)
        for k in ["lhs", "op", "rhs", "result", "timestamp"]:
            if k not in row:
                row[k] = None

        # Append row to DataFrame. pd.concat is used to be compatible with pandas >=1.4
        self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)

    def save(self, path=None):
        """
        Save history to CSV. Returns the Path saved to.
        """
        p = Path(path) if path else (self.csv_path if self.csv_path else Path("history.csv"))
        self.df.to_csv(p, index=False)
        return p

    def load(self, path=None):
        """
        Load history from CSV file. If file does not exist, leaves df unchanged.
        Returns the DataFrame.
        """
        p = Path(path) if path else (self.csv_path if self.csv_path else Path("history.csv"))
        if p.exists():
            self.df = pd.read_csv(p)
        return self.df

    def get_history(self):
        """Return the internal DataFrame for inspection (tests use len(get_history()))."""
        return self.df

    def clear(self):
        """Clear all history records."""
        self.df = pd.DataFrame(columns=["lhs", "op", "rhs", "result", "timestamp"])

    def __len__(self):
        return len(self.df)

    def __repr__(self):
        return self.df.to_string(index=False)
