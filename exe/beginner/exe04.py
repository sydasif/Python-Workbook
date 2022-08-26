print("Well Come, Dear customer!")
print("We provide below services to our customer.")

print("""a) Root Canal Therapy - $250
b) Oral Hygiene Check - $50
c) Emergency Injury Treatment - $100
d) Post-Procedure Check-up - $150
e) Routine Check-ups and Consultation - $75""")

print("For advance payments, customers get a 50% discount")

total = 0

service = input("Please choose one: ")

if service == 'a':
    total = total + 250
elif service == 'b':
    total = total + 50
elif service == 'c':
    total = total + 100
elif service == 'd':
    total = total + 150
elif service == 'e':
    total = total + 75
else:
    print("Thanks")

adv = input("Do you want to pay in today? [y/n] ")

if adv == 'y':
    total = (total * 50) / 100
    print(total)
else:
    print(total)
