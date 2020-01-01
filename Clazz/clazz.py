# -*- coding: utf-8 -*-
class Person():

    
    def __init__(self, age):
        """
        """
        self.age = age
    def __init__(self, age, name):
        """
        """
        self.age = age
        self.name = name
    def sayHello(self):
        print("name :", self.age)

if __name__ == "__main__":
    """
    nếu có nhiều hơn 1 method __init__ thì khi khởi tạo object sẽ nhận method __init__ cuối cùng.
    """
    per = Person(12, "oanh")
    per.sayHello()