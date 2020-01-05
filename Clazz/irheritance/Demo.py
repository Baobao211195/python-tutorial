from Clazz.irheritance import demo1


class Demo:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class Sub_demo_0(Demo):

    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


class Sub_demo_1(Demo):
    pass


class Sub_demo_2(demo1.Sub_demo_2):
    pass


if __name__ == '__main__':
    # demo = Demo("van kem")

    sub_demo = Sub_demo_0("oanhpv")

    sub_demo.say_hi()
    print(""""====================================""")
    print(Demo.say_hi(sub_demo))

    # if isinstance(demo, Demo):
    #     print("demo is instance of Demo class")
    #
    # if issubclass(Sub_demo_0, Demo):
    #     print("there is a sub class")
