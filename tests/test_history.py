import pandas as pd
from app.history import History
import tempfile, os

def test_add_and_save_load(tmp_path):
    h = History()
    h.add(1,'add',2,3,'t')
    p = tmp_path / 'h.csv'
    h.save(p)
    h2 = History()
    h2.load(p)
    assert len(h2.df) == 1
    assert h2.df.iloc[0]['result'] == 3
