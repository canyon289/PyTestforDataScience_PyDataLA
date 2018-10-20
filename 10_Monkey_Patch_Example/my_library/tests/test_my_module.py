import pytest
from .. import my_module
import pandas as pd


@pytest.mark.skip
def test_df_add():
    new_df = my_module.load_data_frame_from_sql_and_add_2()
    assert new_df is not None


def test_df_add_again(monkeypatch):
    def return_df(db, conn):
        return pd.DataFrame([1, 2])

    monkeypatch.setattr(my_module.pd, "read_sql", return_df)

    new_df = my_module.load_data_frame_from_sql_and_add_2()

    assert new_df is not None