import sys
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
            sys.exit()
        else: 
            print("Invalid Choice")
            game_over_choice = input("Would you like to [play] again? or do you want to [quit] playing? ")

def gate():
    pass

def road():
    print("---------------------------------------------------------")
    print("you walk up the road on foot, the music grows")
    print("you follow the music up the road until you arrive at a large gate, flanked by chainlink fence")
    print("you see a little cutout in the gate but not big enough to squeeze through")
    print("the music is coming from the other side of the gate, perhaps someone there knows how to fix a car?")
    print("you see a rusty lock on the gate, and some boxes next to the gate")
    move = input("do you want to [smash] the lock with a rock? or [climb] the fence with the boxes? ")
    if move == "smash":
        print("You strike the lock, and suddenly a vicious dog jumps through the cutout and attacks you")
        game_over()
    elif move == 'climb':
        print("you stack the boxes and climb the fence")
        gate()
    else:
        print("Invalid Choice")
        road()

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
                "resolute in your decision, you start to become more confident in your ability to wait",
                "You can do this, you can wait all night if it takes",
                "By sheer wait-power, you will will your car back to life you tell yourself",
                "You're nowhere near as determined as you initially thought, you can't do this any longer you tell yourself"]
    print("---------------------------------------------------------")
    print("you wait in the car, nothing happens")
    move = input("do you want to [wait] some more, explore the [woods] or walk up the [road] on foot? ")
    while move == 'wait':
        if wait_time < len(wait_messages):
            print(wait_messages[wait_time])
            wait_time += 1
        elif wait_time == len(wait_messages):
            print("you die from the exhaustion of waiting for a miracle, what a pitiful way to go")
            game_over()
        else:
            print("You're nowhere near as determined as you initially thought, you can't do this any longer you tell yourself")
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
    print("you are driving to a friends wedding, and decided to take a shortcut")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("your car is in need of repairs if you are to make it in time for the wedding")
    print("It's quiet, but you think you can hear music coming from somewhere")
    choice = input("Do you.. [wait]? walk up the [road] on foot? or explore the [woods]? ")
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
        
    elif ready == "quit":
        sys.exit()
    else:
        print("Invalid Choice")
        ready = input("Ready to [play]? or [quit] game? ")