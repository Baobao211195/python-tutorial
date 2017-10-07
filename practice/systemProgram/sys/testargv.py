"collect command-line options in a dictionary"
def getopts(argv):
	opts = {}
	while argv:
		opts[argv[0]] = argv[1]
		argv = argv[2:]
	return opts
	# 	if argv[0][0] == '-':
	# 		opts[argv[0]] = argv[1]
	# 		argv = argv[2 :]
	# 	else:
	# 		argv = argv[1:]
	# return opts

if __name__ == '__main__':
	from sys import argv
	myargv = getopts(argv)
	# if '-i' in myargv:
	# 	print myargv['-i']
	print myargv
