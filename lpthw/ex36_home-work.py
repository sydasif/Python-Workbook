from sys import exit

def gold_room():
    print("You are in gold room.")
    print("This room is full of gold.")
    print("How much do you take?")
    
    choice = input("> ")
    
    if str(0) in choice or str(1) in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Good job, you are no greedy.")
    else:
        print("You Greedy Man.")  
        exit(0)


def silver_room():
    print("chatalu is dead, and you are in silver room now.")
    print("This room is full of silver.")
    dead("Take it as you can?")

def bear_room():
    print("You enter in a bear room.")
    print("There is a huge bear in the room.")
    print("Give it 'honey' or 'slap' the bear.")

    choice = input("> ")

    if choice == "honey":
        print("You saved your life.")
        gold_room()
    else:
        dead("You are dead man.")




def chatalu_room():
    print("You enter in chatalu room.")
    print("Chatalu is a huge monster.")
    print("What to do now. Go 'back' or 'fight'.")
    
    while True:

        choice = input("> ")
        
        if choice == 'back':
            silver_room()
        elif choice == 'fight':
            gold_room()
        else:
            print("No way, fight or go back.")


def dead(why):
    print(why, "Good Bye!")
    exit(0)


def start():
    print("You enter in a dark room.")
    print("There are two door in dark room.")
    print("Where you want to go, left or right?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        chatalu_room()
    else:
        dead("No more choice.")

start()
