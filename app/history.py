import pandas as pd

class History:
    _history = pd.DataFrame(columns=["a", "operator", "b", "result", "timestamp"])

    @classmethod
    def add(cls, a, operator, b, result, timestamp):
        cls._history.loc[len(cls._history)] = [a, operator, b, result, timestamp]

    @classmethod
    def show_history(cls):
        return cls._history.copy()

    @classmethod
    def clear_history(cls):
        cls._history = pd.DataFrame(columns=cls._history.columns)

    @classmethod
    def save(cls, path: str):
        cls._history.to_csv(path, index=False)

    @classmethod
    def load(cls, path: str):
        cls._history = pd.read_csv(path)
        return cls._history.copy()  # <-- return DataFrame
