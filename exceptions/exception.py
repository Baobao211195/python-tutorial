"""
+ woring exception in python

"""

def raise_exception():
    while True:
        try:
            x = int(input("please enter a number " ))
            break
        except NameError:
            print("ooop! please try again ")


raise_exception()

    