import pytest
from dessert import Cookie



def test_cookie():
    cookie = Cookie("name", 0, 0)
    assert cookie.name == "name"
    assert cookie.cookie_ammount == 0
    assert cookie.price_per_dozen == 0
    assert cookie.packaging == "Box"
    assert round(cookie.calculate_cost(), 2) == 0.0

    cookie.name = "diffname"
    cookie.cookie_ammount = 5
    cookie.price_per_dozen = 12
    assert cookie.name == "diffname"
    assert cookie.cookie_ammount == 5
    assert cookie.price_per_dozen == 12
    assert round(cookie.calculate_cost(), 2) == 5.0

