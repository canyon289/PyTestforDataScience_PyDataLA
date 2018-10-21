import pytest
from unittest.mock import Mock
from .. import my_module


"""
Solve the first Challenge
"""


def test_get_data_from_api(monkeypatch):
    # Fill in code here

    response = my_module.get_data_from_api()
    assert response == "Fake Response"


"""
Section two bonus
"""


def test_df_add_again(monkeypatch):
    # Fill in code here

    json = my_module.get_json_from_response()
    assert json == ["json_response"]