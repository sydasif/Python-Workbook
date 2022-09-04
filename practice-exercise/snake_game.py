"""Snake, Water and Gun game. Snake beat water, water beat gyun and gun beat snake."""

import random

print("Well come to Snake, water and gun game.")

game_count = 10

comp_win = 0

user_win = 0


option = ["snake", "water", "gun"]

while game_count != 0:
    # comp_choice is computer
    comp_choice = random.choice(option)
    # user_choice is user
    user_choice = input("Your choice:- 'snake', 'water' or 'gun': ")

    if comp_choice == user_choice:
        print("Game is Tie.")
    elif comp_choice == "snake":
        if user_choice == "water":
            print("Playe one win.")
            comp_win += 1
        else:
            print("User win..")
            user_win += 1
    elif comp_choice == "water":
        if user_choice == "gun":
            print("Computer win..")
            comp_win += 1
        else:
            print("User win..")
            user_win += 1
    elif comp_choice == "gun":
        if user_choice == "snake":
            print("Computer win..")
            comp_win += 1
        else:
            print("User win..")
            user_win += 1
    else:
        print("Invalid Input...")

    game_count -= 1

print()

if comp_win > user_win:
    print("Computer win.: ", comp_win)
else:
    print("User win.: ", user_win)
