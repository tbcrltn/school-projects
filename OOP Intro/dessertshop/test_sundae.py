import pytest
from dessert import Sundae

def test_sundae():
    sundae = Sundae("name", 0, 0)
    assert sundae.name == "name"
    assert sundae.price_per_scoop == 0
    assert sundae.scoop_count == 0
    assert sundae.topping_name == ""
    assert sundae.topping_price == pytest.approx(0.0, abs=1e-3)
    assert round(sundae.calculate_cost()) == 0.0
    assert sundae.packaging == "Boat"

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
    assert round(sundae.calculate_cost(), 2) == 26.5

