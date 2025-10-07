from dessert import DessertItem, IceCream, Candy, Cookie, Sundae, Order



def main():
    order = Order()
    order.add((
        Candy("Candy Corn", 1.5, .25),
        Candy("Gummy Bears", .25, .35),
        Cookie("Chocolate Chip", 6, 3.99),
        IceCream("Pistachio", 2, .79),
        Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29),
        Cookie("Oatmeal Raisin", 2, 3.45)
    ))

    order.print_names()

    print(f"Number or orders: {len(order)}")

    

if __name__ == "__main__":
    main()