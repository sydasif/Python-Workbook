import random

num = random.randrange(1,14)
guess = int(input("Enter any number: "))

while num != guess:

    if guess < num :
        print("Too low")
    elif guess > num:
        print("Too high!")
    else:
        break # num = guess
    
    guess = int(input("Enter number again: "))

print("you guessed it right!!")
