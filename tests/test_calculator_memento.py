from app.calculator_memento import Memento, Caretaker
def test_memento_undo_redo():
    c = Caretaker()
    state1 = {'history': 'a'}
    state2 = {'history': 'b'}
    c.save(Memento(state1))
    c.save(Memento(state2))
    m = c.undo({'history':'cur'})
    assert m.get_state() == state2
    r = c.redo()
    assert r is None or hasattr(r,'get_state') 
def test_memento_save_restore():
    memento = CalculatorMemento()
    memento.save_state([1, 2, 3])
    assert memento.restore_state() == [1, 2, 3]

def test_memento_restore_empty():
    memento = CalculatorMemento()
    assert memento.restore_state() is None