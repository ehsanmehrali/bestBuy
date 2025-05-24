import sys
from products import Product
from store import Store
from data_manager.load_cart import add_to_cart, show_cart, delete_cart


def exit_store(store: Store) -> None:
    """ Personalized exit function and delete shopping cart before exit. """
    delete_cart(store)
    print("\nHope to see you again at Best Buy!")
    sys.exit()


def make_order(store: Store) -> None:
    """ Make shopping order by interacting with the user. """
    while True:
        try:
            display_goods(store)
            product_index = input("Which product # do you want (or 'q' to quit)? ").strip().lower()

            if product_index == "q":
                exit_store(store)

            product_index = int(product_index)
            if not 1 <= product_index <= len(store.products):
                raise ValueError("Invalid product index.")

            quantity = int(input("How many do you want? "))
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            add_to_cart(store, product_index, quantity)
            show_cart(store)

            continue_shopping = input("Would you like to continue shopping (y/n)? ").strip().lower()
            if continue_shopping != "y":
                break
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")


def display_goods(store: Store) -> None:
    """ Display all products along with their prices and quantities in stock. """
    print("-" * 55)
    print(f"{'Product Name':<30} {'Price':<10} {'In Stock'}")
    for i, product in enumerate(store.products, start=1):
        print(f"{i}. {product.name:<30} ${product.price:<10} {product.quantity}")
    print("-" * 55)


def display_total_inventory(store: Store) -> None:
    """ Display total number of items in store. """
    total_quantity = store.get_total_quantity()
    print(f"Total items in store: {total_quantity}")


def start(store: Store) -> None:
    """ Display menu and handle user input. """
    menu = {
        1: ("List all products", display_goods),
        2: ("Show total inventory", display_total_inventory),
        3: ("Make an order", make_order),
        4: ("Show cart", show_cart),
        5: ("Delete cart", delete_cart),
        6: ("Quit", exit_store)
    }

    while True:
        try:
            print("\nStore Menu")
            print("-" * 55)
            for item, description in menu.items():
                print(f"{item}. {description[0]}")

            user_choice = int(input("Please choose a number (1-6): "))
            if user_choice not in menu:
                raise ValueError("Invalid choice. Please choose between 1 and 6.")

            menu[user_choice][1](store)

        except (ValueError, KeyError) as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            exit_store(store)


def main() -> None:
    """ Initialize store and run the main program. """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    store = Store(products=product_list)
    start(store)


if __name__ == "__main__":
    main()
