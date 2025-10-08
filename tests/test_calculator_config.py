from app.calculator_config import Config
def test_config_default():
    cfg = Config()
    assert hasattr(cfg, 'history_file')
