print("""
+ lamda expression

""")

def make_incre(n):
    return lambda x: x + n

x = make_incre(12)
print(make_incre(12)(1))
print("""
like java 
    (x, n) -> x + n
    hoi kho hieu
""")
print("""
 example 1
""")    
def lamda1(x):
    return lambda x: x
print("""
equal =  
Note 
    The keyword: lambda (giong -> trong java)
    A bound variable: x (trong tham so truyen vao trong (x) -> java)
    A body: x (la phan body giong -> }} java)
    x -> x
""")    
def func1(x):
    return x

x = (lambda x: x + 1)(1)
print("value of x ", x) # truong hop nhan 1 tham so dau vao

print("""
 truong hop vs muiltiple argument
""")

x = lambda first_name, last_name: first_name + " " + last_name
print(x("oanh", "vankem"))

print("""

+ khai niem ve anonymous function in python
- la function ko co name va duoc tao boi tu khoa "lamda"

+ khai niem Traceback la exception duoc raise trong khi thuc hien 1 lamda function
+ Arguments trong lamda
    - positional arguments
    - Named arguments (sometimes called keyword arguments)
    - Variable list of arguments (often referred to as varargs)
    - Variable list of keyword arguments
    - Keyword-only arguments
""")
print((lambda x, y, z: x + y + z)(1, 2, 3))

print((lambda x, y, z=3: x + y + z)(1, 2))

print((lambda x, y, z=3: x + y + z)(1, y=2))

print((lambda *args: sum(args))(1,2,3))

print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print("""
+ decorator in lamda (sau nay se noi sau)

""")

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
def pring(x):
    return x

y = lambda x: pring(x)

print(y("pham van oanh"))    
