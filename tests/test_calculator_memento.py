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
