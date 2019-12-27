"""
+ thừa kế trong python
"""


class Person():
    pass
    a = "class varibles"


if __name__ == "__main__":
    p = Person()
    p1 = Person()
    print(p.a)

    p.a = "variable for p object "
    print("for p :", p.a)
    print("for p1 :", p1.a)

    print("===========================")
    Person.a = "class changes variable"
    print("for p :", p.a)
    print("for p1 :", p1.a)

    print("===========================", p.__dict__)
    print("===========================", p1.__dict__)
    print("===========================", Person.__dict__)

    p2 = Person()
    print("===========================", p2.__dict__)
