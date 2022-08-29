num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))

opt = input("Enter operator? + , -, *, /: ")

if num1 == 45 and num2 == 3 and opt == '*': 
    print(555)
elif num1 == 56 and num2 == 9 and opt == '+':
    print(77)
elif num1 == 56 and num2 == 4 and opt == '/':
    print(4)
elif opt == '+':
    print(num1 + num2)
elif opt == '-':
    print(num1 - num2)
elif opt == '*':
    print(num1 * num2)
elif opt == '/':
    print(num1 / num2)
else:
    print("Error, Try again")
