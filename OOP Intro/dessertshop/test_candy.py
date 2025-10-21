import pytest
from dessert import Candy
import dessertshop

def test_candy():
    candy = Candy("name", 0, 0)
    assert candy.name == "name"
    assert candy.candy_weight == 0
    assert candy.price_per_pound == 0
    assert round(candy.calculate_cost(), 2) == 0.0

    candy.name = "diffname"
    candy.candy_weight = 5
    candy.price_per_pound = 5
    assert candy.name == "diffname"
    assert candy.candy_weight == 5
    assert candy.price_per_pound == 5
    assert round(candy.calculate_cost(), 2) == 25.0

dessertshop.main()