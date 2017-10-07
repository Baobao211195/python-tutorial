# load config
# connect db
# close
from ConfigLoader import Config
import MySQLdb


# load Config 



dbconfig = Config('db.cfg')
#print dbconfig.config["db_host"]
# """
# thuc hien connect den db
# """
try:
	conn = MySQLdb.connect(
		host=dbconfig.config['db_host'],
		user = dbconfig.config['db_user'],
		passwd = "",
		db = dbconfig.config['db_name'],
		)
	cur = conn.cursor()
	print"Connect to database successful"
	sql = "select *from cds"
	cur.execute(sql)
	#read
	row1 = cur.fetchone()
	print row1
	#insert
	print 
	# spl1 = "INSERT INTO `cds`(`titel`, `interpret`, jahr, id) VALUES (%s,%s,%s,%s)"
	# insert = ('Binh Duong','Tran Tien', 64, 8)
	# try:
	# 	cur.execute(spl1, insert)
	# 	conn.commit()
	# 	# row2 =cur.fetchone()
	# 	# print row2
	# 	print "insert successful"

	# except Exception, e:
	# 	conn.rollback()
	# 	print e

		
	#update
	sql3  = "UPDATE cds SET 'titel' = 'Thai Binh','interpret' = 'Van Kem', jahr= '34', id = '1' WHERE  1 "
	try:
		cur.execute(sql3)
		conn.commit()
	except Exception,e:
		conn.rollback()
		print e
except Exception, e:
	print e
finally:
	cur.close()
	conn.close()


