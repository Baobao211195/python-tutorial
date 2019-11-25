"""
+ run module as script
+ if use main method, must be import in main method

# if __name__ == "__main__":
#     import sys
#     print(sys.argv[1])
#     pass
 else don't use main method we can import free
"""

import module1
import sys
x = module1.func_module_1(1)

print(x, sys.argv[1], sys.argv[2])

print(sys.path)

for x in dir(module1):
    print(x , type(x))

# from numpy  import add

# print(add.reduce)

        