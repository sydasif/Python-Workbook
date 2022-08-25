""" Task-1: A YouTube streamer decided to conduct a survey where users were asked to provide feedback on what they would like to watch in the
next stream. Your job is to create a program that uses the following information and prints out the result of what the user chose, along with a
thank you message. 

What shall I stream next?

a) Days Gone
b) Resident Evil 2
c) Fortnite
d) Apex Legends
e) Death Stranding
f) Surprise Us!

The ending message should be:

You have chosen (option). I appreciate your time and hope to see you at the next one! """

""" The exercise is fairly simple. Most of these will require you to print out information and then store the user-input value. Design the program so that it can understand what 'a' or 'b' or any character that the user chooses is, and then print the same out in the end greetings. You do not have to worry about printing out the name in the end. Just the letter of the selection will do for now."""

""" Remember, the case-sensitive nature of the program still haunts us. Make use of methods like .lower() to ensure it matches our requirements. I will be providing my version of the program in the last chapter as a solution. For now, keep thinking, keep coding.

Hint: While you can use an 'if' statement, I would recommend bypassing that for now. Try and think of more basic means to store and recall values.
This can easily be done without the use of logic and if/else statements. We will revisit this exercise in the future to make it a little more complex and appealing at the same time. """

print("What shall I stream next?")

a = "Days Gone"
b = "Resident Evil 2"
c = "Fortnite"
d = "Apex Legends"
e = "Death Stranding"
f = "Surprise Us!"

print()  # Add blank line

print(f"a) {a}")
print(f"b) {b}")
print(f"c) {c}")
print(f"d) {d}")
print(f"e) {e}")
print(f"f) {f}")

print()  # Add blank line

option = input("Enter your option? ")

if option == 'a':
    print(f"You have chosen {a}. I appreciate your time and hope to see you at the next one!")
elif option == 'b':
    print(f"You have chosen {b}. I appreciate your time and hope to see you at the next one!")
elif option == 'c':
    print(f"You have chosen {c}. I appreciate your time and hope to see you at the next one!")
elif option == 'd':
    print(f"You have chosen {d}. I appreciate your time and hope to see you at the next one!")
elif option == 'e':
    print(f"You have chosen {e}. I appreciate your time and hope to see you at the next one!")
elif option == 'f':
    print(f"You have chosen {f}. I appreciate your time and hope to see you at the next one!")
else:
    print("Your option is not included in the survey, Thanks")
