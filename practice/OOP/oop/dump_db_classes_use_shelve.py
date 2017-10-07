import shelve
print"""
duyet db da duoc sap 
xep trong shelve
"""

db = shelve.open('class-shelve')
for key in db:
	print key, '=>\n ', db[key].name, db[key].pay

bob = db['bob']

print bob.lastName()
print db['tom'].lastName()


print "cap nha database"
sue = db['sue']
sue.giveRaise(.10)
db['sue']= sue
print db['sue'].pay # pay of su da duoc thay doiB