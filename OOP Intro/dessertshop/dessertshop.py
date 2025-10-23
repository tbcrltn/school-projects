from dessert import IceCream, Candy, Cookie, Sundae, Order
from tabulate import tabulate



class DessertShop:
    def user_prompt_candy(self):
        candy = input("What kind of candy?\n-->")
        candy_weight = round(float(input("Enter the weight(lbs)\n-->")),2)
        price_per_pound = round(float(input("Enter the price per pound\n-->")),2)
        return candy, candy_weight, price_per_pound
    
    def user_prompt_cookie(self):
        cookie = input("What kind of cookies?\n-->")
        cookie_ammount = int(input("Enter the ammount\n-->"))
        price_per_dozen = round(float(input("Enter the price per dozen\n-->")),2)
        return cookie, cookie_ammount, price_per_dozen
    
    def user_prompt_icecream(self):
        ice_cream = input("What kind of ice cream?\n-->")
        scoop_count = int(input("Enter the number of scoops\n-->"))
        price_per_scoop = round(float(input("Enter the price per scoop\n-->")),2)
        return ice_cream, scoop_count, price_per_scoop
    
    def user_prompt_sundae(self):
        sundae = input("What kind of ice cream?\n-->")
        topping = input("What topping?\n-->")
        scoop_count = int(input("Enter the number of scoops\n-->"))
        topping_price = round(float(input("Enter the topping price\n-->")))
        price_per_scoop = round(float(input("Enter the price per scoop\n-->")))
        return sundae, topping, scoop_count, topping_price, price_per_scoop






def main():
    data = []
    order = Order()
    shop = DessertShop()
    ordering = True
    while ordering:
        print("""                1: Candy
                2: Cookie
                3: Ice Cream
                4: Sundae\n""")
        
        prompt = input("What would you like to add to the order? (1-4, Enter for done):")


        if prompt == "":
            ordering = False
        else:
            prompt = int(prompt)


        if prompt == 1:
            candy, candy_weight, price_per_pound = shop.user_prompt_candy()
            order.add(Candy(candy, candy_weight, price_per_pound=price_per_pound))
        elif prompt == 2:
            cookie, cookie_ammount, price_per_dozen = shop.user_prompt_cookie()
            order.add(Cookie(cookie, cookie_ammount=cookie_ammount, price_per_dozen=price_per_dozen))
        elif prompt == 3:
            ice_cream, scoop_count, price_per_scoop = shop.user_prompt_icecream()
            order.add(IceCream(ice_cream, scoop_count=scoop_count, price_per_scoop=price_per_scoop))
        elif prompt == 4:
            sundae, topping, scoop_count, topping_price, price_per_scoop = shop.user_prompt_sundae()
            order.add(Sundae(sundae, scoop_count=scoop_count, price_per_scoop=price_per_scoop, topping_name=topping, topping_price = topping_price))

    
    
    
    print("\n\n\n\n")
    for item in order.order:
        data.append([item.name, item.calculate_tax(), item.calculate_cost()])
    data.append(["---------------", "-----", "------"])
    data.append(["Order Subtotal: ", order.order_tax(), order.order_cost()])
    data.append(["Order Total: ", "", round(order.order_tax()+order.order_cost(),2)])
    data.append(["Items in Order: ", "", len(order.order)])
   

    

    print(tabulate(data, headers = ["Name", "Tax", "Cost"], tablefmt="fsql"))

    

    

if __name__ == "__main__":
    main()

