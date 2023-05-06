def box_open():
    pass

def box():
    print("---------------------------------------------------------")
    print("The box is made of fine wood and trimmed in gold")
    print("opening it proves challenging as it seems to be locked")
    print("you notice that the box is adorned with circular pieces of stone")
    print("each stone contains a symbol, and there are 9 stones in total")
    print("upon touching one you realise that the stones are in fact buttons that can be pressed")
    print("---------------------------------------------------------")
    
    correct_sequence = ["wheat", "pig", "baby"]
    current_sequence = []

    move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back] ")

    while True:
        if move == 'back':
            manor_first()
        elif move in ["pig", "bird", "bear", "baby", "wheat", "apple", "sword", "sheep", "snake"]:
            if move == correct_sequence[len(current_sequence)]:
                current_sequence.append(move)
                # Check if the user entered the complete correct sequence
                if current_sequence == correct_sequence or set(current_sequence) == set(correct_sequence):
                    print("---------------------------------------------------------")
                    print("The box opens to reveal its contents")
                    print("---------------------------------------------------------")
                    box_open()
                # If the user entered the correct button in the right order, display satisfying click
                elif move == correct_sequence[len(current_sequence)-1]:
                    print("---------------------------------------------------------")
                    print("You hear a satisfying click")
                    print("---------------------------------------------------------")  
                else:
                    print("---------------------------------------------------------")
                    print("You hear a 'thunk' noise that doesn't sound right")
                    print("---------------------------------------------------------")
                    current_sequence = []                  
            else:
                print("---------------------------------------------------------")
                print("You hear a 'thunk' noise that doesn't sound quite right")
                print("---------------------------------------------------------")
                current_sequence = []               
        else:
            print("Invalid Choice")    
        move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back] ")

box()