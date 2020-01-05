"""

+ open problem vs setter and getter in python
"""


class Demo:

    def __init__(self, x, y, z):
        self.__x = x
        self.y = y  # has deffer vs x
        self.set_z(z)
    """
    + Case 1 : vs x we use setter and getter as oop
    """

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    """
    + Case 2 : y we use properties
    """
    @property
    def y(self):
        return self.__y

    @y.setter  # must be same name of function y and @y.setter
    def y(self, y):
        self.__y = y

    """
    + Case 3 use properties function
    """
    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    z = property(get_z, set_z)

if __name__ == '__main__':

    demo_0 = Demo(1, 2, 3)

    demo_0.z = 90
    print(demo_0.z)
    print(demo_0.y)

    print(demo_0.get_x())


    # demo_0 = Demo(1, 3)
    # demo_1 = Demo(5, 6)
    # print(demo_0.get_x(), demo_0.y)
    #
    # print(demo_1.y)  # we can use .y instead of .get_y()
    #
    # # change value of y
    # demo_1.y = 100
    #
    # print(demo_1.y)

    # demo_0 = Demo(5)
    #
    # demo_1 = Demo(6)
    #
    # demo_0.set_x(4)
    # print(demo_0.get_x())
    #
    # demo_1.set_x(9)
    # print(demo_1.get_x())
