# sort theo key tang dan
# va sort theo value tang dan
D = {1:2,3:4,'a':'b','d':'e'}
# for k, v in D.items():
# 	print k, v
# 	L.sort()
# for t in D.items():
# 	print t,

 

# chuyen thhanh list D.items()
# L = list
# L.sort() # xong yeu cau 1

# sap xep theo value
L2 =[]
for k,v in D.items():
	k1,v1 = v, k
	L2.append(k1, v1)
	L2.sort()
print L2


	 
