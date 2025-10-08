import os
from dotenv import load_dotenv

load_dotenv()

class ConfigError(Exception):
    pass

class Config:
    def __init__(self):
        self.history_file = os.getenv('CALC_HISTORY', 'history.csv')
        try:
            if not isinstance(self.history_file, str):
                raise ConfigError('Invalid history file config')
        except Exception as e:
            raise ConfigError(e)
