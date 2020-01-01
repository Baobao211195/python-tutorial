# -*- coding: utf-8 -*-

"""
============== Static method =============================
"""


class Robot:

    # create a private varible vs double underscores
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod  # create static method
    def robotInstances():
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.robotInstances())
    x = Robot()
    print(x.robotInstances())
    y = Robot()
    print(y.robotInstances())
    print(Robot.robotInstances())
