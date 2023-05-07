import sys
import os

def game_over():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("-------------------YOU DIED: GAME OVER-------------------")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    
    game_over_choice = input("Would you like to [play] again? or do you want to [quit] playing? ")
    while True:
        if game_over_choice == "play":
            starting_room()
        elif game_over_choice == "quit":
            print("Thanks for playing!")
            sys.exit()
        else: 
            print("Invalid Choice")
            game_over_choice = input("Would you like to [play] again? or do you want to [quit] playing? ")


def game_complete():
    print("-------------------------------------------------------------")
    print("You rescue the mechanic preventing her from becoming a demon!")
    print("The two of you walk back to your car, where she helps fix it.")
    print("You give her a ride to a local police station where you both ")
    print("share your story. After the freaky events of the night you   ")
    print("get back out on the road, and make it to your friends wedding")
    print("-------------------------------------------------------------")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("------------------YOU WIN: GAME COMPLETE---------------------")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ")
    sys.exit()


def inside_church():
    print("---------------------------------------------------------")
    print("you enter the church, it's cold and the smell of sulfur is noticeable")
    print("you see a woman in a mechanics uniform tied to an upside down crowss")
    print("all around her are figures in robes lying motionless")
    print("'Please help me!' the woman screams 'These crazy cultists kidnapped me'")
    print("they drank something and said if I stay here on this cross all night I'll turn into a demon'")
    print("'I just want to get out of here and go back to my job fixing cars as a mechanic!!'")
    print("you think to yourself, 'wow this has worked out perfectly'")
    print("---------------------------------------------------------")
    move = input("do you [rescue] the mechanic, or for some unimaginable reason head [back] to the signpost? ")
    while True:
        if move == 'rescue':
            game_complete()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you [rescue] the mechanic, or for some unimaginable reason head [back] to the signpost? ")

def inside_box():
    print("---------------------------------------------------------")
    print("The box opens to reveal its contents")
    print("Inside is a golden key with a cross on it")
    print("you take the key")
    print("---------------------------------------------------------")
    inventory.append("key")
    move = input ("do you inspect the [photo] or head [back]? ")
    while True: 
        if move == 'back':
            manor_first()
        elif move == 'photo':
            photo()
        else:
            print("Invalid Choice")
            move = input ("do you inspect the [photo] or head [back]? ")

def box():
    global box_open
    print("---------------------------------------------------------")
    print("The box is made of fine wood and trimmed in gold")
    print("opening it proves challenging as it seems to be locked")
    print("you notice that the box is adorned with circular pieces of stone")
    print("each stone contains a symbol, and there are 9 stones in total")
    print("upon touching one you realise that the stones are in fact buttons that can be pressed")
    print("---------------------------------------------------------")
    
    correct_sequence = ["sword", "pig", "apple"]
    current_sequence = []

    move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back]? ")

    while True:
        if move == 'back':
            manor_first()
        elif move in ["pig", "bird", "bear", "baby", "wheat", "apple", "sword", "sheep", "snake"]:
            if move == correct_sequence[len(current_sequence)]:
                current_sequence.append(move)
                # Check if the user entered the complete correct sequence
                if current_sequence == correct_sequence or set(current_sequence) == set(correct_sequence):
                    box_open = True
                    inside_box()
                # If the user entered the correct button in the right order, display satisfying click
                elif move == correct_sequence[len(current_sequence)-1]:
                    print("---------------------------------------------------------")
                    print("You hear a satisfying click")
                    print("---------------------------------------------------------")  
                else:
                    print("---------------------------------------------------------")
                    print("You hear a 'thunk' noise that doesn't sound right")
                    if os.path.isfile("note.txt"):
                        print("maybe that [note] you found earlier might help")
                    print("---------------------------------------------------------")
                    current_sequence = []                  
            else:
                print("---------------------------------------------------------")
                print("You hear a 'thunk' noise that doesn't sound quite right")
                if os.path.isfile("note.txt"):
                        print("maybe that [note] you found earlier might help")
                print("---------------------------------------------------------")
                current_sequence = []  

        elif move == 'note':
            print("---------------------------------------------------------")
            with open('note.txt', 'r') as file:
                note_contents = file.read()
                print(note_contents)
            print("---------------------------------------------------------")
            move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back]? ")        
        else:
            print("Invalid Choice")    
        move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back]? ")

