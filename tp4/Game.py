import Character, Enemy, Room


character = Character.Character()

out = Room.Room("Out", [])
garden = Room.Room("Garden", [out])
observatory = Room.Room("Observatory", [garden])
bathroom = Room.Room("Bathroom", [observatory])
toilet = Room.Room("Toilet", [garden, bathroom])
kitchen = Room.Room("Kitchen", [toilet])
prison = Room.Room("Prison", [garden, kitchen])

rooms = [garden, observatory, bathroom, toilet, kitchen, prison]

previousRoom = prison
actualRoom = prison

while (True):
    if actualRoom == out:
        print("You're finally outside ! ")
        break

    actualRoom.nextRooms(previousRoom)

    choice = str.lower(input("Where you want to go ? "))

    for room in actualRoom.rooms:
        if choice == str.lower(room.name) or choice == str.lower(previousRoom.name):
            room.enter(character)

            previousRoom = actualRoom
            actualRoom = room

            print("You're now in the ", actualRoom.name)
            break


