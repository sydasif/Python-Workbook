total = 0
total_men = 0
total_kids = 0

print("Enter '0' for total sum")

while True:    
    age = int(input('Enter Age: '))
    
    if age == 0:
        break
    if age <= 3:
        total_kids += 1
        continue
    else:
        total += 100
        total_men += 1

# optional, can use simple print
print("{:^10} | {:^10} | {:^10}".format("Total Men", "Total Kids", "Total $"))
print("{:^10} | {:^10} | {:^10}".format(total_men, total_kids, total))
