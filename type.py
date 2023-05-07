import sys
import time

def typewriter_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
    print('')  # add newline after typewriter effect

typewriter_text("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
print("lol")