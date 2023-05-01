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
    print("You are in Room 2. In front of you is a button")
    # Code for actions in Room 2
    button_presses = 0
    while True:
        move = input("Enter 'back' to go back to the starting room or 'push' to push the button: ")
        if move == "back":
            starting_room()
            return
        elif move == "push":
            button_presses += 1
            if button_presses >= 5:
                print("You hear a rumbling sound and a secret door opens!")
                move = input("do you enter the secret door or head back? type 'enter' or 'back'")
                if move == "back":
                    starting_room()
                elif move == "enter":
                    secret_room()
                return
            else:
                print("You push the button, but nothing happens.")
        else:
            print("Invalid choice.")

def secret_room():
    print("you are in a secret room")
    # Code for actions in secret room
    move = input("'back' to go back 'look' to look around the secret room")
    if move == "back":
        room2()
    elif move == "look":
        print("you see something")
    else:
        print("Invalid choice.")
        room1()



starting_room()