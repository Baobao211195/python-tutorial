# connect
# close

# dinh nghia class db
# co self , nam, usr., host, db_password, 4 thong so 

# """"db_host = localhost
# db_user = root
# db_name = cdcol
# db_password = root
# """
import MySQLdb
import ConfigLoader

class Database(object):
	"""docstring for Database"""
	def __init__(self, host, user, db, password):
		self.host = raw_input("Nhap Ten host :")
		self.user = raw_input("Nhap Ten User :")
		self.db = raw_input("Nhap Ten Database :")
		self.password = raw_input("Nhap Password :")
	def connect():
		con  = MySQLdb.connect(self.host,self.user,self.db,self.password)
		cur = con.cursor() # dung con tro de lam viec vs DB
		cur.execute("SELECT VERSION()")
		row = cursor.fetchall()
		print "server version",row[0]
		cursor.close()
		con.close()


if __name__ == '__main__':
	main()

