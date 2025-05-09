
import sys

from products import Product
from store import Store



def make_order():
    print("order")


def display_number_of_all_goods():
    print("display_number_of_all_goods")


def display_goods():
    print("display_goods")


def start(store):
    quite =  lambda: (print("\nBye!") or sys.exit())

    dispatcher_menu = {
        1: ("List all products in store", display_goods),
        2: ("Show total amount in store", display_number_of_all_goods),
        3: ("Make an order", make_order),
        4: ("Quit", quite)
    }

    while True:
        try:
            for item, description in dispatcher_menu.items():
                print(f"{item}: {description[0]}")
            user_choice = int(input("Please choose a number(1-4): "))
            if 4 < user_choice < 1:
                raise KeyError
            dispatcher_menu[user_choice][1]()

        except (ValueError, KeyError):
            print("Invalid Input!")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()