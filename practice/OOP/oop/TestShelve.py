import shelve
db = shelve.open('class-shelve')
for key in db:
	print key, '=>\n ', db[key].name, db[key].age,db[key].pay,db[key].job
