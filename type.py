import sys
import time
import select


# def type(text):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.025)
#     print('')  # add newline after typewriter effect



def type(text):
    for char in text:
        if select.select([sys.stdin,],[],[],0.0)[0]:
            sys.stdout.write(text)
            sys.stdout.flush()
            sys.stdin.readline()  # read the input to clear the buffer
            return
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
    print('')

type("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
type("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
type("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
type("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")
type("LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL")

print("lol")