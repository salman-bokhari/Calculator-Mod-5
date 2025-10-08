import pytest
from app.calculator_config import CalculatorConfig

def test_default_config():
    cfg = CalculatorConfig()
    # Should create an empty config dictionary
    assert isinstance(cfg.config, dict)
    assert cfg.config == {}

def test_load_valid_yaml(tmp_path):
    # Create a temporary valid YAML file
    file = tmp_path / "valid.yaml"
    file.write_text("setting: 123")
    cfg = CalculatorConfig(path=file)
    assert cfg.config["setting"] == 123

def test_load_invalid_yaml(tmp_path):
    # Create a temporary invalid YAML file
    file = tmp_path / "invalid.yaml"
    file.write_text(":::: invalid yaml ::::")
    cfg = CalculatorConfig(path=file)
    # Should fall back to empty dict
    assert cfg.config == {}

def test_load_nonexistent_file(tmp_path):
    # Provide a path that does not exist
    file = tmp_path / "does_not_exist.yaml"
    cfg = CalculatorConfig(path=file)
    # Should fall back to empty dict
    assert cfg.config == {}
