import sys
import os


class Config(object):

	def __init__(self, filename):
		
		print "Bat dau thuc hien"
		try:
			self.config = {} # su dung cho cac  instance		
			self.f = open(filename,'r')
			if not self.f.closed:
				self.LoadConfig()

			else:
				sys.exit(0)
		except Exception, e:
			print e
	def __del__(self):
		"""close opened file before exitting
		"""
		try:
			self.f.close()
			print"Config file is closed"

		except Exception, e:
			print e
	def LoadConfig(self):
		print"bat dau thuc hien LoadConfig"
		for line in self.f:
			line = line.strip()
			if not line.startswith("#"):
				ls = line.split(" = ")
				if len(ls) == 2:
					self.config[str(ls[0])] = ls[1]

if __name__ == '__main__':

	mainCf = Config("db.cfg")
	print mainCf.config["db_host"]
	print mainCf.config["db_user"]
	print mainCf.config["db_name"]
	print mainCf.config["db_password"]
