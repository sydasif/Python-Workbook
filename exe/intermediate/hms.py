# Health Management System
# 03 Clients Harry, Rohan, Hammad
# 06 files - 03 for diet and 03 for food

def getdate():
    from datetime import datetime
    now = datetime.now()
    t = now.strftime("%m/%d/%Y_%H:%M:%S")
    return t

dateTime = getdate()
print(dateTime)


print("Well Come to Health Management System...")
print("What do you want?")

print("Read or Write a file?")
print("Enter [0] for Read and [1] for Write.")

read_or_write = int(input("> "))

if read_or_write == 0:
    print("What do you want to retrieve?")
else:
    print("What do you want to enter?")

print("Enter [0] for Food and [1] for Exercise.")

food_or_exercise = int(input("> "))

print("Please enter client name: ")
print("'Harry', 'Rohan', 'Hammad'")

clientName = input("> ")

if clientName.lower() == 'harry' and read_or_write == 0:
    if food_or_exercise == 0:
        f = open('harry_food.txt')
        print(f.read())
        f.close()
    else:
        f = open('harry_exe.txt')
        print(f.read())
        f.close()
elif clientName.lower() == 'harry' and read_or_write == 1:
    if  food_or_exercise == 0:
        print("Enter food name: ")
        food_name = input("> ")
        f = open('harry_food.txt', 'a')
        content = f"{food_name} {dateTime}\n"
        f.write(content)
        f.close()
    else:
        print("Enter Exercise name: ")
        exercise_name = input("> ")
        f = open('harry_exe.txt', 'a')
        content = f"{exercise_name} {dateTime}\n"
        f.write(content)
        f.close()           
else:
    print('...........')