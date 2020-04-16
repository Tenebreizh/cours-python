import math, random

class Enemy():
    def __init__(self):
        self.damage = int(random.random() * 100)

    def attack(self, Character):
        Character.life -= self.damage
        print('You loose ', self.damage, " pts of life")