
class Product:

    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("ValueError")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        return self.active == True


    def active(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        if self.active and 0 < quantity <= self.quantity:
            self.quantity -= quantity
            self.set_quantity(self.quantity)
            total_price = quantity * self.price
            return total_price
