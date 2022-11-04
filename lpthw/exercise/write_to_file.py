from sys import argv

script, fileName = argv

print(f"We're going to erase {fileName}...file")
print("If you want that hit CTRL-C")
print("If you want to continue hit RETURN")

input("?")

print("Opening file.....")
target = open(fileName, 'w')

print("We'er truncating file! Goodbye.")
target.truncate()

print("Add some line to the file")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))
target.close()

print("Done...")

print()

print("Reading file...")
f = open(fileName)
output = f.read()

print(output)
f.close()
