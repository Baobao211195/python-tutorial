D={}
for i in range(1,11):
	s = raw_input("Nhap :")
	if s in D:
		D[s] = D[s]+ 1
	else:
		D[s] = 1
for r in D:
	print r ,"da xua hien", D[r]
"""nhap mot chuoi...in ra chieu dai, 
va dem tu xuat hien trong do..va dem ky tu 
in ra."""