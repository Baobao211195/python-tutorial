'''
save in memory database object to a file with custom formatting;
assume 'endrec','enddb',and '=>' are not used in the data;
assume db is dict of dict;
warning : eval can be dangerous - it
runs string as code;
could also eval() record dict all at once;
could also dbfile.write(key + '\n') vs print (key,file= dbfile);
'''
dbfilename = 'peopel-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'

def storeDatabase(db,dbfilename =dbfilename):
	'formatted dump of database to flat file'
	dbfile = open(dbfilename,'r')
	for key in db:
		print key 
		for (name,value) in db[key].items():
			print str(name) + RECSEP + str(value)
		print ENDREC
	print ENDDB
	dbfile.close()

def LoadDatabase(dbfilename = dbfilename):
	'parse data to reconstruct database'
	dbfile = open(dbfilename)
	import sys
	sys.stdin = dbfile
	db = {}
	key = input()
	while key != ENDDB:
		rec = {}
		field = input()
		while field != ENDREC:
			rec = {}
			name,value = field.split(RECSEP)
			rec[name] = eval(value)
			field = input()
		db[key] = rec
		key = input()
	return db

if __name__ == '__main__':
	from dbfilename import db
	storeDatabase(db,dbfilename)
	# db = LoadDatabase(dbfilename)
	# for key in db:
	# 	print key,'=>',db[key]
	# print db['sue']['name']