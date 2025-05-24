
class Store:
    """
    This class represents a store that holds a collection of products.

    Attributes:
        products (list): A list of Product objects in the store.
    """

    def __init__(self, products: list):
        """
        Initialize a new store with a list of products.

        Args:
            products (list): A list of Product objects.
        """
        self.products = products

    def add_product(self, product: object):
        """
        Add a product to the store's inventory.

        Args:
            product (object): A Product object to add to the store.
        """
        self.products.append(product)

    def remove_product(self, product: object):
        """
        Remove a product from the store's inventory.

        Args:
            product (object): A Product object to remove from the store.

        Raises:
            ValueError: If the product is not found in the store's inventory.
        """
        try:
            self.products.remove(product)
        except ValueError:
            raise ValueError("The product is not found in the store.")

    def get_total_quantity(self) -> int:
        """
        Calculate the total quantity of all products in the store.

        Returns:
            int: The total quantity of products in the store.
        """
        inventory = {product.name: product.quantity for product in self.products}
        total = sum(inventory.values())
        return total # , inventory

    def get_active_products(self) -> list:
        """
        Get a list of active products in the store.

        Returns:
            list: A list of active product names.
        """
        return [product.name for product in self.products if product.is_active]

    def order(self, shopping_list) -> float:
        """
        Process an order and calculate the total price.

        Args:
            shopping_list (list): A list of tuples (product, quantity) where product is a Product object
                                   and quantity is the number of units ordered.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If any product is inactive or the quantity is invalid.
        """
        try:
            invoice = sum([item.buy(quantity) for item, quantity in shopping_list if item in self.products])
            return invoice
        except ValueError as e:
            print(e)