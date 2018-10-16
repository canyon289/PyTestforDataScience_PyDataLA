import pytest

# Python relative import
from .. import my_module

@pytest.fixture(scope="session")
def result_fixture():
    result = my_module.load_data()
    return result


def test_not_three(result_fixture):
    assert result_fixture != 3


def test_object_type(result_fixture):
    assert isinstance(result_fixture, int)


def test_is_five(result_fixture):
    assert result_fixture == 5
