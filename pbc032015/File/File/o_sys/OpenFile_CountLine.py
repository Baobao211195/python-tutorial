import sys
import os



def CountLine(filename):
	count = 0
	f = open(filename, 'r')
	for line in f.readlines():
		count = count + 1
	print "the Number of line is %d line" % count
	return

def main():
	if len(sys.argv) ==1:
		print "File not found"
	else:
		filename = sys.argv[1]
		if os.path.isfile(filename):
			if os.access(filename, os.R_OK):
				CountLine(filename)
			else:
				print"Can not access file :"
		else:
			print "filename is not exist !"
	return

if __name__ == '__main__':
	main()


