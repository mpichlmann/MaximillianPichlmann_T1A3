import sys


church_quiet = False
signpost_visited = False
soup_eaten = 0

def game_over():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
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

def manor_second():
    pass
def manor_kitchen():
    pass

def painting():


def study():
    print("---------------------------------------------------------")
    print("You enter the study where you see a loan chair faced towards a painting")
    print("next to the chair is a small table, on top sits a leatherbound book")
    print("---------------------------------------------------------")
    move = input("do you inspect the [painting] or inspect the [book]? ")
    
    
def manor_first():
    print("---------------------------------------------------------")
    print("You enter the house, you see a study to the left, and some stairs to the right")
    print("In front of you is a small kitchen that seems recently tidied")
    print("---------------------------------------------------------")
    move = input("do you investigate the [study], the [kitchen] or head up the [stairs] ")
    while True:
        if move == 'study':
            study()
        elif move == 'kitchen':
            manor_kitchen()
        elif move == 'stairs':
            manor_second()
        else:
            print("Invalid Choice")
            move = input("do you investigate the [study], the [kitchen] or head up the [stairs] ")

def manor():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    church_quiet = True
    print("---------------------------------------------------------")
    print("you follow the path to until you reach a double story house")
    print("The house resembles an old victorian architectural style")
    print("It's small, definitely not a manor by any means, you wonder why it would be referred to as such")
    print("you notice the door is wide open")
    print("---------------------------------------------------------")
    move = input("do you [enter] the house or head [back] to the signpost? ")
    while True:
        if move == 'enter':
            manor_first()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you [enter] the house or head [back] to the signpost? ")


def church():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    if church_quiet == False:
        print("---------------------------------------------------------")
        print("You follow the direction the sign pointed until you come across a church")
        print("inside you can hear music and singing, although now that you're closer it sounds more like chanting")
        print("you think maybe someone inside can help you fix your car")
        print("---------------------------------------------------------")
        church_quiet = True
    else:
        print("---------------------------------------------------------")
        print("You follow the direction the sign pointed until you come across a church")
        print("you can't hear anything now, but you're sure this is where the music was coming from")
        print("you think maybe someone inside can help you fix your car")
        print("---------------------------------------------------------")
    move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")
    while True:
        if move == "knock" and church_quiet == False:
            print("---------------------------------------------------------")
            print("the music and chanting stops, you hear boots marching towards the door")
            print("the door swings open, you are met by a group of people donned in hoods")
            print("'REMOVE THE INTERLOPER' a voice shouts")
            print("the group of hooded figures reveal the knives under their cloaks and launch at you")
            game_over()
        elif move == 'knock' and church_quiet == True:
            print("---------------------------------------------------------")
            print("you hear a high pitched voice scream out for help")
            print("---------------------------------------------------------")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in or head [back] to the signpost? ")
        elif move == "open":
            print("---------------------------------------------------------")
            print("You try to the door but can't, the door is locked")
            print("---------------------------------------------------------")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")
        elif move == 'look' and church_quiet == False:
            print("---------------------------------------------------------")
            print("You peer through the window and see a group of hooded figures in black robes standing in a circle")
            print("In the center of them you see a woman in a mechanics uniform strapped to an upside down cross")
            print("standing opposite the woman is a figure in a red robe, holding a tome in one hand, and an ornate knife in the other")
            print("You think to yourself 'Maybe that woman in the mechanics uniform can help me fix my car!'")
            print("you also think she might be in a bit of trouble and be in need of some rescuing")
            print("---------------------------------------------------------")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in or head [back] to the signpost? ")
        elif move == 'look' and church_quiet == True:
            print("---------------------------------------------------------")
            print("You peer through the window and see a group of hooded figures lying on the ground in a circle")
            print("In the center of all the figures you see a woman in a mechanics uniform strapped to an upside down cross")
            print("You think to yourself 'Maybe that woman in the mechanics uniform can help me fix my car!'")
            print("you also think she might be in a bit of trouble and be in need of some rescuing")
            print("---------------------------------------------------------")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in or head [back] to the signpost? ")
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, do you [look] in through a window or head [back] to the signpost? ")

def kitchen():
    global kitchen_return 
    kitchen_return = True
    print("---------------------------------------------------------")
    print("you enter the kitchen")
    print("---------------------------------------------------------")
    move = input("you can't see any point to being in the kitchen and think you should head [back]")
    while True:
        if move == 'back': 
            mess_hall()
        else: 
            print("Invalid Choice")
            move = input("you can't see any point to being in the kitchen and think you should head [back]")
        

