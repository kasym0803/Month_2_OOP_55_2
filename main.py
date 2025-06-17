

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мой age {self.age}, мой city {self.city}"

    def is_abult(self):
        if self.age >= 18:
            return f"{self.name} старше 18 лет", True
        else:
            return f"{self.name} не страше 18 лет", False

Kasymbek = Person("Касымбек", 18, "Bishkek")
Aziz = Person("Азиз", 22, "Bishkek")
Aidar = Person("Айдар", 17, "Bishkek")

print(Kasymbek.introduce())
print(Kasymbek.is_abult())

print(Aziz.introduce())
print(Aziz.is_abult())

print(Aidar.introduce())
print(Aidar.is_abult())

