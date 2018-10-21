"""Add tests for adders here """
import pytest
from .. import my_module


@pytest.fixture(scope="session")
def adder_fixture():
    adder = my_module.SingleObject(5)
    return adder


def test_add_4(adder_fixture):
    total = adder_fixture.add_more(4)
    assert total == 9


def test_add_10(adder_fixture):
    total = adder_fixture.add_more(10)
    assert total == 15