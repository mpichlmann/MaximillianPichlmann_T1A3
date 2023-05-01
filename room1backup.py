for i in range(5):
        move = input("Enter 'back' to go back to the starting room or 'push' to push the button: ")
        if move == "back":
            starting_room()
            return
        elif move == "push":
            print(f"You push the button {i+1} times.")
        else:
            print("Invalid choice.")
            continue

    print("You hear a rumbling sound and a secret door opens!")
    move = input("do you enter the secret door or head back? type 'enter' or 'back'")
    # Code for opening the secret door
    if move == "enter":
        secret_room()
    elif move == "back":
        room2()
    else:
        print("Invalid choice.")
        room2()