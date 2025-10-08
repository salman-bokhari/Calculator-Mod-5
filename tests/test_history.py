import pytest
from app.history import History

def test_add_and_save_load(tmp_path):
    h = History()
    h.clear_history()
    h.add(1, "+", 2, 3, "t")
    p = tmp_path / "history.csv"
    h.save(p)
    loaded = History.load(p)
    assert not loaded.empty