def photo():
    print("---------------------------------------------------------")
    print("the photo is a picture of a young boy standing next to an older gaunt looking man")
    print("The pair is standing in front of a church, the boy looks sad")
    print("---------------------------------------------------------")
    move = input("do you look at the [photo] again, inspect the [box], or head [back]? ")
    while True: 
        if move == 'photo':
            photo()
        elif move == 'box' and box_open == False:
            box()
        elif move == 'box' and box_open == True:
            print("You return to the box, proud of how you so brilliantly conquered it's puzzle")
            move = input("do you look at the [photo], or head [back]? ")
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            move = input("do you look at the [photo] again, inspect the [box], or head [back]? ")

def manor_second():
    global box_open
    print("---------------------------------------------------------")
    print("You head up the stairs into a small room")
    print("inside the room is a single bed, an empty bookshelf and a bedside table with a photo on it")
    print("opposite the bed is a writing desk up against the wall")
    print("on the writing desk is what looks like a decorative box with several symbols on it")
    print("---------------------------------------------------------")
    move = input("do you inspect the [box], look at the [photo], or head [back]? ")
    while True:
        if move == 'photo':
            photo()
        elif move == 'box' and box_open == False:
            box()
        elif move == 'box' and box_open == True:
            print("You return to the box, proud of how you so brilliantly conquered it's puzzle")
            move = input("do you look at the [photo], or head [back]? ")
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            move = input("do you inspect the [box], look at the [photo], or head [back]? ")

def manor_kitchen():
    print("---------------------------------------------------------")
    print("You enter the kitchen, it's remarkably tidy")
    print("The shelves are all empty, except for one loan plate and a single glass")
    print("You think to yourself that whoever lives here must enjoy their solitude")
    print("---------------------------------------------------------")
    move = input("You might as well head [back] ")
    while True:
        if move == 'back':
            manor_first()
        else: 
            print("Invalid Choice")
            move = input("Do you head [back]? ")

def painting():
    print("---------------------------------------------------------")
    print("The painting seems to contain a muscular figure front and center")
    print("The figures skin is pale, but covered in patches thick dark hair")
    print("The face is scratched out, making it indistinguishable")
    print("The figure stands in front of flames and dark clouds")
    print("You don't like the painting very much...")
    print("---------------------------------------------------------")
    move = input("do you inspect the [book] or head [back]? ")
    while True:
        if move == 'book':
            book()
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            move = input("do you inspect the [book] or head [back]? ")
def book():
    global note_picked
    if note_picked > 0:
        print("---------------------------------------------------------")
        print("You open the book but can't make any sense of it")
        print("The writing is in some language you've never seen before")
        print("---------------------------------------------------------")
        move = input("do you inspect the [painting], read the [note] you found, or head [back]? ")
        while True:
            if move == 'painting':
                painting()
            elif move == 'back':
                manor_first()
            elif move =='note':
                print("---------------------------------------------------------")
                with open('note.txt', 'r') as file:
                    note_contents = file.read()
                    print(note_contents)
                    print("---------------------------------------------------------")
                move = input('do you inspect the [painting], or head [back] ')
            else: 
                print("Invalid Choice")
                move = input("do you inspect the [painting], read the [note] you found, or head [back]? ")
    elif note_picked == 0:
        print("---------------------------------------------------------")
        print("You open the book but can't make any sense of it")
        print("The writing is in some language you've never seen before")
        print("As you flick through the pages, a small note falls out")
        print("---------------------------------------------------------")
        with open('note.txt', 'w') as file:
            file.write("So it goes the parable of summoning, \nLet those who know it's secrets hold these words. \n\nCut down the non-believers. \nCast away the swine of foolishness. \nPartake in the fruit of our lord. \n\nWith these words, let what has fallen rise again")
        note_picked += 1
        move = input("do you inspect the [painting], read the [note] you found, or head [back]? ")
        while True:
            if move == 'painting':
                painting()
            elif move == 'back':
                manor_first()
            elif move =='note':
                print("---------------------------------------------------------")
                with open('note.txt', 'r') as file:
                    note_contents = file.read()
                    print(note_contents)
                    print("---------------------------------------------------------")
                move = input('do you inspect the [painting], or head [back] ')
            else: 
                print("Invalid Choice")
                move = input("do you inspect the [painting], read the [note] you found, or head [back]? ")

