# create variable
my_var = "Orange Banana Apples Kings Boy"
# create list from 'my_var' variable
my_list = my_var.split(' ')
print(f"My List: {my_list}")
# make new list
new_list = ["Kids", "Bat", "Man", "Car"]
# while loop to add items in my_list from new_list
while len(my_list) != 8:
    # pop() items from new_list
    item = new_list.pop()
    print("Add new items: {}".format(item))
    # add items to my_list
    my_list.append(item)
    print("My list now: ", my_list)

print(new_list)
# create variable from my_list
new_var2 = (' ').join(my_list)

my_list2 = ["Asif", "Ali", "Aashir", "Maaz"]

new_things = new_var2.split()

while len(my_list2) != 0:
     item2 = my_list2.pop()
     new_things.append(item2)

print(new_things)     
