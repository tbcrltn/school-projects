from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name, tax_percent = 7.25):
        self.name = name
        self.tax_percent = tax_percent
    
    @abstractmethod
    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        price = self.calculate_cost() * (self.tax_percent/100)
        return round(price, 2)


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.0):
        DessertItem.__init__(self, name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    
class Cookie(DessertItem):
    def __init__(self, name, cookie_ammount, price_per_dozen):
        DessertItem.__init__(self, name)
        self.cookie_ammount = cookie_ammount
        self.price_per_dozen = price_per_dozen
    
    def calculate_cost(self):
        return round(self.cookie_ammount * (self.price_per_dozen/12),2)




class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0):
        DessertItem.__init__(self, name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)
    


class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name = "", topping_price = 0):
        IceCream.__init__(self, name, scoop_count=scoop_count, price_per_scoop=price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return round((self.scoop_count * self.price_per_scoop)+ self.topping_price, 2)


    def __str__(self):
        return f"Name: {self.name}, Scoop count: {self.scoop_count}, Topping Name: {self.topping_name}, Topping Price: {self.topping_price}"
    


class Order:
    def __init__(self):
        self.order = []

    def add(self, items = ()):
        for item in items:
            self.order.append(item)

    def __len__(self):
        return len(self.order)   

    def print_names(self):
        for item in self.order:
            print(item.name) 

    def order_cost(self):
        total_cost = 0
        for item in self.order:
            total_cost += item.calculate_cost()
        return round(total_cost,2)

    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
    

            



