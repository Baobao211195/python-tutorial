"""
+ class variables : variables can be accessed at the class level
+ instace varibles : variables can be accessed at the instance variable

"""

class Person():
    
    # this is class variable
    person_type = "male"
    person_hello = "hello"
    person_goodby = "good bye"


if __name__ == "__main__":
    person = Person()
    print(person.person_type)   # output male
    print(person.person_hello)  # output hello
    print(person.person_goodby) # output good bye
    