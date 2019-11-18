#!/usr/bin/python
# -*- coding: utf-8 -*-
print("""
+ giới thiệu về function trong python

""")
def fib(n):
    """
    print a fibonacci series up to n
    """
    a, b = 0,1
    """
    a = 0
    b = 1
    """
    lst = []
    while a< n:
        print(" value : ", a)
        lst.append(a)
        a, b = b, a+ b
        """
        c = a + b
        a = b
        b = c
        """
    return lst
lst = fib(100)
print(lst)
print("""=====================
 + default argument
 + default parameter must be at the end of list parameter of function
 func(agr1, arg2, agr3 = 3)
 + note khi default value là nhưng mutable object

""")
def func_default_arg (age, name = "oanh"):
    
    """
    this is function
    """
    tem =  "name is ", name
    print("type of tem : ", type(tem))
    return tem , age
result = func_default_arg(12)
rs = func_default_arg(23, "van kem")
print(result) # type is tuple
print(type(result)) # type is tuple

print(rs)

def func(age, name = "oanh"):
    tem = "%s has %d" % (name, age)
    return tem


print(func(23))    

i = 4
def fu(args=i):
    print (args)
    return

print(fu())
print(fu(i))     

def func_mutable(a):
    l = []
    l.append(a)
    return l


print(func_mutable(12))
print(func_mutable(12))
print(func_mutable(12))

print("L is mutable object")
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("""
 result : 
    [1]
    [1, 2]
    [1, 2, 3]
""")

print("""
+ Keyword Arguments
    *var
    **kvar

""")

def keywordArgument(*name):
    print(type(name))
    print(name)
print(keywordArgument("oanh", "van kem "))

def keywordArgument2(**person):
    print(type(person))
    for x in person:
        print(x, ";", person[x])
print(keywordArgument2(name="oanh", age=232))

dct = {
        'Colorado': 'Rockies',
        'Boston': 'Red Sox',
        'Minnesota': 'Twins',
        'Milwaukee': 'Brewers',
        'Seattle': 'Mariners'
    }
print(type(dct))

print(keywordArgument2(**dct))

print(keywordArgument2(**{
        'Colorado': 'Rockies',
        'Boston': 'Red Sox'}))

print("print tuple==================")
print(keywordArgument("oanh", "vankem"))

print(keywordArgument(*("oanh", "vankem")))

print(keywordArgument2(**dct))

# def fun_only_post(param=2, /):
#     print(param)
print("""
check again 
""")

# fun_only_post("oanh")
def keyword_only_arg(*, arg):
    print(arg)
print(keyword_only_arg(arg="oanh"))

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
# def foo(name, /, **kwds):
#     return 'name' in kwds
# print(type(foo(1, **{'name': 2})))

