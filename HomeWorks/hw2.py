import random

class Heroes():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} method action, {self.hp}"

    def attack(self):
        return f"{self.name} method action, {self.hp}"

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows <= 0:
            return f"{self.name} не может атаковать — стрелы закончились!"

        self.arrows -= 1
        precisions = random.randint(1, 50)
        if precisions <= self.precision:
            print(f"{self.name} успешно поразил цель! Осталось стрел: {self.arrows}, {precisions} точность")
        else:
            print(f"{self.name} промахнулся. Осталось стрел: {self.arrows}, {precisions} точность")

    def rest(self):
        self.arrows += 5
        return f"стрелы пополнены, теперь количесство стрел составляет {self.arrows}"

    def status(self):
        return f"Текущая состание героя, имя: {self.name}, здоровье: {self.hp}, стрелы: {self.arrows}, точ: {self.precision}"



archer = Archer("Рыцарь", 100, 3, 25)
print(archer.attack())
print(archer.rest())
print(archer.status())