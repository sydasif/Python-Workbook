# Rock, Paper, Scissors

"""A rock beats scissors, scissors beat paper by cutting it and paper beats rock by covering it.
Hint: use random module"""

import random

player2 = random.choice(['rock', 'paper', 'scissors'])

print("Your choice: 'Rock', 'Paper' or 'Scissors'")
player1 = input('> ').lower()

if player1 == 'rock' and player2 == 'rock':
    print("Game is Tie...")
elif player1 == 'rock' and player2 == 'scissors':
    print("You Win...")
elif player1 == 'rock' and player2 == 'paper':
    print("You Lose...")

elif player1 == 'scissors' and player2 == 'scissor':
    print("Game is Tie....")
elif player1 == 'scissors' and player2 == 'rock':
    print("You Lose....")
elif player1 == 'scissors' and player2 ==  'paper':
    print("You Win....")

elif player1 == 'paper' and player2 == 'paper':
    print("Game is Tie.....")
elif player1 == 'paper' and player2 == 'rock':
    print("You Win.....")
elif player1 == 'paper' and player2 == 'scissors':
    print("You Lose.....")
else:
    print("Your choice is unknown...")