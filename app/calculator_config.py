import os
from dotenv import load_dotenv

load_dotenv()

HISTORY_FILE = os.getenv("HISTORY_FILE", "history.csv")
