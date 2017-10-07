import sys
import os


class Config(object):
	# config = {} 

	def __init__(self, filename):
		
		print "Bat dau thuc hien"
		try:
			self.config = {} # su dung cho cac instance	
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

	mainCf = Config("config1.txt")
	print mainCf.config
	# mainCf.Load("config1")
	# print mainCf.Main("config1")


	
	# # def Load(self,filename):
	# # 	D = {}
	# # 	f = open("filename","r")
	# # 	for line in f:
	# # 		line = line.strip()
	# # 		if not line.startswith("#"):
	# # 			List = line.split(" = ")
	# # 			if len(List) ==2:
	# # 				D[str(List[0])] = List[1]
	# # 	return

	# def Main(self,filename):
	# 	D = {}
	# 	f = open("filename","r")
	# 	for line in f:
	# 		line = line.strip()
	# 		if not line.startswith("#"):
	# 			List = line.split(" = ")
	# 			if len(List) ==2:
	# 				D[str(List[0])] = List[1]
	# 	return
	# 	# Tenst file
	# 	if len(sys.argv) == 2:
	# 		filename = sys.argv[1]
	# 		if os.path.isfile(filename):
	# 			if os.access(filename, os.R_OK):
	# 				Load(filename)
	# 			else:
	# 				print "filename is not read"
	# 				exit(0)
	# 		else :
	# 			print "filename is not exit"
	# 			exit(0)	
	# 	else:
	# 		print "Thieu tham so "




