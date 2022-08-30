while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter digit...")
    else:
        break

operator = input("Enter operator? + , -, *, /: ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Error, Try again")