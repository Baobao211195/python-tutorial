import sys
import os

def ReadFile(filename):
	f = open(filename, 'r')
	print (f.read())
	f.close()

def main():
	if len(sys.argv) ==1:
		print "File not found"
	else:
		filename = sys.argv[1]
		if os.path.isfile(filename):
			if os.access(filename, os.R_OK):
				ReadFile(filename)
			else:
				print"Can not access file :"
		else:
			print "Filename is not exist !"
	return


if __name__ == '__main__':
	main()

	