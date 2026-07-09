from praktikum.burger import Burger
from praktikum.database import Database
import pytest


@pytest.fixture
def burger():
    burger = Burger()
    return burger