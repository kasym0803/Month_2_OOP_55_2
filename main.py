

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мой age {self.age}, мой city {self.city}"

person = Person("Касымбек", 18, "Bishkek")

print(person.introduce())

# def is_abult():
#     if person.age >= 18:
#         return f"True"
#     else:
#         return f"False"
#     print(is_abult())

