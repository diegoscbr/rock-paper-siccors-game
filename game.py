#game.py

import random 

print("Rock, Paper, Scissors, Shoot!")

#propt user for input

#x = input("Choose 'rock' or 'paper' or 'scissors' ")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print(user_choice)

#COMPUTER CHOICE AT RANDOM

options = ["rock", "paper", "siccors"]

computer_choice = random.choice(options)
print(computer_choice)

