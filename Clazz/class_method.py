# -*- coding: utf-8 -*-

"""
============== Class method =============================
"""


class Robot:

    # create a private varible vs double underscores
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod  # create class method
    def robotInstances(cls): # cls describe for this Object of class , maybe it's better in irheritance case 
        return cls, Robot.__counter # return a tuple

    

if __name__ == "__main__":
    print(Robot.robotInstances())
    x = Robot()
    print(x.robotInstances())
    y = Robot()
    print(x.robotInstances())
    print(Robot.robotInstances())