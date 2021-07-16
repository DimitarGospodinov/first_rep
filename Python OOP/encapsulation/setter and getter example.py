class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property # kontrolirano get-vane na property primerno - if ..
    def age(self):
        return self._age

    @age.setter #kontrolirano setvane na property
    def age(self, value):
        if value <= 0:
            raise Exception("Age must be greater than zero")

        self._age = value

