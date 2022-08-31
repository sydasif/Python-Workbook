print("My Brilliant Little Leap Year Calculator!")
year = int(input("Please enter the year: "))

if (year%4) == 0:
    print(f"{year} is a leap years.")
elif (year%400) == 0:
    print(f"{year} is a leap years.")
else:
    print(f"{year} is not a leap years.")    