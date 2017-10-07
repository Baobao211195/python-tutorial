# -*- coding: utf -8 -*-
# lists of tuple.
#tuple is record afield name and value.
bob = [['name','Bob Smith'],['age',42],['pay',3000],['job','sorfware']]
sue = [['name','Sue John'],['age',45],['pay',4000],['job','hardware']]
people = [bob,sue]
for person in people:
	print person[0][1] ,person[1][1] # lay ten va tuoi
print "Kết thúc phần thứ nhất"
# tim kiem theo nhan
for person in people:
	for (age, value) in person:
		if age == 'age': # in ra tuoi cua tung nguoi
			print value
print "Kết thúc phần thứ hai"
# viet thanh ham tim theo lable :
def TimKiem(ListOfRecord,record,lable): # Listofrecord là people; record la ten list , lable la nhãn cần tìm kiếm
	for person in ListOfRecord:
		for(name,value)	in record:
			if name ==lable:
				return value
print TimKiem(people,bob,'age')
print
for person in people:
	print TimKiem(people,person,'job')
print

	