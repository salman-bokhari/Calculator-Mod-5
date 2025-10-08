import os
from dotenv import load_dotenv

load_dotenv()

class CalculatorConfig:
    HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")
