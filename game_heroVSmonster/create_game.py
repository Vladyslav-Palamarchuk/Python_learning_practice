from random import random
from random import randint


class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def si_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        print(f'{self.name}, отримав {amount} шкоди! Залишилося хп {self.hp}. ')

class Hero(Character):
    def attack(self, enemy):  #додали ворог
        hit = random.randint(1, self.damage)
        print(f"{self.name}, атакує {enemy.name}!")
        enemy.take_damage(hit)