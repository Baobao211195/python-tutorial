from collections import deque

print("""
 + More on list
 + Can use list as stack (append and pop)
""")
lst = []

lst.append(1)
lst.append(0)
lst.append(3)

lst.extend([4,5,6,7])

print(lst)

print("""
+ can use as queue by use dequeue function from queue

""")
q = deque(lst)
print("value when popleft  ", q.popleft())
print("value of list ", lst)
print("value of queu", q)

print("""
 + cac cach khoi tao list
""")

a = list(map(lambda x: x**2, range(10)))
# ham map tra ve 1 iterable
# ham list nham dau vao la 1 iterable
#  tuong duong trong java Instream().generate(0, 10).map(p -> p **2).collect(toList())
print(a)
print("vi du phuc tap ve list")
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

lsta = []
for y in [3,1,4]:
    for x in [1,2,3]:
        if x != y:
            lsta.append((x, y))


print(lsta) 

lstb = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            lstb.append((x, y))
print(lstb)            

lstc = lambda x, y: [(i, j) for i in x for j in y if i != j]

print(lstc([1,2,3], [3,1,4]))
