# Rock, Paper, Scissors

"""A rock beats scissors, scissors beat paper by cutting it and paper beats rock by covering it.
Hint: use random module"""

import random

opt = ["rock", "paper", "scissors"]

while True:
    print("Your choice: 'Rock', 'Paper' or 'Scissors'")
    player1 = input("> ").lower()
    player2 = random.choice(opt)

    # Block no 1
    if player1 == player2:
        print(f"Player2: {player2} Game is Tie.")

    # Block no 2
    elif player1 == "rock":
        if player2 == "scissors":
            print(f"Player2: {player2} You Win.")
        else:
            print(f"Player2: {player2} You lose.")
    # Block no 3
    elif player1 == "scissors":
        if player2 == "paper":
            print(f"Player2: {player2} You Win..")
        else:
            print(f"Player2: {player2} You lose..")
    # Block no 4
    elif player1 == "paper":
        if player2 == "rock":
            print(f"Player2: {player2} You Win...")
        else:
            print(f"Player2: {player2} You lose...")
    else:
        print("Your choice is unknown...")

    print("Whould you like to play again. [y/n]")
    user_choice = input("> ")
    if user_choice.lower() != "y":
        print("Wrong Input. Byeeeee")
        break
