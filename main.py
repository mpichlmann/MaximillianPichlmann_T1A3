def game_over():
    print("---------------------------------------------------------")
    print("YOU DIED: GAME OVER")
    game_over_choice = input("Would you like to [play] again? or do you want to [quit] playing? ")
    while True:
        if game_over_choice == "play":
            starting_room()
            break
        elif game_over_choice == "quit":
            print("Thanks for playing!")
            break
        else: 
            print("Invalid Choice")
            game_over_choice = input("Would you like to [play] again? or do you want to [quit] playing? ")

def road():
    print("you are on a road")

def wood_death():
    print("---------------------------------------------------------")
    print("you wander into the woods")
    print("the music you heard before starts to grow")
    print("as you draw closer, you hear a click beneath your feet")
    print("you look down and see your foot caught on a wire")
    print("you've triggered a makeshift trap, nails fly at you from all directions, killing you")
    game_over()

def car_wait():
    wait_time = 0
    wait_messages = ["You wander what exactly it is you're waiting for...", 
                "You can't really think of anything that you're waiting for...",
                "You think someone finding you on this quiet road in the middle night is pretty unlikely, but still... you wait.",
                "resolute in your decision to wait, you start to become more confident in your ability to wait",
                "You can do this, you can wait all night if it takes",
                "By sheer wait-power, you will will your car back to life you tell yourself"]
    print("---------------------------------------------------------")
    print("you wait in the car, nothing happens")
    move = input("do you want to [wait] some more, explore the [woods] or walk up the [road] on foot? ")
    while move == 'wait':
        if wait_time < len(wait_messages):
            print(wait_messages[wait_time])
            wait_time += 1
        else:
            print("you start to get PISSED OFF")
        move = input("do you want to [wait] some more, explore the [woods] or walk up the [road] on foot? ")
    if move == 'woods':
        wood_death()
    elif move == 'road':
        road()
    else: 
        print("Invalid Choice")
        car_wait()
        


def starting_room():
    print("---------------------------------------------------------")
    print("It's almost midnight, you are driving on a long empty road")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("It's quiet, but you think you can hear music coming from somewhere")
    print("Do you.. [wait]? walk up the [road] on foot? or explore the [woods]? ")
    choice = input("Enter your choice: ")
    if choice == "wait":
        car_wait()
    elif choice == "road":
        road()
    elif choice == "woods":
        wood_death()
    else:
        print("Invalid choice.")
        starting_room()

print("Welcome to 'Spooky Woods' an exploration horror puzzle game!")
print("Your goal is to reach the end and save the day!")
print("Throughout the game you will be presented with choices")
print("Your options will be presented in [square] brackets")
print("simply type your option to proceed, but be careful!")
ready = input("Ready to [play]? or [quit] game? ")
while True:
    if ready == "play":
        starting_room()
        break
    elif ready == "quit":
        break
    else:
        print("Invalid Choice")
        ready = input("Ready to [play]? or [quit] game? ")