#Imports
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from colored import fg, attr
try:
    from pygame import mixer
    mixer.init()
except:
    print("Error Loading Music")

def signpost():
    global kitchen_return 
    kitchen_return = False
    
    global church_quiet
    
        
    if signpost_visited == False:
        print("---------------------------------------------------------")
        print("You continue up the path, the music gets louder")
        print("The path leads to a clearing in the trees, you can make out the shape of buildings in the dark")
        print("you appear to be in some sort of summer camp, singing can now be heard accompanying the music")
        print("The music and singing seems to be coming from a church you can see up the way")
        print("In front of you is a signpost with different destinations on it")
        print("---------------------------------------------------------")
    else:
        church_quiet = True
        print("---------------------------------------------------------")
        print("you return to the signpost")
        print("you notice you can no longer hear the music or the singing that you did previously")
        print("---------------------------------------------------------")
    move = input("The signpost reads: " + fg('yellow') + "[mess hall]" + attr('reset') + ", " + fg('yellow') + "[church]" + attr('reset') + ", " + fg('yellow') + "[manor]" + attr('reset') + ", ")
    while True:
        if move == 'mess hall':
            pass #mess_hall()
        elif move == 'church':
            pass #church()
        elif move == 'manor':
            pass #manor()
        else: 
            print("Invalid Choice")
            move = input("The signpost reads: " + fg('yellow') + "[mess hall]" + attr('reset') + ", " + fg('yellow') + "[church]" + attr('reset') + ", " + fg('yellow') + "[manor]" + attr('reset') + ", " + fg('yellow') + "[dorms]" + attr('reset') + " ")