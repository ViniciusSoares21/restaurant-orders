from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_carne = Ingredient("carne")
    ingredient_carne2 = Ingredient("carne")
    ingredient_frango = Ingredient("frango")

    assert ingredient_carne.__hash__() == ingredient_carne2.__hash__()
    assert ingredient_frango.__hash__() != ingredient_carne.__hash__()
    assert ingredient_carne.__eq__(ingredient_carne) is True
    assert ingredient_carne.__eq__(ingredient_frango) is False
    assert ingredient_carne.name == "carne"
    assert ingredient_carne.__repr__() == "Ingredient('carne')"

    assert Restriction.ANIMAL_MEAT in ingredient_carne.restrictions
    assert Restriction.ANIMAL_DERIVED in ingredient_carne.restrictions

