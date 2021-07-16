from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name):
        super(Drink, self).__init__(name, Drink.QUANTITY)


q = Drink("f")
print(q.quantity)