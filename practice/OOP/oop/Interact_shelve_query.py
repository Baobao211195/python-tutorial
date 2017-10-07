# -*- coding: utf8 -*-
import shelve

fieldnames = ('name','age', 'job', 'pay')
print type(fieldnames) # kieu tuple
db = shelve.open('class-shelve') # mo db co ten la class-shelve truoc do
maxfield = max(len(f) for f in fieldnames)

while True:
	key = raw_input('\nkey ? => ')
	if not key:
		break
	try:
		record = db[key]
	except :
		print 'No such key "%s" !' % key
	else:
		for field in fieldnames:
			print field.ljust(maxfield), '=>', getattr(record,field)
"""
hàm getattr là hàm built in đe lây
thuôc tinh cua doi tuong khi mà có mot
chuoi ten cua no
và ljust là phuong thuc cua string

"""
