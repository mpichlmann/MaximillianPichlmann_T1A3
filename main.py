import sys

signpost_visited = False

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

def church():
    signpost_visited = True
    print("---------------------------------------------------------")
    print("You follow the direction the sign pointed until you come across a church")
    print("inside you can hear music and singing, although now that you're closer it sounds more like chanting")
    print("you think maybe someone inside can help you fix your car")
    move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")
    while True:
        if move == "knock":
            print("the music and chanting stops, you hear boots marching towards the door")
            print("the door swings open, you are met by a group of people donned in hoods")
            print("'REMOVE THE INTERLOPER' a voice shouts")
            print("the group of hooded figures reveal the knives under their cloaks and launch at you")
            game_over()
        elif move == "open":
            print("You try to the door but can't, the door is locked")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")
        elif move == 'look': 
            print("You peer through the window and see a group of hooded figures in black robes standing in a circle")
            print("In the center of them you see a woman in a mechanics uniform strapped to an upside down cross")
            print("standing opposite the woman is a figure in a red robe, holding a tome in one hand, and an ornate knife in the other")
            print("You think to yourself 'Maybe that woman in the mechanics uniform can help me fix my car!'")
            print("you also think she might be in a bit of trouble and be in need of some rescuing")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")




def kitchen():
    print("you enter the kitchen")

def mess_hall():
    
    print("---------------------------------------------------------")
    print("You follow the path until you reach a large wooden building")
    print("Entering the building you find a row of dining tables, at the back you see a door leading to a kitchen")
    print("Amongst all the empty dishes you see a bowl of soup it seems someone has left out")
    move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost ")
    while True:
        if move == 'eat':
            print("You eat the soup, it tastes funny, ")
        elif move == 'kitchen':
            kitchen()
        elif move == 'back':
            signpost_visited = True
            signpost()
        else: 
            print("Invalid Choice")
            move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost ")

def signpost():
    if signpost_visited == False:
        print("---------------------------------------------------------")
        print("The path leads to a clearing in the trees, you can make out the shape of buildings in the dark")
        print("you appear to be in some sort of summer camp, singing can now be heard accompanying the music")
        print("In front of you is a signpost with different destinations on it")
    else:
        print("---------------------------------------------------------")
        print("you return to the signpost")
        print("you notice you can no longer hear the music or the singing that you did previously")
    move = input("The signpost reads [mess hall],[dorms],[church],[manor]")
    if move == 'mess hall':
        mess_hall()
    elif move == 'dorms':
        dorms()
    elif move == 'church':
        church()
    elif move == 'manor':
        manor()
    else: 
        print("Invalid Choice")
        signpost()

def gate():
    print("---------------------------------------------------------")
    print("On the other side of the gate you see a dog sleeping and a path leading up to the source of the music")
    move = input("do you [pet] the dog or continue up the [path]? ")
    if move == 'pet':
        print("As you touch the dog, it wakes up and attacks you!")
        game_over()
    elif move == 'path':
        print("You continue up the path, the music gets louder")
        signpost()
    else: 
        print("Invalid Choice")
        gate()
        
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
        print("---------------------------------------------------------")
        print("you stack the boxes and climb the gate")
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
    while True:
        if choice == "wait":
            car_wait()
        elif choice == "road":
            road()
        elif choice == "woods":
            wood_death()
        else:
            print("Invalid choice.")
            choice = input("Do you.. [wait]? walk up the [road] on foot? or explore the [woods]? ")

print("Welcome to 'Spooky Woods' an exploration horror puzzle game!")
print("Your goal is to reach the end without dying and save the day!")
print("Throughout the game you will be presented with choices in [square] brackets")
print("simply type the option in square brackets to proceed, but be careful!")
ready = input("Ready to [play]? or [quit] game? ")
while True:
    if ready == "play":
        starting_room()
    elif ready == "quit":
        sys.exit()
    else:
        print("Invalid Choice")
        ready = input("Ready to [play]? or [quit] game? ")