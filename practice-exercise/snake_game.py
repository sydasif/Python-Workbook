"""Snake, Water and Gun game. Snake beat water, water beat gyun and gun beat snake."""

import random

print("Well come, Snake, water and gun game.")

GAME_COUNT = 10
COMP_WIN = 0
USER_WIN = 0

while GAME_COUNT != 0:

    computer_choice = random.choice(["snake", "water", "gun"])
    user_choice = input("Your choice:- 'snake', 'water' or 'gun': ")

    if computer_choice == user_choice:
        print("Game Tie.")
    elif computer_choice == "snake":
        if user_choice == "water":
            print("Computer Win.")
            COMP_WIN += 1
        else:
            print("User Win.")
            USER_WIN += 1
    elif computer_choice == "water":
        if user_choice == "gun":
            print("Computer Win.")
            COMP_WIN += 1
        else:
            print("User Win.")
            USER_WIN += 1
    elif computer_choice == "gun":
        if user_choice == "snake":
            print("Computer Win.")
            COMP_WIN += 1
        else:
            print("User Win.")
            USER_WIN += 1
    else:
        print("Invalid Input...")

    GAME_COUNT -= 1

print()

if COMP_WIN > USER_WIN:
    print("Computer Win: ", COMP_WIN)
else:
    print("User Win: ", USER_WIN)
