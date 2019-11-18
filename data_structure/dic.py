print("""
+ about dictionary on python
+ like Map in java
+ store keys and values
+ **kwargs
+ index by keys and keys is imutable type 
+ any object is immutable type can be key in dictionary
+ if typle is key => data of tuple must be immutable type
+ key is unique 

""")

dtic1 = {'jack': 4098, 'sape': 4139}

keys = list(dtic1)
print("list(d) return about list of key of dict ", keys)


dict2 = dict()
dict2[1] = "oanh"
dict2[3] = "oanh4"
dict2[2] = "oanh2"

print("value of dic 2  , ", dict2)

print("constructor is a iterable===============")
it = [(1,"oanh"), (2,"oanh2"), (3,"oanh3"), (4,"oanh4")]
dict3 = dict(it)

print("value of dic 3  , ", dict3)

print("constructor is a keyword arguments **kwargs===============")

def create_dict(**kwargs):
    return dict(kwargs)

print(create_dict(name1="oanh",name2="oanh2",name3="oanh3"))