# "read numbers till eof and show spuare"
def interact():
	print "Hello stream world"
	while True:
		try:
			reply = input(" Enter numbers >: ")
		except Exception as e:
			print str(e)
			break
		else:
			num = int(reply)
			print "%d squared is %d " %(num, num**2)
	print "Bye "
if __name__ == '__main__':
		interact()	