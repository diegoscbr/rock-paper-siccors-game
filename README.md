# rock-paper-siccors-game

## DESCRIPTION
ROCK PAPER SCISSORS GAME THAT GENERATES A RANDOM COMPUTER OUTPUT AND TAKES IN A USER INPUT. PROGRAM RUNS ON THE COMMAND-LINE. PROGRAM OUTPUTS INCLUDE: 
* VIRTUAL ENVIRONMENT THAT DISPLAYS PLAYER NAME AT THE TOP OF THE PROGRAM
* PROMPT FOR PLAYER TO CHOOSE ROCK, PAPER, OR SCISSORS
* RANDOM SELECTION FOR COMPUTER
* DETERMINE WINNER OF GAME (COMPUTER OR PLAYER)
* VALIDATE USER CHOICE
* DISPLAY USER AND COMPUTER CHOICES 
* CONGRAGULATORY MESSAGE OR PROMPT TO TRY AGAIN

## ISNSTALLING PROGRAM
* OPEN COMMAND LINE
* DOWNLOAD GAME AT https://github.com/diegoscbr/rock-paper-siccors-game/blob/bc9f64fd5a21de55b856c7b1da23a36b07bba17e/game.py
* TO SET UP ENVIRONMENTAL VARIABLE PLAYER_NAME:
    *first need to pip install python-dotenv from the command-line, inside an active virtual environment
    *THEN IN THE TEXT EDITOR:
    >import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print(x)
   
   
   
    * Then your local ".env" file contents should be:
    >PLAYER_NAME="Jon Snow"
#(dot-env instructions pulled from professor Rossetti's repository https://github.com/s2t2/rock-paper-scissors-game/blob/main/game.py)
*  NOTE: MAKE SURE PYTHON IS INSTALLED 

## HOW TO RUN GAME
* MAKE SURE YOU ARE IN THE GAME's DIRECTORY ON THE COMMAND-LINE
* TO RUN THE GAME TYPE: python game.py
* TYPE IN A CHOICE AFTER THE COMPUTER PROMPTS YOU
* COMPUTER ILL OUTPUT RESULTS
* TO RUN AGAIN TYPE: python game.py
* TO STOP PROGRAM TYPE: exit()