print 'Chuong trinh python stickers'
try:
	while True :
		s = input("Nhap stickers : ")
		if s == 'q':
			break
		elif s == 1:
			print 'Bieu tuong :P'
		elif s == 2:
			print'Bieu tuong =D'
		elif s == 3:
			print'Bieu tuong :v'
		elif s == 4:
			print'Bieu tuong :)'
		elif s == 5:
			print'Bieu tuong <3'
except Exception:
	print NameError,'Moi ban nhap lai !'



