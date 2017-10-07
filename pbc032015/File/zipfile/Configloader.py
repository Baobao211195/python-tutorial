def Load(self,filename):
	D = {}
	f = open("filename","r")
	for line in f:
		line = line.strip()
		if not line.startswith("#"):
			List = line.split(" = ")
			if len(List) ==2:
				D[str(List[0])] = List[1]
	return

def Main(self,filename):
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if os.path.isfile(filename):
			if os.access(filename, os.R_OK):
				Load(filename)
			else:
				print "filename is not read"
				exit(0)
		else :
			print "filename is not exit"
			exit(0)	
	else:
		print "Thieu tham so "



if __name__ == '__main__':
	Main()
