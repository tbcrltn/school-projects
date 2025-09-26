class DessertItem:
    def __init__(self, name):
        self.name = name


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.0):
        DessertItem.__init__(self, name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    
class Cookie(DessertItem):
    def __init__(self, name, cookie_weight, price_per_dozen):
        DessertItem.__init__(self, name)
        self.cookie_weight = cookie_weight
        self.price_per_dozen = price_per_dozen




class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0):
        DessertItem.__init__(self, name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop


class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0):
        IceCream.__init__(self, name, scoop_count=scoop_count, price_per_scoop=price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price


    def __str__(self):
        return f"Name: {self.name}, Scoop count: {self.scoop_count}, Topping Name: {self.topping_name}, Topping Price: {self.topping_price}"
    




sundae = Sundae("chocolate fudge", 2, 3,topping_name = "Fudge", topping_price= 1 )
print(sundae)