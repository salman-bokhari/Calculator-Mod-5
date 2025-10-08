import pytest
from app.calculator_config import CalculatorConfig, ConfigError


def test_config_defaults(monkeypatch):
    monkeypatch.setenv('HISTORY_CSV', '')
    # empty will raise
    with pytest.raises(ConfigError):
        CalculatorConfig()

def test_config_with_valid_env(monkeypatch):
    monkeypatch.setenv('HISTORY_CSV', 'history.csv')
    config = CalculatorConfig()
    assert config.history_csv == 'history.csv'

def test_config_custom_value(monkeypatch):
    monkeypatch.setenv('HISTORY_CSV', 'custom_history.csv')
    config = CalculatorConfig()
    assert config.history_csv == 'custom_history.csv'
