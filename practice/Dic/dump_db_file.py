from make_db_file import LoadDatabase
db = LoadDatabase()
for key in db:
	print key,'=>\n',db[key] 
print db['sue']['name']
