# README

## (R3) Attributions
### Music:
#### Main Menu / Game Start Screen Music:
'The Invitation' by Blood Lord
#### Gameplay Music:
'Crystal Lake Camp Map' from Friday the 13th (NES)
#### Rescue Ending Music: 
'Celebrate [8 Bit Tribute to Kool & The Gang]' by 8 Bit Universe
#### Incantation Ending Music: 
'Boss' from Plok! (SNES)

## (R4) Source Control Repository (GitHub) 
https://github.com/mpichlmann/MaximillianPichlmann_T1A3

## (R5) Code Styling
PEP 8 - Style Guide for Python Code



Throughout the code I have adhered to the guidelines outlined by Guido et al in PEP 8. Lines of code do not exceed 79 characters in length, function and variable names do not contain unnecessary capitals and adequate white space is given where required. 

It is stated in PEP 8: "A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.", and as such I have endeavoured to maintain consistent styling within this project as best as possible.

Van Rossum, G., Warsaw, B. and Coghlan, N. (2001). *PEP 8 - Style Guide for Python Code*. [online] Python.org. Available at: https://peps.python.org/pep-0008/ [Accessed 10 May 2023].
‌
## Features
### Choose your own path!
The game features the ability to read different user inputs and allow the user to decide which path they would like to take to proceed... or perish...

### Freely explore!
the game features a partial open world where the player can go back and forth between locations at their own whim when they choose.

### Multiple Endings! 
There are multiple ways the game can end depending on what the player does throughout their playthrough, adding replay ability to the game. The game comes with a game start, game over, and game complete screen allowing the player to try another playthrough without ever having to close the app. 

### Solve Puzzles! 
The game features solvable puzzles for the player to overcome as well clues as to how to solve them. At certain stages the user may have to interact with items in the game, add items to their inventory, and return to locations with newfound information and items. 

### Music and Colour!
The game utilises audio and visual python packages to create a spooky and haunting atmospheric experience for the player.

### A Compelling mystery!
Throughout the game the player has the opportunity to uncover interesting information about the world, the characters, and the story.

## Implementation Plan



## Help Documentation

### Installation Instructions
I have tried my best to cater to a range of devices and setups by creating three different bash scripts to choose from. Depending on if you are running a linux terminal or a mac terminal you can choose to run either LinuxGame.sh by entering ./LinuxGame.sh or ./MacGame.sh respectively. 

These scripts will first install some libraries using either sudo apt-get for linux or brew for mac. These scripts are the way the game is intended to be played as the libraries are required for pygame mixer to play music properly during the game. After installing the necessary libraries they will then install the necessary dependencies for the game by using pip3 to read the requirements.txt file. 

If for whatever reason these bash scripts do not work, you can simply run the NoSoundGame script by entering ./NoSoundGame.sh in your terminal. This script will simply install the dependencies and forgo installing the libraries needed for music. The game will run fine but will display an 'error' message where music would normally be playing, everything else however still works fine.

### Dependencies
The game makes use of a few python packages, which will need to be installed along with their respective dependencies. A list of dependencies can be found in the requirements.txt file included, but I will also leave them here for convenience: 

- certifi==2023.5.7
- charset-normalizer==3.1.0
- click==8.1.3
- colorama==0.4.6
- colored==1.4.4
- docopt==0.6.2
- idna==3.4
- markdown-it-py==2.2.0
- mdurl==0.1.2
- pipreqs==0.4.13
- pycolour==1.0.3
- pygame==2.4.0
- Pygments==2.15.1
- requests==2.30.0
rich==13.3.5
shellingham==1.5.0.post1
typer==0.8.0
urllib3==2.0.2
yarg==0.1.9

### System Requirements 
All the game requires to the run is modest hardware that any modern PC from the past 10 years would surely have. There is no need for a high powered CPU or GPU, large amounts of RAM or anything of that nature. To run the game users will need an operating system that supports the use of a terminal/command line, such as Linux or Mac. If you are running Windows it is recommended to use an Ubuntu terminal through WSL. 
