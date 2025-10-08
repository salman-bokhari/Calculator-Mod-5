import pandas as pd

class History:
    _history_df = pd.DataFrame(columns=['a', 'op', 'b', 'result', 'type'])

    @classmethod
    def add(cls, a, op, b, result, type_):
        """Add an entry to history."""
        cls._history_df = pd.concat([
            cls._history_df,
            pd.DataFrame([{'a': a, 'op': op, 'b': b, 'result': result, 'type': type_}])
        ], ignore_index=True)

    @classmethod
    def get_history(cls):
        if cls._history_df.empty:
            return []
        return cls._history_df.to_dict(orient='records')

    @classmethod
    def clear_history(cls):
        cls._history_df = cls._history_df.iloc[0:0]

    @classmethod
    def save(cls, path):
        cls._history_df.to_csv(path, index=False)

    @classmethod
    def load(cls, path):
        cls._history_df = pd.read_csv(path)
