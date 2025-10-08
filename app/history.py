import pandas as pd
import os

class HistoryManager:
    def __init__(self, csv_path='history.csv', auto_save=True):
        self.csv_path = csv_path
        self.auto_save = auto_save
        self.df = pd.DataFrame(columns=['op', 'a', 'b', 'result'])

        if os.path.exists(self.csv_path):
            try:
                self.df = pd.read_csv(self.csv_path)
            except Exception:
                # Corrupted file: start fresh
                self.df = pd.DataFrame(columns=['op', 'a', 'b', 'result'])

    def add(self, op, a, b, result):
        self.df = pd.concat([self.df, pd.DataFrame([{'op':op,'a':a,'b':b,'result':result}])], ignore_index=True)
        if self.auto_save:
            self.save()

    def save(self, path=None):
        path = path or self.csv_path
        self.df.to_csv(path, index=False)

    def load(self, path=None):
        path = path or self.csv_path
        self.df = pd.read_csv(path)

    def clear(self):
        self.df = self.df.iloc[0:0]
        if self.auto_save:
            self.save()

    def all(self):
        return self.df.copy()
