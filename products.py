class Product:
    """
    This class represents a product with a name, price, quantity, and active status.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.
        active (bool): The active status of the product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a new product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If the name is empty or price or quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Name cannot be empty, and price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Get the current quantity of the product.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the product and deactivate it if the quantity is zero.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity > 0:
            self._activate()
        else:
            self._deactivate()

    def is_active(self) -> bool:
        """
        Check if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def _activate(self):
        """ Activate the product. """
        self.active = True

    def _deactivate(self):
        """ Deactivate the product. """
        self.active = False

    def show(self) -> str:
        """
        Display the product details.

        Returns:
            str: A string representing the product's name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buy a certain quantity of the product.

        Args:
            quantity (int): The quantity to be bought.

        Returns:
            float: The total price for the purchased quantity.

        Raises:
            ValueError: If the product is inactive or the quantity to be bought is invalid.
        """
        if not self.active:
            raise ValueError("Product is inactive.")
        if 0 < quantity <= self.quantity:
            self.quantity -= quantity
            self.set_quantity(self.quantity)
            total_price = quantity * self.price
            return total_price
        else:
            raise ValueError("Invalid quantity. Must be between 1 and the available quantity.")
