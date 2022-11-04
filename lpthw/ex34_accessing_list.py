animals  = ['bear', 'python3.6', 'peacock', 'kangroo', 'whale', 'platypus']
i = 0
for animal in animals:
    i += 1
    output = f"The {i} animal is {animal} at index '{animals.index(animal)}' in the list"
    print(output) 
