import os
from dotenv import load_dotenv

load_dotenv()

class CalculatorConfig:
    def __init__(self, file_path=None):
        self.HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")
        self.CONFIG_FILE = file_path
