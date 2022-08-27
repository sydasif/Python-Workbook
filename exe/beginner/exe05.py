print("Well come... Guess the number game.")

sec_num = 14
num_of_guess = 5

while num_of_guess > 0:

    num_of_guess -= 1

    user_num = int(input("Enter a number to guess the secret number: "))
    
    if user_num > sec_num:
        print("Your number is too high.")
    elif user_num < sec_num:
        print("Your number is too low.")
    else:
        print("You Win!")
        break
    
    print(f"Number of guess left: {num_of_guess}")

print("Game over...")
