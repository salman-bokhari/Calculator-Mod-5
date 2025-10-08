import os
from dotenv import load_dotenv

load_dotenv()

class ConfigError(Exception):
    pass

class CalculatorConfig:
    def __init__(self):
        self.history_csv = os.getenv('HISTORY_CSV', 'history.csv')
        self.auto_save = os.getenv('AUTO_SAVE', 'true').lower() in ('1','true','yes')

        # validate
        if not self.history_csv:
            raise ConfigError('HISTORY_CSV must be set')
