print("""
+ Module in python

+ make modules to import others or main modules

""")

print("===== import all function on module")
import module1

x = module1.func_module_1(2)
print(x)

print(module1.__doc__)
print(module1.__file__)
print(module1.__name__)
print(module1.__package__)
print("print values variable in module1 ", module1.values)

print("===== import specific function on a module")
from module1 import func_module_1
from math import pi, sqrt

print('value of pi is ', pi)

print('sqrt function ', sqrt(9))

# from sys import call_tracing, stdout