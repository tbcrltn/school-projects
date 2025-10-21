import pytest
from dessert import IceCream
import dessertshop

def test_icecream():
    icecream = IceCream("name")
    assert icecream.name == "name"
    assert icecream.price_per_scoop == pytest.approx(0.0, abs=1e-3)
    assert icecream.scoop_count == 0
    assert round(icecream.calculate_cost(), 2) == 0.0

    icecream.name = "diffname"
    icecream.price_per_scoop = 5.0
    icecream.scoop_count = 5
    assert icecream.name == "diffname"
    assert icecream.price_per_scoop == pytest.approx(5.0, abs=1e-3)
    assert icecream.scoop_count == 5
    assert round(icecream.calculate_cost(), 2) == 25.0

dessertshop.main()