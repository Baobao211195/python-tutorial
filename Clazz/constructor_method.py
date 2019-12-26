class Person():
    """
    + __init__ ko phải là constructor mà chỉ là một function constructor

    """
    def __init__(self):
        print("This is the constructor method.")

    def __init__(self, name):
        self.name =  name
        print("This is the constructor method.")

    def swim(self):
        print("the shark is swimming")

    def be_awesome(self):
        print("the shark is being awesome")
    
    def sayHello(self):
        print("hello ", self.name)


if __name__ == "__main__":
    # person = Person()
    person = Person("van")
    person.be_awesome() 
    person.swim()
    person.sayHello()

    person2 = Person("oanh")
    person2.sayHello()