# -*- coding: utf8 -*-
print """cap nhat cac object
da co trong shelve
"""
import shelve
from Person import Person

filename = ('name','age','job','pay')
db = shelve.open('class-shelve')

while True:
	key = raw_input('\nkey ? => ')
	if key=='s':
		print "ket Thuc update and add new" 
		break
	if key in db:
		record = db[key] # câp nhat record da co sang
	else:				  # hoac luu thanh cac record moi
		record = Person(name = '?', age = '?',pay = '?',job = '?')
	for field in filename:
		currval = getattr(record,field)
		newtext = raw_input('\t[%s]=%s\n\t\tnew?=>'%(field,currval))
		if newtext:
			setattr(record,field,eval(newtext))
	db[key] = record
db.close()

"""
hàm setattr(object, name,value) set tên thuoc tinh cua mot doi tuong
setattr(x,'y',v) => x.y =v
gan ten thuoc tinh y cua doi tuong x = v

ham eval("mot string") -> kieu int : ham eval chuyen mot string thanh kieu int
nguoc lai voi ham repr(kieu int) -> mot string

"""
print"""kiem tra sau khi update db_shelve
"""
db = shelve.open('class-shelve')
for key in db:
	print key, '=>\n ', db[key].name, db[key].age,db[key].pay,db[key].job
