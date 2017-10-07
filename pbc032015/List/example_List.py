>>> oanh = ["van oanh",42,30000,"sorfware"]
>>> oanh = ["van kem",45,50000,"hardware"]
>>> van = ["van kem",45,50000,"hardware"]
>>> python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python' is not defined
>>> cls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cls' is not defined
>>> exit()
PS C:\Users\PC>
PS C:\Users\PC> python
Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 3
Type "help", "copyright", "credits" or "license" for more i
>>> oanh = ["van oanh", 42, 30000, "sorfware"]
>>> van = ["van kem", 45, 50000, "hardware"]
>>> love = [oanh,van]
>>> love[1][0]
'van kem'
>>> for i in love:
...     print i
...
['van oanh', 42, 30000, 'sorfware']
['van kem', 45, 50000, 'hardware']
>>> for i in love:
...     print i[0].split()[-1]
...
oanh
kem
>>> for i in love: print(i[2])
...
30000
50000
>>> pay = [i[2] for i in love]
>>> _
'van kem'
>>> pay = [i[2] for i in love]
>>> pay
[30000, 50000]
>>> pay = map((lambda x:x[2]),people)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'people' is not defined
>>> pay = map((lambda x:x[2]),love)
>>> list(pay)
[30000, 50000]
>>> sum(map((lambda x:x[2]),love))
80000
>>> map((lambda x:x[2]),love)
[30000, 50000]
>>> love.append("ha",50,0,None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (4 given)
>>> love.append(["ha",50,0,None])
>>> len(love)