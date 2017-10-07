# reading and writting files
from sys import argv
script, filename = argv
 
print("We're going to erase %r." % filename)
print("if you don't want that, hit CTRL -C ")
print("If you do want that, hit RETURN.")

input("? ")

print("Opening the file...")
target = open(filename, 'w') # mở file và chế độ là write

print("Truncating the file. Goodbye !")
target.truncate()

print("Nơ I'm going to ask you for three lines.")
lines 1 = input("line 1: ")
lines 2 = input("line 2: ")
lines 3 = input("line 3: ")


print("I'm going to write these to the file.")

target.write(lines 1)
target.write("\n")
target.write(lines 2)
target.write("\n")
target.write(lines 3)
target.write("\n")
print(" And finally, we close it.")
target.close()