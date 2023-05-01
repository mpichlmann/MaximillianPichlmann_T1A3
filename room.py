print("you are in a room with two doors in front of you, type 1 to enter door 1 and type 2 to enter door 2")
room = "starting room"

while True: 
    door = int(input())
    if door == 1: 
        print("you are now in room 1")
        room = "room 1"
    elif door == 2: 
        print("you are now in room 2")
        room = "room 2"
    elif door == "go back":
        print("You are now back in the starting room")
    