from make_db_file import LoadDatabase, storeDatabase

db = LoadDatabase()

db['Tom']['name'] = 'My Tom'
storeDatabase(db)