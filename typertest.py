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
