# Health Management System


def timeStamp():
    from datetime import datetime

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
    return date_time


time_stamp = timeStamp()


# def get_name(person):
#     return person

# we use labda to create same as above function
get_name = lambda person: person


print("Well Come to Health Management System...")

while True:

    try:
        print("What do you want?")

        print("Read or Write a file?")
        print("Enter [0] for Read and [1] for Write.")

        read_write = int(input("> "))

        if read_write == 0:
            print("What do you want to retrieve?")
        else:
            print("What do you want to enter?")

        print("Enter [0] for Food and [1] for Exercise.")

        food_or_exercise = int(input("> "))

        print("Please enter client name: ")
        print("'Harry', 'Rohan', 'Hammad'")

        clientName = input("> ").lower()

        name = get_name(clientName)

        if clientName == name and read_write == 0:
            if food_or_exercise == 0:
                f = open(f"{name}_food.txt")
                print(f.read())
                f.close()
            else:
                f = open(f"{name}_exe.txt")
                print(f.read())
                f.close()
        elif clientName == name and read_write == 1:
            if food_or_exercise == 0:
                print("Enter food name: ")
                food = input("> ")
                f = open(f"{name}_food.txt", "a")
                content = f"{food} {time_stamp}\n"
                f.write(content)
                f.close()
            else:
                print("Enter Exercise name: ")
                exercise = input("> ")
                f = open(f"{name}_exe.txt", "a")
                content = f"{exercise} {time_stamp}\n"
                f.write(content)
                f.close()
        else:
            print("Client does not exist...")
    except ValueError:
        print("Invalid Input")
    except FileNotFoundError:
        print("No such file or directory exsit...")

    print("Do you run again? [yes/no]")

    option = input("> ").lower()
    if option != "no":
        continue
    else:
        break
