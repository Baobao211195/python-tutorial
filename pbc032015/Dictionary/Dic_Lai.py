s = raw_input("Nhap :")
b = s.split() # bien s thanh list cac tu
print b
D={}
for i in range(len(b)):
	if b[i] in D:
		D[b[i]] = D[b[i]]+ 1
	else:
		D[b[i]] = 1
for r in D:
	print r ,"da xua hien", D[r]
# """nhap mot chuoi...in ra chieu dai, 
# va dem tu xuat hien trong do..va dem ky tu 
# in ra."""
b = list(s) # bien s thanh  list cac ky tu trong chuoi
print b
D={}
for i in range(len(b)):
	if b[i] in D:
		D[b[i]] = D[b[i]]+ 1
	else:
		D[b[i]] = 1
for r in D:
	print r ,"da xua hien", D[r]