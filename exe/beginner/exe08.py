"""Q-2: A freelance programmer was tasked with creating a simple
program to determine the eligibility of a profile for an auto-loan.
Based on some specific information and conditions, such as the candidate
should be less than 45 years of age, must have a minimum of a certain
number as income and should not have any criminal records, the
program was to determine if the same person was eligible for a loan or not.
The programmer wrote the following program:
"""

print("Your doorway to auto-loan eligibility check!")
print("Please provide complete information for best results")

#name = input("Please enter your full name: ")
age = int(input("Enter your age: "))
income = int(input("Please enter your income per month: "))
#nature_of_job = input("Do you work full-time, part-time or as a freelancer?:")

has_license = input("Do you have a valid license? [y/n]: ")
if has_license.lower() == "y":
    has_license = True
else:
    has_license = False

has_criminal_record = input("In the last 5 years, do you have any criminal records? [y/n]: ")
if has_criminal_record.lower() == 'y':
    has_criminal_record = True
else:
    has_criminal_record = False

if age > 45 and income >= 8000 and has_license == True and has_criminal_record == False:
    print("You are not eligible your age should be less than 45.")
elif age < 45 and income >= 5000 and has_license == True and has_criminal_record == False:
    print("You are eligible to apply for a loan")
elif has_criminal_record == True:
    print("You are not eligible for a loan")
elif income < 5000:
    print("You are not eligible at this time")
else:
    print("Please be patient as one of our specialists will be in touch!")