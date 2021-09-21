#game.py

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print(x)


import random 

print(" WELCOME TO Rock, Paper, Scissors, Shoot!")
 

#propt user for input

#x = input("Choose 'rock' or 'paper' or 'scissors' ")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

#COMPUTER CHOICE AT RANDOM

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)

if user_choice not in options:
    print("INVALID OPT.")
    exit()
#adapted from GIANNA in slack
if computer_choice == user_choice:
    print ("NO WINNER,TIE! TRY AGAIN!")
   
elif computer_choice == 'rock' and user_choice == 'scissors':
    print ("COMPUTER WINS, rock beat scissors, try again!")

elif computer_choice == 'scissors' and user_choice == 'paper':
    print ("COMPUTER WINS, scissors beat paper, try again!")

elif computer_choice == 'paper' and user_choice =='rock':
    print ("COMPUTER WINS, paper beat rock, try again!")

elif computer_choice == 'scissors' and user_choice == 'rock':
    print ("YOU WIN! Guess you're smarter than a computer;)")

elif computer_choice == 'paper' and user_choice == 'scissors':
    print ("YOU WIN! Guess you're smarter than a computer;)")

elif computer_choice == 'rock' and user_choice == 'paper':
    print ("YOU WIN! Guess you're smarter than a computer;)")
