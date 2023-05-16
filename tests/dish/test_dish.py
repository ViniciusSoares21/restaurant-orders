from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient_carne = Ingredient("carne")

    my_dish = Dish('vj', 99.00)
    my_dish_2 = Dish('vj', 99.00)
    my_dish_3 = Dish('Trybe', 40000.00)
    assert my_dish.name == 'vj'
    assert my_dish.__hash__() == my_dish_2.__hash__()
    assert my_dish.__hash__() != my_dish_3.__hash__()
    assert my_dish.__eq__(my_dish_2) is True
    assert my_dish.__eq__(my_dish_3) is False
    assert my_dish.__repr__() == "Dish('vj', R$99.00)"

    my_dish.add_ingredient_dependency(ingredient_carne, 3)

    assert my_dish.recipe.get(ingredient_carne) == 3
    assert Restriction.ANIMAL_MEAT in my_dish.get_restrictions()
    assert Restriction.ANIMAL_DERIVED in my_dish.get_restrictions()
    assert my_dish.get_ingredients() == {Ingredient('carne')}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('error', '3')

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish('error', 0)
