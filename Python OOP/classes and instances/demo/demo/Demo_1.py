class Person:
    def __init__(self, name, age, city, country):
        self.age = age
        self.city = city
        self.country = country
        self.name = name

class Circle:
    def __init__(self,radius):
        self.radius = radius




pesho = Person("Pesho", 11, "sofia", "Bulgaria")

# print(get_values(pesho, ['city', 'country']))
# print(get_values(pesho, ['name', 'country']))
print(getattr(pesho,'city'))
