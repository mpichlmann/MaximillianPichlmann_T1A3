# Imports
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from colored import fg, attr
# Error handling for music - if the music does not work,
# the game will still run, but will display an error message.
# If the music DOES work, then no error message will be displayed,
# and the game will run as intended, with music.
try:
    from pygame import mixer
    mixer.init()
except:
    print("Error Loading Music")
# End of imports

# Death screen
def game_over():
    # Music
    try:
        mixer.music.load('death.mp3')
        mixer.music.play(loops=-1)
    except:
        print("Error Loading Music")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("-------------------" + fg('red') + "YOU DIED: GAME OVER" + 
          attr('reset') + "-------------------")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    play_again()

# Play again prompt    
def play_again():
    while True:
        # Error handling input - if the user enters one of the options 
        # presented the corresponding function will be called. If the user 
        # fails to enter any of the options, an error message will be 
        # displayed and the user will be prompted to enter an input again. 
        # This process will be present for all functions in the game and 
        # will repeat until the user enters an approved input option. 
        move = input("Would you like to " + fg('yellow') + "[play]" + 
                     attr('reset') + " again? or do you want to " + 
                     fg('yellow') + "[quit]" + attr('reset') + " playing? ")
        if move == "play":
            starting_room()
        elif move == "quit":
            print("Thanks for playing!")
            sys.exit()
        else: 
            print("Invalid Choice")
            

# Game win screen
def game_complete():
    # Music
    try:
        mixer.music.load('win.mp3')
        mixer.music.play(loops=-1)
    except:
        print("Error Loading Music")
    print("-------------------------------------------------------------")
    print("You rescue the mechanic preventing her from becoming a demon!")
    print("The two of you walk back to your car, where she helps fix it.")
    print("You give her a ride to a local police station where you both ")
    print("share your story. After the freaky events of the night you   ")
    print("get back out on the road, and make it to your friends wedding")
    print("-------------------------------------------------------------")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("------------------" + fg('green') + "YOU WIN: GAME COMPLETE" + 
          attr('reset') + "--------------------")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ")
    play_again()

# Incantation ending
def incantation_ending():
    # Music
    try:
        mixer.music.load('demon.mp3')
        mixer.music.play(loops=-1)
    except:
        print("Error Loading Music")
    print("-------------------------------------------------------------")
    print("You recite the incantation that you found in the dorms")
    print("The walls shake, and fire bursts from the ground")
    print("You feel a great hunger within you, and rage fills your mind")
    print("You transform into THE DARK ONE, ready to unleash EVIL ")
    print("-------------------------------------------------------------")
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("------------------" + fg('red') + "YOU WIN: GAME COMPLETE" + 
          attr('reset') + "--------------------")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ ")
    play_again()

#Inside the church
global incantation
global soup_eaten
def inside_church():
    print("---------------------------------------------------------")
    print("you enter the church, it's cold and the smell of"
          " sulfur is noticeable")
    print("you see a woman in a mechanics uniform tied to"
          " an upside down crowss")
    print("all around her are figures in robes lying motionless")
    print("'Please help me!' the woman screams 'These crazy cultists"
          " kidnapped me'")
    print("they drank something and said if I stay here on this cross"
          " all night I'll turn into a demon'")
    print("'I just want to get out of here and go back to my job"
          " fixing cars as a mechanic!!'")
    print("you think to yourself, 'wow this has worked out perfectly'")
    print("---------------------------------------------------------") 
    while True:
        if incantation == True and soup_eaten > 0:
            move = input("do you " + fg('green') + "[rescue]" + 
                         attr('reset') + " the mechanic, recite the evil " + 
                         fg('red') + "[incantation]" + attr('reset') + 
                         ", or for some unimaginable reason head " + 
                         fg('yellow') + "[back]" + attr('reset') + 
                         " to the signpost? ")
        else: 
            move = input("do you " + fg('green') + "[rescue]" + 
                         attr('reset') + " the mechanic, or for some"
                         " unimaginable reason head " + fg('yellow') + 
                         "[back]" + attr('reset') + " to the signpost? ")
        if move == 'rescue':
            game_complete()
        elif move == 'incantation' and incantation == True \
            and soup_eaten > 0:
            incantation_ending()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")

#Inside the box
def inside_box():
    print("---------------------------------------------------------")
    print("The box opens to reveal its contents")
    print("Inside is a golden key with a cross on it")
    print("You take the key")
    print("---------------------------------------------------------")
    inventory.append("key")
    while True: 
        move = input("do you inspect the " + fg('yellow') + "[photo]" +
                      attr('reset') + " or head " + fg('yellow') + 
                      "[back]" + attr('reset') + "? ")
        if move == 'back':
            manor_first()
        elif move == 'photo':
            photo()
        else:
            print("Invalid Choice")
            

