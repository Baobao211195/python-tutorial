# try:
# 	a = int(raw_input("Nhap mot so :"))
# except ValueError :
# 	print ValueError
print'welcome to program.... '
print"""
		click '4' to division
		click '3' to multiple
		click '2' to add
		click '1' to subtract
		click '2' to Fibonaci
"""
try:
	s = int(input("The math : "))
	if s == 4:	
		a = input("The first number :")
		b = input("The second number:")
		print("The result is %.2f" % (a/b))
	elif s == 3:	
		a = int(input("The first number:"))
		b = int(input("The second number:"))
		print("The result is %d" % (a*b))
	elif s == 2:	
		a = int(input("The first number:"))
		b = int(input("The second number:"))
		print("The result is %d" % (a+b))
	elif s == 1:	
		a = int(input("The first number:"))
		b = int(input("The second number:"))
		print("The result is %d" % (a-b))
	elif s == 0:
		n = int(input("Limit of the sequence is :"))
		a,b = 0,1
		while b< n:
			print b
			c = a+b
			a = b
			b = c
	elif (s!=4) or (s!=3) or (s!=1)or (s!=2) or (s!=0):
		print 'you make Error..please..retype!'
except NameError:
	print 'you make NameError..please..retype!'
except ZeroDivisionError:
	print 'you make ZeroDivisionError..please..retype!'
		
	
