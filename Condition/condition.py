print("""

+ More condition
 + in and notin check element exist in sequence
 + is and is not check 2 object is the same object (use equals() in java)
 + change condition

""")

print("=======+ change condition===================")
a = 8
b = 5
c = 10
if a > b < c:
    print("condition is chained a > b and b < c")

print("====== and or operator =====================")

st = "oanhpv"
if st:
    print(type(st))
    print("oanh pv")
st1 = ""
if st1:
    print("empty")
def fuunc(x):
    if x:
        return x
a = fuunc("van kem")
b = fuunc(1)
print(type(a), type(b))

print("===== Boolean operator =================")

a, b, c, d, e = '',"van",'','kem', "oanh"
x = a and b or c or d or e
print("type of x ", type(x), "value of x", x)

print("value of a and b ", a and b)
print("value of a or b ", a or b)

print("=== and operator=================") 
print( 1 and "oanh")
print( 1 and '')

print("oanh" and 1)
print('' and 1)

print("van " and "oanh")
print(1 and 2)
print("==== or operator====================")

print( 1 or "oanh")
print( 1 or '')

print("oanh" or 1)
print('' or 1)

print("van " or "oanh")
print(1 or 2)

print("===== use or to swap 2 number")
x = 1
y = 2

print(y or x, x or y)
print(x, y)

print("==== comparision two sequences")
print((1,2,3) == [1,2,4])
print((1,2,3) > [1,2,4])
print((1,2,3) < [1,2,4])

print('ABC' < 'C' < 'Pascal' < 'Python')

print('XBC' < 'C' < 'Pascal' < 'Python')

print([1,2,3] < [1,2,4])
print([1,2,3] > [1,2,4])
print([1,2,4] == [1,2,4])

print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))

print((1, 2)                 < (1, 2, -1))
print((1, 2, 3, 4)           < (1, 2, 4))

print((1, 2, 3)             == (1.0, 2.0, 3.0))