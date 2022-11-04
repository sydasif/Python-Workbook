my_list = []                                     

def number(num):
    for i in range(0, num): 
        print(f"My list: {my_list}") 
        print(f"Adding '{i}' to my_list") 
        my_list.append(i) 
       

number(6)
print(f"My list now: {my_list}")   
