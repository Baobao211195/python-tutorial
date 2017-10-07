bob = {'name':'Bob Smint','age':42,'pay':4200,'job':'Sorfware'}
sue = {'name':'Sue John','age':45,'pay':4500,'job':'Hardware'}
people = [bob,sue]
a = [] # make a empty list
for person in people:
	a.append(person['name'])	#append value corresponse key into list
print a # new list has two value is name
	# if person['name'] == 'Sue John':
	# 	print person['pay']
print "Sum total pay"
for person in people:
	print person['pay']
	# print sum(person['pay'])
print """
		 use SQL queries
		 	"""
for person in people:
	if person['age'] >=45:
		print person['age']**2 # in ra 45*2
	else:
		print person['age'] # in ra 42