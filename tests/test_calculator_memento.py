from app.calculator_memento import CalculatorMemento

def test_memento_save_restore():
    memento = CalculatorMemento()
    memento.save_state([1, 2, 3])
    assert memento.restore_state() == [1, 2, 3]

def test_memento_restore_empty():
    memento = CalculatorMemento()
    assert memento.restore_state() is None
