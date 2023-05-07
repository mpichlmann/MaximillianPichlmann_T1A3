import sys
import time

def typewriter_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print('')  # add newline after typewriter effect

# Example usage:
typewriter_text(" ( )(_))\ ) `  )   ))\   /(_)) (    (     ))\ )\())\())\  (    )\))(   ")
typewriter_text("(_(_()|()/( /(/(  /((_) (_))   )\   )\  '/((_|_))((_)((_) )\ )((_))\   ")
typewriter_text("|_   _|)(_)|(_)_\(_))   / __| ((_)_((_))(_)) | |_| |(_|_)_(_/( (()(_)  ")
typewriter_text("  | | | || | '_ \) -_)  \__ \/ _ \ '  \() -_)|  _| ' \| | ' \)) _` |   ")
typewriter_text("  |_|  \_, | .__/\___|  |___/\___/_|_|_|\___| \__|_||_|_|_||_|\__, |   ")
typewriter_text("       |__/|_|                                                |___/    ")


import time

def typer(text):
    if text == '':
        print()  # typer a newline character when the recursion ends
        return
    else:
        print(text[0], end='', flush=True)  # typer the first character in the text
        time.sleep(0.05)  # Wait for a short amount of time
        typer(text[1:])  # Call the typer() function recursively with the remaining text

with open('note.txt', 'r') as file:
    note_contents = file.read()
    print(note_contents)

with open('note.txt', 'w') as file:
    file.write("In great veneration of their master, \nthe people offered up their most prized possesions. \n\nThe old farmer, his finest crop. \nThe slight swineheard, his stoutest pig. \nThe beggarly grandam, her beloved babe. \n\nThe master saw these gifts and was pleased")


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
    move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \nor head [back]" )
    while True:
        if move == 'back':
            print("yo")
        elif move in ["pig", "bird", "bear", "baby", "wheat", "apple", "sword", "sheep", "snake"]:
            current_sequence.append(move)
            if current_sequence == correct_sequence:
                print("The box opens to reveal its contents")
                break
            elif len(current_sequence) == len(correct_sequence) and current_sequence != correct_sequence:
                print("The box doesn't seem to open. Maybe you pressed the wrong sequence of buttons?")
                current_sequence = []
            else:
                print("You pressed the", move, "button")
        else:
            print("Invalid Choice")
        move = input("do you press one of symbols [pig][bird][bear][baby][wheat][apple][sword][sheep][snake] \n or head [back] ")