#Box puzzle
def box():
    global box_open
    print("---------------------------------------------------------")
    print("The box is made of fine wood and trimmed in gold")
    print("opening it proves challenging as it seems to be locked")
    print("you notice that the box is adorned with circular pieces of stone")
    print("each stone contains a symbol, and there are 9 stones in total")
    print("upon touching one you realise that the "
          "symbols are in fact buttons that can be pressed")
    print("---------------------------------------------------------")
    correct_sequence = ["sword", "pig", "apple"]
    current_sequence = []
    while True:
        move = input("do you press one of symbols " + fg('yellow') + 
                     "[pig][bird][bear][baby][wheat][apple][sword]"
                     "[sheep][snake]" + attr('reset') + " \nor head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        if move == 'back':
            manor_first()
        elif move in ["pig", "bird", "bear", "baby", "wheat", 
                      "apple", "sword", "sheep", "snake"]:
            if move == correct_sequence[len(current_sequence)]:
                current_sequence.append(move)
                # Check if the user entered the complete correct sequence
                if current_sequence == correct_sequence or\
                    set(current_sequence) == set(correct_sequence):
                    box_open = True
                    inside_box()
                elif move == correct_sequence[len(current_sequence)-1]\
                      or move == correct_sequence[0]:
                    print("----------------------------------"
                          "-----------------------")
                    print("You hear a satisfying click")
                    print("-------------------------------"
                          "--------------------------")  
                else:
                    print("------------------------------"
                          "---------------------------")
                    print("You hear a 'thunk' noise that doesn't sound right")
                    if os.path.isfile("note.txt"):
                        print("maybe that " + fg('yellow') + "[note]" + 
                              attr('reset') + " you found earlier might help")
                    print("----------------------------------"
                          "-----------------------")
                    current_sequence = []                  
            else:
                print("-------------------------------"
                      "--------------------------")
                print("You hear a 'thunk' noise that "
                      "doesn't sound quite right")
                if os.path.isfile("note.txt"):
                    print("maybe that " + fg('yellow') + "[note]" + 
                          attr('reset') + " you found earlier might help")
                print("---------------------------------"
                      "------------------------")
                current_sequence = []  
        elif move == 'note':
            print("---------------------------------------------------------")
            with open('note.txt', 'r') as file:
                note_contents = file.read()
                print(note_contents)
            print("---------------------------------------------------------")
        else:
            print("Invalid Choice")

#Inspecting the photo
def photo():
    print("---------------------------------------------------------")
    print("the photo is a picture of a young boy standing "
          "next to an older gaunt looking man")
    print("The pair is standing in front of a church, the boy looks sad")
    print("---------------------------------------------------------")
    while True: 
        move = input("do you look at the " + fg('yellow') + "[photo]" + 
                     attr('reset') + " again, inspect the " + fg('yellow') + 
                     "[box]" + attr('reset') + ", or head " + fg('yellow') + 
                     "[back]" + attr('reset') + "? ")
        if move == 'photo':
            photo()
        elif move == 'box' and box_open == False:
            box()
        elif move == 'box' and box_open == True:
            print("---------------------------------------------------------")
            print("You return to the box, proud of how you "
                  "so brilliantly conquered it's puzzle")
            print("---------------------------------------------------------")
            move = input("do you look at the " + fg('yellow') + "[photo]" +
                          attr('reset') + ", or head " + fg('yellow') + 
                          "[back]" + attr('reset') + "? ")
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            
#Second floor of the manor
def manor_second():
    global box_open
    print("---------------------------------------------------------")
    print("You head up the stairs into a small room")
    print("inside the room is a single bed, an empty bookshelf"
          " and a bedside table with a photo on it")
    print("opposite the bed is a writing desk up against the wall")
    print("on the writing desk is what looks like a "
          "decorative box with several symbols on it")
    print("---------------------------------------------------------")
    while True:
        move = input("do you inspect the " + fg('yellow') + "[box]" + 
                     attr('reset') + ", look at the " + fg('yellow') + 
                     "[photo]" + attr('reset') + ", or head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        if move == 'photo':
            photo()
        elif move == 'box' and box_open == False:
            box()
        elif move == 'box' and box_open == True:
            print("---------------------------------------------------------")
            print("You return to the box, proud of how you so "
                  "brilliantly conquered it's puzzle")
            print("---------------------------------------------------------")
            move = input("do you look at the " + fg('yellow') + "[photo]" + 
                         attr('reset') + ", or head " + fg('yellow') + 
                         "[back]" + attr('reset') + "? ")
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
        
# Manor kitchen
def manor_kitchen():
    print("---------------------------------------------------------")
    print("You enter the kitchen, it's remarkably tidy")
    print("The shelves are all empty, except for one "
          "loan plate and a single glass")
    print("You think to yourself that whoever lives "
          "here must enjoy their solitude")
    print("---------------------------------------------------------")
    while True:
        move = input("You might as well head " + fg('yellow') + 
                     "[back]" + attr('reset') + " ")
        if move == 'back':
            manor_first()
        else: 
            print("Invalid Choice")
            
# Inspecting the painting
def painting():
    print("---------------------------------------------------------")
    print("The painting seems to contain a muscular figure front and center.")
    print("The figure's skin is pale, but covered in "
          "patches of thick dark hair,")
    print("the face is scratched out, making it indistinguishable.")
    print("The figure stands in front of flames and dark clouds.")
    print("You don't like the painting very much...")
    print("---------------------------------------------------------")
    while True:
        move = input("do you inspect the " + fg('yellow') + "[book]" + 
                     attr('reset') + " or head " + fg('yellow') + 
                     "[back]" + attr('reset') + "? ")
        if move == 'book':
            book()
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            
# Inspecting the book and collecting a note clue
def book():
    global note_picked
    if note_picked > 0:
        print("---------------------------------------------------------")
        print("You open the book but can't make any sense of it")
        print("The writing is in some language you've never seen before")
        print("---------------------------------------------------------")
        move = input("do you inspect the " + fg('yellow') + "[painting]" + 
                     attr('reset') + ", read the " + fg('yellow') + 
                     "[note]" + attr('reset') + " you found, or head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        while True:
            if move == 'painting':
                painting()
            elif move == 'back':
                manor_first()
            elif move =='note':
                print("--------------------------------"
                      "-------------------------")
                with open('note.txt', 'r') as file:
                    note_contents = file.read()
                    print(note_contents)
                    print("-------------------------------"
                          "--------------------------")
                move = input("do you inspect the " + fg('yellow') + 
                             "[painting]"+ attr('reset') + ", or head " + 
                             fg('yellow') +"[back]" + attr('reset') +" ")
            else: 
                print("Invalid Choice")
                move = input("do you inspect the " + fg('yellow') + 
                             "[painting]" + attr('reset') + ", read the " + 
                             fg('yellow') + "[note]" + attr('reset') + 
                             " you found, or head " + fg('yellow') + 
                             "[back]" + attr('reset') + "? ")
    elif note_picked == 0:
        print("---------------------------------------------------------")
        print("You open the book but can't make any sense of it")
        print("The writing is in some language you've never seen before")
        print("As you flick through the pages, a small note falls out")
        print("---------------------------------------------------------")
        with open('note.txt', 'w') as file:
            file.write("So it goes the parable of summoning, \nLet those "
                       "who know it's secrets hold these words. \n\nCut "
                       "down the non-believers. \nCast away the swine of "
                       "foolishness. \nPartake in the fruit of our lord."
                       " \n\nWith these words, "
                       "let what has fallen rise again")
        note_picked += 1
        move = input("do you inspect the " + fg('yellow') + "[painting]" + 
                     attr('reset') + ", read the " + fg('yellow') + 
                     "[note]" + attr('reset') + " you found, or head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        while True:
            if move == 'painting':
                painting()
            elif move == 'back':
                manor_first()
            elif move =='note':
                print("----------------------------------"
                      "-----------------------")
                with open('note.txt', 'r') as file:
                    note_contents = file.read()
                    print(note_contents)
                    print("--------------------------------"
                          "-------------------------")
                move = input("do you inspect the " + fg('yellow') + 
                             "[painting]"+ attr('reset') + 
                             ", or head " + fg('yellow') +"[back]" + 
                             attr('reset') +" ")
            else: 
                print("Invalid Choice")
                move = input("do you inspect the " + fg('yellow') + 
                             "[painting]" + attr('reset') + ", read the " + 
                             fg('yellow') + "[note]" + attr('reset') + 
                             " you found, or head " + fg('yellow') + 
                             "[back]" + attr('reset') + "? ")

# Entering the study
def study():
    global note_picked
    print("---------------------------------------------------------")
    print("You enter the study where you see a lone "
          "chair faced towards a painting")
    print("next to the chair is a small table, on top "
          "sits a leatherbound book")
    print("---------------------------------------------------------")
    while True:
        move = input("do you inspect the " + fg('yellow') + "[painting]" + 
                     attr('reset') + ", inspect the " + fg('yellow') + 
                     "[book]" + attr('reset') + " or head " + fg('yellow') + 
                     "[back]" + attr('reset') + "? ")
        if move == 'painting': 
            painting()
        elif move == 'book':
            book()
        elif move == 'back':
            manor_first()
        else:
            print("Invalid Choice")
            
# The first floor of the manor
def manor_first():
    print("---------------------------------------------------------")
    print("You're standing in the vestibule of the house, you see "
          "a study to the left, and some stairs to the right")
    print("In front of you is a small kitchen that seems recently tidied")
    print("---------------------------------------------------------")
    while True:
        move = input("do you investigate the " + fg('yellow') + "[study]" + 
                     attr('reset') + ", the " + fg('yellow') + "[kitchen]" + 
                     attr('reset') + ", head up the " + fg('yellow') + 
                     "[stairs]" + attr('reset') + " or head " + 
                     fg('yellow') + "[back]" + attr('reset') + 
                     " to the signpost? ")
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
            
# Outside the manor
def manor():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    church_quiet = True
    print("---------------------------------------------------------")
    print("you follow the path to until you reach a double story house")
    print("The house resembles an old victorian architectural style")
    print("It's small, definitely not a manor by any means, you "
          "wonder why it would be referred to as such")
    print("you notice the door is wide open")
    print("---------------------------------------------------------")
    while True:
        move = input("do you " + fg('yellow') + "[enter]" + attr('reset') + 
                     " the house or head " + fg('yellow') + "[back]" + 
                     attr('reset') + " to the signpost? ")
        if move == 'enter':
            manor_first()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            
# Arriving at the church
def church():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    if church_quiet == False:
        print("---------------------------------------------------------")
        print("You follow the direction the sign pointed "
              "until you come across a church")
        print("inside you can hear music and singing, although now that "
              "you're closer it sounds more like chanting")
        print("you think maybe someone inside can help you fix your car")
        print("---------------------------------------------------------")     
    else:
        print("---------------------------------------------------------")
        print("You follow the direction the sign pointed "
              "until you come across a church")
        print("you can't hear anything now, but you're sure this is "
              "where the music was coming from")
        print("you think maybe someone inside can help you fix your car")
        print("---------------------------------------------------------")
    move = input("do you " + fg('yellow') + "[knock]" + attr('reset') + 
                 " at the door, simply " + fg('yellow') + "[open]" + 
                 attr('reset') + " the door and let yourself in, do you " + 
                 fg('yellow') + "[look]" + attr('reset') + 
                 " in through a window or head " + fg('yellow') + 
                 "[back]" + attr('reset') + " to the signpost? ")
    while True:
        if move == 'knock' and church_quiet == False:
            print("---------------------------------------------------------")
            print("the music and chanting stops, you hear boots "
                  "marching towards the door")
            print("the door swings open, you are met by a group "
                  "of people donned in hoods")
            print("'REMOVE THE INTERLOPER' a voice shouts")
            print("the group of hooded figures reveal the knives "
                  "under their cloaks and launch at you")
            game_over()
        elif move == 'knock' and church_quiet == True:
            print("---------------------------------------------------------")
            print("you hear a high pitched voice scream out for help")
            print("---------------------------------------------------------")
            move = input("do you " + fg('yellow') + "[knock]" + 
                         attr('reset') + " at the door, simply " + 
                         fg('yellow') + "[open]" + attr('reset') + 
                         " the door and let yourself in, " + fg('yellow') + 
                         "[look]" + attr('reset') + 
                         " through a window or head " + fg('yellow') + 
                         "[back]" + attr('reset') + " to the signpost? ")
        elif move == 'open':
            if "key" in inventory:
                inside_church()
            else:
                print("---------------------------------"
                      "------------------------")
                print("You try to open the door but can't, it's locked")
                print("--------------------------------"
                      "-------------------------")
                move = input("do you " + fg('yellow') + "[knock]" + 
                             attr('reset') + " at the door, simply " + 
                             fg('yellow') + "[open]" + attr('reset') + 
                             " the door and let yourself in, do you " + 
                             fg('yellow') + "[look]" + attr('reset') + 
                             " in through a window or head " + fg('yellow') + 
                             "[back]" + attr('reset') + " to the signpost? ")  
        elif move == 'look' and church_quiet == False:
            print("---------------------------------------------------------")
            print("You peer through the window and see a group of hooded"
                  " figures in black robes standing in a circle")
            print("In the center of them you see a woman in a mechanics "
                  "uniform strapped to an upside down cross")
            print("standing opposite the woman is a figure in a red robe,"
                  " holding a tome in one hand, and an ornate "
                  "knife in the other")
            print("You think to yourself 'Maybe that woman in the mechanics "
                  "uniform can help me fix my car!'")
            print("you also think she might be in a bit of trouble and "
                  "be in need of some rescuing")
            print("---------------------------------------------------------")
            move = input("do you " + fg('yellow') + "[knock]" + 
                         attr('reset') + " at the door, simply " + 
                         fg('yellow') + "[open]" + attr('reset') + 
                         " the door and let yourself in or head " + 
                         fg('yellow') + "[back]" + attr('reset') + 
                         " to the signpost? ")
        elif move == 'look' and church_quiet == True:
            print("---------------------------------------------------------")
            print("You peer through the window and see a group of hooded "
                  "figures lying on the ground in a circle")
            print("In the center of all the figures you see a woman in a "
                  "mechanics uniform strapped to an upside down cross")
            print("You think to yourself 'Maybe that woman in the mechanics"
                  " uniform can help me fix my car!'")
            print("you also think she might be in a bit of trouble"
                  " and be in need of some rescuing")
            print("---------------------------------------------------------")
            move = input("do you " + fg('yellow') + "[knock]" + 
                         attr('reset') + " at the door, simply " + 
                         fg('yellow') + "[open]" + attr('reset') + 
                         " the door and let yourself in or head " + 
                         fg('yellow') + "[back]" + attr('reset') + 
                         " to the signpost? ")
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")
            move = input("do you " + fg('yellow') + "[knock]" + 
                         attr('reset') + " at the door, simply " + 
                         fg('yellow') + "[open]" + attr('reset') + 
                         " the door and let yourself in, do you " + 
                         fg('yellow') + "[look]" + attr('reset') + 
                         " in through a window or head " + fg('yellow') + 
                         "[back]" + attr('reset') + " to the signpost? ")

# The mess hall kitchen
def kitchen():
    global kitchen_return 
    kitchen_return = True
    print("---------------------------------------------------------")
    print("you enter the kitchen")
    print("---------------------------------------------------------")
    while True:
        move = input("you can't see any point to being in the kitchen and "
                     "think you should " + fg('yellow') + 
                     "[back]" + attr('reset') + " ")
        if move == 'back': 
            mess_hall()
        else: 
            print("Invalid Choice")
            
# Arriving at / returning to the mess hall
def mess_hall():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    church_quiet = True
    global soup_eaten
    if kitchen_return == False and soup_eaten == 0:
        print("---------------------------------------------------------")
        print("You follow the path until you reach a large wooden building")
        print("Entering the building you find a row of dining tables,"
              " at the back you see a door leading to a kitchen")
        print("Amongst all the empty dishes you see a bowl of soup "
              "it seems someone has left out")
        print("---------------------------------------------------------")
        move = input("Do you " + fg('yellow') + "[eat]" + attr('reset') + 
                     " the bowl of soup? explore the " + fg('yellow') + 
                     "[kitchen]" + attr('reset') + " at the back, or head " + 
                     fg('yellow') + "[back]" + attr('reset') + 
                     " to the signpost? ")
    elif kitchen_return == False and soup_eaten > 0:
        print("---------------------------------------------------------")
        print("You follow the path until you reach a large wooden building")
        print("Entering the building you find a row of dining tables,"
              " at the back you see a door leading to a kitchen")
        print("---------------------------------------------------------")
        move = input("explore the " + fg('yellow') + "[kitchen]" +
                      attr('reset') + " at the back, or head " + 
                      fg('yellow') + "[back]" + attr('reset') + 
                      " to the signpost? ")
    elif kitchen_return == True and soup_eaten == 0:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("Do you " + fg('yellow') + "[eat]" + attr('reset') +
                      " the bowl of soup? explore the " + fg('yellow') +
                        "[kitchen]" + attr('reset') + 
                        " at the back, or head " + fg('yellow') + 
                        "[back]" + attr('reset') + " to the signpost? ")
    else:
        print("---------------------------------------------------------")
        print("you head back to the dining area")
        print("---------------------------------------------------------")
        move = input("explore the " + fg('yellow') + "[kitchen]" + 
                     attr('reset') + " at the back, or head " + 
                     fg('yellow') + "[back]" + attr('reset') + 
                     " to the signpost? ")
    while True:
        if move == 'eat':
            if soup_eaten == 0:
                soup_eaten += 1
                print("--------------------------------"
                      "-------------------------")
                print("You eat the soup, it tastes funny, ")
                print("------------------------------"
                      "---------------------------")
            else: 
                print("Invalid Choice")
            move = input("do you explore the " + fg('yellow') + 
                         "[kitchen]" + attr('reset') + " at the back"
                         ", or head " + fg('yellow') + "[back]" + 
                         attr('reset') + " to the signpost? ")
        elif move == 'kitchen':
            kitchen()
        elif move == 'back':
            signpost()
        else: 
            print("Invalid Choice")
            if soup_eaten > 0:
                move = input("Do you explore the " + fg('yellow') + 
                             "[kitchen]" + attr('reset') + 
                             " at the back, or head " + fg('yellow') + 
                             "[back]" + attr('reset') + " to the signpost? ")
            else:
                move = input("Do you " + fg('yellow') + "[eat]" + 
                             attr('reset') + " the bowl of soup? explore the "
                               + fg('yellow') + "[kitchen]" + attr('reset') + 
                               " at the back, or head " + fg('yellow') + 
                               "[back]" + attr('reset') + 
                               " to the signpost? ")

# Dorm 1
def dorm1():
    global dorms_visited
    dorms_visited = True
    global journal_read
    print("---------------------------------------------------------")
    print("You enter the first dorm, and see two bunk "
          "beds on either side of the room")
    print("A dresser desk sits up against the wall in between the bunk")
    print("On one of the beds you spot a journal")
    print("---------------------------------------------------------")
    while True:
        move = input("do you inspect the " + fg('yellow') + "[dresser]" + 
                     attr('reset') + ", read the " + fg('yellow') + 
                     "[journal]" + attr('reset') + ", or head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        if move == 'back':
            dorms()
        elif move == 'dresser':
            if journal_read == True and 'iron_key' not in inventory:
                print("------------------------------"
                      "---------------------------")
                print("Inside the dresser you see robes "
                      "and dirty work clothes")
                print("You find a small iron key taped to"
                      " the top of the dresser")
                inventory.append('iron_key')
                print("-----------------------------"
                      "----------------------------")
            else:
                print("-----------------------------"
                      "----------------------------")
                print("Inside the dresser you see robes "
                      "and dirty work clothes")
                print("-----------------------------"
                      "----------------------------")
        elif move == 'journal':
            print("---------------------------------------------------------")
            print("The Journal seems to have several entries, dating back "
                  "what seems like a few months")
            print("The most recent entry reads:")
            print("")
            print("Soon the big night will be upon us... what all of our "
                  "devotion has been leading to...")
            print("I hope everything goes well, but I have to confess I'm a"
                  " little concerned about one of my fellow followers")
            print("He started out joyful in the work we were doing, but "
                  "gradually he seems to have changed")
            print("like his focus is elsewhere...")
            print("---------------------------------------------------------")
        else:
            print("Invalid Choice")

# Dorm 2
def dorm2():
    global dorms_visited
    dorms_visited = True
    global journal_read
    print("---------------------------------------------------------")
    print("You enter the second dorm, and see a bunk bed on the right, "
          "and two writing desks on the left")
    print("A dresser desk sits up against the wall in between the "
          "bunk bed and the writing desks")
    print("On top of one of the desks looks to be a journal of some sort")
    print("---------------------------------------------------------")
    while True:
        move = input("do you search the " + fg('yellow') + "[dresser]" + 
                     attr('reset') + ", read the " + fg('yellow') + 
                     "[journal]" + attr('reset') + " or head " + 
                     fg('yellow') + "[back]" + attr('reset') + "? ")
        if move == 'back':
            dorms()
        elif move == 'dresser':
            print("---------------------------------------------------------")
            print("Rummaging through the dresser you only find robes, "
                  "some dirty work clothes and a photo")
            print("The photo is of a group of young men and women, "
                  "they're all smiling, all except one")
            print("---------------------------------------------------------")
        elif move == 'journal':
            journal_read = True
            print("---------------------------------------------------------")
            print("The Journal seems to have several entries, dating"
                  " back what seems like a few months")
            print("The most recent entry, dated today, reads:")
            print("")
            print("This is it, all of our hard work has led to this "
                  "moment. With the completion")
            print("of the ritual, the dark one will be summoned and "
                  "this world will be done with!")
            print("Finally, I can make this confession without fear "
                  "of our leader's punishment.")
            print("I do not wish to summon the dark one..."
                  "I wish to BECOME the dark one!")
            print("My research of the dark scriptues has led me "
                  "to an evil incantation.")
            print("One needs only to consume our unholy soup and "
                  "utter the phrase in a holy place") 
            print("and a transformation will occur in the one who speaks it!")
            print("")
            print("I've had to be so careful so as to not get caught...")
            print("I wrote the phrase down so I don't forget it, hid it in my"
                  " lockbox, stashed it under the bed in the dorm next-door")
            print("and I even hid the key to the lockbox in the OTHER dorm,"
                  " taped to the top of the inside of the dresser")
            print("but now none of it matters... they're calling us to the"
                  " chapel now, this is my last entry")
            print("---------------------------------------------------------")
        else:
            print("Invalid Choice")
# Dorm 3
def dorm3():
    global dorms_visited
    dorms_visited = True
    global journal_read
    global incantation
    print("---------------------------------------------------------")
    print("You enter the third dorm, and see a bunk bed on the "
          "right, and a single writing desk on the left")
    print("A dresser desk sits up against the wall with some photos"
          " on top of it")
    print("Next to the photos, a journal can be found")
    print("---------------------------------------------------------")
    while True:
        if journal_read == True:
            move = input("do you check under the " + fg('yellow') + 
                         "[bed]" + attr('reset') + ", search the " + 
                         fg('yellow') + "[dresser]" + attr('reset') + 
                         ", read the " + fg('yellow') + "[journal]" + 
                         attr('reset') + ", or head " + fg('yellow') + 
                         "[back]" + attr('reset') + "? ")
        else: 
            move = input("do you search the " + fg('yellow') + "[dresser]" + 
                         attr('reset') + ", read the " + fg('yellow') + 
                         "[journal]" + attr('reset') + " or head " + 
                         fg('yellow') + "[back]" + attr('reset') + "? ")
        if move == 'back':
            dorms()
        elif move == 'journal':
            print("---------------------------------------------------------")
            print("The Journal seems to have several "
                  "entries, dating back what seems like a few months")
            print("The most recent entry reads:")
            print("")
            print("Man... I never should have joined "
                  "this stupid 'spiritual movement'")
            print("I should have listened to my "
                  "mum and continued my IT Diploma")
            print("All these guy talk about is "
                  "summoning the dark lord")
            print("and bringing about the end of "
                  "days...Like... I just wanted")
            print("to stop staring at screens and "
                  "get some exercise...I think")
            print("I may have let this whole thing get a bit out of hand...")
            print("---------------------------------------------------------")
        elif move == 'dresser':
            print("---------------------------------------------------------")
            print("Inside the dresser you see robes and dirty work clothes")
            print("stashed amongst all the clothes you"
                  " find a few sci-fi novels")
            print("---------------------------------------------------------")
        elif move == 'bed' and journal_read == True:
            if 'iron_key' in inventory:
                incantation = True 
                print("-------------------------------"
                      "--------------------------")
                print("You search under the bed and find a lockbox")
                print("Using the key you found, you open the "
                      "box to reveal a piece of parchment")
                print("It reads:")
                print("")
                print("Corpus meum offero")
                print("----------------------------"
                      "-----------------------------")
            else:
                print("-----------------------------"
                      "----------------------------")
                print("You search under the bed and find a "
                      "lockbox, but you can't open it")
                print("--------------------------------"
                      "-------------------------")
        else:
            print("Invalid Choice")

# Arriving at the row of dorms
def dorms():
    global signpost_visited
    signpost_visited = True
    global church_quiet
    church_quiet = True
    global dorms_visited
    if dorms_visited == True:
        print("---------------------------------------------------------")
        print("You stand in front of the row of dorms")
        print("Looking at each of their numbers, "
              "you wander what dark secrets,")
        print("the inhabitants may be keeping")
        print("---------------------------------------------------------")
    else:
        print("---------------------------------------------------------")
        print("You arrive at what looks like a row of numbered dorms")
        print("Each dorm has two steps leading up to it's front door")
        print("The wooden dorms seem worn and run down, "
              "they've definitely seen better days")
        print("---------------------------------------------------------")
    while True:
        move = input("do you enter dorm " + fg('yellow') + "[1]" + 
                     attr('reset') + " " + fg('yellow') + "[2]" + 
                     attr('reset') + " " + fg('yellow') + "[3]" + 
                     attr('reset') + " or head " + fg('yellow') + 
                     "[back]" + attr('reset') + " to the signpost? ")
        if move == '1':
            dorm1()
        elif move == '2':
            dorm2()
        elif move == '3':
            dorm3()
        elif move == 'back':
            signpost()
        else:
            print("Invalid Choice")

#Arriving at / returning to the signpost
def signpost():
    global kitchen_return 
    kitchen_return = False
    global church_quiet
    global dorms_visited
    dorms_visited = False      
    if signpost_visited == False:
        print("---------------------------------------------------------")
        print("You continue up the path, the music gets louder")
        print("The path leads to a clearing in the trees, you can make out "
              "the shape of buildings in the dark")
        print("you appear to be in some sort of summer camp, singing can now"
              " be heard accompanying the music")
        print("The music and singing seems to be coming from a church you "
              "can see up the way")
        print("In front of you is a signpost with different destinations "
              "on it")
        print("---------------------------------------------------------")
    else:
        church_quiet = True
        print("---------------------------------------------------------")
        print("you return to the signpost")
        print("you notice you can no longer hear the music or the singing"
              " that you did previously")
        print("---------------------------------------------------------")
    while True:
        move = input("The signpost reads: " + fg('yellow') + "[church]" + 
                     attr('reset') + ", " + fg('yellow') + "[manor]" + 
                     attr('reset') + ", " + fg('yellow') + "[dorms]" + 
                     attr('reset') + ", " + fg('yellow') + "[mess hall]" + 
                     attr('reset') + " ")
        if move == 'mess hall':
            mess_hall()
        elif move == 'church':
            church()
        elif move == 'manor':
            manor()
        elif move == 'dorms':
            dorms()
        else: 
            print("Invalid Choice")

# Arriving at the gate      
def gate():
    print("---------------------------------------------------------")
    print("you stack the boxes and climb the gate")
    print("now that you're on the other side of the gate you see a "
          "sleeping dog and a path leading up to the source of the music")
    print("---------------------------------------------------------")
    while True:
        move = input("do you " + fg('yellow') + "[pet]" + attr('reset') + 
                     " the dog or continue up the " + fg('yellow') + 
                     "[path]" + attr('reset') + "? ")
        if move == 'pet':
            print("---------------------------------------------------------")
            print("As you touch the dog, it wakes up and attacks you!")
            print("---------------------------------------------------------")
            game_over()
        elif move == 'path':
            signpost()
        else: 
            print("Invalid Choice")
            
# Walking up the road  
def road():
    print("---------------------------------------------------------")
    print("you walk up the road on foot, the music grows")
    print("you follow the music up the road until you arrive at a large "
          "gate, flanked by chainlink fence")
    print("you see a little cutout in the gate but not big enough "
          "to squeeze through")
    print("the music is coming from the other side of the gate, "
          "perhaps someone there knows how to fix a car?")
    print("you see a rusty lock on the gate, and some boxes next to the gate")
    print("---------------------------------------------------------")
    while True:
        move = input("do you want to " + fg('yellow') + "[smash]" + 
                     attr('reset') + " the lock with a rock? or " + 
                     fg('yellow') + "[climb]" + attr('reset') + 
                     " the fence with the boxes? ")
        if move == "smash":
            print("You strike the lock, and suddenly a vicious dog jumps"
                  " through the cutout and attacks you")
            game_over()
        elif move == 'climb':
            gate()
        else:
            print("Invalid Choice")
            
# Exploring the woods
def wood_death():
    print("---------------------------------------------------------")
    print("you wander into the woods")
    print("the music you heard before starts to grow")
    print("as you draw closer, you hear a click beneath your feet")
    print("you look down and see your foot caught on a wire")
    print("you've triggered a makeshift trap, nails fly at you "
          "from all directions, killing you")
    print("---------------------------------------------------------")
    game_over()

# Waiting in the car
def car_wait():
    wait_time = 0
    wait_messages = ["You wander what exactly it is you're waiting for...", 
                "You can't really think of anything that you're"
                " waiting for...",
                "You think someone finding you on this quiet road in the "
                "middle night is pretty unlikely, but still... you wait.",
                "resolute in your decision, you start to become more "
                "confident in your ability to wait",
                "You can do this, you can wait all night if it takes",
                "By sheer wait-power, you will will your car back to life "
                "you tell yourself",
                "You're nowhere near as determined as you initially thought"
                ", you can't do this any longer you tell yourself"]
    print("---------------------------------------------------------")
    print("you wait in the car, nothing happens")
    print("---------------------------------------------------------")
    move = input("Do you want to " + fg('yellow') + 
                     "[wait]" + attr('reset') + " some more, explore the " + 
                     fg('yellow') + "[woods]" + attr('reset') + 
                     " or walk up the " + fg('yellow') + "[road]" + 
                     attr('reset') + " on foot? ")
    while move == 'wait':
        if wait_time < len(wait_messages):
            print("---------------------------------------------------------")
            print(wait_messages[wait_time])
            print("---------------------------------------------------------")
            wait_time += 1
        else:
            print("---------------------------------------------------------")
            print("you die from the exhaustion of waiting for a "
                  "miracle, what a pitiful way to go")
            print("---------------------------------------------------------")
            game_over()
        move = input("Do you want to " + fg('yellow') + 
                     "[wait]" + attr('reset') + " some more, explore the " + 
                     fg('yellow') + "[woods]" + attr('reset') + 
                     " or walk up the " + fg('yellow') + "[road]" + 
                     attr('reset') + " on foot? ")
    if move == 'woods':
        wood_death()
    elif move == 'road':
        road()
    else: 
        print("Invalid Choice")
        car_wait()
        
def starting_room():
    # Resetting variables
    #
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
    global journal_read
    journal_read = False
    global incantation
    incantation = False
    if os.path.isfile("note.txt"):
        os.remove("note.txt")
    # Music
    try:
        mixer.music.load('game.mp3')
        mixer.music.play(loops=-1)
    except:
        print("Error Loading Music")
    # Opening Text
    print("---------------------------------------------------------")
    print("It's almost midnight, you are driving on a long empty road")
    print("you are driving to a friends wedding, "
          "and decided to take a shortcut")
    print("Trees surround you on either side of the road")
    print("Your engine whines and sputters, the car slows to a halt")
    print("your car is in need of repairs if you are to"
          " make it in time for the wedding")
    print("It's quiet, but you think you can hear "
          "music coming from somewhere")
    print("---------------------------------------------------------")
    
    while True:
        choice = input("Do you " + fg('yellow') + "[wait]" + attr('reset') + 
            "? walk up the " + fg('yellow') + "[road]" + attr('reset') + 
            " on foot? or explore the " + fg('yellow') + "[woods]"
              + attr('reset') + "? ")
        if choice == "wait":
            car_wait()
        elif choice == "road":
            road()
        elif choice == "woods":
            wood_death()
        else:
            print("Invalid choice.")
            
# Start screen of the game
def game_start():
    try:
        mixer.music.load('menu.mp3')
        mixer.music.play(loops=-1)
    except:
        print("Error Loading Music")
    print("---------------------------------------------------------")
    print("Welcome to 'Spooky Woods' an exploration horror puzzle game!")
    print("Your goal is to reach the end without dying and save the day!")
    print("Throughout the game you will be presented with choices in "
          + fg('yellow') + "[square]" + attr('reset') + " brackets")
    print("simply type your choice in lower-case to proceed, but be careful!")
    print("---------------------------------------------------------") 
    while True:
        # Error handling for getting user input.
        # If the user enters one of the options presented the corresponding,
        # function will be called. If the user fails to enter any of the 
        # options, an error message will be displayed and the user will be
        # prompted to enter an input again. This process will repeat for all
        # functions in the game and will repeat until the user enters an 
        # approved input option. 
        ready = input("Ready to " + fg('yellow') + "[play]" + attr('reset')
            + "? or " + fg('yellow') + "[quit]" + attr('reset') + " game? ")
        if ready == "play":
            starting_room()
        elif ready == "quit":
            sys.exit()
        else:
            print("Invalid Choice")

# Calls the game_start function to run the game         
game_start()