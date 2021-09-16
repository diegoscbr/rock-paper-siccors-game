#game.py

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


if computer_choice == user_choice:
    print ("Draw!")
    
elif computer_choice == 'rock' and user_choice == 'scissors':
    print ("Computer wins, rock beat scissors, try again!")

elif computer_choice == 'scissors' and user_choice == 'paper':
    print ("Computer wins, scissors beat paper, try again!")

elif computer_choice == 'paper' and user_choice =='rock':
    print ("Computer wins, paper beat rock, try again!")

elif computer_choice == 'scissors' and user_choice == 'rock':
    print ("YOU WIN! Guess you're smarter than a computer;)")

elif computer_choice == 'paper' and user_choice == 'scissors':
    print ("YOU WIN! Guess you're smarter than a computer;)")

elif computer_choice == 'rock' and user_choice == 'paper':
    print ("YOU WIN! Guess you're smarter than a computer;)")
