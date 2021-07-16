class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def is_quantity(self, q) -> bool:
        if self.quantity - q >= 0:
            return True

    def decrease(self, quantity: int):
        if self.is_quantity(quantity):
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity
