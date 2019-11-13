print("""
+ if else

""")

x = True
if x:
    print("no bằng true")
else:
    print("Nó không bằng true")

y = True
if x:
    print("no bằng true")
elif y:
    print("Y equals true too")
else:
    print("khong ai bang true")

print("""
 + if demo example 
 + sử dụng elif để thay thế cho switch case

 =======================================
""")

# x = int(input("Nhap so : "))
# if x < 0:
#     print("nho hon 0")
# elif x == 0:
#     print(" == 0")
# elif x == 1:
#     print(" == 1")
# else:
#     print("No thing")
print("""
+ FOR statement
===================================================
""")

lst = ["1", "2dfdfd", "3fdfdf"]
for x in lst:
    print(x, len(x), lst.index(x))
    if x == "1":
        lst.remove(x)
        lst.append("343")

print(lst)

print("""
+ break and continue statement
====================================================================
""")

print("""
+ Else trong loop
for/else

==========================Example 1===============================
""")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
print("""
============================Example 2===================================
""")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')