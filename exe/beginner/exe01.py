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
