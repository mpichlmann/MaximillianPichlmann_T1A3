


def wood_death():
    print("you wander into the woods")
    print("the music you heard before starts to grow")
    print("as you draw closer, you hear a click beneath your feet")
    print("you look down and see your foot caught on a wire")
    print("you've triggered a makeshift trap, nails fly at you from all directions, killing you")
    game_over()

def starting_room():
    print("It's almost midnight, you are driving on a long empty road")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("It's quiet, but you think you can hear music coming from somewhere")
    print("Do you.. [wait]? walk up the [road] on foot? or explore the [woods]? ")
    choice = input("Enter your choice: ")
    if choice == "wait":
        room1()
    elif choice == "road":
        room2()
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
ready = input("Ready to [play]? ")
if ready == "play":
    starting_room()