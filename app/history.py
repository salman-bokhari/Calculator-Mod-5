import pandas as pd

class History:
    def __init__(self):
        self.df = pd.DataFrame(columns=["a","op","b","result","t"])

    def add(self, a, op, b, result, t=None):
        self.df.loc[len(self.df)] = {"a":a, "op":op, "b":b, "result":result, "t":t}

    @classmethod
    def clear_history(cls):
        cls.df = cls.df.iloc[0:0]

    def get_history(self):
        return self.df

    def save(self, path):
        self.df.to_csv(path, index=False)

    def load(self, path):
        self.df = pd.read_csv(path)
