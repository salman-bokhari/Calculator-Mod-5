import os
try:
    # optional: if python-dotenv is available this will load .env
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv not required for tests; ignore if unavailable.  # pragma: no cover
    pass

class ConfigError(Exception):
    pass

class Config:
    """
    Minimal config class used by tests. Reads CALC_HISTORY env var or defaults.
    """
    def __init__(self):
        self.history_file = os.getenv('CALC_HISTORY', 'history.csv')
        try:
            if not isinstance(self.history_file, str):
                raise ConfigError('Invalid history file config')
        except Exception as e:
            raise ConfigError(e)
