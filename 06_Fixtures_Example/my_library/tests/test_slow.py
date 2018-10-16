import pytest

# Python relative import
from .. import my_module


def test_not_three():
    result = my_module.load_data()
    assert result != 3

def test_object_type():
    result = my_module.load_data()
    assert isinstance(result, int)

def test_is_five():
    result = my_module.load_data()
    assert result == 5
