from dessert import DessertItem, IceCream, Candy, Cookie, Sundae, Order
from tabulate import tabulate


def main():
    data = []
    order = Order()
    order.add((
        Candy("Candy Corn", 1.5, .25),
        Candy("Gummy Bears", .25, .35),
        Cookie("Chocolate Chip", 6, 3.99),
        IceCream("Pistachio", 2, .79),
        Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29),
        Cookie("Oatmeal Raisin", 2, 3.45)
    ))
    for item in order.order:
        data.append([item.name, item.calculate_tax(), item.calculate_cost()])
    data.append(["---------------", "-----", "------"])
    data.append(["Order Subtotal: ", order.order_tax(), order.order_cost()])
    data.append(["Order Total: ", "", order.order_tax()+order.order_cost()])
    data.append(["Items in Order: ", "", len(order.order)])
   

    

    print(tabulate(data, headers = ["Name", "Tax", "Cost"], tablefmt="fsql"))

    

    

if __name__ == "__main__":
    main()