import pytest
import os
from app.calculator_config import CalculatorConfig

def test_config_default_values(tmp_path):
    file = tmp_path / "nonexistent.yaml"
    config = CalculatorConfig()
    assert isinstance(config.config, dict)

def test_invalid_yaml(tmp_path):
    file = tmp_path / "invalid.yaml"
    file.write_text(":::: invalid yaml ::::")
    config = CalculatorConfig()
    assert isinstance(config.config, dict)