def study():
    global note_picked
    print("---------------------------------------------------------")
    print("You enter the study where you see a lone chair faced towards a painting")
    print("next to the chair is a small table, on top sits a leatherbound book")
    print("---------------------------------------------------------")
    move = input("do you inspect the [painting], inspect the [book] or head [back]? ")
    while True:
        if move == 'painting': 
            painting()
        elif move == 'book':
            book()
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            move = input("do you inspect the [painting], inspect the [book] or head [back]? ")
     
def manor_first():
    print("---------------------------------------------------------")
    print("You're standing in the vestibule of the house, you see a study to the left, and some stairs to the right")
    print("In front of you is a small kitchen that seems recently tidied")
    print("---------------------------------------------------------")
    move = input("do you investigate the [study], the [kitchen], head up the [stairs] or head [back] to the signpost? ")
    while True:
        if move == 'study':
            study()
        elif move == 'kitchen':
            manor_kitchen()
        elif move == 'stairs':
            manor_second()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you investigate the [study], the [kitchen] or head up the [stairs] or head [back] to the signpost? ")

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
        if move == 'knock' and church_quiet == False:
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
            move = input("do you [knock] at the door, simply [open] the door and let yourself in, [look] through a window or head [back] to the signpost? ")
        elif move == 'open':
            if "key" in inventory:
                inside_church()
            else:
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
    move = input("you can't see any point to being in the kitchen and think you should head [back] ")
    while True:
        if move == 'back': 
            mess_hall()
        else: 
            print("Invalid Choice")
            move = input("you can't see any point to being in the kitchen and think you should head [back] ")
        

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
        move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost? ")
    elif kitchen_return == False and soup_eaten > 0:
        print("---------------------------------------------------------")
        print("You follow the path until you reach a large wooden building")
        print("Entering the building you find a row of dining tables, at the back you see a door leading to a kitchen")
        print("---------------------------------------------------------")
        move = input("explore the [kitchen] at the back, or head [back] to the signpost? ")
    elif kitchen_return == True and soup_eaten == 0:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost? ")
    else:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("explore the [kitchen] at the back, or head [back] to the signpost? ")
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
            move = input("explore the [kitchen] at the back, or head [back] to the signpost? ")
        elif move == 'kitchen':
            kitchen()
        elif move == 'back':
            signpost()
        else: 
            print("Invalid Choice")
            move = input("Do you [eat] the bowl of soup? explore the [kitchen] at the back, or head [back] to the signpost? ")

def signpost():
    global kitchen_return 
    kitchen_return = False
    if signpost_visited == False:
        print("---------------------------------------------------------")
        print("You continue up the path, the music gets louder")
        print("The path leads to a clearing in the trees, you can make out the shape of buildings in the dark")
        print("you appear to be in some sort of summer camp, singing can now be heard accompanying the music")
        print("The music and singing seems to be coming from a church you can see up the way")
        print("In front of you is a signpost with different destinations on it")
        print("---------------------------------------------------------")
    else:
        global church_quiet
        church_quiet = True
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
    #RESETTING VARIABLES
    global signpost_visited
    signpost_visited = False
    global church_quiet
    church_quiet = False
    global soup_eaten
    soup_eaten = 0
    global note_picked
    note_picked = 0
    global box_open
    box_open = False
    global inventory
    inventory = []
    if os.path.isfile("note.txt"):
        os.remove("note.txt")
    #Opening Text
    print("---------------------------------------------------------")
    print("It's almost midnight, you are driving on a long empty road")
    print("you are driving to a friends wedding, and decided to take a shortcut")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("your car is in need of repairs if you are to make it in time for the wedding")
    print("It's quiet, but you think you can hear music coming from somewhere")
    print("---------------------------------------------------------")
    choice = input("Do you [wait]? walk up the [road] on foot? or explore the [woods]? ")
    while True:
        if choice == "wait":
            car_wait()
        elif choice == "road":
            road()
        elif choice == "woods":
            wood_death()
        else:
            print("Invalid choice.")
            choice = input("Do you [wait]? walk up the [road] on foot? or explore the [woods]? ")

def game_start():
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

game_start()