import pytest
from dessert import DessertItem
import dessertshop

#doesnt work because it is an abstract class
def test_dessert():
    dessert = DessertItem("name")
    assert dessert.name == "name"

    dessert.name = "diffname"
    assert dessert.name == "diffname"

    
    

    


dessertshop.main()

    





