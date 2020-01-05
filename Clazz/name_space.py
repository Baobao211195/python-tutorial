"""
+ global and nonlocal in python
"""


def test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # change variable in the module
        spam = "nonlocal spam"

    def do_global():
        global spam  # become global variable at the high level modules
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

test()
print("In global scope:", spam)