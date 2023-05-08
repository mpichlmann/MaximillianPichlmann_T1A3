# README

## References

## GitHub 
https://github.com/mpichlmann/MaximillianPichlmann_T1A3

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
