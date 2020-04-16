import random, Enemy

class Room():
    def __init__(self, name, nextRooms):
        self.name = name
        self.rooms = nextRooms

    def nextRooms(self, previousRoom):
        print('Room where you can go: ')
        for room in self.rooms:
            print("- ", room.name)

        if previousRoom != self:
            print("- ", previousRoom.name)

    def enter(self, Character):
        if int(random.random() * 100) > 50:
            print('Oh no ! There is an monster !')
            Enemy.Enemy().attack(Character)
            print('You now have ', Character.life, ' pts of life')
