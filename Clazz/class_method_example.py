class Pet:
    
    _name_ = "this is pet class"
    @classmethod
    def print_name(cls):
        print(cls._name_)

class Dog(Pet):
    _name_ = "this is dog class"


class Cat(Pet):
    _name_ = "this is cat class"

if __name__ == "__main__":
    Pet.print_name()
    Dog.print_name()
    Cat.print_name()