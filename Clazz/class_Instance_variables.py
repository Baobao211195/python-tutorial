"""
+ class variables : variables can be accessed at the class level
+ instace varibles : variables can be accessed at the instance variable

"""
class Person():
    
    # this is class variable
    person_type     = "male"
    person_hello    = "hello"
    person_goodby   = "good bye"

    #create instace variable
    def __init__(self, name, age):
        self.name   = name
        self.age    = age
    

if __name__ == "__main__":
    # person = Person()
    # print(person.person_type)   # output male
    # print(person.person_hello)  # output hello
    # print(person.person_goodby)  # output good bye
    
    # instance variable
    person_1 = Person("vankem", 23)
    print(person_1.name)
    print(person_1.age)

    person_2 = Person("oanh", 28)
    print(person_2.name)
    print(person_2.age)
    