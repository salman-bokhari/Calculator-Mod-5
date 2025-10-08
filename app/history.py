import pandas as pd
from pathlib import Path

class History:
    def __init__(self, csv_path=None):
        self.csv_path = Path(csv_path) if csv_path else None
        self.df = pd.DataFrame(columns=['lhs','op','rhs','result','timestamp'])

    def add(self, lhs, op, rhs, result, timestamp):
        row = dict(lhs=lhs, op=op, rhs=rhs, result=result, timestamp=timestamp)
        self.df = pd.concat([self.df, pd.DataFrame([row])], ignore_index=True)
        return row

    def save(self, path=None):
        path = Path(path or self.csv_path or 'history.csv')
        self.df.to_csv(path, index=False)
        return path

    def load(self, path=None):
        path = Path(path or self.csv_path or 'history.csv')
        if path.exists():
            self.df = pd.read_csv(path)
        return self.df
