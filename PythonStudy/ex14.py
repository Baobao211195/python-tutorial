# Prompting and passing 
from sys import argv
oanh, user_name = argv
promt = '> '

print("Hi %s, I'am the %s script." %(user_name, oanh))
print("I'd like to ask you a few the question.")
print("Do you like me %s ?" % user_name)
like = input(promt)

print("Where do you live %s?" % user_name)
lives = input(promt)

print("What kind of computer do you have ?")
computer = input(promt)

print("""
Aright, so you said %r about linking me.
You live %r. Not sure where that is.
And you have a %r computer. Nice.""" %(like,lives,computer))