
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CART_FILE_PATH = os.path.join(BASE_DIR, "data", "basket.csv")


def add_to_cart(store, index, order_quantity):
    """ Add items to shopping cart. """
    product = store.products[index - 1]
    name = product.name
    price = product.price
    total_price = price * order_quantity
    quantity_in_stock = product.quantity

    oversubscribe = order_quantity > quantity_in_stock
    if oversubscribe:
        raise IndexError(f"The number of orders({order_quantity}) is greater than the quantity of '{name} in stock({quantity_in_stock}).")

    product.buy(order_quantity)
    file_exists = os.path.isfile(CART_FILE_PATH)
    # Create shopping cart or append item to cart if exists.
    with open(CART_FILE_PATH, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Product Name", "Unit Price", "Quantity", "Total Price"])
        writer.writerow([name, price, order_quantity, total_price])


def show_cart(_):
    """ Display current shopping cart content. """
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


def restore_cart_to_inventory(store):
    """ Restore shopping cart items to inventory. """
    product_lookup = {product.name: product for product in store.products}

    with open(CART_FILE_PATH, "r", newline="", encoding="utf8") as handle:
        reader = csv.DictReader(handle)

        for row in reader:
            name = row["Product Name"]
            quantity = int(row["Quantity"])

            if name in product_lookup:
                product_lookup[name].set_quantity(
                    product_lookup[name].get_quantity() + quantity
                )


def delete_cart(store):
    """ Delete shopping cart if exists. """
    if os.path.exists(CART_FILE_PATH):
        restore_cart_to_inventory(store)
        os.remove(CART_FILE_PATH)
        print("Shopping cart successfully deleted.")
    else:
        print("Shopping cart does not exists!")