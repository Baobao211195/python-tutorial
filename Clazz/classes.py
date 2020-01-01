# -*- coding: utf-8 -*-
"""
start vs class in python
"""

class Shark():
    """
    + create class shark
    + self : reference to objects are created base on class
    + self : always first

    """
    # define method

    def swim(self):
        print("the shark is swimming")

    def be_awesome(self):
        print("the shark is being awesome")
    def say(self):
        """
        + hàm này phải có tối thiểu 1 tham số
        """
        print("shark says hello")


if __name__ == "__main__":
    shark = Shark()
    shark.say() 

        
