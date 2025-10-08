import pytest
from app.calculator_memento import CalculatorMemento

def test_memento_save_restore():
    memento = CalculatorMemento()
    state = [1,2,3]
    memento.save_state(state)
    restored = memento.restore_state()
    assert restored == state

def test_memento_restore_empty():
    memento = CalculatorMemento()
    assert memento.restore_state() is None
