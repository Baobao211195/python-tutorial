# -*- coding: utf-8 -*-

class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


if __name__ == '__main__':
    a = A()
    print("initial object")
    a.foo(1)
    
    print("salary_fsoft" > "salay_cmc")

    print("calling class method by instance")
    a.class_foo(1)

    # print("calling class method by Class of object")
    # A.class_foo(1)
    #
    print("calling static method by instance")
    a.static_foo(1)
    #
    # print("calling static method by Class")
    # A.static_foo(1)
    #
    # print("========================================")
    # print(a.foo(1))
