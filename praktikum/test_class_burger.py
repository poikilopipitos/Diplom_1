from unittest.mock import Mock


class TestBurger:

    def test_set_buns_sets_bun(self,burger):
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_list(self,burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert len(burger.ingredients) == 2 and ingredient_1 in burger.ingredients and ingredient_2 in burger.ingredients

    def test_remove_ingredient_removes_ingredient_by_index(self,burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1 and ingredient_1 in burger.ingredients

    def test_move_ingredient_moves_ingredient_to_new_position(self,burger):
        ingredient_1 = Mock()
        ingredient_2 = Mock()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_2 and ingredient_1 in burger.ingredients

    def test_get_price_returns_correct_price(self,burger):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 200
        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 100

        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        assert burger.get_price() == 500

    def test_get_receipt_returns_correct_receipt(self,burger):
        bun_1 = Mock()
        bun_1.get_name.return_value = "black bun"
        bun_1.get_price.return_value = 100

        ingredient_1 = Mock()
        ingredient_1.get_name.return_value = "hot sauce"
        ingredient_1.get_price.return_value = 200
        ingredient_1.get_type.return_value = "sauce"

        ingredient_2 = Mock()
        ingredient_2.get_name.return_value = "sour cream"
        ingredient_2.get_price.return_value = 100
        ingredient_2.get_type.return_value = "sauce"

        burger.set_buns(bun_1)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        receipt = burger.get_receipt()

        assert "(==== black bun ====)" in receipt and "sauce hot sauce" in receipt and "sauce sour cream" in receipt and "Price: 500" in receipt