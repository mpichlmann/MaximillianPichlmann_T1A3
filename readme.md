# README

## Video Presentation of Terminal Application
https://www.youtube.com/watch?v=YVkbj98YNZs

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
## (R6) Features
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

## (R7) Implementation Plan
https://trello.com/b/c63p91Cr/t1a3 - Link to my Trello implementation plan where all activity can be viewed

### Implementation Plan Overview
Throughout the development of the game I made use of Trello to track, assign, and prioritise different features and components of the game. Initially when I was still getting familiar with Trello, I only created a few basic cards. My first goal was to design the plot of the game, design the MVP (Minimum Viable Product), and to find suitable python packages that could be implemented into the MVP. I knew that as development and designing begun that certain decisions and directions would become obvious and so I didn't worry about having too much structure too early on. 

![First Image](https://i.imgur.com/VuJncGX.jpg)
*What my Trello Workspace looked like on Day 1*

As I had decided to develop a text based game my first task was to design the plot of the game. Before I could start building the game I needed to know how it starts, how it ends, and how the player gets from one to the other. I started out with some rough sketches and ideas which gradually transformed into a basic map of the world of the game, and how the player navigated it. 

![rough ideas](https://i.imgur.com/KBRzzYf.jpg)
![map of game](https://i.imgur.com/f9eIxnH.jpg)
!['flowchart' of game](https://i.imgur.com/8G9a3hv.jpg)

Once I had finished designing the plot of the game, I had to make a start on designing the game itself, i.e. how it will be coded. I had to plan out how to make use of functions, variables, loops, error testing and imported packages. At this point I was able to add a few more things to the Trello workspace, and plan out the days that each task would be completed. Previously I had created separate lists for each day I would complete a task, but as I got deeper into development I switched to instead keeping it simple and only using the three Trello lists of 'To Do, Doing, and Complete' with each card having a due date assigned to it. This way was easier, cleaner and made more sense. 

![Trello as of 6th of May](https://i.imgur.com/cYWH5Yq.jpg)
*what trello looked like before*
![home](https://i.imgur.com/kVSo0r7.jpg)
*what trello looked like after I adjusted how I used it*
![MVP Checklist](https://i.imgur.com/0rjX7C7.jpg)

I started on coding the MVP as well as researching what python packages I could use to add to my game. Initially I created a basic game where a player starts in one room, and can navigate to their choice of two other rooms. Once I had successfully achieved that I would know how to implement that same feature into the main game. By this point I had also decided on some python packages that I could add to the game to create some atmosphere. Although ASCII art and Typewriter were initially planned, incorporating them was not viable, and instead I settled for simply using a text colouring package, pygame for music, os for files, and sys to allow the user to quit the game if they like.  

![packages](https://i.imgur.com/OuZ3hr6.jpg)
![checklist](https://i.imgur.com/yhBazNz.jpg)

Development proceeded smoothly and each day I was able to mark a different feature/component of the development process as completed. The game featured the ability to explore, to solve puzzles, to pick up items and add them to your inventory. I eventually finished coding an MVP that included functions, loops, error testing and everything else that was required. From there I decided to incorporate a second ending to the game as an extra feature, something that I had previously thought of and added to that section of my Trello workspace. 

![Code Basic Game](https://i.imgur.com/dojOg3t.jpg)
![trello home](https://i.imgur.com/1YJM26y.jpg)
![extra features](https://i.imgur.com/EQmWweT.jpg)

After I had completed the alternate ending to the game, my next task was to clean up the code and add some comments for readability. In summary, my implementation plan was as follows: I did some very rough sketches of a very basic overview of the game. I then used Trello to plan out all the features I wanted, and what would be required in an MVP. I then started on building the MVP, and researching python packages, making use of Trello along the way. Once the MVP was built with everything that it required, I decided to add an alternate ending to the game. Finally once all the code was cleaned up and made easier to read, I was able to sit back and enjoy a Trello workspace that looked like this: 

![Trello Done](https://i.imgur.com/DwWifJO.jpg)

## (R8) Help Documentation

### Installation Instructions
I have tried my best to cater to a range of devices and setups by creating several different bash scripts to choose from. Using your terminal simply navigate to the 'src' directory of this project where you can then enter your choice of './Game.sh', './PythonInstaller.sh', './LinuxGame.sh', './MacGame.sh' or './NoSoundGame.sh'. The 'Game.sh' script will attempt to automatically detect your operating system, install python (which is a requirement), install the required libraries and dependencies and then run the game. This script is inteded to be a 'all in one' script that can do everything you need, simplyifing the whole process. I've also included a separate script that will attempt to automatically detect your operating systen and just install python, leaving the libaries and dependencies for later. The reasoning behind this compartmentalisation is that if an error is encountered it's best for the user to have alternatives. 

You may even already have Python installed in which case you won't need either of the above mentioned scripts and you can simply just run the 'LinuxGame.sh' or 'MacGame.sh' scripts. These scripts will first install some libraries using either sudo apt-get for linux or brew for mac. These scripts are the way the game is intended to be played as the libraries are required for pygame mixer to play music properly during the game. After installing the necessary libraries they will create and activate a virtual environment in the directory. Finally they will then install the necessary dependencies for the game by using pip3 to read the requirements.txt file. After all these preliminary steps have been performed the game will run. 

If for whatever reason these bash scripts do not work, you can simply run the NoSoundGame script by entering ./NoSoundGame.sh in your terminal in the 'src' directory. This script will simply forgo installing the libraries needed for music. The game will run as normal but will display an 'error' message where music would usually be playing, everything else however still works fine. If any of the scripts fail to run due to not having the necessary permission simply enter in your terminal: 'chmod +x "script" ', replacing "script" with the name of the script you are running, i.e "chmod +x LinuxGame.sh" etc, which will alter the permissions, allowing the script to be executed. 

### How to run the script
simple type in your terminal './YourChosenScript.sh' replacing 'YourChosenScript.sh' with the name of the script you have chosen. For example LinuxGame.sh will be executed by entering './LinuxGame.sh' (minus the quotation marks).

NOTE: You may already have the afformentioned libraries installed, in which case running NoSoundGame.sh will result in the game running with sound anyway!

### Dependencies
The game makes use of a few python packages, which will need to be installed along with their respective dependencies. A list of dependencies can be found in the requirements.txt file included, but I will also list them here for convenience: 

- certifi==2023.5.7
- charset-normalizer==3.1.0
- click==8.1.3
- colorama==0.4.6
- colored==1.4.4
- docopt==0.6.2
- exceptiongroup==1.1.1
- idna==3.4
- iniconfig==2.0.0
- markdown-it-py==2.2.0
- mdurl==0.1.2
- packaging==23.1
- pipreqs==0.4.13
- pluggy==1.0.0
- pycolour==1.0.3
- pygame==2.4.0
- Pygments==2.15.1
- pytest==7.3.1
- requests==2.30.0
- rich==13.3.5
- shellingham==1.5.0.post1
- tomli==2.0.1
- typer==0.8.0
- urllib3==2.0.2
- yarg==0.1.9

All of these should be installed when your run any of the provided bash scripts mentioned above, however if you wanted to install them manually simply use your terminal to navigate to the game's 'src' directory where the game's source code is located, create and activate a virtual environment, and enter 'pip3 install -r requirements.txt' which will install the required packages and dependencies.

### System Requirements 
All the game requires to the run is modest hardware that any modern PC from the past 10 years would surely have. There is no need for a high powered CPU or GPU, large amounts of RAM or anything of that nature. To run the game users will need an operating system that supports the use of a terminal/command line, such as Linux or Mac. If you are running Windows it is recommended to use an Ubuntu terminal through WSL. 

### How the game works
Once you've run the provided bash scripts and all of the required packages and/or libraries have been installed, the game will open. From here you will be provided with some instructions on how to proceed through the game. The game takes simple text input from the player to determine what movements the player would like to make. If you make the wrong choice, you may end up dying (in the game) and will be prompted with a game over screen asking if you'd like to play again. Try your best to make it to the end, explore the world, learn about the spooky mysteries hidden in the game, and most of all, have fun! 


