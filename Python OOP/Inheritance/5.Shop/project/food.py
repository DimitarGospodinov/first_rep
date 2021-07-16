from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name):
        super(Food, self).__init__(name, Food.QUANTITY)


q = Food("f")
print(q.quantity)