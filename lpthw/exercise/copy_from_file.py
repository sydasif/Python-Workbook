from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"We're copying text from {from_file} to {to_file}")

print(f"Reading from {from_file}...")
data = open(from_file).read()
print(data)

print(f"Does, {to_file} exist? {exists(to_file)}")

print("Hit RETURN or CTRL-C to abort.")
input("?")

print(f"Copying to {to_file}...")
f = open(to_file, 'w')
wr = f.write(data)
f.close()
print("Done...")

