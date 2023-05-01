import typer
import sys
import time

def typewriter_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')  # add newline after typewriter effect

# Example usage:
typewriter_text("Hello and welcome to the game, prepare to be spooked")