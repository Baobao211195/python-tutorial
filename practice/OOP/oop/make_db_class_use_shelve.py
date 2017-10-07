# -*- coding: utf8 -*-
import shelve
from Person import Person
from Manager_Inheritance import Manager

bob = Person('van oanh', 43, 3000, 'sorfware')
sue = Person('Nguyen van', 45, 5000, 'Economic')
tom = Manager('Tom done', 50, 60000)

db = shelve.open('class-shelve') # mo mot file rong trong shelve và luu db vao
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
# db.close()

for key in db:
	print key, '=>\n ', db[key].name, db[key].pay
	

bob = db['bob']

print (bob.lastName())
print (db['tom'].lastName())
print db['sue'].pay
//            try {
//                if (pStmt != null) {
//                    pStmt.close();
//                }
//            } catch (SQLException ex) {
//                logger.error("DbActive ErrorCode: " +ex.getErrorCode() + " Error: " + ex.getMessage() + " STACK: " + ex);
//            }