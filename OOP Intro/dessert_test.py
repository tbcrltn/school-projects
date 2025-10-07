import pytest
from dessert import DessertItem, Candy, Sundae, IceCream, Cookie
import dessertshop


def test_dessert():
    dessert = DessertItem("name")
    assert dessert.name == "name"

    dessert.name = "diffname"
    assert dessert.name == "diffname"

def test_candy():
    candy = Candy("name", 0, 0)
    assert candy.name == "name"
    assert candy.candy_weight == 0
    assert candy.price_per_pound == 0

    candy.name = "diffname"
    candy.candy_weight = 5
    candy.price_per_pound = 5
    assert candy.name == "diffname"
    assert candy.candy_weight == 5
    assert candy.price_per_pound == 5
    

def test_cookie():
    cookie = Cookie("name", 0, 0)
    assert cookie.name == "name"
    assert cookie.cookie_weight == 0
    assert cookie.price_per_dozen == 0

    cookie.name = "diffname"
    cookie.cookie_weight = 5
    cookie.price_per_dozen = 5
    assert cookie.name == "diffname"
    assert cookie.cookie_weight == 5
    assert cookie.price_per_dozen == 5
    

def test_sundae():
    sundae = Sundae("name", 0, 0)
    assert sundae.name == "name"
    assert sundae.price_per_scoop == 0
    assert sundae.scoop_count == 0
    assert sundae.topping_name == ""
    assert sundae.topping_price == pytest.approx(0.0, abs=1e-3)

    sundae.name = "diffname"
    sundae.price_per_scoop = 5
    sundae.scoop_count = 5
    sundae.topping_name = "topping"
    sundae.topping_price = 1.5
    assert sundae.name == "diffname"
    assert sundae.price_per_scoop == 5
    assert sundae.scoop_count == 5
    assert sundae.topping_name == "topping"
    assert sundae.topping_price == pytest.approx(1.5, abs=1e-3)

    
    

def test_icecream():
    icecream = IceCream("name")
    assert icecream.name == "name"
    assert icecream.price_per_scoop == pytest.approx(0.0, abs=1e-3)
    assert icecream.scoop_count == 0

    icecream.name = "diffname"
    icecream.price_per_scoop = 1.5
    icecream.scoop_count = 5
    assert icecream.name == "diffname"
    assert icecream.price_per_scoop == pytest.approx(1.5, abs=1e-3)
    assert icecream.scoop_count == 5


dessertshop.main()

    





