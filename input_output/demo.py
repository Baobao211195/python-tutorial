"""
+ str() -> return value of string to human readable 
+ repr() -> return value can be read by the interpreter

"""

print(repr("oanh pv"))  # 'oanhpv'
 
print(str("oanh pv")) # oanh pv

print(repr((1212, 3343, ('oanh', 'van'))))

print("=========== Formatted String Literals===================")

import math
print(f'pham van oanh {math.pi:.3f}')

x = 'oanh pv'
print(f'value of oanh {x}')

dictionary = {'oanh':3434, 'vankem':343434, 'pham':9}

# :numer to the number of characters wide
for k, v in dictionary.items():
    print(f'{k:7} === {v:1d}')
"""
The result : 
oanh    === 3434
vankem  === 343434
pham    === 9

"""
print("""
+  use format() method
""")
st = "{} pham van oanh, {}"
print(st.format('hello', 'hello van kem'))

st = "{0} pham van oanh, {1}"
print(st.format('hello', 'van kem'))

st = "{1} pham van oanh, {0}"
print(st.format('hello', 'van kem'))