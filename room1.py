def starting_room():
    print("You are in a room with two doors in front of you.")
    print("Type 1 to enter Door 1 or type 2 to enter Door 2.")
    choice = input("Enter your choice: ")
    if choice == "1":
        room1()
    elif choice == "2":
        room2()
    else:
        print("Invalid choice.")
        starting_room()

def room1():
    print("You are in Room 1.")
    # Code for actions in Room 1
    move = input("Enter 'back' to go back to the starting room: ")
    if move == "back":
        starting_room()
    else:
        print("Invalid choice.")
        room1()

def room2():
    print("You are in Room 2.")
    # Code for actions in Room 2
    move = input("Enter 'back' to go back to the starting room: ")
    if move == "back":
        starting_room()
    else:
        print("Invalid choice.")
        room2()

starting_room()