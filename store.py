
class Store:


    def __init__(self, products: list):
        self.products = products


    def add_product(self, product: object):
        self.products.append(product)


    def remove_product(self, product: object):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        inventory = {product.name: product.quantity for product in self.products}
        total = sum(inventory.values())
        return total # , inventory


    def get_all_products(self) -> list:
        return [product.name for product in self.products if product.active]


    def order(self, shopping_list) -> float: # [(bose, 5), (mac, 30)]
        try:
            invoice = sum([item.buy(quantity) for item, quantity in shopping_list if item in self.products])
            return invoice
        except ValueError as e:
            print(e)