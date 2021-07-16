class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):  # площ
        area_circle = Circle.pi * pow(self.radius, 2)
        return area_circle

    def get_circumference(self):  # обиколка
        area_circumference = Circle.pi * self.radius * 2
        return area_circumference


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
