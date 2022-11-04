from sys import argv

script, file_name = argv

text = open(file_name)

print(f"Here's your file {file_name}")
print(text.read())

print("Type the file name again: ")
file_again = input("> ")

text_again = open(file_again)

print(text_again.read())
