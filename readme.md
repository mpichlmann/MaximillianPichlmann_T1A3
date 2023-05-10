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

Van Rossum, G., Warsaw, B. and Coghlan, N. (2001). PEP 8 - Style Guide for Python Code. [online] Python.org. Available at: https://peps.python.org/pep-0008/ [Accessed 10 May 2023].

Throughout the code I have adhered to the guidelines outlined by Guido et al in PEP 8. Lines of code do not exceed 79 characters in length, function and variable names do not contain unnecessary capitals and adequate white space is given where required. 

It is stated in PEP 8: "A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.", and as such I have endeavoured to maintain consistent styling in regard to the use of quotations and naming conventions within this project as best as possible. 
‌

## Code Styling

## List of Features
### Freely Explore 

### Inventory System

### Solveable Puzzle

### Main Menu & Game Over Screen

## Implementation Plan


## Help Documentation
### System Requirements 
### Installation Instructions
I have tried my best to cater to a range of devices and setups by creating three different bash scripts to choose from. Depending on if you are running a linux terminal or a mac terminal you can choose to run either LinuxGame.sh by entering ./LinuxGame.sh or ./MacGame.sh respectively. 

These scripts will first install some libraries using either sudo apt-get for linux or brew for mac. These scripts are the way the game is intended to be played as the libraries are required for pygame mixer to play music properly during the game. After installing the necessary libraries they will then install the necessary dependencies for the game by using pip3 to read the requirements.txt file. 

If for whatever reason these bash scripts do not work, you can simply run the NoSoundGame script by entering ./NoSoundGame.sh in your terminal. This script will simply install the dependencies and forgo installing the libraries needed for music. The game will run fine but will display an 'error' message where music would normally be playing, everything else however still works fine.  
