# State Dict
states = {
        "Balochistan": "BN",
        "Sindh": "SH",
        "Punjab": "PB",
        "Khyber": "KP"
        }

# Cities Dict
cities = {
        "BN": "Qutta",
        "SH": "Karachi",
        "PB": "Lahore",
        "KP": "Peshawer"
        }

# print states and abbreviation
print('-' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print city and state
print('-' * 20)
for state, city in list(cities.items()):
    print(f"{state} has a City: {city}")

# now print both at same time
print('-' * 20)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has a City: {cities[abbrev]}")

# safely get value
print("--" * 10)
state = states.get("Gilgit")
if not state:
    print("Sorry, Does not exists")

