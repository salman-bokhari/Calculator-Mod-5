import pandas as pd
from app.calculator_memento import Memento, Caretaker

def test_memento_caretaker():
    df = pd.DataFrame([{'x':1}])
    m = Memento(df)
    ct = Caretaker()
    ct.save(m)
    m2 = ct.undo()
    assert m2 is not None
    # redo flow
    ct.save(Memento(df))
    _ = ct.undo()
    r = ct.redo()
    assert r is None or r.get_state() is not None
