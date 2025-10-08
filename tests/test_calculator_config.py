import os
from app.calculator_config import CalculatorConfig, ConfigError

def test_config_defaults(monkeypatch):
    monkeypatch.setenv('HISTORY_CSV','')
    # empty will raise
    with pytest.raises(ConfigError):
        CalculatorConfig()
