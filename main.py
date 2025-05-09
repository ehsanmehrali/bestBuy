
import sys

from products import Product
from store import Store


def make_order():
    print("order")


def display_number_of_all_goods(store):
    """ Total number of all goods. """
    total_number =store.get_total_quantity()
    print(f"Total of {total_number} items in store")


def display_goods(store):
    """ Display all products along with their prices and quantities in stock. """
    print("------")
    for i, _ in enumerate(store.products):
        print(f"{i + 1}. {store.products[i].name}, Price: ${store.products[i].price}: {store.products[i].quantity}")
    print("------")


def start(store):
    """ Display menu and call user commands(features). """

    # Personalized exit function
    quite =  lambda _: (print("\nHope to see you again at Best Buy!") or sys.exit())

    dispatcher_menu = {
        1: ("List all products in store", display_goods),
        2: ("Show total amount in store", display_number_of_all_goods),
        3: ("Make an order", make_order),
        4: ("Quit", quite)
    }

    while True:
        try:
            print("\n   Store Menu")
            print("   ----------")
            for item, description in dispatcher_menu.items():
                print(f"{item}. {description[0]}")

            user_choice = int(input("Please choose a number(1-4): "))

            if 4 < user_choice < 1:
                raise KeyError
            dispatcher_menu[user_choice][1](store)

        except (ValueError, KeyError):
            print("Invalid Input!")
        except KeyboardInterrupt:
            quite(store)


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