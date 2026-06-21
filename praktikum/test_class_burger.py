import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


from burger import Burger

@pytest.fixture
def burger():
    burger = Burger()
    return burger


class Burger:

    def test_set_buns_sets_bun(self,burger):
        burger.set_buns()
        assert len(burger.List) == Bun

    def test_add_ingredient_adds_ingredient_to_list(self,burger):
        burger.add_ingredient()
        assert len(burger.List[Ingredient]) == 1

    def test_remove_ingredient_removes_ingredient_by_index(self,burger):
        burger.remove_ingredient(0)
        assert len(burger.List[Ingredient]) == 0

    def test_move_ingredient_moves_ingredient_to_new_position(self,burger):
        burger.move_ingredient(1)
        assert burger.ingredients == 1

    def test_get_price_returns_correct_price(self,burger):
        price = burger.get_price()
        assert burger.price == price
        
    def test_get_receipt_returns_correct_receipt(self,burger):
        receipt = burger.get_receipt()
        assert burger.receipt == receipt

