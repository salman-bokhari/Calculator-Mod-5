import os
import pandas as pd
from app.history import HistoryManager

def test_history_add_save_load(tmp_path):
    p = tmp_path / 'h.csv'
    hm = HistoryManager(csv_path=str(p), auto_save=False)
    hm.add('+',1,2,3)
    assert not hm.df.empty
    hm.save()
    hm2 = HistoryManager(csv_path=str(p), auto_save=False)
    assert not hm2.df.empty
    os.remove(str(p))
