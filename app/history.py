import pandas as pd
from datetime import datetime

class History:
    """Manages calculator operation history using a pandas DataFrame."""

    def __init__(self):
        # Initialize an empty DataFrame for storing history
        self.df = pd.DataFrame(columns=["lhs", "op", "rhs", "result", "timestamp"])

    def add(self, *args, **kwargs):
        """
        Add a calculation record to the history.
        Supports both:
          - history.add(lhs, op, rhs, result, timestamp)
          - history.add(calc_dict)
        """
        # If a single dictionary is passed (e.g., calc.to_dict())
        if args and isinstance(args[0], dict):
            row = args[0]
        else:
            # Unpack individual arguments
            if len(args) == 5:
                lhs, op, rhs, result, timestamp = args
                row = {
                    "lhs": lhs,
                    "op": op,
                    "rhs": rhs,
                    "result": result,
                    "timestamp": timestamp,
                }
            else:
                # In case someone used keyword arguments
                row = {
                    "lhs": kwargs.get("lhs"),
                    "op": kwargs.get("op"),
                    "rhs": kwargs.get("rhs"),
                    "result": kwargs.get("result"),
                    "timestamp": kwargs.get("timestamp", datetime.now().isoformat()),
                }

        # Add the row to the DataFrame
        self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)

    def get_all(self):
        """Return all history records."""
        return self.df.to_dict(orient="records")

    def clear(self):
        """Clear all records from history."""
        self.df = pd.DataFrame(columns=["lhs", "op", "rhs", "result", "timestamp"])

    def __len__(self):
        """Return the number of records in history."""
        return len(self.df)

    def __repr__(self):
        """String representation of the history."""
        return self.df.to_string(index=False)
