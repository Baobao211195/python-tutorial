print """Chuong trinh quan ly hoc sinh"
	"Bam 1 de nhap thong tin"
	"Bam 2 de in thong tin"
	"Bam 3 de sap xep thong in"
	"Bam 4 de quit chuong trinh"""
List_Truong = []
Dic_HocSinh = {}
i = 0
while  True:
	s = input("Nhap yeu cau :")	
	# them hoc sinh
	if s == 1 :   
		Dic_HocSinh["ID"] = i
		Dic_HocSinh["Hovaten"] = raw_input("Ho va ten :")
		Dic_HocSinh["Tuoi"] = input("Nhap tuoi :")
		Dic_HocSinh["Nam sinh"] = raw_input("Nhap nam sinh :")
		List_Truong.append(Dic_HocSinh)
		Dic_HocSinh = {}
		i= i+1
		# print List_Truong
	# print information
	elif s == 2:
		for i in range(len(List_Truong)):
			print List_Truong[i]
	# tim kiem
	elif s == 3:
		hs = raw_input("Nhap ten hoc sinh can tim kiem :")
		a = 0
		for i in range(len(List_Truong)):
			if List_Truong[i]["Hovaten"] == hs:
				print "So thu tu %d" %a, List_Truong[i].values()
				a = a+1
			else:
				print "Khong co hoc sinh trong danh sach tim kiem"
				# print str(List_Truong[i]["ID"])+' '+str(List_Truong[i]["Hovaten"])+' '+str(List_Truong[i]["Tuoi"])+' '+str(List_Truong[i]["Nam sinh"])	
											
			# print List_Truong[i]
			# for x in range(len(List_Truong[i])):
			# 	if x == student:
			# 		print x
					# print str(List_Truong[x]["ID"]) + List_Truong[x]["Hovaten"] +List_Truong[x]["Tuoi"] + List_Truong[x]["Nam Sinh"]
	# thay doi thong tin 
	elif s==4:
		







	# 		if List_Truong[i]["Hovaten"] == s:
	# 			
	# 		else:
	# 			print "Khong tim thay hoc sinh can tim :"
	# # chinh sua thong tin
	# elif s ==4:

			





thuat toan 
 ket qua D = {"Db_sever" : "192.168","db_port": 1521}


 doc tung dong 
 	voi moi dong strip
 	kiem tra co dau # o dau
 		neu co # thi bo qua
 	neu : NO #	
 		tach split("_=_") => list 
 	gia tri dau tien duoc gan thanh key
 	D[list[0]] = list[1]
 print D