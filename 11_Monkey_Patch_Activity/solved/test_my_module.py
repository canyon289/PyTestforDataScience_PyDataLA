import pytest
from unittest.mock import Mock
from .. import my_module


"""
Solve the first Challenge
"""
def test_get_data_from_api(monkeypatch):

    # Make a function that when called returns a fake response
    def return_fake_response(url):
        return "Fake Response"

    monkeypatch.setattr(my_module.requests, "get", return_fake_response)
    response = my_module.get_data_from_api()
    assert response == "Fake Response"


def test_get_data_from_api_using_lambda(monkeypatch):

    monkeypatch.setattr(my_module.requests, "get", lambda x: "Fake Response")
    response = my_module.get_data_from_api()
    assert response == "Fake Response"


def test_get_data_from_api_using_mock(monkeypatch):
    fake_get = Mock(return_value="Fake Response")
    monkeypatch.setattr(my_module.requests, "get", fake_get)
    response = my_module.get_data_from_api()
    assert response == "Fake Response"


"""
Section two bonus
"""


def test_df_add_again(monkeypatch):

    # A mock with an attribute json which is another mock whos other return value is ["json_response"] when called
    response_mock = Mock(json=Mock(return_value=["json_response"]))

    # Return response_mock when called
    monkeypatch.setattr(my_module.requests, "get", lambda x: response_mock)

    json = my_module.get_json_from_response()
    assert json == ["json_response"]