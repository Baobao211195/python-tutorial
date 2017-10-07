print("Hello, this is my program")
print("Ban muon thuc hien phem tinh gi ?")
try:
	s = int(input("phep toan thu hien : "))
	if s== 1:
		print("moi ban nhap gia tri: ")
		a = int(input("Gia tri thu nhat :"))
		b = int(input("Gia tri thu hai :"))
		print("Ket qua la %d" % (a*b))
	elif s == 2:	
		print("moi ban nhap gia tri: ")
		a = int(input("Gia tri thu nhat :"))
		b = int(input("Gia tri thu hai :"))
		print("Ket qua la %d" % (a-b))
	elif s == 3:	
		print("moi ban nhap gia tri: ")
		a = int(input("Gia tri thu nhat :"))
		b = int(input("Gia tri thu hai :"))
		print("Ket qua la %d" % (a+b))
	elif s == 4:	
		print("moi ban nhap gia tri: ")
		a = int(input("Gia tri thu nhat :"))
		b = int(input("Gia tri thu hai :"))
		if b==0:
			print ZeroDivisionError
		else:
			print("Ket qua la %d" % (a//b))

	# elif s == 5:
	# 	print("Moi ban nhap gia tri:")
	# 	n = int(input("Gia tri n :"))
	# 	a,b =0,1
	# 	while b< n:
	# 		print(b,end=" ")
	# 		c = a+b
	# 		a =  b
	# 		b = c 
except ValueError:
	print ValueError
except ZeroDivisionError:
	print ZeroDivisionError
except ValueError:
	print ValueError
except ValueError:
	print ValueError
finally:
	pass
	