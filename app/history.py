import pandas as pd

class History:
    def __init__(self):
        self.df = pd.DataFrame(columns=["a", "b", "operation", "result"])

    def add(self, a, op, b, result):
        """Add a calculation to history."""
        self.df.loc[len(self.df)] = {"a": a, "b": b, "operation": op, "result": result}

    def get_history(self):
        return self.df

    def save(self, path):
        self.df.to_csv(path, index=False)

    def load(self, path):
        self.df = pd.read_csv(path)
