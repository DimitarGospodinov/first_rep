class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        filter_obj = [p for p in self.products if p.name == product_name][0]
        if filter_obj:
            return filter_obj

    def remove(self, product_name):
        filter_obj = [p for p in self.products if p.name == product_name]
        if filter_obj:
            self.products.remove(filter_obj[0])

    def __repr__(self):
        result = []
        for m in self.products:
            result.append(f"{m.name}: {m.quantity}")
        return "\n".join(result)
