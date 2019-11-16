print("""

+ tap hop cac element phan tach nhau bang giau phay
+ tuple is immutable object

+ if element of type is mutable object, we can modify these mutable objects

+ Thuc hien packing and unpacking

""")

tp = 23, 32, 54, "oanh"
print("type of tp : ", type(tp))

print(tp)

tp = tp, ([1,2,1])
print ("new tp ", tp)

print("old value of mutable object (list) ", tp[1][1])

tp[1][1] = 323

print("new value after change ", tp)

x= 12
y = 23
z = "dfd"
t = ()

t = x, y, z # packing tuple

print(t)

a, b, c = t # unpacking tuple
print(a)
print(b)
print(c)
