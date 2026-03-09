
from random import randint


class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f'{self.name}, отримав {amount} шкоди! Залишилося хп {self.hp}. ')


class Hero(Character):
    def attack(self, enemy):  #додали ворог
        hit = randint(1, self.damage)
        print(f"{self.name}, атакує {enemy.name}!")
        enemy.take_damage(hit)

    def heal(self):
        self.hp += 20
        print(f"{self.name} лікування! Поточне здоров'я {self.hp}")


class Monster(Character):
    def attack(self, enemy):  # додали ворог
        hit = randint(1, self.damage)
        print(f"{self.name}, атакує {enemy.name}!")
        enemy.take_damage(hit)

player = Hero("Лицар", 100, 21)
dragon = Monster("Драконіс", 120, 20)


while player.is_alive() and dragon.is_alive():
    print("\n --------Твій хід --------")
    action = input("1 - Атакувати, 2 - Лікуватися")

    if action == "1":
        player.attack(dragon)
    elif action == "2":
        player.heal()

    if dragon.is_alive():
        print("\n Монстр атакує у відповідь!")
        dragon.attack(player)

if player.is_alive():
    print("Дракон переміг, перемога!")
else:
    print("Монстр переміг((")