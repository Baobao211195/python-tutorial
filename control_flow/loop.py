print("""

+ loop techniques

""")
print("""
=========================================================
+ Loop a dictionary

""")
dic = dict()
dic[1] = "vankem"
dic[2] = "vanoanh"
dic[3] = "van ham"
print(dic)

for k, v in dic.items():
    print("key " , k,  " and value ", v)

print("""
+ get index of list
use enumarate() function
""")

ls = ["a", "b", "c", "d"]
for i, k in enumerate(ls):
    print(i, k)

print("""
+ loop two and more list data on the same time
use zip() function
""")

ls2 = [1,2,3]
for p, a in zip(ls, ls2):
    print(p, a)

ls = [34,34]
for p, a in zip(ls, ls2):
    print(p, a)
    
print("""
+ use reserved() function to  for nguoc
""")

print("value of nan ", float('NaN'))
print("type of nan ", type(float('NaN')))



    