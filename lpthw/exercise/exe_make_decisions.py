print("You enter in a house.")
print("There's is a dark room with two door.")
print("Where do you want to go #1 or #2?")

door = input("> ")

if door == "1":
    print("There's is gaint bear in the room.")
    print("What to do?.")
    print("1. Run through window.")
    print("2. Eat a cake.")
    print("3. Shoot a bear.")

    bear = input("> ")

    if bear == "1":
        print("That's good, You save your life.")
    elif bear == "2":
        print("Good eat a cake, and run through window.")
    else:
        print("Mad man, You will die.")

elif door == "2":
    print("There's is a dog in a room.")
    print("What to do now?")
    print("1. Go back.")
    print("2. Open the dog.")

    dog = input("> ")

    if dog == "1":
        print("You do nothing, Good by.")
    else:
        print("Good choice, enjoy.")

else:
    print("Go back, invalid input.")
