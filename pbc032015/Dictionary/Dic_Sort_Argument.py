# D = {'1':'c','b':'d','a':'b'}
# print sorted(D, key = str.lower) # thuc hien ham key = str.lower roi moi so sanh
# print sorted(D, key = str.lower,reverse = True)
D2 = [('a',10,'pop'),('b', 2, 'rock'),('c', 5 ,'country')]
print D2.sort()
print
print D2.sort(reverse=True)
print
print D2.sort(key = lambda D2:D2[1])
