# -*- coding: utf8 -*-
import sys
import os
import shelve	

def InteractDbShelve(dbfilename):
	"""
	hàm đê tuong ta vs db shelve
	"""
	# dbfile = raw_input("\nNhap ten Db : ")
	db = shelve.open(dbfilename)
	fieldnames = ('name','age', 'job', 'pay')
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
	return
def Main():
	if len(sys.argv) == 1:
		print "Lack out of parameter"
	else:
		dbfilename = sys.argv[1]
		if os.path.isfile(dbfilename):
			if os.access(dbfilename, os.R_OK):
				InteractDbShelve(dbfilename)
			else:
				print "DB file  is imposible to read"
				exit(0)
		else:
			print "BD file is not exist"
			exit(0)
	return
if __name__ == '__main__':
	Main()	