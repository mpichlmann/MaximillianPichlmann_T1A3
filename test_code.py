# Imports - Including these imports in this test file so that the tests run smoothly
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from colored import fg, attr
# Error testing music - if the music does not work,
# the game will still run, but will display an error message.
# If the music DOES work, then no error message will be displayed,
# and the game will run as intended, with music.
try:
    from pygame import mixer
    mixer.init()
except:
    print("Error Loading Music")
# End of imports


#Adjusted the code from the main file to make it testable. After having passed the test, the corresponding returns for each input can be altered to suit their purpose in the main game. 
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
    ready = input("Ready to " + fg('yellow') + "[play]" + attr('reset')
        + "? or " + fg('yellow') + "[quit]" + attr('reset') + " game? ")
    if ready == "play":
        return "Playing Game"
    elif ready == "quit":
        return "System Exit"
    else:
        return "Invalid Choice"

signpost_visited = False    
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
            return "Mess Hall Selected"
        elif move == 'church':
            return "Church Selected"
        elif move == 'manor':
            return "Manor Selected"
        elif move == 'dorms':
            return "Dorms Selected"
        else: 
            return "Invalid Choice"