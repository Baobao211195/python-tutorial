print("""
+ set in python
+ no duplicate element
+ unordered element
+ sets do not support indexing, slicing, or other sequence-like behavior.
+ mutable
""")

setdata =  {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("type of set  ", type(setdata))

setExx = set()
setExx.add("fdfd")
setExx.add("123")
setExx.add("123")
print(setExx)

def check_exist(setdata):
    return {i for i in setdata if i not in "fdfdfd"}

st = lambda x: {i for i in x if i not in "fdfdfd"}

print("value of st " , st(setExx))
print("""
+ collection of characters
""")

a = set("fdafadfdaffdsaf")
print("value of set a ,", a)