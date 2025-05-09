
import sys

from data_manager.load_cart import add_to_cart, show_cart, delete_cart
from products import Product
from store import Store


def exit_store(store):
    """ Personalized exit function and delete shopping cart before exit. """
    # Hope to see you again at Best Buy!
    delete_cart(store)
    print("\nHope to see you again at Best Buy!")
    sys.exit()


def make_order(store):
    """ Make shopping order. """
    while True:
        try:
            display_goods(store)
            number_of_types_of_goods = len(store.products)

            print("When you want to finish order, enter q.")
            product_index = input("Which product # do you want? ").strip().lower()

            if product_index == "q":
                exit_store(store)

            product_index = int(product_index)
            if number_of_types_of_goods < product_index or int(product_index) < 1:
                raise ValueError

            number_of_product = input("How many do you want? ")
            if product_index == "q":
                return

            add_to_cart(store, int(product_index), int(number_of_product))
            show_cart(store)
            back_to_shopping = input("Would you like to continue shopping(y-n)? ")

            if back_to_shopping == "y":
                continue
            else:
                break
        except ValueError:
            print("Invalid Input!")
        except IndexError as e:
            print(e)


def display_number_of_all_goods(store):
    """ Total number of all goods. """
    total_number =store.get_total_quantity()
    print(f"Total of {total_number} items in store")


def display_goods(store):
    """ Display all products along with their prices and quantities in stock. """
    print("-" * 55)
    print(f"   {'Product Name:':<30} {'Price:':12} {'In Stock'}")
    for i, _ in enumerate(store.products):
        print(f"{i + 1}. {store.products[i].name:-<30} ${store.products[i].price:-<15} {store.products[i].quantity}")
    print("-" * 55)


def start(store):
    """ Display menu and call user commands(features). """
    dispatcher_menu = {
        1: ("List all products in store", display_goods),
        2: ("Show total amount in store", display_number_of_all_goods),
        3: ("Make an order", make_order),
        4: ("Show cart", show_cart),
        5: ("Delete shopping cart", delete_cart),
        6: ("Quit", exit_store)
    }

    while True:
        try:
            print("\n   Store Menu")
            print("-" * 55)
            for item, description in dispatcher_menu.items():
                print(f"{item}. {description[0]}")

            user_choice = int(input("Please choose a number(1-6): "))

            if 4 < user_choice < 1:
                raise KeyError
            dispatcher_menu[user_choice][1](store)

        except (ValueError, KeyError):
            print("Invalid Input!")
        except KeyboardInterrupt:
            exit_store(store)


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