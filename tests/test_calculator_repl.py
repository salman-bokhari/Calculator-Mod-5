import pytest
from app.calculator_repl import CalculatorFacade, LoggerObserver, AutoSaveObserver
from app.calculator_config import CalculatorConfig

def test_facade_and_observers(tmp_path):
    cfg = CalculatorConfig()
    cfg.history_csv = str(tmp_path / 'h.csv')
    cfg.auto_save = False
    fac = CalculatorFacade(config=cfg)
    fac.attach(LoggerObserver())
    fac.attach(AutoSaveObserver(fac.history))
    res = fac.calculate('+',1,2)
    assert res == 3
    fac.save(str(tmp_path / 'out.csv'))
    fac.clear_history()
    assert fac.history.df.empty
