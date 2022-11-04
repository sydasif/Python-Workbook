my_list = []

def numbers(number, increment):
    """This function use while loop to
    print numbers"""
    i = 0
    while i < number:
        print(f" At top of i: {i}")
        my_list.append(i)
        print("My list now: ", my_list)
        i = i + increment
        print(f"At bottom of i: {i}")

numbers(10, 3)
print("==================")
print("My list: {}".format(my_list))
