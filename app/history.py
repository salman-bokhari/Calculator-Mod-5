import pandas as pd

class History:
    df = pd.DataFrame(columns=["a", "operator", "b", "result"])

    @classmethod
    def add(cls, a, op, b, result):
        cls.df = pd.concat([cls.df, pd.DataFrame([{
            "a": a,
            "operator": op,
            "b": b,
            "result": result
        }])], ignore_index=True)

    @classmethod
    def get_history(cls):
        return cls.df.copy()

    @classmethod
    def clear_history(cls):
        cls.df = cls.df.iloc[0:0]

    @classmethod
    def save(cls, path):
        cls.df.to_csv(path, index=False)

    @classmethod
    def load(cls, path):
        cls.df = pd.read_csv(path)
