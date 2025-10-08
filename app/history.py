import pandas as pd
from app.calculator_config import CalculatorConfig

class History:
    df = pd.DataFrame()
    file = CalculatorConfig().HISTORY_FILE

    @classmethod
    def add(cls, id, op, a, b, result):
        cls.df = pd.concat([cls.df, pd.DataFrame([{
            'id': id, 'operation': op, 'a': a, 'b': b, 'result': result
        }])], ignore_index=True)
        cls.save_history()

    @classmethod
    def get_history(cls):
        return cls.df.copy()

    @classmethod
    def clear_history(cls):
        cls.df = cls.df.iloc[0:0]
        cls.save_history()

    @classmethod
    def save_history(cls):
        cls.df.to_csv(cls.file, index=False)

    @classmethod
    def load_history(cls):
        try:
            cls.df = pd.read_csv(cls.file)
        except FileNotFoundError:
            cls.df = pd.DataFrame(columns=['id', 'operation', 'a', 'b', 'result'])
