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