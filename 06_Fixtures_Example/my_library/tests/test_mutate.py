"""
Show that fixtures preserver mutable objects
"""
import pytest 
from .. import my_module

# Try different scope="session" to see what happens. 
@pytest.fixture(scope="class")
def some_list():
    return [1,2,3]


def test_pop(some_list):
    my_module.drop_list_item(some_list)
    assert some_list == [1,2]


def test_add(some_list):
    my_module.add_item_to_list(some_list)
    assert some_list == [1,2,3,10]


