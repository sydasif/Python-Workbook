print("Well come.......")

i = 0

while i < 3:

    i += 1

    first_name = input("Please, enter your first name: ")
    last_name = input("Enter your last name: ")
    age = input("Enter your age: ")
    score = int(input("Enter your number in examination: "))

    name = (f"{first_name} {last_name}")

    # formula = score/total*100
    percentage = (score/600) * 100
    percentage = round(percentage)
    
    if percentage >= 60 and percentage<= 80:
        print(f"{name}, you scored {percentage}% and admission is approved.")
    elif percentage >= 80:
        print(f"{name}, you scored {percentage}%  and eligible for a scholarship.")
    else:
        print(f"{name}, you scored {percentage}% and not eligible. Thank you.")
        