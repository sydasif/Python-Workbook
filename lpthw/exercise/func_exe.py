# define function
def family(*args):
    name, age, kids = args
    print(f"Your name: {name}")
    print(f"Your age: {age}")
    print(f"You have {kids} kids.")


print("call function with direct arguments.") 
family("Asif", 43, 3)

my_name = "Asif"
my_age = 43
my_kids = 3

print("call function with variables.")
family(my_name, my_age, my_kids)

your_name = input("What is your name: ")
your_age = input("What is your age: ")
your_kids = input("How many kids you have? ")
family(your_name, your_age, your_kids)
