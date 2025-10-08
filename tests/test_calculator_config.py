import pytest
from app.calculator_config import Config
def test_config_default():
    cfg = Config()
    assert hasattr(cfg, 'history_file')
def test_config_default_values(tmp_path):
    file = tmp_path / "nonexistent.yaml"
    config = calculator_config.CalculatorConfig(str(file))
    assert config.config == {}

def test_invalid_yaml(tmp_path):
    file = tmp_path / "invalid.yaml"
    file.write_text(":::: not valid yaml")
    with pytest.raises(Exception):
        calculator_config.CalculatorConfig(str(file))