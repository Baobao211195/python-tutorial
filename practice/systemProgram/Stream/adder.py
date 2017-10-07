import sys
sum = 0
while True:
	try:
		line = raw_input("> :")
		# raw_input("> ") # or call sys.stdin.readlines()
	except EOFError:
		break
	else:
		sum = sum + int(line)
print sum