# -*- coding: utf-8 -*-

"""
+ class variables : variables can be accessed at the class level
+ instace varibles : variables can be accessed at the instance variable
+ bản chất việc tạo ra thay đổi value của class variable của một instance
là việc lưu trữu và một dictionary tách biệt của instance đó

"""


class Person():

    # this is class variable
    person_type = "male"
    person_hello = "hello"
    person_goodby = "good bye"

    a = "class varibles"

    # create instace variable
    # def __init__(self, name, age):
    #     self.name   = name
    #     self.age    = age


class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == "__main__":
    # person = Person()
    # print(person.person_type)   # output male
    # print(person.person_hello)  # output hello
    # print(person.person_goodby)  # output good bye

    # instance variable
    # person_1 = Person("vankem", 23)
    # print(person_1.name)
    # print(person_1.age)

    # person_2 = Person("oanh", 28)
    # print(person_2.name)
    # print(person_2.age)

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

    print("===========================",
          p.__class__.__dict__)  # trỏ về class của p

    print("===========we can count the number of instance of class C as below example================")
    x = C()
    print("Number of instances: : " + str(C.counter))

    y = C()
    print("Number of instances: : " + str(C.counter))

    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
