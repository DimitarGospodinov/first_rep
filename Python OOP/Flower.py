is_happy = False


class Flower():

    def __init__(self, name, req):

        self.name = name
        self.req = req

    def water(self, flower_water):
        if flower_water >= self.req:
            global is_happy
            is_happy = True

    def status(self):
        if is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