def mess_hall():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    church_quiet = True
    global soup_eaten
    if kitchen_return == False and soup_eaten == 0:
        print("---------------------------------------------------------")
        print("You follow the path until you reach a large wooden building")
        print("Entering the building you find a row of dining tables, at the back you see a door leading to a kitchen")
        print("Amongst all the empty dishes you see a bowl of soup it seems someone has left out")
        print("---------------------------------------------------------")
        move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost ")
    elif kitchen_return == False and soup_eaten > 0:
        print("---------------------------------------------------------")
        print("You follow the path until you reach a large wooden building")
        print("Entering the building you find a row of dining tables, at the back you see a door leading to a kitchen")
        print("---------------------------------------------------------")
        move = input("explore the [kitchen] at the back, or head [back] to the signpost ")
    elif kitchen_return == True and soup_eaten == 0:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost ")
    else:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("explore the [kitchen] at the back, or head [back] to the signpost ")
    while True:
        if move == 'eat':
            if soup_eaten == 0:
                soup_eaten += 1
                print("---------------------------------------------------------")
                print("You eat the soup, it tastes funny, ")
                print("---------------------------------------------------------")
            else: 
                print("---------------------------------------------------------")
                print("YOU ALREADY ATE THE SOUP, nice try though")
                print("---------------------------------------------------------")
            move = input("explore the [kitchen] at the back, or head [back] to the signpost ")
        elif move == 'kitchen':
            kitchen()
        elif move == 'back':
            signpost()
        else: 
            print("Invalid Choice")
            move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost ")

def signpost():
    global kitchen_return 
    kitchen_return = False
    if signpost_visited == False:
        print("---------------------------------------------------------")
        print("You continue up the path, the music gets louder")
        print("The path leads to a clearing in the trees, you can make out the shape of buildings in the dark")
        print("you appear to be in some sort of summer camp, singing can now be heard accompanying the music")
        print("In front of you is a signpost with different destinations on it")
        print("---------------------------------------------------------")
    else:
        print("---------------------------------------------------------")
        print("you return to the signpost")
        print("you notice you can no longer hear the music or the singing that you did previously")
        print("---------------------------------------------------------")
    move = input("The signpost reads [mess hall],[church],[manor] ")
    while True:
        if move == 'mess hall':
            mess_hall()
        elif move == 'church':
            church()
        elif move == 'manor':
            manor()
        else: 
            print("Invalid Choice")
            move = input("The signpost reads [mess hall],[church],[manor] ")

def gate():
    print("---------------------------------------------------------")
    print("you stack the boxes and climb the gate")
    print("now that you're on the other side of the gate you see a sleeping dog and a path leading up to the source of the music")
    print("---------------------------------------------------------")
    move = input("do you [pet] the dog or continue up the [path]? ")
    while True:
        if move == 'pet':
            print("As you touch the dog, it wakes up and attacks you!")
            game_over()
        elif move == 'path':
            signpost()
        else: 
            print("Invalid Choice")
            move = input("do you [pet] the dog or continue up the [path]? ")
        
def road():
    print("---------------------------------------------------------")
    print("you walk up the road on foot, the music grows")
    print("you follow the music up the road until you arrive at a large gate, flanked by chainlink fence")
    print("you see a little cutout in the gate but not big enough to squeeze through")
    print("the music is coming from the other side of the gate, perhaps someone there knows how to fix a car?")
    print("you see a rusty lock on the gate, and some boxes next to the gate")
    print("---------------------------------------------------------")
    move = input("do you want to [smash] the lock with a rock? or [climb] the fence with the boxes? ")
    while True:
        if move == "smash":
            print("You strike the lock, and suddenly a vicious dog jumps through the cutout and attacks you")
            game_over()
        elif move == 'climb':
            gate()
        else:
            print("Invalid Choice")
            move = input("do you want to [smash] the lock with a rock? or [climb] the fence with the boxes? ")

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
            print("---------------------------------------------------------")
            print(wait_messages[wait_time])
            wait_time += 1
        else:
            print("---------------------------------------------------------")
            print("you die from the exhaustion of waiting for a miracle, what a pitiful way to go")
            game_over()
        move = input("do you want to [wait] some more, explore the [woods] or walk up the [road] on foot? ")
    if move == 'woods':
        wood_death()
    elif move == 'road':
        road()
    else: 
        print("Invalid Choice")
        car_wait()
        
def starting_room():
    global signpost_visited
    signpost_visited = False
    print("---------------------------------------------------------")
    print("It's almost midnight, you are driving on a long empty road")
    print("you are driving to a friends wedding, and decided to take a shortcut")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("your car is in need of repairs if you are to make it in time for the wedding")
    print("It's quiet, but you think you can hear music coming from somewhere")
    print("---------------------------------------------------------")
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
print("---------------------------------------------------------")
print("Welcome to 'Spooky Woods' an exploration horror puzzle game!")
print("Your goal is to reach the end without dying and save the day!")
print("Throughout the game you will be presented with choices in [square] brackets")
print("simply type the option in square brackets to proceed, but be careful!")
print("---------------------------------------------------------")
ready = input("Ready to [play]? or [quit] game? ")
while True:
    if ready == "play":
        starting_room()
    elif ready == "quit":
        sys.exit()
    else:
        print("Invalid Choice")
        ready = input("Ready to [play]? or [quit] game? ")