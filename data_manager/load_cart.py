import csv
import os
from store import Store
from products import Product

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, "data")
CART_FILE_PATH = os.path.join(BASE_DIR, "data", "basket.csv")


def add_to_cart(store: Store, index: int, order_quantity: int) -> None:
    """ Add items to shopping cart and update inventory. """
    product = store.products[index - 1]
    if order_quantity > product.quantity:
        raise IndexError(f"Insufficient stock for {product.name}. Available: {product.quantity}, Ordered: {order_quantity}")

    product.buy(order_quantity)

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    file_exists = os.path.isfile(CART_FILE_PATH)
    with open(CART_FILE_PATH, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Product Name", "Unit Price", "Quantity", "Total Price"])
        total_price = product.price * order_quantity
        writer.writerow([product.name, product.price, order_quantity, total_price])


def show_cart(store: Store) -> None:
    """ Display the contents of the shopping cart. """
    if not os.path.exists(CART_FILE_PATH):
        print("Cart is empty.")
        return

    total = 0
    print("\n🛒 Your Cart:")
    print("-" * 75)
    with open(CART_FILE_PATH, mode="r", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        print(f"{header[0]:<30} {header[1]:<15} {header[2]:<15} {header[3]}")
        print("-" * 75)
        for row in reader:
            name, unit_price, quantity, row_total = row
            total += float(row_total)
            print(f"{name:<30} ${unit_price:<15} {quantity:<15} ${row_total}")
    print("-" * 75)
    print(f"{'Total':<63} ${total:.2f}")


def restore_cart_to_inventory(store: Store) -> None:
    """ Restore cart items back to the inventory. """
    product_lookup = {product.name: product for product in store.products}

    with open(CART_FILE_PATH, "r", newline="", encoding="utf8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            name = row["Product Name"]
            quantity = int(row["Quantity"])
            if name in product_lookup:
                product_lookup[name].set_quantity(product_lookup[name].get_quantity() + quantity)


def delete_cart(store: Store) -> None:
    """ Delete shopping cart and restore items to inventory. """
    if os.path.exists(CART_FILE_PATH):
        restore_cart_to_inventory(store)
        os.remove(CART_FILE_PATH)
        print("Shopping cart successfully deleted.")
    else:
        print("Shopping cart does not exist.")
